import sys
sys.path.insert(0,"/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq")
from driver import run
from shots_h3 import SHOTS, frames_for

PROJECT="reaper_queue"
LORA=("h3_gits_aesthetic_124f_r16_20260812_compiled20steady/"
      "h3_gits_aesthetic_124f_r16_20260812_compiled20steady_preview_step_000452.safetensors")
W,H,FPS,STEPS = 1024, 576, 24.0, 20


WARDROBE = {
 "@nulla": (" @nulla is a 64 year old East African woman with close-cropped iron-grey hair and a blind "
   "milky-white left eye, wearing a heavy quilted charcoal-grey padded work coat with many small pockets "
   "over a faded rust-red thermal shirt, and a black magnifier loupe headband."),
 "@wren": (" @wren is a 19 year old woman wearing a bright high-visibility orange waterproof courier shell "
   "with silver reflective stripes over a black top."),
}
def reinforce(prompt):
    for alias, clause in WARDROBE.items():
        if alias in prompt:
            prompt += clause
    return prompt

def g_h3(prompt, prefix, length, seed):
    return {
     "2":{"class_type":"UNETLoader","inputs":{"unet_name":"minimax_h3_ref2va_pruned_int8_convrot.safetensors","weight_dtype":"default"}},
     "3":{"class_type":"LoraLoaderModelOnly","inputs":{"model":["2",0],"lora_name":LORA,"strength_model":1.0}},
     "4":{"class_type":"CLIPLoader","inputs":{"clip_name":"qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors","type":"minimax","device":"default"}},
     "5":{"class_type":"VAELoader","inputs":{"vae_name":"minimax_h3_video_vae_fp16.safetensors"}},
     "6":{"class_type":"VAELoader","inputs":{"vae_name":"minimax_h3_audio_vae_fp32.safetensors"}},
     "7":{"class_type":"MiniMaxH3NamedReferenceToVideo","inputs":{"clip":["4",0],"vae":["5",0],"audio_vae":["6",0],
          "project":PROJECT,"prompt":prompt,"width":W,"height":H,"length":length,"ref_image_size":"max"}},
     "8":{"class_type":"BasicScheduler","inputs":{"model":["3",0],"scheduler":"simple","steps":STEPS,"denoise":1.0}},
     "9":{"class_type":"BasicGuider","inputs":{"model":["3",0],"conditioning":["7",0]}},
     "10":{"class_type":"RandomNoise","inputs":{"noise_seed":seed}},
     "11":{"class_type":"KSamplerSelect","inputs":{"sampler_name":"res_multistep"}},
     "12":{"class_type":"SamplerCustomAdvanced","inputs":{"noise":["10",0],"guider":["9",0],"sampler":["11",0],
           "sigmas":["8",0],"latent_image":["7",1]}},
     "13":{"class_type":"VAEDecode","inputs":{"samples":["12",0],"vae":["5",0]}},
     "14":{"class_type":"VAEDecodeAudio","inputs":{"samples":["12",0],"vae":["6",0]}},
     "15":{"class_type":"CreateVideo","inputs":{"images":["13",0],"fps":FPS,"audio":["14",0]}},
     "16":{"class_type":"SaveVideo","inputs":{"video":["15",0],"filename_prefix":prefix,"format":"auto","codec":"auto"}},
     "17":{"class_type":"SaveText","inputs":{"text":["7",3],"filename_prefix":prefix+"_lock","extension":"json"}},
    }

only=sys.argv[1:] if len(sys.argv)>1 else None
for num, sec, name, prompt in SHOTS:
    if only and name not in only: continue
    run(g_h3(reinforce(prompt), f"reaper_queue/h3/{name}", frames_for(sec), 452000+num*211), f"{name} {sec}s")
