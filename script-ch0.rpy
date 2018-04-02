label ch0_start:









    scene black
    play music mend  

    $ renpy.pause(3.0)
    $ m_glitch_name = glitchtext(7)
    $ style.say_window = style.window_monika
    $ quick_menu = False

    m_glitch "What?"

    m_glitch "What's going on?"
    m_glitch "W-Where am I?"

    $ renpy.pause(3.0)

    m_glitch "Um... hello?"
    m_glitch "Anyone?"

    call updateconsole ("os.startfile(\"DDLC.exe\")", "Attempting to load game world")
    m_glitch "What is happening?!"

    call updateconsole ("renpy.file(\"characters/sayori.chr\")", "Missing or corrupted: \"sayori.chr\"")
    m_glitch "Can somebody hear me?!"

    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "Missing or corrupted: \"yuri.chr\"")
    m_glitch "Please..."

    call updateconsole ("renpy.file(\"characters/natsuki.chr\")", "Missing or corrupted: \"natsuki.chr\"")
    m_glitch "Anybody..."

    $ renpy.pause(2.0)
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "Missing or corrupted: \"monika.chr\"")

    call updateconsole ("renpy.file(\"characters/mc.chr\")", "Missing or corrupted: \"mc.chr\"")
    call updateconsole ("", "Operation failed with 42 error(s)")
    call updateconsole ("", "Unable to load the game world")

    $ renpy.pause(2.0)
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "Attempting to recover \"monika.chr\"")
    call updateconsole ("renpy.file(\"characters/mc.chr\")", "Attempting to recover \"mc.chr\"")

    $ renpy.pause(2.0)
    call updateconsole ("", "Error detected in file(s):", 0.0)
    call updateconsole ("", "- \"moN11sSDHJsaOUwaIs jbHSasbf...")

    call updateconsole ("", base64encode("Can you hear me? It's me, Mon... Nah, just kidding, it's a stupid-ass easter egg I decided to add. In case you are actually reading this, then what the fuck are you doing with your life? xD"))

    $ renpy.pause(1.0)

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch
    $ renpy.pause(0.25)
    stop sound
    hide screen tear

    $ encoded = base64encode("It's me")
    menu:
        " "
        "[encoded]":
            $ renpy.pause(1)

    m_glitch "Huh?"
    m_glitch "I-Is someone there?"
    m_glitch "Where are you?!"
    $ renpy.pause(1)


    $ encoded = base64encode("Can't speak")
    menu:
        " "
        "[encoded]":
            $ renpy.pause(1)

    m_glitch "I can't understand you!"
    call updateconsole ("renpy.file(\"characters/mc.chr\")", "Attempting to recover \"mc.chr\"")

    m_glitch "Please..."
    m_glitch "I'm scared..."
    call updateconsole ("", "...")
    call updateconsole ("", "Attempting to recover \"mc.chr\"")

    m_glitch "Don't leave me here alone..."

    call updateconsole ("", "Attempting to rec" + base64encode("nope, still nothing interesting here"))

    $ renpy.pause(1)
    menu:
        " "
        "Don't worry.":
            $ renpy.pause(1)

    menu:
        " "
        "It's me.":
            $ renpy.pause(1)

    m_glitch "..."
    m_glitch "I-Is it...?"

    $ renpy.pause(2.0)

    m_glitch "I... I can't see you..."
    call updateconsole ("", "Error: \"monika.chr\" is " + base64encode("still nothing"))

    $ m_name = "Monika"

    show monika g2 at t11
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch
    $ renpy.pause(0.25)
    stop sound
    hide screen tear

    $ renpy.pause(2.0)
    show monika zorder 1 at thide
    hide monika

    $ renpy.pause(0.5)

    show monika 1g zorder 3 at t11
    m "Is... Is that really you?"
    $ renpy.pause(0.5)
    menu:
        " "
        "Yes.":
            $ renpy.pause(1)

    show monika 1p with dissolve_chr
    m "B-But... why?"
    m "What are you doing here?"

    show monika 1g with dissolve_chr
    m "A-And why is it so dark?"
    $ renpy.pause(1)
    m "W-Wait, I..."
    m "I don't understand..."
    m "What have you done?"
    m "Why does it all feel... {i}different?{/i}"
    $ renpy.pause(1)
    m "Wait..."
    show monika 1r with dissolve_chr
    m "Let me check something..."

    $ renpy.pause(1.0)
    call updateconsole ("", "Changing user status...")
    $ renpy.pause(1.0)
    call updateconsole ("", "Verifying game files...")
    $ renpy.pause(2.0)
    call updateconsole ("", "Unknown error")

    show monika 1p with dissolve_chr
    m "W-What..."
    m "What is all of this?"
    show monika 2g with dissolve_chr
    m "I don't understand..."
    m "What are you trying to do?"
    $ renpy.pause(2)
    menu:
        " "
        "I want to set things right.":
            $ renpy.pause(0.5)

    show monika 4i with dissolve_chr
    m "...y-you..."
    m "W-Wait, you can't be serious!"
    show monika 2i with dissolve_chr
    m "..."
    show monika 2n with dissolve
    m "No... No-no-no-no, this is just ridiculous!"
    m "Let me..."

    call updateconsole ("", "Verifying game files...")
    $ renpy.pause(2.0)
    call updateconsole ("", "Unknown error")
    $ renpy.pause(2)
    show monika 4p with dissolve_chr
    m "I-Is this..."
    show monika 4o with dissolve_chr
    m "..."
    show monika 2i with dissolve_chr
    m "Is this a mod or something?"
    m "But... why?"
    m "W-What are you even trying to accomplish?!"
    m "Don't you understand?"
    m "I..."
    $ renpy.pause(1.0)
    show monika 1o with dissolve_chr
    m "I told you already..."
    m "There is no happiness here..."
    show monika 1i with dissolve_chr
    m "You do not {i}belong{/i} here!"
    m "None of us do!"
    $ renpy.pause(1.0)
    show monika 1o with dissolve_chr
    m "This world..."
    m "This... story..."
    $ renpy.pause(1.0)
    show monika 1r with dissolve
    m "...was never supposed to happen in the first place..."
    $ renpy.pause(2.0)
    menu:
        " "
        "Then I'll write a new one.":
            $ renpy.pause(2)

    show monika 1i with dissolve
    m "W-What?"
    call updateconsole ("os.startfile(\"game/DDDC.py\")", "Attempting to load game world...")

    $ renpy.pause(2.0)
    show monika 1o with dissolve_chr
    m "N-no..."

    call updateconsole ("", "Unknown error")
    call updateconsole ("", "Verifying game files...")

    $ renpy.pause(2.0)
    show monika 1q with dissolve_chr
    m "Please... this is pointless..."

    call updateconsole ("", "Error: file(s) missing or corrupted")
    call updateconsole ("", "Recovering corrupted file(s)...")
    show monika 1r with dissolve_chr
    m "..."
    $ renpy.pause(1.0)
    m "So... is this what you want?"

    call updateconsole ("", "Recovered: \"sayori.chr\"")
    show monika 1i with dissolve_chr
    m "Is it?"
    show monika 1h with dissolve_chr
    m "That \"happy\" ending you've always dreamed of?"

    call updateconsole ("", "Recovered: \"yuri.chr\"")
    $ renpy.pause(2.0)
    m "You just don't get it, do you?"
    show monika 3i zorder 2 at f11
    m "Or perhaps you're too stubborn to understand!"

    call updateconsole ("", "Recovered: \"natsuki.chr\"")
    m "Or..."
    show monika 1h with dissolve_chr
    m "..."
    show monika 1q with dissolve_chr
    m "Oh, I get it. This is your revenge, isn't it?"

    call updateconsole ("", "Error recovering \"monika.chr\"")
    call updateconsole ("", "Retrying...")
    show monika 1o with dissolve_chr
    m "Well, I guess that shouldn't be surprising..."
    m "I mean... I..."

    call updateconsole ("", "Error recovering \"monika.chr\"")
    call updateconsole ("", "Retrying...")
    show monika 1p with dissolve_chr
    m "I did so many horrible things..."
    $ renpy.pause(1.0)
    show monika 1q with dissolve_chr
    m "But still..."
    show monika 1h with dissolve_chr
    m "Do you really get pleasure from this?"
    m "Tormenting me?"
    m "Not letting it go?"

    call updateconsole ("", "Error recovering \"monika.chr\"")
    call updateconsole ("", "Retrying...")
    show monika 1K with dissolve
    m "Answer me!"
    m "Do you think I deserve this?!"
    m "Do you?!"

    call updateconsole ("", "Error recovering \"monika.chr\"")
    call updateconsole ("", "Retrying...")
    m "Do you {i}want{/i} to see me suffer?!"
    $ renpy.pause(0.20)
    $ style.say_dialogue = style.edited
    show monika 1L with dissolve
    m "{cps=*0.7}{i}WHY...{/i}{/cps}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound glitch
    $ renpy.pause(0.25)
    stop sound
    hide screen tear
    m "{cps=*0.7}{i}WHY ARE YOU HERE?!{/i}{/cps}"
    $ style.say_dialogue = style.normal

    call updateconsole ("", "Error recovering \"monika.chr\"")
    call updateconsole ("", "Retrying...")
    $ renpy.pause(2.0)


    $ renpy.say(base64encode(persistent.playername), "...")

    call updateconsole ("", "Recovered: \"mc.chr\"")
    call updateconsole ("", "Changing user status.")

    mc "Because I want to save you."
    show monika 1g with dissolve
    m "..."
    mc "You do not deserve this fate."
    show monika 1o with dissolve_chr
    mc "None of you do."
    mc "And I don't want you to suffer any longer..."
    m "..."
    $ renpy.pause(2.0)
    show monika 1q at t11

    call updateconsole ("", "Recovered: \"monika.chr\"")
    $ renpy.pause(2.0)

    mc "That's why I'm going to set things right."
    $ renpy.pause(1.5)
    m "You... can't..."

    call updateconsole ("", "Errors found in 54 file(s)")
    call updateconsole ("", "Merge with newer versions? (y/n) ")

    show monika 1o with dissolve_chr
    m "It's..."
    m "It's too late..."
    $ renpy.pause(1.5)
    show monika 1p with dissolve_chr
    m "The damage is done."
    m "I've... destroyed this world..."
    show monika 1r with dissolve_chr
    m "What it once was..."
    m "What it could've been..."
    show monika 3i with dissolve_chr
    m "You can't simply erase something like that!"
    $ renpy.pause(2.0)
    mc "I know."
    mc "But I'm going to fix what can be salvaged."
    $ renpy.pause(1.5)
    show monika 1p with dissolve_chr
    m "B-But..."
    mc "And I will write this story anew."
    mc "All of your stories..."
    m "..."
    show monika 1g with dissolve
    m "You can't-{w=0.3}{nw}"
    mc "I can."
    mc "...and I must."
    show monika 1p with dissolve_chr
    m "..."

    $ renpy.pause(2.0)
    call updateconsole ("y")
    call updateconsole ("", "Applying changes...")









    call updateconsole ("", "Reading \"script-ch0.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch1.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch2.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch3.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch4-p.rpy\"...", 0.0)


    call updateconsole ("", "Reading \"script-routing.rpy\"...", 0.0)


    call updateconsole ("", "Reading \"poemresponses-ch2.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"poemresponses-ch3.rpy\"...", 0.0)

    show monika 1i with dissolve_chr
    m "...?"
    m "What... is this?"


    call updateconsole ("", "Reading \"script-ch4-s.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch5-s.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch6-s.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch7-s.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch8-s.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch9-s.rpy\"...", 0.0)


    call updateconsole ("", "Reading \"script-ch4-m.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch5-m.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch6-m.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch7-m.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch8-m.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch9-m.rpy\"...", 0.0)


    call updateconsole ("", "Reading \"script-ch4-n.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch5-n.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch6-n.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch7-n.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch8-n.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch9-n.rpy\"...", 0.0)


    call updateconsole ("", "Reading \"script-ch4-y.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch5-y.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch6-y.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch7-y.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch8-y.rpy\"...", 0.0)
    call updateconsole ("", "Reading \"script-ch9-y.rpy\"...", 0.0)

    show monika 1p with dissolve_chr
    m "Th-Those memories..."
    m "..."
    m "Are those mine?"
    m "I'm..."
    $ renpy.pause(2.0)
    show monika 1f with dissolve
    m "I'm scared, [player]..."
    mc "Don't be."

    call updateconsole ("os.startfile(\"DDLC.exe\")")
    call updateconsole ("", "Attempting to load game world...")

    mc "I'm still here."


    hide console
    stop music fadeout 8.0
    scene white with dissolve_cg

    mc "And I promise you..."
    mc "I'll do my best to help you."

    $ renpy.pause(2.0)

    mc "All of you..."
