label ch4_prologue:


    if persistent.playthrough == 0:
        stop music fadeout 2.0
        $ renpy.pause(1)

        $ style.say_dialogue = style.edited
        m_glitch "Oh my, we're finally getting to the good part, aren't we?"
        $ style.say_dialogue = style.normal

    scene bg bedroom with fade
    play music t2
    $ s_name = "???"

    s "[player]! Wake up!!!"

    $ renpy.pause(0.5)
    mc "Huh?"

    $ renpy.pause(0.5)
    "I hear an annoying girl shouting from outside my house."

    mc "Ughhh... Sayori..."

    "I get up from my bed to look out my window."
    "..."
    "I see her outside, waving at me."
    "Am I about to be late again?"
    "Without wasting any more time, I get ready as fast as I can and run to meet Sayori outside."

    scene bg residential_day with wipeleft_scene

    $ s_name = "Sayori"

    show sayori 4x at t11
    s "Aha! I woke up earlier than you this time!"

    mc "Yeah, yeah... I must've taken a while to think of a topic for my poem last night.."

    "I say that just so she gets the gist of the reason I woke up this late."

    show sayori 1g with dissolve_chr
    s "But you {i}did{/i} sleep last night, right?"
    "I nod my head and start walking to school, desperately fighting the urge to collapse right then and there on the sidewalk."

    scene bg corridor with wipeleft_scene

    "With the first class over, Sayori and I meet each other in the corridor."
    "I felt a bit dizzy while I was in class, a side effect of getting fewer than six hours of sleep and still dragging myself to school."
    "My stomach was making all kinds of noises throughout the morning, too."
    "It was probably what I made for dinner last night or something."

    show sayori 1g at t11
    s "Hey, you didn't forget to eat breakfast, right?"

    mc "Huh?"

    show sayori 1f with dissolve
    s "You look pale... as if you're hurt or something..."

    "Oh yeah, I forgot to have breakfast on top of that."
    "What a way to start the day."
    "Sayori seems worried, which she often is whenever I look even half as terrible as I do today."

    mc "Don't worry Sayori, I'm fine.."

    "I guess I'll just get something to eat at the cafeteria after our next class..."

    show sayori 1g with dissolve
    s "You're not going to get sick, right?"
    show sayori 3h with dissolve_chr
    s "If you are, I'll come over and stay the night."

    mc "What?! No! No way, Sayori, that's just wrong!"

    show sayori 6i with dissolve_chr
    s "I'm serious, [player]!"
    s "I don't want to see you fall sick! It would make me really sad..."

    "And that's why you've offered to come to my place twice already?"
    show sayori 1f with dissolve
    "Sayori, oblivious to the scandalous nature of her statement, looks up at me with concerned eyes."

    mc "I'm fine, Sayori, really. Don't worry about me."

    show sayori 3e with dissolve
    s "You sure?"

    mc "Yes, Sayori, I'm okay, trust me."
    mc "Tell you what, I'd feel better if you came to the cafeteria with me after the next class, how about that?"

    show sayori 1b with dissolve_chr
    s "Hmmm..."

    show sayori 1x at h11
    s "Okay! I'll treat you to something! They might even have some garlic bread today!"

    mc "Sounds good."


    scene bg cafeteria with wipeleft_scene

    "Class went by faster than I anticipated. The teacher gave us our assignments and left the class."
    "Masses of students started heading to the cafeteria."
    "In a matter of minutes, I find myself standing at a crowded cafeteria along with Sayori."

    show sayori 1m at t11
    s "Wow... There's a lot of people here... I wonder if I'll be able to squeeze through and get something..."

    mc "To be honest, I think it's better if we don't eat here... It's way too crowded."

    show sayori 3j with dissolve_chr
    s "No! I promised I'd get you something to eat, after all!"

    mc "Sayori, there's no ne-{w=0.5}{nw}"

    show sayori 1c at t31
    s 1c "Wait here!{w=0.5}{nw}"

    show sayori zorder 1 at lhide
    hide sayori
    "Sayori rushes into the crowd, disappearing from sight."

    mc "And there she goes, I guess..."

    "I slowly look for two seats that aren't occupied..."

    show monika 1a at t32
    show yuri 1a at t33
    "Eventually, I notice Monika and Yuri sitting together."
    show monika 6j with dissolve_chr
    "Monika waves for me to come and join them."
    show monika 1b at f32
    m "Hey, [player]! I rarely see you around here."
    m "Come, have a seat."

    mc "Thanks, Monika. Hey, Yuri."

    show monika 1a at t32
    show yuri 1m at f33
    y "Good to to see you, [player]."
    show monika 2b at f32
    show yuri at t33
    m "Did you come here alone?"

    mc "No, I'm here with Sayori."

    show yuri 1a with dissolve_chr

    mc "She should be in line right now... Said that she'd buy me a garlic bread or something..."

    show monika 2a at t32
    "I take a seat, trying my best not to look at them too much. Don't want Monika and Yuri to notice the bags under my eyes."
    "It's enough that I already made Sayori worried, so causing the others to join her..."
    "...no, I won't be able to withstand that lecturing from all four of them."
    "Speaking of {i}four...{/i}"

    mc "By the way, where's Natsuki?"

    show yuri 2i at f33
    y "Probably eating her homemade cupcakes at her own class, if I had to guess."
    show yuri 2j with dissolve_chr
    y "She says the cafeteria food is too... greasy for her taste."

    mc "Yeah, and I'm afraid she has a point..."

    show sayori 4p at l31
    show monika 2c at t32
    show yuri 2B at t33
    "Sayori suddenly appears next to us, panting heavily."

    s "Haaah, s-sorry to keep you waiting... hah..."

    show monika 1a with dissolve_chr
    show yuri 1a with dissolve_chr
    s "There was so little space in that crowd to breathe... I had to push myself in there to buy it..."

    show sayori 1m with dissolve_chr
    $ renpy.pause(0.5)
    show sayori 1n with dissolve_chr
    $ renpy.pause(0.5)
    show sayori 1m with dissolve_chr
    $ renpy.pause(0.5)
    show sayori 1n with dissolve_chr
    "Sayori takes few extra seconds to catch her breath."

    show sayori 1o with dissolve
    s "..."
    show sayori 1q with dissolve_chr
    s "Okay... I think I'm good now..."

    show monika 1e with dissolve_chr
    show yuri 1m with dissolve_chr
    show sayori 3x with dissolve_chr
    s "Here! Your garlic bread!"

    mc "Thanks, Sayori. Why don't you grab a seat?"

    show monika 3j with dissolve_chr
    m "Hi, Sayori!"
    show sayori 1b at h31
    s "Oh!"
    show sayori 4r with dissolve_chr
    s "Hey there, I didn't notice you at first!"
    show sayori 1r with dissolve_chr
    show monika 2a with dissolve_chr
    show yuri 1a with dissolve_chr
    "Sayori's face shines with joy as she notices that I found us some company."

    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "I let the girls have their chat, trying to draw as little attention to myself as possible and eating my late breakfast."
    "I'm always amazed at the lengths Sayori goes to do the smallest things for me."
    "If Natsuki was here, she would've said something like:"


    stop music fadeout 2.0
    scene white with dissolve_cg
    play music t7

    show natsuki 4w at t11
    n "You're the absolute worst, you know that?"
    show natsuki 4e with dissolve
    n 4e "You made a {i}girl{/i} push through a crowd just to buy {i}you{/i} some food?! How pathetic..."

    stop music fadeout 2.0
    scene cafeteria with dissolve_cg

    mc "*sigh*"
    "I would've done it myself, but Sayori was dead set on getting it for me."
    "And I really don't want her to worry too much."



    scene bg corridor with wipeleft_scene

    "After lunch, we all go back to our respective classes."
    "And shortly after, the classes are over."
    "I'm once again going to the clubroom, curious what this day has to offer."
    "I also can't help but to feel a bit anxious. I catch myself checking if I forgot to bring my poem every few minutes."
    mc "*sigh*"
    mc "I really hope this one is finally somewhat decent..."

    play sound closet_open
    scene bg club_day with fade

    "..."
    "Hmm, looks like I'm the first one here this time around..."
    "They're probably late or something, I guess I'll just take a seat and wait."

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
