import sys, os, glob, shutil
sys.path.insert(0,"/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq")
from driver import run
from shots import SHOTS, NEG

ROOT="/home/tetsuo/AI/ComfyUI"
IN=os.path.join(ROOT,"input","reaper_queue"); os.makedirs(IN, exist_ok=True)
W,H,FPS=832,480,16
def frames_for(sec): return int(round(sec*FPS/4))*4+1

def g_i2v(rel, motion, prefix, length, seed):
    return {
     "1":{"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":"wan2.2-i2v-rapid-aio-v10-nsfw.safetensors"}},
     "2":{"class_type":"LoadImage","inputs":{"image":rel,"upload":"image"}},
     "3":{"class_type":"CLIPTextEncode","inputs":{"clip":["1",1],"text":motion}},
     "4":{"class_type":"CLIPTextEncode","inputs":{"clip":["1",1],"text":NEG}},
     "5":{"class_type":"WanImageToVideo","inputs":{"positive":["3",0],"negative":["4",0],"vae":["1",2],
          "start_image":["2",0],"width":W,"height":H,"length":length,"batch_size":1}},
     "6":{"class_type":"ModelSamplingSD3","inputs":{"model":["1",0],"shift":5.0}},
     "7":{"class_type":"KSampler","inputs":{"model":["6",0],"positive":["5",0],"negative":["5",1],
          "latent_image":["5",2],"seed":seed,"steps":4,"cfg":1.0,
          "sampler_name":"euler_ancestral","scheduler":"beta","denoise":1.0}},
     "8":{"class_type":"VAEDecode","inputs":{"samples":["7",0],"vae":["1",2]}},
     "9":{"class_type":"CreateVideo","inputs":{"images":["8",0],"fps":FPS}},
     "10":{"class_type":"SaveVideo","inputs":{"video":["9",0],"filename_prefix":prefix,"format":"auto","codec":"auto"}},
    }

only=sys.argv[1:] if len(sys.argv)>1 else None
for num, sec, name, still, motion in SHOTS:
    if only and name not in only: continue
    src=sorted(glob.glob(f"{ROOT}/output/reaper_queue/frames/{name}_*.png"))
    if not src: print("MISSING",name); continue
    shutil.copy(src[-1], os.path.join(IN,name+".png"))
    run(g_i2v(f"reaper_queue/{name}.png", motion, f"reaper_queue/clips/{name}",
              frames_for(sec), 700000+num*211), f"{name} {sec}s")