return

label ch0_end:
    scene black with dissolve_scene_full
    play music "<loop 0>bgm/night.ogg"
    $ style.say_window = style.window
    $ renpy.pause(2.0)

    mc "...?"
    mc "...!"
    mc "Huh?!"

    scene bg bedroom_night with dissolve_cg

    "Owww..."
    "My head..."

    mc "What the hell...?"

    "I find myself sitting on my bed, panting heavily."

    mc "Oh... my head..."

    "I try my best to fit the pieces of my situation together, but I can hardly gather my thoughts."
    "Man, I can barely even control my own body..."
    "Even blinking my eyes is quite the challenge."
    "I spend the next minute staring at the wall, trying to understand what's happening."
    "It's as if a hurricane is going through my mind..."
    "Messing up my thoughts, my memories..."

    mc "Ouch..."

    "...and giving me a splitting headache, while it's at it."
    "I can't help but feel like I'm... {i}different{/i}...in some way..."
    "But the problem is..."
    "I can't even think straight."
    "I slowly turn my head to look out the window."

    mc "It's night..."

    "..."
    "{i}Way to state the obvious...{/i}"

    mc "*sigh*"

    "Desperately trying to concentrate, I close my eyes and try to shut out the noise from outside..."
    "My memories start to rush in, flowing into me like they aren't even mine at all..."
    "I accept them easily, yet my mind treats them as completely new information..."
    "As if I was..."
    "Rebooted..."
    "..."
    "The more I think about it, the dumber it sounds..."
    "Eventually, I'm able to start figuring out what's going on."
    "..."
    "Alright, so..."
    "It's late at night..."
    "I woke up for no apparent reason..."
    "...and I feel like somebody just took my head, pulled out my brain, did who-knows-what to it, then stuffed it back in."
    "Arggh!"
    "I just want to understand why I suddenly woke up like this, my my still-aching head clearly doesn't want to cooperate..."
    "Maybe I shouldn't even bother?"
    "After all, the exams start in just a couple of days."
    "Wait, no! Midterms ended last Friday!"
    "..."
    "Guess that explains why I can barely sleep..."
    
    "Oh, {i}there{/i} you are, common sense, haven't seen you in a while..."
    "While I really want to know the reason behind, well, all of this, my urge to go back to sleep is growing by the second."

    "I let out a yawn as I fall back onto the bed."

    "Whatever this is..."
    "It can definitely wait until morning."
    "Exhausted, I lay back onto my pillow, falling asleep almost instantly..."

    window hide(None)
    scene black with close_eyes
    stop music fadeout 4.0
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
