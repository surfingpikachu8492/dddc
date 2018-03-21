



label ch0_main:
    python:
        monika = ""
        try:
            monika = renpy.file("../characters/monika.chr").read(1)
        except:
            with open(config.basedir + "/characters/monika.chr", "wb") as f:
                pass
    if not monika:
        call monika_deleted
        pass
    python:
        natsuki = ""
        try:
            natsuki = renpy.file("../characters/natsuki.chr").read(1)
        except:
            with open(config.basedir + "/characters/natsuki.chr", "wb") as f:
                pass
    if not natsuki:
        call natsuki_deleted
        pass
    python:
        sayori = ""
        try:
            sayori = renpy.file("../characters/sayori.chr").read(1)
        except:
            with open(config.basedir + "/characters/sayori.chr", "wb") as f:
                pass
    if not sayori:
        call sayori_deleted
        pass
    python:
        yuri = ""
        try:
            yuri = renpy.file("../characters/yuri.chr").read(1)
        except:
            with open(config.basedir + "/characters/yuri.chr", "wb") as f:
                pass
    if not yuri:
        call yuri_deleted
        pass
    python:
        silverzone = ""
        try:
            silverzone = renpy.file("../characters/silverzone.chr").read(1)
        except:
            with open(config.basedir + "/characters/silverzone.chr", "wb") as f:
                pass
    if not silverzone:
        call silverzone_deleted
        pass
    python:
        jackburst = ""
        try:
            jackburst = renpy.file("../characters/jackburst.chr").read(1)
        except:
            with open(config.basedir + "/characters/jackburst.chr", "wb") as f:
                pass
    if not jackburst:
        call jackburst_deleted
        pass
    if persistent.playername == "Monika":
        call monika_named
        return
    if persistent.playername == "monika":
        call monika_named
        return


    stop music fadeout 2.0
    scene bg corridor
    with dissolve_scene_full
    play music t2

    "After school, I take my usual route straight to my clubroom."

    scene bg club_day
    with wipeleft_scene

    "Upon arriving I see a stunningly beautiful girl sitting in a chair writing in a notebook."
    "She immediately noticed me and got up from her seat and greet me."
    m "[player]?"
    show monika 1a zorder 2 at t11
    mc "Oh... Hi Monika.."
    m 1b "How are you doing at school?"
    show monika 1a
    mc "I'm fine, just having stress studying."
    m 2e "I see..."
    m 4e "I agree, studying for the final exam is really stressful."
    mc "What about you? How are you doing at school."
    m 2k "Me? I'm fine!"
    m 1e "Why do you ask?"
    m 5a "Are you interested in me?"
    mc "Don't be silly, i'm just asking."
    mc "Why do you judge that so quickly..."
    m 1l "Ahahaha.."
    m 1m "I'm just teasing..."
    "This girl is Monika. She's the Club President of the {i}Literature Club{/i} and is one of the most popular girls in school."
    show monika 1a zorder 1 at t11
    "At first glance would imagine her to be the type of diva in school that bosses everyone around, but she's not that type of a person.."
    show monika zorder 1 at thide
    hide monika
    "She's kind, caring, intelligent and innocent."
    $ s_name = "???"
    s "Heeeeeeeeyy!!!"
    show sayori 4r zorder 2 at f21
    $ s_name = "Sayori"
    s "What are you guys talking about?"
    show sayori 4q
    mc "Well... Nothing.."
    show sayori 1a zorder 2 at t21
    show monika 1k zorder 3 at f22
    m "We're just chatting!"
    show monika 1j
    mc "..."
    mc "What she just said...."
    m 1l "Ahahaha..."
    show monika 1x zorder 1 at thide
    hide monika
    show sayori 1a zorder 2 at t11
    "This cheerful girl is Sayori, my childhood friend and neighbour."
    "She's sweet and bubbling with energy."
    "She tends to be really clumsy and somewhat disorganized. But she's always reliable."
    $ n_name = "???"
    n "There you are, [player]!"
    show sayori 1a zorder 2 at t21
    show natsuki 4e zorder 3 at f22
    $ n_name = "Natsuki"
    n "I thought you were at your classroom!"
    n 4c "I was looking for you!"
    show natsuki 1g zorder 2 at t22
    show sayori zorder 3 at h21
    s 4m "Ehh??"
    show sayori at s21
    s 1o "Why are you looking for him?..."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 5b zorder 2 at t11
    n "I needed him to help me carry books to the teacher's desk."
    n 12c "If you don't wanna help, I'll just do it myself."
    show natsuki 1g zorder 2 at t21
    show monika 1b zorder 3 at f22
    m "I think it's better if you'd go help her [player]."
    m 4k "After all, she's quite a frail girl."
    show natsuki 1p zorder 2 at t11
    show monika 4j zorder 1 at thide
    hide monika
    n "I'm not frail!"
    n 1y "I I'm just.. small.."
    n 5q "A-Anyways, are you gonna help me or not?"
    show natsuki 5s
    mc "Yeah, yeah I'll help you out.. But as payment, you have to share some of the cupcakes you made."
    n 5w "What? No! I baked these cupcakes for myself!"
    n 5x "If you're really gonna demand a reward like that, I'll be better off carrying the books myself!"
    show natsuki 5w2
    mc "Heh... I'm just joking.. Don't take it seriously."
    mc "I'll help you get the book, no cupcake required."
    n 5t2 "Hmph."
    "This adorable girl is Natsuki. Another member of the {i}Literature Club{/i}."
    show natsuki 5g
    "Like me, she is a person of great intellect, only consuming the finest genre of literature."
    show natsuki zorder 1 at thide
    hide natsuki
    "..."
    "She reads manga."
    "A lot of manga."
    "Natsuki has always been acting defiant and arrogant to me since I met her like she's always trying to avoid me or something."
    "I can say in depth that she's a compassionate girl."

    scene bg corridor
    show natsuki 1g zorder 2 at t11
    with wipeleft_scene

    "After helping Natsuki, we return to the clubroom for our club activities."
    n 2b "Just so you know, I didn't ask for your help just to spend more time with you or anything."
    n 5c "I just needed a hand to help carry the books!"
    show natsuki 5g
    mc "I know, I know.. Just happy to help."
    show natsuki zorder 1 at thide
    hide natsuki

    scene bg club_day
    with wipeleft_scene

    "We rejoin Monika and Sayori in the clubroom."
    show yuri 1b zorder 2 at t11
    y "Oh, hello [player]."
    show yuri 1a at t11
    mc "Hey there Yuri, are you feeling better? You called in sick yesterday and we were worried."
    y 3d "Sorry that I had you worried, but I am feeling much better."
    y 4a "Anyways, are you okay with your studies?"
    y 4b "I would be happy to give extra tuition if you need help."
    mc "Ahahaha, I'm okay with my studies Yuri. Don't worry about me."
    show yuri 4c
    "{i}(That's somewhat of a lie, but I'd hate to cause her any trouble.){/i}"
    "Yuri's a quiet girl. She doesn't speak much, but she's still trying her best to socialize."
    show yuri zorder 1 at thide
    hide yuri
    "However most of the time she sits in the back by herself reading her novels. I still have no idea what type of novels she's really into."
    "I'll do my best to make her feel more comfortable here."
    "Off to the distance I see Monika, Sayori, and Natsuki chatting while occasionally glancing at me."
    show natsuki 4c at f11
    n "They're close together huh... I'm started to think that Yuri have feelings about him..."
    show natsuki 4g zorder 2 at t21
    show monika 1d2 zorder 3 at f22
    m "Natsuki, don't gossip about them, they might be able to hear you you know. Plus it's just rude."
    show monika 1c2
    mc "So, what are you girls talking about?"
    show natsuki zorder 2 at t31
    show monika zorder 2 at t32
    show sayori 1b zorder 3 at f33
    s "We're just talking about you [player]."
    show monika 1c zorder 2 at t32
    show sayori zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Yeah, you and Yuri being so close together all of a sudden."
    mc "What.. We aren't that close!!! We're just being friendly to each other. That's all!"
    show natsuki 2g zorder 2 at t41
    show monika zorder 2 at t42
    show sayori zorder 2 at t43
    show yuri 2e zorder 3 at f44
    y "Are you guys talking about me?"
    show yuri 1e zorder 2 at t44
    show natsuki 5b zorder 3 at f41
    n "Yeah, we are."
    show natsuki 5g zorder 2 at t41
    mc "Not really, don't mind Natsuki. We're just... just..."
    show monika zorder 3 at f42
    m 2b "We're discussing about the poems we're going to write to showcase for the school festival."
    show monika 2a
    show yuri 1a zorder 2 at t44
    mc "Y-Yeah, that's right."
    m 4b "Anyone have any ideas what should we write about?"
    show monika 1a zorder 2 at t42
    show sayori 4r zorder 3 at f43
    s "Ah! how about writing a poem about the future?"
    show sayori 4q
    mc "That's kinda strange..."
    show sayori zorder 2 at s43
    s 5c "Heh.. that's mean..."
    show monika zorder 2 at t42
    show sayori 1a zorder 2 at t43
    show natsuki 4d zorder 3 at f41
    n "What about writing a poem of Animals? I mean, every animal has it's own perks."
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 4a zorder 2 at t21
    show yuri 2b zorder 2 at t22
    stop music fadeout 1.0
    y "Natsuki's idea seems fine. But i'd suggest writing about the surroundings, like nature."
    show natsuki zorder 3 at t21
    show yuri 1a zorder 2 at t22
    play music t7
    n 5c "'Seems fine?' It's way better than your idea!"
    show yuri 1e
    n 5y "Writing about surroundings and nature? That'll make people sleep at the festival!"
    show natsuki 5g zorder 2 at t21
    show yuri zorder 3 at f22
    y 2r "Excuse me, but nature is beautiful in many ways. The peacefulness of an untouched forest or the vibrant colors of the Northern Lights..."
    y 3m "It's the perfect topic for a poem."
    y 3l "Writing about hidden beauty and tranquility is what poetry is all about."
    y 1j "I can hardly to turn a subject like an animals into a poem."
    show yuri 1i zorder 2 at t22
    show natsuki zorder 3 at f21
    n 1p "What?! A poem about animals is easy! You can write something about the life of a cats in many ways!"
    show yuri zorder 2 at t22
    show natsuki zorder 3 at f21
    n 4y "Like how they behave and what they do is cute!"
    show yuri 1g zorder 2 at t33
    show natsuki 5w2 zorder 2 at t31
    show monika 1g zorder 3 at f32
    m "Come on guys, don't argue over something trivial."
    show monika zorder 1 at thide
    hide monika
    show yuri 1g zorder 2 at t22
    show natsuki 4e zorder 3 at f21
    n "It's not me who started arguing by the way. Yuri started it."
    show natsuki 4g zorder 2 at t21
    show yuri zorder 3 at f22
    y 3r "What? No! I wasn't arguing, I was just stating facts."
    show yuri zorder 2 at t22
    show natsuki zorder 3 at f21
    n 4y "Facts? Those aren't facts! Those are just words made to start an argument!"
    show natsuki 4y2 zorder 2 at t21
    show yuri zorder 3 at f22
    y 1k "{i}*sigh*{/i}"
    show yuri 1c zorder 2 at t22
    show natsuki zorder 3 at f21
    n 1v "It's your fault we started arguing, [player]!"
    show natsuki 1w2 zorder 2 at t21
    mc "Huh? What?! What did I do?!"
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    hide yuri
    hide natsuki
    "In an instant, everyone in the clubroom started laughing."
    "The clubroom became livelier after Natsuki's joke. We all gave our ideas and went about making poems for the festival."
    stop music fadeout 2.0
    return

