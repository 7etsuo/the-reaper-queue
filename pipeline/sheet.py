import sys
sys.path.insert(0, "/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq")
from driver import run

def sheet_graph(desc, prefix, seed):
    return {
      "2":  {"class_type":"UNETLoader","inputs":{"unet_name":"ideogram4_fp8_scaled.safetensors","weight_dtype":"default"}},
      "16": {"class_type":"UNETLoader","inputs":{"unet_name":"ideogram4_unconditional_fp8_scaled.safetensors","weight_dtype":"default"}},
      "3":  {"class_type":"CLIPLoader","inputs":{"clip_name":"qwen3vl_8b_fp8_scaled.safetensors","type":"ideogram4","device":"default"}},
      "4":  {"class_type":"VAELoader","inputs":{"vae_name":"flux2-vae.safetensors"}},
      "5":  {"class_type":"KSamplerSelect","inputs":{"sampler_name":"euler"}},
      "7":  {"class_type":"AgenCCharacterSheetPrompt","inputs":{"clip":["3",0],"character_description":desc}},
      "8":  {"class_type":"CFGOverride","inputs":{"model":["2",0],"cfg":3.0,"start_percent":0.7,"end_percent":1.0}},
      "17": {"class_type":"ConditioningZeroOut","inputs":{"conditioning":["7",0]}},
      "18": {"class_type":"ConditioningZeroOut","inputs":{"conditioning":["7",1]}},
      "9":  {"class_type":"DualModelGuider","inputs":{"model":["8",0],"positive":["7",0],"cfg":7.0,"model_negative":["16",0],"negative":["17",0]}},
      "6":  {"class_type":"Ideogram4Scheduler","inputs":{"steps":48,"width":2016,"height":1344,"mu":0.0,"std":1.5}},
      "10": {"class_type":"RandomNoise","inputs":{"noise_seed":seed}},
      "11": {"class_type":"EmptyFlux2LatentImage","inputs":{"width":2016,"height":1344,"batch_size":1}},
      "12": {"class_type":"SamplerCustomAdvanced","inputs":{"noise":["10",0],"guider":["9",0],"sampler":["5",0],"sigmas":["6",0],"latent_image":["11",0]}},
      "13": {"class_type":"VAEDecode","inputs":{"samples":["12",0],"vae":["4",0]}},
      "19": {"class_type":"DualModelGuider","inputs":{"model":["8",0],"positive":["7",1],"cfg":7.0,"model_negative":["16",0],"negative":["18",0]}},
      "22": {"class_type":"Ideogram4Scheduler","inputs":{"steps":48,"width":896,"height":1344,"mu":0.0,"std":1.5}},
      "20": {"class_type":"RandomNoise","inputs":{"noise_seed":seed+1}},
      "21": {"class_type":"EmptyFlux2LatentImage","inputs":{"width":896,"height":1344,"batch_size":1}},
      "23": {"class_type":"SamplerCustomAdvanced","inputs":{"noise":["20",0],"guider":["19",0],"sampler":["5",0],"sigmas":["22",0],"latent_image":["21",0]}},
      "24": {"class_type":"VAEDecode","inputs":{"samples":["23",0],"vae":["4",0]}},
      "15": {"class_type":"AgenCCharacterSheetFinalize","inputs":{"image":["13",0],"portrait":["24",0]}},
      "14": {"class_type":"SaveImage","inputs":{"images":["15",0],"filename_prefix":prefix}},
    }

NULLA = ("An original 64-year-old woman, East African features, lean wiry build, deeply lined angular face "
  "with high flat cheekbones and a broad nose, close-cropped iron-grey hair worn about one centimetre long, "
  "her own left eye clouded milky pale blue from a failed ocular implant with a faint hairline scar running "
  "from that eyebrow down across the cheekbone, her own right eye dark brown and sharp, deeply weathered "
  "dark brown skin, both hands scarred with small round solder burns and old healed cuts, wearing a heavy "
  "quilted charcoal-grey work coat covered in dozens of small stitched utility pockets over a faded rust-red "
  "thermal shirt, a black magnifier headband rig with two flip-down lenses pushed up onto her forehead, "
  "fingerless grey wool gloves")

if __name__ == "__main__":
    run(sheet_graph(NULLA, "reaper_queue/sheets/nulla", 452011), "PROOF nulla sheet")
