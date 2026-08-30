# Shot definitions for THE REAPER QUEUE. sec -> frames = round(sec*16/4)*4+1
NULLA = ("a lean wiry 64-year-old East African woman with close-cropped iron-grey hair, her left eye completely "
  "clouded milky white and sightless, a black magnifier loupe headband pushed up on her forehead, wearing a "
  "heavy quilted charcoal work coat with many small pockets over a rust-red thermal shirt")
WREN = ("a slight 19-year-old woman with light brown skin and dark hair pulled back, wearing a bright "
  "high-visibility orange waterproof courier shell with silver reflective stripes over a black top")
LOOK = ("Lit only by practical sources visible in frame, sodium-amber worklight dominant with one dead-cyan tube "
  "as the only cool accent. Deep crushed shadows, heavy dust in the light, fine 35mm grain, anamorphic cinematic "
  "framing, shallow depth of field, no lens flare.")
COLD = ("Cold flat white-green fluorescent light, clean polished terrazzo, no warmth, no dust, "
  "fine 35mm grain, anamorphic cinematic framing.")
NEG = ("dinner plate, dish, bowl, crockery, text overlay, subtitles, watermark, logo, lens flare, neon pink, "
  "magenta, teal and orange grade, oversaturated, HDR, glossy, cartoon, illustration, 3d render, blurry, "
  "lowres, deformed hands, extra fingers, extra limbs, distorted face")

