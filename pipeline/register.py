import sys
sys.path.insert(0,"/tmp/user/1000/claude-1000/-home-tetsuo-AI-ComfyUI/a1fcaa85-dc71-4bb6-9633-7e14d3cfdffc/scratchpad/rq")
from driver import run

PROJECT="reaper_queue"
REFS=[("nulla","character","Nulla"),("wren","character","Wren"),("tally","character","Tally"),
      ("kiosk","location","Repair kiosk"),("market","location","Underlevel market"),
      ("transit","location","Transit concourse"),
      ("drive","prop","Data drive"),("keycard","prop","Signing key card")]

for alias, kind, disp in REFS:
    g={"1":{"class_type":"LoadImage","inputs":{"image":f"rq_refs/{alias}.png","upload":"image"}},
       "2":{"class_type":"ApproveH3ReferenceImage","inputs":{"image":["1",0],"project":PROJECT,
            "alias":alias,"kind":kind,"variant":"hero","make_default":True,
            "display_name":disp,"notes":"The Reaper Queue approved reference"}},
       "3":{"class_type":"SaveText","inputs":{"text":["2",1],"filename_prefix":f"rq_refs/{alias}_record","extension":"json"}}}
    run(g, f"approve @{alias}")
