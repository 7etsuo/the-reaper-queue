#!/usr/bin/env bash
set -euo pipefail
ROOT=/home/tetsuo/AI/ComfyUI
CL=$ROOT/output/reaper_queue/h3
WK=/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq/cut3
mkdir -p "$WK"; rm -f "$WK"/*.mp4 "$WK"/list.txt

SHOTS="s01_drive_insert:4 s02_tally_cold:3 s03_market_wide:6 s04_nulla_bench:5 s05_queue_monitor:4
s06_nulla_cu:5 s07_wren_enters:5 s08_card_slide:5 s09_wren_reads:5 s10_hand_reader:5
s11_lights_fail:4 s12_shove:5 s13_run:4 s14_empty_kiosk:5 s15_transit_still:5
s16_handing_out:6 s17_overhead_spread:6 s18_thousand_screens:5 s19_final_screen:3"

for e in $SHOTS; do
  n=${e%%:*}; sec=${e##*:}; nf=$((sec*24))
  src=$(ls "$CL/${n}_"*.mp4 2>/dev/null | head -1)
  [ -z "$src" ] && { echo "MISSING $n"; exit 1; }
  ffmpeg -v error -y -i "$src" \
    -filter_complex "[0:v]trim=end_frame=$nf,setpts=PTS-STARTPTS,crop=iw:trunc(iw/2.39/2)*2,scale=1920:-2:flags=lanczos,format=yuv420p[v];[0:a]atrim=0:$(echo "scale=4;$nf/24"|bc),asetpts=PTS-STARTPTS[a]" \
    -map "[v]" -map "[a]" -r 24 -c:v libx264 -crf 16 -preset slow -c:a aac -b:a 192k "$WK/$n.mp4"
  echo "file '$WK/$n.mp4'" >> "$WK/list.txt"
  printf '  %-22s %ss / %sf\n' "$n" "$sec" "$nf"
done

ffmpeg -v error -y -f concat -safe 0 -i "$WK/list.txt" -c:v libx264 -crf 16 -preset slow \
  -c:a aac -b:a 192k -pix_fmt yuv420p "$WK/picture_amb.mp4"

# score over the model's own per-shot ambience
ffmpeg -v error -y -i "$WK/picture_amb.mp4" -i "$ROOT/output/reaper_queue/score_00001.flac" \
 -filter_complex "[0:a]volume=0.9[amb];[1:a]atrim=0:83,asetpts=PTS-STARTPTS,adelay=7000|7000,afade=t=in:st=7:d=2.5,afade=t=out:st=86:d=4,volume=0.65[mus];[amb][mus]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-17:TP=-1.5:LRA=11[a]" \
 -map 0:v -map "[a]" -frames:v 2160 -c:v libx264 -crf 16 -preset slow -c:a aac -b:a 192k \
 "$ROOT/output/reaper_queue/THE_REAPER_QUEUE_H3_90s.mp4"

echo "=== FINAL ==="
ffprobe -v error -show_entries format=duration -show_entries stream=codec_type,codec_name,width,height,nb_frames \
 -of default=nw=1 "$ROOT/output/reaper_queue/THE_REAPER_QUEUE_H3_90s.mp4"