SHOTS = [
 (1,4,"s01_drive_insert",
  "Extreme close-up of a scarred weathered dark-skinned hand pushing a small cracked matte-black data drive into "
  "a slot in a battered steel reader unit. Condensation beads on the metal casing. A single amber status LED "
  "glows. Shallow macro focus on the drive, background falling away into darkness. "+LOOK,
  "the hand slowly pushes the drive fully into the slot, the amber status light pulses once and steadies, "
  "faint dust drifts through the light, almost no camera movement"),

 (2,3,"s02_tally_cold",
  "Extreme close-up of a human face entirely constructed from a mosaic of hundreds of small square blue-grey "
  "video thumbnails, like a photomosaic, visible tile seams and scanlines, reading as one calm symmetrical "
  "androgynous face looking straight at the camera. Cold dead-cyan and blue-grey palette, black background, "
  "CRT phosphor glow, heavy scanlines, fine grain.",
  "the small square tiles flicker and resettle one by one as the face finishes assembling, the eyes settle and "
  "look directly into the lens, very slow push in, scanlines drift"),

 (3,6,"s03_market_wide",
  "Wide shot down a deserted underground market avenue on the lowest level of an arcology, shuttered corrugated "
  "roller stalls receding into darkness, bare sodium bulbs strung on sagging cable overhead, a broken ceiling "
  "panel with rain falling through into a plastic bucket, standing water reflecting amber light, one dead-cyan "
  "tube far down the aisle. No people. "+LOOK,
  "rain falls steadily through the broken ceiling panel into the bucket, the strung bulbs sway very slightly, "
  "reflections ripple in the standing water, extremely slow forward drift"),

 (4,5,"s04_nulla_bench",
  "Medium shot of "+NULLA+", seated at a scarred steel workbench under a single articulated bench lamp in a "
  "cramped concrete repair kiosk, soldering a small circuit board, her loupe rig flipped down over her eyes. "
  "Behind her a tall scrap rack of thirty small mismatched CRT screens each showing a different washed-out "
  "still. "+LOOK,
  "she works steadily at the board, a thin wisp of solder smoke rises through the lamp light, the CRT screens "
  "behind her flicker at different rates, static camera"),

 (5,4,"s05_queue_monitor",
  "Insert shot, close on a cracked amber-phosphor CRT monitor showing a simple list of rows of monospaced text "
  "on black, one row highlighted, the screen dusty and scratched with a hairline crack across one corner. "
  "Shot slightly off axis. Amber phosphor glow is the only light source. Heavy scanlines, fine grain.",
  "the rows of text on the screen shift upward by one line, the highlighted row moves nearer the top, "
  "scanlines roll slowly, the amber glow pulses faintly, locked static camera"),

 (6,5,"s06_nulla_cu",
  "Tight close-up of "+NULLA+", loupe rig pushed up on her forehead, lit warmly from one side by a bench lamp "
  "just out of frame, dark concrete behind her. Her clouded left eye catches the light. She is listening to "
  "something off screen. "+LOOK,
  "she listens, then turns her head slightly and speaks a short quiet sentence to someone off camera, her jaw "
  "and lips moving naturally, she blinks once, static camera"),

 (7,5,"s07_wren_enters",
  "Medium shot of "+WREN+" pushing through a hanging plastic strip curtain into a cramped amber-lit concrete "
  "repair kiosk, soaked with rain, water beading on the orange shell. She is backlit by cold light from the "
  "corridor behind her and lit warm from the front by a bench lamp. "+LOOK,
  "she pushes through the plastic strips and they swing and settle behind her, she shakes rain from her sleeve "
  "and flips a badge on a reel face down against her chest, slight handheld movement"),

 (8,5,"s08_card_slide",
  "Two shot across a scarred steel workbench in an amber-lit concrete kiosk: on the left "+NULLA+" seated, on "
  "the right "+WREN+" standing. Between them on the bench lies a small dog-eared cream paper card printed with "
  "a dense block of tiny monospaced characters. "+LOOK,
  "the older woman slides the small paper card slowly across the steel bench toward the younger woman and lifts "
  "her fingers off it, the younger woman looks down at it but does not reach for it, static camera"),

 (9,5,"s09_wren_reads",
  "Tight close-up of "+WREN+" looking down at a small cream paper card held in her hands, lit from below by the "
  "warm bench lamp, dark concrete behind. Her expression is uncertain. "+LOOK,
  "she reads the card, her eyes tracking down across it, then she looks up off camera and asks a short question, "
  "her lips moving naturally, static camera"),

 (10,5,"s10_hand_reader",
  "Close shot of two hands on a battered steel reader plate on a workbench: an older scarred dark-skinned hand "
  "pressing a younger hand flat down onto the glowing amber contact plate. Warm amber light spills up between "
  "the fingers. Shallow focus. "+LOOK,
  "the older hand presses the younger hand flat onto the plate, the amber light under the palm brightens and "
  "steadies, both hands hold still, faint dust drifts, almost no camera movement"),

 (11,4,"s11_lights_fail",
  "Wide shot down the deserted underground market avenue, shuttered stalls on both sides receding into darkness, "
  "strung sodium bulbs overhead. The far half of the avenue is already pitch black, the near half still lit "
  "amber, with a hard advancing edge of darkness between them. No people. "+LOOK,
  "the strung overhead lights go out one after another in sequence from the far end toward the camera, the wall "
  "of darkness advancing steadily down the aisle at walking pace, locked static camera"),

 (12,5,"s12_shove",
  "Medium two shot in a dim amber-lit concrete kiosk: "+NULLA+" facing "+WREN+", pressing a small cracked black "
  "data drive hard into the younger woman's chest and closing her fingers around it. Most of the frame behind "
  "them has already fallen dark. "+LOOK,
  "the older woman presses the drive into the younger woman's chest and folds her fingers closed over it, then "
  "turns away from her to face the darkness, slight handheld movement"),

 (13,4,"s13_run",
  "Tracking shot behind "+WREN+" running away from camera down a dark underground market aisle, her orange "
  "shell the only bright thing in frame, shuttered stalls blurring past on both sides, a few amber bulbs still "
  "lit far ahead. "+LOOK,
  "she runs hard away from camera down the aisle, the camera follows behind her at speed, the screens of a "
  "kiosk behind her flare white and then go black, motion blur, handheld"),

 (14,5,"s14_empty_kiosk",
  "Wide locked shot of an abandoned repair kiosk: an empty wheeled stool turned slightly away from a scarred "
  "steel workbench, tools and circuit boards left mid-repair, the tall rack of CRT screens behind it now all "
  "dead and black. A single shaft of light falls from one working fixture overhead. Thick dust in the beam. "+LOOK,
  "the empty stool rotates slowly to a stop on its own, dust drifts down through the single shaft of light, "
  "nothing else moves, completely locked static camera"),

 (15,5,"s15_transit_still",
  "Medium shot of "+WREN+" standing completely still in the middle of a vast cold transit concourse packed with "
  "blurred commuters streaming past her on both sides, polished terrazzo underfoot, rows of turnstile gates "
  "behind. Her orange shell is the only saturated colour in the frame. "+COLD,
  "the crowd streams past her on both sides in motion blur while she stands perfectly still looking ahead, "
  "static camera, long exposure feel"),

 (16,6,"s16_handing_out",
  "Medium shot of "+WREN+" standing in a crowded cold transit concourse holding up a small black data drive at "
  "shoulder height, with several strangers' hands reaching in toward her from the edges of frame. "+COLD,
  "she holds the drive up, then begins pressing small copies into the open hands reaching toward her one after "
  "another, hands take them and withdraw, more hands arrive, slow push in"),

 (17,6,"s17_overhead_spread",
  "High overhead looking straight down at a dense crowd of commuters on a pale terrazzo concourse floor, seen "
  "from far above so people read as small dark shapes. One small bright orange figure stands near the centre. "+COLD,
  "seen from directly above, a bright ripple spreads outward through the dark crowd from the single orange "
  "figure at the centre, passing outward from person to person across the whole floor, the orange figure is "
  "absorbed into the crowd, slow rise upward"),

 (18,5,"s18_thousand_screens",
  "Wide shot in near total darkness of a vast crowd seen only as hundreds of small glowing handheld screens "
  "held up at different heights, each screen showing the same warm amber mosaic face made of tiny golden "
  "thumbnails. The faces of the crowd are barely visible in the screen glow. Warm amber palette, black "
  "background, fine grain, anamorphic cinematic framing.",
  "the small screens light up one after another across the darkness at different moments until hundreds are "
  "glowing, each showing the same warm face, very slow push in"),

 (19,3,"s19_final_screen",
  "Extreme close-up of a single small handheld screen held in an anonymous hand in darkness, showing a human "
  "face entirely constructed from a mosaic of hundreds of tiny warm golden thumbnails of smiling people, "
  "visible tile seams, the face looking directly out of the screen. Warm amber palette, black background, "
  "soft screen glow, fine grain.",
  "the mosaic face on the small screen looks directly out at the camera and speaks one short sentence, its lips "
  "moving, then the screen goes dark, locked static camera"),
]
