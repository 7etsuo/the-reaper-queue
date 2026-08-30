# The Reaper Queue

A 90 second cyberpunk short, generated locally in ComfyUI.

`THE_REAPER_QUEUE_90s.mp4` is the finished film. 1920x804 (2.39:1), 16 fps, 90.000 seconds, 19 shots.

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

Motion is Wan 2.2 image to video, 4 steps, cfg 1.0, euler_ancestral, 832x480, then cropped to
2.39:1 and scaled to 1920 wide.

The score is ACE-Step, instrumental, generated at 94 seconds and cut to 90 with a silent first 7
seconds so the music enters on the third shot.

`pipeline/` holds the scripts that produced everything. Paths in them are machine specific.

    driver.py     submit graphs to ComfyUI and poll for results
    sheet.py      character sheets
    plates.py     location plates, props, the two mosaic faces
    shots.py      the 19 shot definitions, still prompt and motion prompt per shot
    i2v2.py       image to video for all 19 shots
    score.py      the instrumental score
    assemble.sh   trim to exact frame counts, crop to 2.39:1, concat

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

Nulla's coat reads brown in several shots instead of the quilted charcoal from her sheet, and in one
shot her gender reads wrong. Per shot text to image cannot hold identity the way an edit model
composite from an approved sheet would.

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
