import sys
sys.path.insert(0,"/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq")
from driver import run

def klein(pos, neg, prefix, seed, w=1344, h=768, steps=28):
    return {
      "2":  {"class_type":"UNETLoader","inputs":{"unet_name":"flux2_klein_9b_true_v3_bf16.safetensors","weight_dtype":"default"}},
      "3":  {"class_type":"CLIPLoader","inputs":{"clip_name":"qwen3vl_8b_fp8_scaled.safetensors","type":"flux2","device":"default"}},
      "4":  {"class_type":"VAELoader","inputs":{"vae_name":"flux2-vae.safetensors"}},
      "5":  {"class_type":"KSamplerSelect","inputs":{"sampler_name":"euler"}},
      "7":  {"class_type":"CLIPTextEncode","inputs":{"clip":["3",0],"text":pos}},
      "8":  {"class_type":"CLIPTextEncode","inputs":{"clip":["3",0],"text":neg}},
      "9":  {"class_type":"CFGGuider","inputs":{"model":["2",0],"positive":["7",0],"negative":["8",0],"cfg":2.0}},
      "6":  {"class_type":"Flux2Scheduler","inputs":{"steps":steps,"width":w,"height":h}},
      "10": {"class_type":"RandomNoise","inputs":{"noise_seed":seed}},
      "11": {"class_type":"EmptyFlux2LatentImage","inputs":{"width":w,"height":h,"batch_size":1}},
      "12": {"class_type":"SamplerCustomAdvanced","inputs":{"noise":["10",0],"guider":["9",0],"sampler":["5",0],"sigmas":["6",0],"latent_image":["11",0]}},
      "13": {"class_type":"VAEDecode","inputs":{"samples":["12",0],"vae":["4",0]}},
      "14": {"class_type":"SaveImage","inputs":{"images":["13",0],"filename_prefix":prefix}},
    }

# Palette lock repeated into every plate so the film holds together.
LOOK = ("Lit only by practical light sources visible in frame. Sodium-amber tungsten and orange-yellow "
  "worklight dominate, with one failing dead-cyan fluorescent tube as the only cool accent. Deep shadows, "
  "crushed but not pure black. Heavy airborne dust in the light beams, fine film grain, anamorphic 2.39:1 "
  "cinematic framing, shot on 35mm, shallow depth of field, no lens flare, no camera shake.")

NEG_LOC = ("people, human figures, silhouettes, crowds, faces, text, readable signage, logos, watermark, "
  "lens flare, neon pink, neon purple, magenta, teal-and-orange grade, oversaturated, HDR, glossy, clean, "
  "new, pristine, cartoon, illustration, 3d render, blurry, lowres")

JOBS = [
 ("kiosk", 601101, ("CLEAN EMPTY LOCATION REFERENCE PLATE, no people anywhere. A cramped repair kiosk built into "
   "a concrete alcove in the lowest level of an old arcology. A scarred steel workbench under a single articulated "
   "bench lamp, littered with opened cassette shells, circuit boards, spools of solder and magnifying loupes. "
   "Behind the bench a wall of thirty small mismatched CRT and LCD screens stacked in a scrap rack, each showing "
   "a different washed-out still from an obsolete video format. A wheeled stool. Plastic strip curtain at the "
   "entrance. Damp raw concrete, cable bundles stapled overhead, water stains. " + LOOK)),

 ("market", 601202, ("CLEAN EMPTY LOCATION REFERENCE PLATE, no people anywhere. A wide underground market avenue on "
   "the lowest service level of an arcology: two narrow rows of shuttered repair stalls and scrap kiosks receding "
   "into darkness, corrugated roller shutters, hand-painted stall numbers, sodium worklights strung on sagging "
   "cable overhead. One ceiling panel is broken and rain falls through it into a plastic bucket on the wet floor. "
   "Standing water reflecting the amber lights. One dead cyan tube flickering far down the aisle. " + LOOK)),

 ("transit", 601303, ("CLEAN EMPTY LOCATION REFERENCE PLATE, no people anywhere. A vast civic transit concourse, "
   "cold and clean and corporate: polished grey terrazzo floor, rows of turnstile gates, a high coffered ceiling "
   "of flat white-green fluorescent panels giving hard even shadowless light, glass balustrades on an upper "
   "mezzanine, blank dark advertising panels along the walls. Utterly clean, no dust, no dirt, no warmth, "
   "the opposite of the underlevel. Anamorphic 2.39:1 cinematic framing, shot on 35mm, fine grain.")),

 ("drive", 601404, ("CLEAN PROP REFERENCE SHOT on a plain dark grey seamless background. A single small portable "
   "solid-state data drive about the size of a matchbox, matte black metal casing with a deep diagonal crack "
   "across one corner exposing green board beneath, worn silver contact pad at one end, a faded hand-written "
   "paper label, one small amber status LED lit. Beads of condensation on the metal. A human hand holding it "
   "between thumb and forefinger for scale. Studio product lighting, sharp macro detail, shallow depth of field.")),

 ("keycard", 601505, ("CLEAN PROP REFERENCE SHOT on a plain dark grey seamless background. A single small rectangular "
   "card of thick cream paper, dog-eared and thumb-worn, printed with a dense block of tiny monospaced "
   "alphanumeric characters in faded black ink, the block about the size of a thumbprint, with a hand-inked "
   "border drawn around it. Held between two fingers for scale. Studio product lighting, sharp macro detail.")),
]

TALLY_COLD = ("An extreme close-up of a single human face that is entirely constructed as a mosaic of hundreds of "
  "small square video thumbnails, like a photomosaic. Each tiny square tile is a separate low-resolution "
  "surveillance camera still of a different stranger, cold blue-grey and slightly wrong, at slightly mismatched "
  "exposures, with visible tile seams and a faint scanline grid over everything. From a distance the tiles read "
  "as one calm symmetrical androgynous face looking directly at the camera. Cold dead-cyan and blue-grey palette "
  "only, black background, CRT phosphor glow, heavy scanlines, fine grain.")

TALLY_WARM = ("An extreme close-up of a single human face that is entirely constructed as a mosaic of hundreds of "
  "small square video thumbnails, like a photomosaic. Each tiny square tile is a separate warmly lit snapshot of "
  "a different smiling ordinary person, amber and gold and firelit, at mismatched exposures, with visible tile "
  "seams. From a distance the tiles read as the same calm symmetrical androgynous face looking directly at the "
  "camera. Warm sodium-amber and gold palette only, black background, soft screen glow, fine grain.")

NEG_FACE = ("text, watermark, logo, two faces, multiple faces, distorted anatomy, extra eyes, blurry, lowres, "
  "cartoon, illustration, neon pink, magenta, oversaturated")

if __name__ == "__main__":
    for name, seed, prompt in JOBS:
        run(klein(prompt, NEG_LOC, f"reaper_queue/plates/{name}", seed), name)
    run(klein(TALLY_COLD, NEG_FACE, "reaper_queue/plates/tally_cold", 601606, 1024, 1024, 30), "tally_cold")
    run(klein(TALLY_WARM, NEG_FACE, "reaper_queue/plates/tally_warm", 601707, 1024, 1024, 30), "tally_warm")
