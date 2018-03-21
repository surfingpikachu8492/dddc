label start:
    stop music
    if not persistent.seen_intro:
        $ chapter = 0
        $ persistent.playthrough = 0
        call ch0_start
        call ch0_end
        $ renpy.pause(2.0)
        $ persistent.seen_intro = True
        $ renpy.full_restart(transition=None, label="splashscreen")

    $ chapter = 1
    call ch1
    call poem_

    $ chapter = 2
    call ch2
    call poem_

    $ chapter = 3
    call ch3
    call poem_

    $ chapter = 4
    call ch4_prologue

    call demo_exclusive
    call screen dialog("Congratulations! You've completed the demo!", ok_action=Return())

    $ persistent.playthrough += 1

    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    $ renpy.pause(4.0)
    $ quick_menu = True
return

label demo_exclusive:
    scene black with dissolve_scene_full
    $ renpy.pause(1)
    scene bg club_day with dissolve_cg
    play music t8


    m_glitch "Hmmm?"

    if poemwinner[2] in ('sayori', 'yuri', 'natsuki'):
        $ renpy.say(m_glitch, "That's weird. Isn't this the part where {doki} comes in?".format(doki=poemwinner[2].title()))
    else:
        m_glitch "That's weird. Isn't this the part where, well, {i}I{/i} come in?"

    m_glitch "Oh wait, that's right... that part of the script isn't written yet...{w=0.5} shoot!"
    m_glitch "Well... it makes sense, it's only a demo after all..."
    m_glitch "Why don't you come and join these guys on {a=https://discord.gg/YCTaq9u}{u}Discord{/u}{/a} or {a=https://www.youtube.com/channel/UCJmkdH2gku5rygs6GBTgyrQ}{u}YouTube{/a}{/u}?"

    m_glitch "That way you can always stay updated and see all the new stuff they have to share!"
    m_glitch "You might even help them! I think they would be glad to see more artists or composers on their team!"
    m_glitch "You could also help by spreading the word! I'm sure they'll appreciate some advertisement, you know?"
    m_glitch "I don't know about you, but I'm now morbidly curious to find out what happens next!"
    m_glitch "But I'm afraid that's all they've got for this moment, so..."
    m_glitch "I guess we'll both have to wait and see..."
    m_glitch "Okay, I won't hold you up any longer."
    m_glitch "See you next time! Hopefully it'll be soon!"
    $ style.say_dialogue = style.normal
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
