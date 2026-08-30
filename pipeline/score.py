import sys
sys.path.insert(0,"/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq")
from driver import run

TAGS = ("instrumental, no vocals, dark ambient, industrial drone, slow cinematic build, sparse analog sub bass, "
        "low sustained strings, tape hiss, room tone, distant metallic clank, minimal, melancholy, tense, "
        "no drums until late, soft kick entering in the final third, 68 bpm, film score, underscore")

g = {
 "1":{"class_type":"CheckpointLoaderSimple","inputs":{"ckpt_name":"ace_step_v1_3.5b.safetensors"}},
 "2":{"class_type":"TextEncodeAceStepAudio","inputs":{"clip":["1",1],"tags":TAGS,"lyrics":"","lyrics_strength":0.0}},
 "3":{"class_type":"TextEncodeAceStepAudio","inputs":{"clip":["1",1],
      "tags":"vocals, singing, voice, lyrics, spoken word, upbeat, cheerful, major key, pop, dance, distorted guitar",
      "lyrics":"","lyrics_strength":0.0}},
 "4":{"class_type":"EmptyAceStepLatentAudio","inputs":{"seconds":94.0,"batch_size":1}},
 "5":{"class_type":"KSampler","inputs":{"model":["1",0],"positive":["2",0],"negative":["3",0],
      "latent_image":["4",0],"seed":880417,"steps":50,"cfg":5.0,
      "sampler_name":"euler","scheduler":"simple","denoise":1.0}},
 "6":{"class_type":"VAEDecodeAudio","inputs":{"samples":["5",0],"vae":["1",2]}},
 "7":{"class_type":"SaveAudio","inputs":{"audio":["6",0],"filename_prefix":"reaper_queue/score"}},
}
run(g,"score 94s")
