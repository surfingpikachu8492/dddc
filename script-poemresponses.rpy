label poemresponse_start:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        $ skip_poem = False
        if not renpy.music.get_playing() or renpy.music.get_playing() not in (audio.t5, audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day with wipeleft_scene
        $ skip_transition = False
    label poemresponse_start2:
        $ skip_poem = False
        if poemsread == 0:
            $ menutext = "Who should I show my poem to first?"
        else:
            $ menutext = "Who should I show my poem to next?"

        menu:
            "[menutext]"

            "Sayori" if not s_readpoem:
                $ s_readpoem = True
                call poemresponse_sayori
            "Natsuki" if not n_readpoem:
                $ n_readpoem = True
                call poemresponse_natsuki
            "Yuri" if not y_readpoem:
                $ y_readpoem = True
                call poemresponse_yuri
            "Monika" if not m_readpoem:
                $ m_readpoem = True
                call poemresponse_monika

        $ poemsread += 1
        if poemsread < 4:
            jump poemresponse_loop

    $ s_readpoem = n_readpoem = y_readpoem = m_readpoem = False
    $ poemsread = 0
    scene bg club_day with wipeleft_scene
    return

label poemresponse_sayori:
    scene bg club_day
    with wipeleft_scene

    if chapter == 2:

        call poemresponse_2_sayori
    elif chapter == 3:

        call poemresponse_3_sayori
    return

label poemresponse_natsuki:
    scene bg club_day
    with wipeleft_scene

    if chapter == 2:

        call poemresponse_2_natsuki
    elif chapter == 3:

        call poemresponse_3_natsuki
    return

label poemresponse_yuri:
    scene bg club_day
    with wipeleft_scene

    if chapter == 2:

        call poemresponse_2_yuri
    elif chapter == 3:

        call poemresponse_3_yuri
    return

label poemresponse_monika:
    scene bg club_day
    with wipeleft_scene

    if chapter == 2:

        call poemresponse_2_monika
    elif chapter == 3:

        call poemresponse_3_monika
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
