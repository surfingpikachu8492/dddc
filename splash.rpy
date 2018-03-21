








init python:
    menu_trans_time = 1

    splash_message_default = "This game is not suitable for those who like Horror,\nThose who like to play Original DDLC."

    splash_messages = [
    "Please support Doki Doki Literature Club."
    "Monika is watching you code."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


init python:
    if not persistent.do_not_delete:
        if persistent.playthrough <= 2:
            try: renpy.file("../characters/monika.chr")
            except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        if persistent.playthrough <= 1 or persistent.playthrough == 4:
            try: renpy.file("../characters/natsuki.chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
            try: renpy.file("../characters/yuri.chr")
            except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        if persistent.playthrough == 0 or persistent.playthrough == 4:
            try: renpy.file("../characters/sayori.chr")
            except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
        if persistent.playthrough == 0 or persistent.playthrough == 4:
            try: renpy.file("../characters/silverzone.chr")
            except: open(config.basedir + "/characters/silverzone.chr", "wb").write(renpy.file("silverzone.chr").read())
        if persistent.playthrough == 0 or persistent.playthrough == 4:
            try: renpy.file("../characters/jackburst.chr")
            except: open(config.basedir + "/characters/jackburst.chr", "wb").write(renpy.file("jackburst.chr").read())


label splashscreen:

    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")





    default persistent.first_run = False
    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "[config.name] is a Doki Doki Literature Club fan mod created by SilverZone430"
        "It is designed to be played only after the official game has been completed, and might contains spoilers for the official game."
        "The mod is designed to be like a dating sim. Your choices on a waifu depends on the poem you write."
        menu:
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
            "I agree.":
                pass
            "I don't care just get into the GOD DAMN GAME ALREADY!":
                "Woah... CHILL! I'm opening it!"
                pass
            "I don't agree.":
                "Disagree huh..."
                "Well done."
                "Can't believe you disagree it."
                "You know, i try to think of it..."
                "You actually haven't finish the game right?"
                "Maybe?... I don't know.."
                $ style.say_dialogue = style.edited
                "{cps=*3}Did you come back and see what is this message?{/cps}{nw}"
                "{cps=*3}Maybe you have already tried a lot of time to see this messages.{/cps}{nw}"
                $ style.say_dialogue = style.normal
                "Press OK to get out of this Disagreement."
                "Don't you ever press that again."
                $ renpy.call_screen("dialog", "OK.", ok_action=Return())
                $ renpy.call_screen("dialog", "Ok...", ok_action=Return())
                $ renpy.call_screen("dialog", "Okay.", ok_action=Return())
                $ renpy.call_screen("dialog", "Okay...", ok_action=Return())
                $ renpy.call_screen("dialog", "What...", ok_action=Return())
                $ renpy.call_screen("dialog", "What the heck?", ok_action=Return())
                "Just now I was thinking on it.."
                "Why do you disagree this?"
                "Is it because you trying to know what happen when you press disagree?"
                "I see..."
                "I want you to be honest, alright?"
                menu:
                    "Are you really really Disagree with this?"
                    "Yes.":
                        "I see..."
                        "I SEE!!!"
                        "DISAGREE????"
                        "I finally know the feeling when a developer trying to warning us and we just skip all of those {i}EULA{/i} for no reason."
                        $ renpy.call_screen("dialog", "What the heck do you want?", ok_action=Return())
                        "Nothing."
                        "Cause you disagree the {i}EULA{/i}, I'mma tell you something."
                        "I won't tell you that you are about to enter the game."
                        "But I'm sorry, you're not allowed to enter the mod."
                        $ persistent.first_run = True
                        $ renpy.call_screen("dialog", "Goodbye.", ok_action=Quit())
                    "No.":
                        "I see..."
                        "What a great honest."
                        "But i call it a {i}LIE{/i}"
                        "Because i don't trust people."
                        "But except you."
                        "But you pressed {i}'I don't agree'{/i}."
                        "I kinda Triggered."
                        "But..."
                        "You're not allowed to enter the mod... yet."
                        "Cause you pressed {i}I don't agree{/i}."
                        "We'll meet again.. Shall we?"
                        $ persistent.first_run = True
                        $ renpy.call_screen("dialog", "Alright.", ok_action=Return())
                        $ renpy.call_screen("dialog", "Goodbye.", ok_action=Quit())
            "I haven't completed the game yet.":
                "Get the fuck out of the fan mod. before you get killed. Okay?"
                "I'm sorry someone was messing my files but who is it?"
                "Oh i'm sorry but you're not allowed to play this mod until you complete the main game."
                "Goodbye."
                $ renpy.call_screen("dialog", "Goodbye...", ok_action=Quit())
        scene tos2
        with Dissolve(1.5)
        pause 1.0




        scene white
        with Dissolve(1.5)

        $ persistent.first_run = True



    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload and not _restart:
        jump autoload


    $ config.allow_skipping = False


    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)

    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"

        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None


    $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    return

screen main_menu() tag menu:




    style_prefix "main_menu"

    add "menu_bg"
    add "menu_art_y"
    add "menu_art_n"
    frame




    use navigation

    add "menu_particles"
    add "menu_particles"
    add "menu_particles"
    add "menu_logo"
    add "menu_art_s"
    add "menu_particles"
    add "menu_art_m"
    add "menu_fade"

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "v. [config.version]":
                style "main_menu_version"


    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
