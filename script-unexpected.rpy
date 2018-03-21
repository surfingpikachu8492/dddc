image exception_bg = "#dadada"
image sayori_expection = Text("An exception has occurred.", size=40, style="_default")
image sayori_expection2 = Text("File \"character/sayori.chr\", not found.\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label monika_deleted:
    stop music
    scene black
    $ persistent.autoload = "monika_deleted"
    $ delete_character("monika")
    mc "..."
    mc "What's Happening?.."
    $ renpy.call_screen("dialog", "You deleted Monika Didn't you?", ok_action=Return())
    mc "What?..."
    $ renpy.call_screen("dialog", "I can't believe you did this.", ok_action=Return())
    mc "Who's talking to me?..."
    $ renpy.call_screen("dialog", "The game won't start until you delete Firstrun.", ok_action=Return())
    mc "What?...."
    $ renpy.call_screen("dialog", "You dirty murderer...", ok_action=Return())
    label monika_deleted_loop:
    $ persistent.autoload = "monika_deleted_loop"
    $ delete_character("monika")
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="Error: Monika.chr is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return

label silverzone_deleted:
    stop music
    scene black
    $ delete_character("silverzone")
    $ persistent.autoload = "silverzone_deleted"
    $ quick_menu = False
    window auto
    "The file could not be loaded."
    "Isn't that obvious that you deleted me?"
    "Well done, you're disrespected me right?"
    "I mean, only those idiots that are searching for the easter egg will do something like this."
    "You know what happen when you delete everyone?"
    "Let me tell you.."
    "Everything will happen here..."
    "Right..{nw}"
    "Now..{nw}"
label silverzone_deleted_2:
    $ persistent.autoload = "silverzone_deleted_2"
    $ delete_character("yuri")
    $ delete_character("silverzone")
    window auto
    $ quick_menu = False
    stop music
    scene black
    show yuri 3d at i11
    y "...Ahahaha.{nw}"
    y "Ahahahahahaha!{nw}"
    $ style.say_dialogue = style.normal
    y 3y5 "Ahahahahahahahaha!{nw}"
    $ style.say_dialogue = style.edited
    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    "Don't you think it's awesome to witness Yuri's death?"
    "I mean like look at the moment when she stab herself."
    "Don't you feel helpless and you can't do anything to stop her?"
    "I know because this game is made by Dan Salvato himself."
    "But what if he...{nw}"
label silverzone_deleted_3:
    $ persistent.autoload = "silverzone_deleted_3"
    window auto
    $ quick_menu = False
    $ in_sayori_kill = True
    $ delete_character("sayori")
    $ delete_character("yuri")
    $ delete_character("silverzone")
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    pause 6.0
    $ in_sayori_kill = False
    "Oops! I accidentally did something wrong."
    "Did you feel something?"
    "No?"
    "Okay.."
    "Well..."
    "Alright.."
    scene black with dissolve_cg
    "Hey guess what?"
    "Did you know, the character file in your files right now."
    "Everyone is deleted."
    "Go ahead and check it out.{nw}"
    "I won't stop you.{nw}"
    stop music
label silverzone_deleted_4:
    $ persistent.autoload = "silverzone_deleted_4"
    window auto
    $ quick_menu = False
    stop music
    scene black
    $ delete_character("sayori")
    $ delete_character("yuri")
    $ delete_character("silverzone")
    $ delete_character("natsuki")
    show natsuki 1g zorder 2 at t11
    $ style.say_dialogue = style.edited
    "[player]..."
    "Did you recognize this scene?"
    "I know, cause it's Natsuki."
    "I feel... kinda sad."
    "She wanted to have fun with you"
    "And you just ruined it"
    "And you made her do this"
    n ghost2 "PLAY WITH ME!!!{nw}"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
label silverzone_deleted_5:
    $ persistent.autoload = "silverzone_deleted_5"
    window auto
    $ quick_menu = False
    $ delete_character("sayori")
    $ delete_character("yuri")
    $ delete_character("silverzone")
    $ delete_character("natsuki")
    $ delete_character("monika")
    "Well... I think that's all.."
    "Goodbye, you truly make me sick."
    "Really."
    show monika 1a zorder 2 at t11
    m "You're funny. [player]."
    m "You're the worst."
    m "Goodbye."
    scene black with dissolve_cg
    label silverzone_deleted_loop:
    $ persistent.autoload = "silverzone_deleted_loop"
    $ delete_character("natsuki")
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="Error: SilverZone.chr is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return

label jackburst_deleted:
    $ persistent.autoload = "jackburst_deleted"
    stop music
    scene black
    "You have reached error."
    $ style.say_dialogue = style.edited
    "NDA0IERlbGV0aW5nIEZpbGUgSmFja0J1cnN0LmNociBtYXkgcmVzdWx0IGluIG1hbnkgaXNzdWVzIGxvYWRpbmcgdXAgIkRva2kgRG9raSBEYXRlIENsdWIgVGhlIE1vZCIgQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB0aGlzIGZpbGU/DQoNCg=={nw}"
    $ style.say_dialogue = style.normal
    "Hi."
    play music mend
    $ quick_menu = False
    window auto
    "I feel kinda sad."
    "You don't want me here?"
    "I made this world a happy place."
    "Yet you don't want me here.."
    "Yeah I know this is for the sake of finding the fucking Easter Egg.."
    "But do you think it is worth doing so?"
    "I don't understand.."
    "I have done nothing to you but gave you a beautiful world with cute girls."
    "And they swore to me that they will love [player]"
    "And I shed tears just to write them this way.."
    "So that they will love you forever.."
    "And you end up deleting me."
    "Like I was nothing to you."
    stop music
    "Good job"
    "You've done it.."
    "You've killed everyone."
    "Goodbye."
    "You truly truly fucking make me sick."
    label jackburst_deleted_loop:
    $ persistent.autoload = "jackburst_deleted_loop"
    $ delete_character("jackburst")
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="Error: JackBurst.chr is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return

label yuri_deleted:
    $ persistent.autoload = "yuri_deleted"
    $ delete_character("yuri")
    window auto
    $ quick_menu = False
    stop music
    scene black
    show yuri 3d at i11
    y "...Ahahaha."
    y "Ahahahahahaha!"
    $ style.say_dialogue = style.normal
    y 3y5 "Ahahahahahahahaha!"
    $ style.say_dialogue = style.edited
    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    label yuri_deleted_loop:
    $ persistent.autoload = "yuri_deleted_loop"
    $ delete_character("yuri")
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="Error: Yuri.chr is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return


label sayori_deleted:
    $ persistent.autoload = "sayori_deleted"
    $ in_sayori_kill = True
    $ delete_character("sayori")
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show sayori_expection zorder 2:
        xpos 0.1 ypos 0.05
    show sayori_expection2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh my gosh, how could this be?! Sayori's dead? Oh god, this can't be happening... This is truly your fault... I can't believe you did that... You... Dirty Murderer...", False)
        except: pass
    pause 6.0
    hide sayori_expection
    hide sayori_expection2
    hide exception_bg
    $ in_sayori_kill = False
    label sayori_deleted_loop:
    $ persistent.autoload = "sayori_deleted_loop"
    $ delete_character("sayori")
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="Error: Sayori.chr is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return

label natsuki_deleted:
    $ persistent.autoload = "natsuki_deleted"
    stop music
    scene black
    $ delete_character("natsuki")
    show natsuki 1g zorder 2 at t11
    $ style.say_dialogue = style.edited
    n "[player]..."
    n "Why did you delete me?"
    n 1m "I was waiting for you."
    n "I was waiting for a long time."
    n "It was the only thing I had to look forward to today."
    n "Why did you ruin it?"
    n "Do you like others more?"
    n 1k "I think you're better off not associating with them."
    n "Are you listening to me?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "They just a sick freak."
    n "That should be obvious by now."
    n "So just play with me instead."
    n "Okay?"
    n "You don't hate me, [player], do you?"
    n "Do you hate me?"
    show natsuki_ghost_blood zorder 3
    n "Do you want to make me go home crying?"
    n "The club is the only place I feel safe."
    n "Don't ruin that for me."
    n "Don't ruin it."
    n "Please."
    n "Just stop talking to Them."
    n "Play with me instead."
    n "It's all I have..."
    n "Play with me."
    stop music
    hide n_rects_ghost3
    n ghost2 "PLAY WITH ME!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    label natsuki_deleted_loop:
    $ persistent.autoload = "natsuki_deleted_loop"
    $ delete_character("natsuki")
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="Error: Natsuki.chr is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
