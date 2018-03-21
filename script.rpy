


label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer


    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True




    if persistent.playthrough == 0:

        $ chapter = 0
        call ch0_main
        call ch0_afterday


        call poem
        python:
            try: renpy.file(config.basedir + "/A-Little-Easter-Egg.txt")
            except: open(config.basedir + "/A Little Easter Egg", "wb").write(renpy.file("/Scripts/A-Little-Easter-Egg.txt").read())


        $ chapter = 1
        call ch1_main
        call end_demo

        jump credits
        return
    if persistent.playthrough == 1:

        pass

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
