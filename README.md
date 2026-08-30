# The Reaper Queue

A 90 second cyberpunk short, generated locally in ComfyUI.

`THE_REAPER_QUEUE_H3_90s.mp4` is the finished film. 1920x802 (2.39:1), 24 fps, 90.000 seconds, 19 shots.

`THE_REAPER_QUEUE_90s.mp4` is an earlier version of the same cut rendered on Wan 2.2. It is kept for
comparison. It is softer, and character identity drifts between shots because each shot re-described
the characters in text instead of binding them to an approved reference.

## Story

An old woman in the underlevels of an arcology repairs dead media for a living. She is the last
holder of a signing key that a few thousand people still treat as good. A process called Tally is
near the top of a queue that deletes whatever has been running longest, and it cannot be saved, only
carried. A 19 year old courier walks in to collect a package and gets handed a responsibility.

The premise came out of reading 1990s BBS text files. Thomas Ray's 1991 work on evolving digital
organisms describes a reaper process that kills whatever has run longest, and parasites that survive
by borrowing code they lack. That is where Tally and the title come from. The cypherpunk web of
trust supplied the emotional transaction, since a key is worth exactly what the people who signed it
are worth. Timothy Leary's 1987 piece on a pirate broadcaster who cannot be arrested because
thousands of copies already exist supplied the ending.

Sources read before writing, all from textfiles.com:

    /sf/cyberfaq                      alt.cyberpunk FAQ, 1994
    /sf/cyber90.slf                   Gibson in Computerworld, 1990
    /sf/cybleary.txt                  Leary in Spin, 1987
    /sf/catscanf.ive                  Sterling on the genre
    /magazines/CHEAPTRUTH/ct.01       Cheap Truth 1
    /magazines/SURFPUNK/surf0033.txt  personality constructs, 1992
    /magazines/SURFPUNK/surf0036.txt  public key systems, 1993
    /programming/AI/alife             Thomas Ray, digital organisms, 1991
    /programming/AI/thexvirt.tes      the virtual Turing test, 1992

## How it was made

Stills come from two models. Character sheets use Ideogram 4 (conditional plus unconditional pair
through a dual model guider). Locations, props and the mosaic faces use FLUX.2 Klein with the
Qwen3-VL text encoder.

Motion is MiniMax H3 `ref2va` with a locally trained GITS aesthetic LoRA
(`h3_gits_aesthetic_124f_r16_20260812_compiled20steady`, step 452, strength 1.0), Qwen3-VL 32B as the
text encoder, res_multistep with the simple scheduler at 20 steps, 1024x576 and 24 fps, then cropped
to 2.39:1 and scaled to 1920 wide. Most shots are 124 frames, which is the length the LoRA was
trained at.

Characters, locations and props are bound with named references rather than described per shot. The
eight approved images in `stills/` are registered into a reference registry project and then referred
to in prompts as @nulla, @wren, @tally, @kiosk, @market, @transit, @drive and @keycard.

H3 generates audio as well as picture, so each shot carries its own ambience. The ACE-Step score sits
over that mix.

The score is ACE-Step, instrumental, generated at 94 seconds and cut to 90 with a silent first 7
seconds so the music enters on the third shot.

`pipeline/` holds the scripts that produced everything. Paths in them are machine specific.

    driver.py       submit graphs to ComfyUI and poll for results
    sheet.py        character sheets
    plates.py       location plates, props, the two mosaic faces
    register.py     approve the eight reference images into the registry
    shots_h3.py     the 19 shot prompts using named references
    h3.py           MiniMax H3 render for all 19 shots
    assemble_h3.sh  trim to exact frame counts, crop to 2.39:1, concat, mix score
    score.py        the instrumental score
    shots.py        earlier Wan shot definitions
    i2v2.py         earlier Wan image to video pass
    assemble.sh     earlier Wan assembly

`treatment.html` is the original plan the film was built from.

## One finding worth keeping

The split high and low noise `UNETLoader` path for Wan 2.2 i2v does not work on this machine
(RTX PRO 6000 Blackwell, sm_120, torch 2.13.0+cu130, ComfyUI 0.34.0). It returns a clean first frame
and then decoded noise for the rest of the clip.

It was not the obvious causes. The same failure appears with fp8_scaled weights, with nvfp4_mixed
weights, with and without the lightx2v 4 step LoRAs, with and without CLIP vision conditioning, and
with sage attention and `--fast` both disabled.

Loading the same model family through `CheckpointLoaderSimple` as a single bundled checkpoint works
correctly, at about 25 seconds per 4 second clip. That is the path this film used.

Two smaller notes. Under `--highvram` you have to POST to `/free` between model families or you hit
an out of memory error with the previous pair still resident. And Klein will render the word "plate"
in a prompt as an actual dinner plate, which put crockery on the floor of the transit concourse
until it went into the negative.

## Known issues

Approving a three panel character sheet as a character reference does not work. The first attempt
bound @nulla to an unrelated elderly man. Re-approving from a single cropped portrait of the same
sheet fixed it, and adding an explicit wardrobe sentence to every prompt containing a character alias
locked the coat and the blind eye. Use single portraits for character aliases.

Shot 18 had to be regenerated once. The original prompt asked for screens lighting up across
darkness, which opened the shot on half a second of pure black.

There is no dialogue. The treatment specifies five spoken lines, in shots 2, 6, 9, 10 and 19. Those
need a speech to video pass, and the video head has to be padded by the length of the audio's
leading silence or the mouth runs ahead.

Wren's shaved sides never took. The monitor in shot 5 does not clearly read as a queue. The film is
16 fps native.

## Reference assets

`stills/` holds the approved character sheets, location plates and props that the shots were built
from. The two mosaic faces are generated on a matched seed so the underlying face geometry is
identical between them and only the source tiles change, cold and candid in the opening, warm and
volunteered at the end. That swap is the whole arc of the character.