label ch0_afterday:
    stop music fadeout 2.0
    scene bg corridor with dissolve_scene_full
    play music t3
    "The next day..."
    "Walking to the clubroom was a pain. I mean, my head is killing me."
    "Endurance was key to scoring well on the final exams, but the school day finally ended.."
    "Guess I should relax for a bit."
    scene bg club_day with wipeleft_scene
    "I entered the clubroom and saw Monika reviewing her poem."
    show monika 1b zorder 2 at t11
    m "Oh hey [player]."
    show monika 1a zorder 2 at t11
    mc "Hey Monika."
    m 2g "You look troubled.."
    m 2i "Are you okay?"
    show monika 2h
    mc "I'm fine, because of the final exam I have to study everyday.."
    m 1d "I see..."
    m 4l "Do not over pressure because of the final exam!"
    m 4k "Anyway, this is my poem!"
    show monika 4j
    "Monika shows me her poem."
    "She seems pretty eager to show me her poem."
    mc "Let's see..."
    call showpoem (poem_m1, img="monika 1a")
    mc "..."
    m 5a "So.. what do you think of my poem?"
    mc "It's a warm and soothing poem.. It makes me feel safe.. Somehow."
    m 1k "Oh! I didn't know my poem could make you feel that way."
    show monika 1j
    mc "It's okay, it's still an amazing poem though. It could be used to showcase on our school festival!"
    m 3b "Really? Wow! Thank you [player]! This was one of my bes-{nw}"
    show monika 1d zorder 1 at t21
    show sayori 4r zorder 2 at h22
    s "Hey! Hey! [player]! Look at my poem that I made!"
    show monika 1c
    show sayori 4q
    mc "Sayori, watch your manners."
    mc "You just interuppted Monika when she was talking."
    show sayori 4p at s22
    s "Eh..."
    s 5d "Sorry Monika, I was too excited."
    m 1l "Ahaha, don't worry Sayori, it's okay."
    show sayori at thide
    hide sayori
    show monika 1a at t11
    mc "So, Monika. You were saying?"
    m 4b "This was one of my best poems."
    show monika 4a
    mc "Really? You must've tried your best for that."
    m 1j "Well, honestly it wasn't too difficult. I just thought really hard about it."
    show monika 1e at t21
    show sayori 4r at hf22
    s "Okay! Okay! Look at my poem!"
    show monika at thide
    hide monika
    show sayori at t11
    mc "Okay.."
    call showpoem (poem_s1, img="sayori 1a") from _call_showpoem_1
    mc "Wow, you wrote this?"
    s 4r "Yeah! How is it?"
    show sayori 4q
    mc "It gave me the same feeling as Monika's poem"
    s 1b "How did it make you feel?"
    mc "Warm and Soothing.."
    show sayori 4m at h11
    s "Really?!"
    show sayori 4r at h11
    s "Haha, I outdid myself!"
    show sayori at h11
    s "My poem was on par with Monika's!"
    show sayori 4q at t11
    mc "Think again, yours aren't even close to Monika's standard."
    show sayori 5c at s11
    s "But I wrote more words than Monika.."
    s 5c "I wrote 68 words and Monika wrote 63 words..."
    mc "Er.. That's not the point.."
    s 5d "I even used awesome words."
    mc "Again, not the point.."
    show sayori zorder 2 at t21
    show monika 4b zorder 3 at f22
    m "Well, it's not about the amount.. It's the quality.."
    show sayori 3o zorder 3 at f21
    show monika 4a zorder 2 at t22
    s "Heh... Monika is bragging about her poem.."
    show sayori 1o zorder 2 at t21
    show monika zorder 3 at f22
    m 1l "Eh?!?! I was just stating facts..."
    show monika 1x zorder 2 at t22
    show sayori 1r zorder 3 at f21
    s "Haha! I was joking Monika. J-o-k-i-n-g."
    show sayori 1q zorder 2 at t21
    mc "heh.. It's true though.. you did brag about your poem's quality."
    show monika 5c at h22
    m "[player] you meanie.."
    show sayori at thide
    show monika at thide
    hide sayori
    hide monika
    "After i read finish their poems, I glanced at Natsuki and Yuri."
    "They seemed like they're discussing something."
    "I went over and talked to them."

    with wipeleft_scene

    show natsuki 1a zorder 2 at t21
    show yuri 1a zorder 2 at t22
    mc "Are you guys okay here?"
    show natsuki 4k zorder 3 at f21
    n "Yeah we're fine, we were just comparing each other's poem."
    n 4i "Yuri's poem is super classy however you read it."
    n 4q "I.. kinda like it.."
    show natsuki 4i zorder 2 at t21
    show yuri 2d zorder 3 at f22
    y "Really?"
    y 3c "Well, I didn't think that you'd like it."
    show natsuki 4w zorder 3 at f21
    show yuri zorder 2 at t22
    n "Of course it should be amazing, you're one of the smartest students in this school you know?"
    n 12c "I would be disappointed if you weren't that good."
    show natsuki 12b zorder 2 at t21
    mc "Can I see both of your poems?"
    show natsuki 4l at t11
    show yuri at thide
    hide yuri
    n 4l "Yeah sure, go ahead. It's one of my favourite topics."
    call showpoem (poem_n1, img="natsuki 2a") from _call_showpoem_2
    n 2c "So.. How was it?"
    show natsuki 2g at t11
    mc "It's.. cute.. I guess.."
    n 1o "It's not cute! It's an extremely deep and thought-provoking poem!"
    n 4y "Well, I wouldn't expect you to understand.."
    n 5y "Since you're the type of person that never leaves his house."
    show natsuki 5y2
    mc "..Hey! I do leave the house once in a while."
    n 4d "Really? where do you go?"
    show natsuki 4a
    mc "..."
    mc "The.. park or something...?"
    n 4y "Hah.. Obviously.."
    show natsuki 4y2
    mc "Forget about it!"
    show natsuki 2a at t21
    show yuri 1a zorder 2 at t22
    mc "Anyways, can I see your poem Yuri?"
    show yuri 3b at t11
    show natsuki zorder 1 at thide
    hide natsuki
    y "Please do."
    call showpoem (poem_y1, img="yuri 1a") from _call_showpoem_3
    mc "..."
    y 3o "How was it? Was it okay? Or did it weird you out?"
    show yuri 3u
    mc "Weird me out? No, It didin't!"
    mc "Why would you think that?"
    y 2n "Ah..."
    y 2o "Well..."
    y 4b "I tried my best to express nature's beauty in a poem."
    y 4c "And thought I used too many eccentric words."
    mc "It wasn't weird at all, it was a beautiful and calming poem."
    mc "This is good enough for the festival."
    y 1f "You think so?"
    y 3k "Ah.."
    y 1c "I'm flattered."
    mc "Don't feel flattered, it was a great poem after all."
    show natsuki 5b zorder 3 at f21
    show yuri 1a zorder 2 at t22
    n "Keep your fluttering heart at a distance you two.."
    stop music fadeout 1.0
    n 5c "Because I have a huge question for you [player].."
    show natsuki 5g zorder 2 at t21
    mc "And what's that?"
    show natsuki zorder 3 at f21
    n 5m "Where is your poem?"
    show yuri 1e at t22
    show natsuki 5g zorder 2 at t21
    mc "Oh....."
    mc "Uhh...."
    play music t6
    "{i}Crap!{/i} I forgot to write a poem! After yesterday's club activities I left in a hurry to study and forgot to write a poem for the festival!"
    mc "I.. Kinda left it at home.."
    show natsuki 5e at f21
    n "Heh.. Did you really left it at home or did you forget to write it?"
    show natsuki 5g zorder 2 at t21
    show yuri 3h zorder 3 at f22
    y "Oh my.."
    show yuri 3g zorder 2 at t22
    "I turn my head to face the other girls, who are staring at me with disapproving eyes."
    "They must've overheard Natsuki's comment."
    "Here it comes..."
    show sayori 5c zorder 3 at t33
    show natsuki 5g zorder 2 at t31
    show yuri 1g zorder 2 at t32
    s "Heheh.. We tried our hardest to produce a poem for the festival.."
    show sayori 5d zorder 3 at s33
    s "Yet [player] didin't even try to make one.."
    show sayori zorder 2 at t43
    show yuri 1e zorder 2 at t42
    show natsuki zorder 2 at t41
    show monika 2l zorder 3 at t44
    m "Well.. It's okay that you forgot about writing one.."
    m 4k "You can submit it tomorrow. After all, we all make mistakes here..."
    show yuri 1e
    show sayori 5c
    show monika 4x zorder 2 at t44
    "I feel like I'm being talked to like a child who knocked over the cookie jar, though admittedly this is somewhat warranted based on my actions."
    "I've never felt more guilty over something so small in my whole life."
    show natsuki 5e zorder 3 at f41
    n "Don't assure him Monika, times like these call for discipline, not nurturing."
    show yuri 1i
    n 5f "As punishment, [player] will have to write 50 poems!"
    show natsuki 5g zorder 2 at t41
    mc "What?!"
    show monika 1l zorder 3 at f44
    m "Ahaha, you don't have to be so cold to him Natsuki.."
    m 1e "It's just a poem."
    show yuri 1a
    show natsuki 5t2 zorder 3 at f41
    show monika zorder 2 at t44
    n "Hmph."
    stop music fadeout 1.0
    show natsuki at thide
    show monika at thide
    show yuri at thide
    show sayori at thide
    hide natsuki
    hide monika
    hide yuri
    hide sayori
    with wipeleft
    play music t2
    "The last school bell rang. It was finally time to go home."
    "I bade Monika and Yuri goodbye and walked home with Sayori."
    scene bg residential_day with wipeleft_scene
    show sayori 3g zorder 2 at t11
    s "Hey, are you okay?"
    show sayori 3f
    mc "Hm? Why do you ask?"
    s 4j "You kinda spaced out while we were walking.."
    show sayori 4f
    mc "Oh, I was just thinking about the poem i'm supposed to write for tomorrow."
    mc "Even after reading everyone else's..."
    mc "I'm still stuck on what I'd like to write about..."
    s 1n "Oh I see.."
    show sayori 4r at h11
    s "Would you like me to come over and help?"
    show sayori 4q
    mc "Come over to my place just to help write a poem?"
    mc "You must have a motive in doing so.."
    show sayori 5c at s11
    s "Hey! I was just trying to help.."
    mc "No thanks Sayori, I can handle it myself."
    mc "You go home and rest early."
    mc "You better not wake up late again tomorrow."
    s 5d "Heh..."
    "I noticed a sad look in her eyes when I turned down her offer."
    "Sayori and I parted ways. "
    show sayori at thide
    hide sayori
    "I entered my home and started feeling lonely."
    "It was mostly because of going back home to an empty house that truly made me feel this way."
    "But I tried my best to not let that get to me and went about cooking dinner for myself."
    scene bg bedroom with wipeleft_scene
    "After my bath I sat down and started thinking about making a poem."
    "But finding a topic was hard."
    "What should I write about?"
    return

label monika_named:
    stop music fadeout 2.0
    $ config.window_hide_transition = None
    $ quick_menu = False
    scene bg corridor
    with dissolve_scene_full
    play music t2g
    queue music t2g2
    $ config.window_hide_transition = Dissolve(.2)
    $ gtext = glitchtext(60)
    "{cps=60}[gtext]{/cps}{nw}"
    scene club day
    with wipeleft_scene
    $ gtext = glitchtext(90)
    "{cps=60}[gtext]{/cps}{nw}"
    $ gtext = glitchtext(64)
    "{cps=60}[gtext]{/cps}{nw}"
    $ m_name = glitchtext(12)
    $ mc = glitchtext(15)
    m "[mc]{nw}?"
    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    m "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    m "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    label monika_named_loop:
    $ persistent.autoload = "monika_named_loop"
    $ delete_character("silverzone")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("sayori")
    $ delete_character("monika")
    $ delete_character("jackburst")
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
