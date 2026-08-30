# H3 named-reference prompts. 24 fps. frames must be >= sec*24 and congruent to 5 mod 17.
LOCK = ("Preserve the exact identity, face, wardrobe and colour palette of every named reference. "
        "Lit only by practical sources visible in frame, sodium-amber dominant with one dead-cyan tube "
        "as the only cool accent. Deep crushed shadows, heavy dust in the light, fine 35mm grain, "
        "shallow depth of field, no camera shake, no lens flare.")
COLDLOCK = ("Preserve the exact identity, face and wardrobe of every named reference. Cold flat white-green "
        "fluorescent light, polished terrazzo, no warmth, no dust, fine 35mm grain, no camera shake.")

SHOTS = [
 (1,4,"s01_drive_insert",
  "A single continuous cinematic shot. Extreme close-up of an old scarred dark-skinned hand pushing @drive "
  "into a slot in a battered steel reader unit inside @kiosk. Condensation on the casing, the amber status "
  "light pulses once and steadies, dust drifts through the lamp light. Almost no camera movement. "+LOCK),
 (2,3,"s02_tally_cold",
  "A single continuous cinematic shot. Extreme close-up of @tally on a screen in darkness. The small square "
  "tiles that make up the face flicker and resettle one by one as it finishes assembling, then the eyes "
  "settle and look directly into the lens. Very slow push in, scanlines drift. Cold dead-cyan and blue-grey "
  "palette, black background, CRT phosphor glow. Preserve the exact mosaic face identity of @tally."),
 (3,6,"s03_market_wide",
  "A single continuous cinematic shot. Wide establishing shot down the empty aisle of @market. Rain falls "
  "steadily through the broken ceiling panel into a plastic bucket, the strung bulbs sway very slightly, "
  "reflections ripple in the standing water. No people. Extremely slow forward drift. "+LOCK),
 (4,5,"s04_nulla_bench",
  "A single continuous cinematic shot. Medium shot of @nulla seated at the workbench in @kiosk under the "
  "articulated bench lamp, her loupe rig flipped down, soldering a small circuit board. A thin wisp of solder "
  "smoke rises through the lamp light, the wall of small screens behind her flickers at different rates. "
  "Static camera. "+LOCK),
 (5,4,"s05_queue_monitor",
  "A single continuous cinematic shot. Insert, close on a cracked amber-phosphor CRT monitor in @kiosk "
  "showing a vertical list of monospaced rows on black with one row highlighted. The rows shift upward by "
  "one line and the highlighted row moves nearer the top. Scanlines roll slowly, the amber glow pulses "
  "faintly. Locked static camera. "+LOCK),
 (6,5,"s06_nulla_cu",
  "A single continuous cinematic shot. Tight close-up of @nulla in @kiosk, loupe rig pushed up on her "
  "forehead, lit warmly from one side by a bench lamp just out of frame. Her clouded blind left eye catches "
  "the light. She listens to something off screen, then turns her head slightly and speaks a short quiet "
  "sentence, her lips moving naturally, and blinks once. Static camera. "+LOCK),
 (7,5,"s07_wren_enters",
  "A single continuous cinematic shot. Medium shot of @wren pushing through the hanging plastic strip curtain "
  "into @kiosk, soaked with rain, water beading on her orange shell. The plastic strips swing and settle "
  "behind her. She shakes rain from her sleeve and flips the badge on its reel face down against her chest. "
  "Slight handheld movement. "+LOCK),
 (8,5,"s08_card_slide",
  "A single continuous cinematic shot. Two shot across the workbench in @kiosk, @nulla seated on the left and "
  "@wren standing on the right, with @keycard lying on the steel between them. @nulla slides @keycard slowly "
  "across the bench toward @wren and lifts her fingers off it. @wren looks down at it but does not reach for "
  "it. Static camera. "+LOCK),
 (9,5,"s09_wren_reads",
  "A single continuous cinematic shot. Tight close-up of @wren in @kiosk looking down at @keycard held in her "
  "hands, lit from below by the warm bench lamp. Her eyes track down across it, then she looks up off camera "
  "and asks a short question, her lips moving naturally. Static camera. "+LOCK),
 (10,5,"s10_hand_reader",
  "A single continuous cinematic shot. Close on two hands on a battered steel reader plate on the workbench "
  "in @kiosk. The older scarred hand of @nulla presses the younger hand of @wren flat down onto the glowing "
  "amber contact plate. The light under the palm brightens and steadies. Both hands hold still, dust drifts. "
  "Almost no camera movement. "+LOCK),
 (11,4,"s11_lights_fail",
  "A single continuous cinematic shot. Wide locked shot down the aisle of @market. The strung overhead lights "
  "go out one after another in sequence from the far end toward the camera, a hard wall of darkness advancing "
  "steadily down the aisle at walking pace. No people, no alarm. Locked static camera. "+LOCK),
 (12,5,"s12_shove",
  "A single continuous cinematic shot. Medium two shot in @kiosk with most of the frame behind them already "
  "fallen dark. @nulla presses @drive hard into the chest of @wren and folds her fingers closed over it, then "
  "turns away from her to face the darkness. Slight handheld movement. "+LOCK),
 (13,4,"s13_run",
  "A single continuous cinematic shot. Tracking from behind @wren running hard away from camera down the dark "
  "aisle of @market, her orange shell the only bright thing in frame, closed shutters blurring past on both "
  "sides, two dim amber bulbs far ahead. The screens of a kiosk behind her flare white then go black. Motion "
  "blur, handheld. "+LOCK),
 (14,5,"s14_empty_kiosk",
  "A single continuous cinematic shot. Wide locked shot of @kiosk abandoned. The empty wheeled stool rotates "
  "slowly to a stop on its own, tools left mid-repair, the wall of screens now all dead and black. Dust "
  "drifts down through a single shaft of light. Nothing else moves. Completely locked static camera. "+LOCK),
 (15,5,"s15_transit_still",
  "A single continuous cinematic shot. Medium shot of @wren standing perfectly still in the middle of "
  "@transit while a dense crowd of commuters streams past her on both sides in motion blur. Her orange shell "
  "is the only saturated colour in frame. Static camera. "+COLDLOCK),
 (16,6,"s16_handing_out",
  "A single continuous cinematic shot. Medium shot of @wren in @transit holding @drive up at shoulder height, "
  "then pressing small copies into the open hands reaching toward her from the edges of frame one after "
  "another. Hands take them and withdraw, more hands arrive. Slow push in. "+COLDLOCK),
 (17,6,"s17_overhead_spread",
  "A single continuous cinematic shot. High overhead looking straight down at the dense crowd on the pale "
  "floor of @transit, people reading as small dark shapes. A bright ripple spreads outward through the crowd "
  "from a single bright orange figure at the centre, passing from person to person across the whole floor "
  "until the orange figure is absorbed into the crowd. Slow rise upward. "+COLDLOCK),
 (18,5,"s18_thousand_screens",
  "A single continuous cinematic shot. Wide shot of a vast dense crowd at night, already lit from below by "
  "hundreds of small handheld screens held up at many different heights, filling the whole frame from "
  "foreground to far background. Every screen shows the face of @tally rebuilt from warm golden tiles. The "
  "faces of the crowd are clearly visible in the warm screen glow. More screens keep rising and lighting up. "
  "The frame is bright and full of glowing screens from the very first frame, never black, never empty. "
  "Very slow push in. Warm sodium-amber and gold palette, fine grain."),
(19,3,"s19_final_screen",
  "A single continuous cinematic shot. Extreme close-up of a single small handheld screen held in an "
  "anonymous hand in darkness, showing the face of @tally rebuilt from warm golden tiles of smiling people. "
  "The face looks directly out of the screen and speaks one short sentence, its lips moving, then the screen "
  "goes dark. Locked static camera. Warm amber palette, black background, soft screen glow, fine grain."),
]

def frames_for(sec):
    f = max(5, round(sec*24))
    while f % 17 != 5 or f < sec*24:
        f += 1
    return f
