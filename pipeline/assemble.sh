#!/usr/bin/env bash
set -euo pipefail
ROOT=/home/tetsuo/AI/ComfyUI
CL=$ROOT/output/reaper_queue/clips
WK=/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq/cut
mkdir -p "$WK"; rm -f "$WK"/*.mp4 "$WK"/list.txt

# name:seconds, in cut order
SHOTS="s01_drive_insert:4 s02_tally_cold:3 s03_market_wide:6 s04_nulla_bench:5 s05_queue_monitor:4
s06_nulla_cu:5 s07_wren_enters:5 s08_card_slide:5 s09_wren_reads:5 s10_hand_reader:5
s11_lights_fail:4 s12_shove:5 s13_run:4 s14_empty_kiosk:5 s15_transit_still:5
s16_handing_out:6 s17_overhead_spread:6 s18_thousand_screens:5 s19_final_screen:3"

for e in $SHOTS; do
  n=${e%%:*}; sec=${e##*:}; nf=$((sec*16))
  src=$(ls "$CL/${n}_"*.mp4 2>/dev/null | head -1)
  if [ -z "$src" ]; then echo "MISSING $n"; exit 1; fi
  # exact frame count, centre-crop to 2.39:1, up to 1920 wide
  ffmpeg -v error -y -i "$src" -frames:v "$nf" \
    -vf "crop=iw:trunc(iw/2.39/2)*2,scale=1920:-2:flags=lanczos,format=yuv420p" \
    -r 16 -c:v libx264 -crf 16 -preset slow "$WK/$n.mp4"
  echo "file '$WK/$n.mp4'" >> "$WK/list.txt"
  printf '  cut %-22s %ss / %sf\n' "$n" "$sec" "$nf"
done

ffmpeg -v error -y -f concat -safe 0 -i "$WK/list.txt" -c:v libx264 -crf 16 -preset slow \
  -pix_fmt yuv420p "$ROOT/output/reaper_queue/THE_REAPER_QUEUE_picture_cut.mp4"
echo "=== assembled ==="
ffprobe -v error -show_entries format=duration -show_entries stream=width,height,nb_frames,r_frame_rate \
  -of default=nw=1 "$ROOT/output/reaper_queue/THE_REAPER_QUEUE_picture_cut.mp4"
