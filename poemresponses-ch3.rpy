# ----------------------------------------------------------------------------------------------
# All poem responses for all four girls (with all four appeals) for day 3 (Wednesday)
# ----------------------------------------------------------------------------------------------

label poemresponse_3_sayori:
    show sayori 1x at t11
    s "So, [player], 'take two,' huh?"
    mc "You could say that."

    show sayori 1a with dissolve_chr
    s "Do you think you managed to make some progress?"

    mc "I was hoping that you would tell me."

    show sayori 2b with dissolve_chr
    s "Oh, come on, you should have at least some faith in yourself."
    s "I'll tell you what I think and I won't be too harsh. You can count on that."
    show sayori 1b with dissolve_chr
    s "But you should still have at least some expectations of your own."

    mc "Well... what can I say..."
    mc "I tried my best. I listened to what all of you had to say and maybe even learned a lesson or two."

    show sayori 1q with dissolve_chr
    s "I'm sure you did!"
    show sayori 3x with dissolve_chr
    s "I mean, you're not the brightest student in the school, of cour--"
    show sayori 5b with dissolve_chr
    s "{i}O-Okay, now that's just mean...{/i}"

    mc "I'd be offended if it wasn't the sad but honest truth."

    show sayori 5a with dissolve_chr
    s "I was just trying to say that I believe in you."
    s "I know that you're not a fan of literature and all, but still...I think you'll manage."

    mc "I'll 'manage,' huh?"

    show sayori 5b with dissolve_chr
    s "Ehehe..."

    mc "No offense, Sayori, but inspiring speeches aren't your thing."

    show sayori 3h with dissolve_chr

    s "Come on! I was just trying to help!"

    mc "Well, you know what they say. 'The road to hell is paved with good intentions'..."

    show sayori 3b with dissolve
    s "...?"

    mc "..."
    mc "Sigh..."
    mc "In short, don't do that. Or, at least, don't do what you can't do."

    show sayori 1b with dissolve_chr
    s "Oh... Okay..."

    "Sayori was never good with idioms..."

    mc "Who'll go first? Me again?"

    show sayori 1a with dissolve_chr
    s "Only if you want to!"

    "To be fair, I hardly have a preference..."

    mc "Here you go, then."

    "I give Sayori my notebook."

    scene bg club_day with wipeleft_scene

    $ renpy.call("poemresponse_3_sayori_appeal_{appeal}".format(appeal=poemwinner[1]))

    "Sayori gives me a sheet with her poem."
    mc "At least this one doesn't have any stains on it, so that's a good sign."

    show sayori 5a with dissolve
    s "Ehehehe..."

    call showpoem (poem_s_2)

    show sayori 1a with dissolve
    mc "..."

    show sayori 3x with dissolve_chr
    s "So? What do you think?"

    mc "I... would even go as far as to say that I'm... somewhat amazed..."

    show sayori 4x with dissolve_chr
    s "Wow, really?"
    show sayori 4r at h11
    s "Yay! That means I outdid myself!"
    show sayori 4x with dissolve_chr
    s "Tell me what you like about it!"
    show sayori 4r at h11
    $ renpy.pause(0.3)
    show sayori 4r at h11
    s "Tell me, tell me, tell me!"

    mc "Calm down, jeez!"

    show sayori 5a with dissolve
    s "S-Sorry..."
    s "I just worked really hard on this one, and I'm getting excited..."

    mc "Well, I really like the mood."
    mc "It's calm, it's soothing, and yet, it's not as carefree as I'd expect..."
    mc "I'd say it's somewhat... philosophical, you know?"

    show sayori 1C with dissolve
    s "Really?"

    mc "You tried to write about our everyday lives, right?"
    mc "The clouds being good days and rainclouds, the bad ones?"

    show sayori 1o with dissolve_chr
    s "Hmmm... yeah, I think you have a point..."

    mc "Wait, what? You mean you don't know what you meant?"

    "To be fair, when was the last time Sayori did something with a good explanation and reason behind it?"

    show sayori 1d with dissolve_chr
    s "Well, not exactly. I knew I had something in mind, but I just couldn't figure it out..."
    show sayori 1y with dissolve_chr
    s "I had an image... a memory of how I walked in the park... watching the clouds..."
    show sayori 1q with dissolve_chr
    s "...how I was lying there on the grass... it was so warm and sunny..."
    s "...I was watching the sky, the feeling of the time passing almost... gone..."
    show sayori 1k with dissolve_chr
    s "...but then, suddenly everything became so dim, so gray..."
    s "...and in a matter of minutes I was already running back home, covering my head from raindrops."

    mc "..."
    mc "W-Wait, Sayori, but you almost never walked to park on your own. When did that--"

    show sayori 1f with dissolve
    s "..."

    mc "O-Oh..."

    "Realization hits me and I feel a sense of guilt washing over me..."
    "I'm such a fool..."
    "Those times where we had drifted apart..."
    "It might have been easy for me, but for someone like Sayori..."
    "..."
    "Man, I really feel like I... betrayed her..."

    mc "I'm sorry..."

    show sayori 3l with dissolve
    s "I-It's okay, [player], really!"
    s "Please don't read too much into it."
    show sayori 1y with dissolve
    s "After all..."
    s "{i}It's just a little raincloud...{/i}"

    "She sings the line as if it were a part of a light-hearted song, but I can still hear notes of sadness in her voice."

    mc "Sayori..."

    show sayori 1b with dissolve_chr
    s "Huh?"

    mc "I'm not going to leave you, I promise."

    show sayori 1G with dissolve_chr
    s "..."

    "We spend a few seconds in silence."
    "I'm still trying my best to calm down that small hurricane of emotions going through me..."
    "What did she say yesterday?"
    "{i}It's all about emotions behind it?{/i}"
    "{i}It could describe the beauty of our everyday lives, and those little things that make us a bit happier.{/i}"
    "Yeah, guess I should have given Sayori more credit, at least on her skills in poetry."

    mc "Heh... you really impressed me, Sayori, I'll give you that."

    show sayori 1q with dissolve_chr
    s "I'm glad to hear it. As I said, I worked really hard on this one."

    mc "To be fair, I never expected you to fill your poem with such emotions."

    show sayori 1b with dissolve_chr
    s "Hmm? Why's that?"

    mc "Oh, come on. How can I expect my little fluffhead Sayori to ever be sad?"

    show sayori 4F with dissolve_chr
    s "A f-f-fluffhead? Hahahahaha!"

    mc "Well, I was just thinking of your cheerful personality..."
    mc "Plus, your hair is kinda fluffy, so... yeah. 'Fluffhead' it is."

    show sayori 4D with dissolve_chr
    s "Ahahahahaha!"

    "Seeing her smile and hearing her laugh again, I can't help but to smile myself."
    "...nor can I help but to ruffle her hair again a bit."
    show sayori 1q with dissolve
    "I then start petting her on the head."
    "She really looks like a kitten, I almost expect her to start purring at this point."

    mc "Okay, Sayori, I have to go now."
    mc "Keep your chin up, okay?"

    show sayori 1x at h11
    s "Don't worry! With you around, I have a grin on my face 24/7!"

    mc "Works for me."

    show sayori zorder 1 at thide
    hide sayori
    "I stand up and start walking away."
    "I'm glad we had this little chat. Seeing Sayori sad? I never thought I'd see the day..."
    "And I definitely don't plan on seeing it again."

    scene bg club_day with wipeleft_scene
    return

label poemresponse_3_sayori_appeal_sayori:
    if poemwinner[0] == "sayori":
        show sayori 1d at t11
        s "..."
        s "Awww... that's so sweet!"
        show sayori 2l with dissolve_chr
        s "A bit... messy... but sweet..."

        mc "I don't know about my poem, but the quality of your feedback clearly hasn't improved so far."

        show sayori 1F with dissolve_chr
        s "Y-Yeah... yeah, I know..."
        show sayori 1E with dissolve_chr
        s "Well, it's still pretty... raw... just like your last one..."
        show sayori 1G with dissolve_chr
        s "But I'm just happy to see that you're making progress."
        show sayori 1l with dissolve_chr
        s "And that you don't let yourself be... i-influenced..."
        show sayori 1o with dissolve_chr
        s "{i}That's the word, right?{/i}"
        show sayori 1l with dissolve_chr
        s "...by anyone."
        show sayori 1y with dissolve_chr
        s "You stick to your style, not trying to change it just to impress someone."
        show sayori 3y with dissolve_chr
        s "Heh... but you did listen to my advice, I guess..."
    else:
        show sayori 1a at t11
        s "..."
        show sayori 4x with dissolve_chr
        s "Heeeey! Now that's what I'm talking about!"

        mc "Sayori, if there's something that I don't know in this world..."
        mc "...then it is {i}exactly{/i} what are you usually talking about."

        show sayori 1l with dissolve_chr
        s "Ehehehe..."
        s "Okay, okay. You have a point there..."
        show sayori 3y with dissolve_chr
        s "What I'm trying to say is that someone might say that your style is too simple..."
        show sayori 1G with dissolve_chr
        s "But I think that it's actually very nice."
        show sayori 1a with dissolve
        s "And, you know, sometimes poems like these can be much deeper than any of those filled with... metaphorical stuff and cool words..."
        show sayori 1y with dissolve_chr
        s "After all, sometimes the simplest things of our lives are the most important."
        show sayori 1F with dissolve_chr
        s "And while I can't say you haven't improved too much so far..."
        show sayori 1G with dissolve_chr
        s "...I'm glad to see that my advice helped."

    mc "Your advice?"

    show sayori 5b with dissolve
    s "Well, y-yeah... at least I hope it was mine..."
    s "I mean, you've listened to all of us yesterday..."

    mc "Yeah... I did... What about it?"

    s "Ehehe..."
    s "[player]..."

    show sayori 5a with dissolve
    s "I'm not that bad when compared with the others, right?"

    mc "Huh?"

    show sayori 5b with dissolve_chr
    s "W-When it comes to literature, I mean..."
    s "It's just that Yuri has her beautiful style..."
    s "...Natsuki can say in few words something that the others can only describe in a whole novel..."
    s "...and Monika is just overall perfect."

    s "And I'm just--"

    mc "...and you are my dear friend, Sayori."

    show sayori 1e with dissolve
    s "...?"

    mc "Really, Sayori, I kinda thought that I'm the one here who's the least confident about my skills..."
    mc "...and yet now you're making me look like a writer with years of experience!"

    show sayori 1y with dissolve_chr
    s "Well, I can't say I'm that much more interested in literature than you..."

    mc "And yet that doesn't stop you from being a vice president here."
    show sayori 1G with dissolve_chr
    mc "Besides, if we're going to discuss your skills in poetry, you were quite confident about your style during the argument yesterday."

    show sayori 3y with dissolve_chr
    s "Yeah... and I really hope I didn't offend anyone while I was doing that..."

    mc "Oh, come on! You were just stating your opinion! And a good one at that!"

    show sayori 1b with dissolve_chr
    s "Hmmm?"

    mc "Just like you said yourself, even if you're writing about our everyday lives, you can still make the reader experience all the emotions you had in mind while writing it."
    mc "It might seem simple at first, but it has it's own beauty."

    show sayori 4x at h11
    s "Yeah! Exactly!"

    show sayori 1x with dissolve_chr
    s "I'm so glad you understand!"
    show sayori 3E with dissolve_chr
    s "You know, we might even have more things in common than you say!"
    show sayori 1E with dissolve_chr
    s "Even if it's just the style of our poems..."

    mc "Sayori, I'm glad to have a friend like you, I'll give you that..."
    mc "...but I'm afraid we're still veeeeeery different."
    show sayori 1G with dissolve_chr
    mc "Besides, just like I said yesterday, I don't have even a slightest clue to what I'm doing and if I even have any style to begin with."

    show sayori 1a with dissolve
    s "Yeah, you might be right. But even if your style changes once you actually... find yourself, I'll still be happy."
    show sayori 4r with dissolve_chr
    s "Because you're now here and that's what really matters!"

    mc "I suppose you're right."
    mc "Okay, now how about you finally show me your poem?"

    show sayori 1y with dissolve_chr
    s "Okay."
    return

label poemresponse_3_sayori_appeal_natsuki:
    if poemwinner[0] == "natsuki":
        show sayori 1q at t11
        s "..."
        s "Ehehehe..."
        mc "Sayori, do you have any sense of shame at all?"
        show sayori 1b with dissolve_chr
        s "Huh?"
        mc "You were laughing at my poem yesterday..."
        mc "And now you're doing the same, at this new one!"
        show sayori 4s with dissolve_chr
        s "S-Sorry, I just can't help it. It's so cute!"
        mc "W-What? 'Cute'?!"
        show sayori 1D at h11
        s "Bwahahahahaha!"
        mc "...?"
        s "Ahahahaha!"
        mc "..."
        "It takes at least ten seconds for Sayori to finally calm down. The others are already throwing awkward glances in our direction."
        show sayori 1F with dissolve_chr
        s "Hahaha... hah... I'm so-... I'm s-sorry..."
        show sayori 3E with dissolve_chr
        s "You even sound like her!"
        mc "Sayori, neither your rambling nor your laughter are giving me any clue on what you're even on about..."
        show sayori 3l with dissolve_chr
        s "Y-Yeah, s-sorry..."
        s "I just wanted to say that both your poems are so similar..."
        s "...they actually remind me of someone."
    else:
        show sayori 1b at t11
        s "..."
        show sayori 1c with dissolve_chr
        s "Whoa, now that's some drastic change."
        mc "Huh? What are you on about?"
        show sayori 3c with dissolve_chr
        s "Well, it's different from your last one..."
        show sayori 3b with dissolve
        s "Like... {i}very{/i} different..."
        s "..."
        show sayori 1c with dissolve_chr
        s "What made you change your style so much?"
        mc "Hmmm..."
        mc "Well, I don't have a straight answer to that, but..."
        mc "Maybe I wrote it like that after yesterday's feedback or something..."
        mc "Honestly, I don't know, it just came out that way."
        show sayori 2d with dissolve_chr
        s "No offense, but... it didn't help you much."
        mc "Well... at least I tried."
        show sayori 1a with dissolve_chr
        s "Hey, I didn't say it's bad! You just didn't make much progress, but I'm guessing you're just experimenting a bit..."
        show sayori 1x with dissolve_chr
        s "You know, trying to find your style and all?"
        mc "Maybe..."
        mc "So what's your opinion on it? That new... style I chose, or at least you said I did."
        show sayori 1q with dissolve_chr
        s "Well... now that you asked..."
        s "...it actually reminds me of someone..."

    mc "Someone?"
    show sayori 1r with dissolve_chr
    s "Oh, you know. Just look at your poem and tell me who likes writing them like this?"
    show sayori 2n with dissolve
    s "Or at least she said she did. I've only seen two of her poems so far..."

    mc "W-Wait, you mean... you're talking about someone from our club?"

    show sayori 4r with dissolve_chr
    s "Of course, silly! Where else would you get inspiration for writing a poem like this one?"
    show sayori 1x with dissolve_chr
    s "Just think. Does it ring a bell? Short, simple, and effi-{w=0.7}{nw}"
    show sayori 1o with dissolve
    s "Eff...ish...?"
    mc "Efficient..."
    show sayori 1l with dissolve_chr
    s "Yeah, that one..."

    mc "So... who should it remind me of?"

    show sayori 4x with dissolve_chr
    s "Natsuki, of course! It's obviously her style!"
    show sayori 3l with dissolve_chr
    s "Okay, not exactly her style, but... similar to hers..."

    mc "...and still lacking quality in comparison?"

    s "Y-Yeah, kinda..."

    mc "Well, at least you're honest."
    mc "Besides, I'm pretty sure it's just a coincidence. We hardly know each other, so us having the same style sounds quite far-fetched."

    show sayori 1x with dissolve_chr
    s "Hmm... You know, now that I think about it, it might actually be a very good thing!"

    mc "How so?"

    show sayori 3x with dissolve_chr
    s "Well, since you two have something in common, it should be easier for you to become friends, right?"
    show sayori 4x with dissolve_chr
    s "Have I told you that she also likes reading manga?"
    mc "I think that's one of the first things I learned about her."
    "I chuckle as my memory starts bringing up the image of her face."
    mc "Her reaction is something you can't easily forget..."
    show sayori 4p with dissolve
    s "{i}Manga is literature!{/i}"
    show sayori 1D with dissolve

    "We both start covering our mouths to at least somewhat muffle our laughter."
    "I really hope Natsuki didn't hear Sayori mocking her. Otherwise, we're both goners..."
    mc "Ahahaha... phew... Okay, Sayori, let's bring it down a notch..."
    show sayori 1l with dissolve
    s "Ahaha... Yeah, or else Natsuki will strangle us both..."
    mc "Yeah..."
    show sayori 1y with dissolve_chr
    "We both settle down, finally."
    "I clear my throat, trying to put on my business face again."
    mc "So..."
    mc "Want to show me your poem now?"
    show sayori 4x with dissolve_chr
    s "Of course!"
    return

label poemresponse_3_sayori_appeal_yuri:
    if poemwinner[0] == "yuri":
        show sayori 1n at t11
        s "..."
        s "Wow, you're really into this stuff, aren't you?"
        mc "Are we still talking about my poem? Because the last time you said something like that, you were blaming me for watching too much anime."
        show sayori 1r with dissolve_chr
        s "Well, yes, I was talking about your poem..."
        show sayori 1s with dissolve_chr
        s "...but now that you've mentioned it, I still think that you watch too much anime!"
        mc "Sigh..."
        mc "Get to the point, Sayori."
        show sayori 3x with dissolve_chr
        s "Well, this poem is very similar to your previous one!"
        show sayori 3l with dissolve_chr
        s "In both style and... quality, I'm afraid..."
        show sayori 1x with dissolve_chr
        s "But there is something more to it..."
        mc "What do you mean?"
        show sayori 1a with dissolve_chr
        s "Well, your style... it's very complex and unusual, definitely something I didn't expect from you..."
        show sayori 4x with dissolve_chr
        s "But I think I finally get where it comes from!"
        mc "Oh really? Surprise me."
    else:
        show sayori 1b at t11
        s "..."
        s "Hmm... Now that was unexpected..."
        mc "What was, Sayori? I'm still having trouble reading your thoughts, you know?"
        show sayori 1q with dissolve_chr
        s "Ehehehe..."
        show sayori 1a with dissolve_chr
        s "I'm just saying that it's really weird that you've suddenly changed your style so much."
        show sayori 3n with dissolve_chr
        s "I mean, this one is different from your previous poem..."
        show sayori 3o with dissolve_chr
        s "You used so many complicated words and... metaphors and all that stuff..."
        mc "No offense, Sayori, but I think that you and I have a slightly different level of 'complicated,' especially when it comes to words..."
        show sayori 5c with dissolve
        s "Hey, no need to be mean about it!"
        mc "Wish I was, but I'm afraid that I'm just telling the truth."
        show sayori 5d with dissolve_chr
        s "..."
        mc "So, can you tell me what you think about it?"
        mc "I get that it's different, and it makes sense since I tried to recall what you all told me yesterday, you know? Actually listen to your feedback?"
        mc "The real question is: Did it get better or worse?"
        show sayori 3c with dissolve_chr
        s "You know, to be fair, it's hard for me to say."
        s "Because I don't think I understand your poem at all."
        show sayori 1c with dissolve_chr
        s "Its style, its meaning, its language... all of it is so-{w=0.7}{nw}"
        show sayori 1o with dissolve_chr
        s "Wait a minute..."
        show sayori 1E with dissolve_chr
        s "Waaaaait a minute..."
        show sayori 3E with dissolve_chr
        s "I think I finally understand where it's all coming from!"
        mc "Well, then you've found out something even I don't know, congrats."

    show sayori 1q with dissolve_chr
    s "Ehehehe..."
    s "[player], tell me..."
    show sayori 1x with dissolve_chr
    s "Are you trying to imitate Yuri's style?"

    mc "..."
    mc "That's definitely not something I expected to hear..."
    mc "I mean, come on. My poems can't possibly be close to Yuri's standard!"

    show sayori 2E with dissolve_chr
    s "Well, I never said they were on par with her poems, but I think you are... kinda following her example."

    mc "Really? And that's after just two poems? And even though I wrote the first one before I learned what her style was?"
    mc "Don't be ridiculous, Sayori."

    show sayori 1d with dissolve_chr
    s "Well, I might be mistaken, of course..."
    show sayori 2c with dissolve_chr
    s "But think of the bright side!"
    show sayori 2x with dissolve_chr
    s "If you two like this writing style, then that could be your common ground of sorts!"

    mc "Um... I suppose..."

    show sayori 4r with dissolve_chr
    s "I'm sure she'll love it!"
    show sayori 1l with dissolve_chr
    s "A-And she could also give you some good advice. She's the one here with most experience, after all..."

    mc "Honestly, Sayori, if you hadn't told me that my poems are close to Yuri's..."
    mc "...I don't think I would have even noticed that."
    mc "So all of that might be a mere coincidence at this point."

    show sayori 1y with dissolve_chr
    s "Yeah... You might be right."
    mc "..."
    s "..."

    "{i}Why the awkward pause again?{/i}"

    mc "L-Let's just forget about this whole thing and move on..."

    show sayori 1b with dissolve_chr
    s "Hmmm?"

    mc "Can you show me your poem now?"

    show sayori 2x with dissolve_chr
    s "Oh, okay!"
    return

label poemresponse_3_sayori_appeal_monika:
    if poemwinner[0] == "monika":
        show sayori 1a at t11
        s "..."
        s "You seem to really like this style."
        show sayori 3c with dissolve_chr
        s "But to be fair, I think you're giving yourself quite a challenge."
        mc "I think I heard something similar yesterday..."
        show sayori 1x with dissolve_chr
        s "It's not surprising. You try to make your poems so serious, so complex, and yet so easy to understand!"
        s "It looks like you're dashing through, trying to be the best at everything!"
        mc "Do I succeed in it?"
        show sayori 3l with dissolve_chr
        s "Ehhh... not really..."
        mc "Figured as much."
        show sayori 1b with dissolve_chr
        s "What's more interesting is that I think I've seen something similar before..."
    else:
        show sayori 1b at t11
        s "..."
        show sayori 3c with dissolve_chr
        s "Wow, why the sudden change?"
        mc "What are you talking about?"
        show sayori 1c with dissolve_chr
        s "Well, it's different from your previous poem. That's why I'm wondering."
        mc "Define 'different,' Sayori."
        show sayori 1g with dissolve_chr
        s "Um, I mean it's... not like the one you wrote before..."
        mc "..."
        mc "Sayori, promise me one thing..."
        show sayori 4x at h11
        s "Which one?"
        mc "Please don't ever try to write a thesaurus."
        show sayori 3B with dissolve_chr
        s "A what?"
        mc "..."
        mc "I guess I'm fine with that answer..."
        mc "Okay, can you now tell me how it's different?"
        show sayori 1c with dissolve_chr
        s "Well, it feels like you were trying to reach some new heights..."
        show sayori 3c with dissolve_chr
        s "You know, change your style, make everything super classy?"
        show sayori 3o with dissolve
        s "I can't put my finger on it, but it feels like I've seen it somewhere before..."

    mc "Well, wherever you saw it, it definitely belongs to a much better writer than me."

    "{i}That's not how you say \"an actual writer\", dude...{/i}"

    show sayori 1q with dissolve_chr
    s "Yeeeeah... definitely..."

    mc "...?"
    mc "What's with that look, Sayori? And that voice?"

    show sayori 2q with dissolve_chr
    s "Oh, you know, nothing..."
    mc "Sayori, you know that saying 'nothing' in situations like this means there's actually something, right?"

    show sayori 2r with dissolve_chr
    s "Hehehe... Of course I do, silly. That's why I'm doing it."

    mc "..."
    mc "Spit it out already. I'm not in the mood for games..."

    show sayori 1x with dissolve_chr
    s "Well, there's only one person I know who's constantly trying to be the best of the best!"
    s "And I'm guessing her attitude started rubbing off on you, didn't it, [player]?"

    mc "{i}Her?{/i}"

    show sayori 4r with dissolve_chr
    s "Oh quit playing stupid, you know I'm talking about Monika!"

    "Did {i}Sayori{/i} just tell {i}me{/i} to quit playing stupid?"

    show sayori 1x with dissolve_chr
    s "You decided to follow in her footsteps, right? Look up to her?"
    show sayori 3x with dissolve_chr
    s "It's only natural, since she's, you know, always so good at what she does!"
    show sayori 3l with dissolve_chr
    s "Which is... anything, really..."

    mc "Are you... serious right now?"

    show sayori 1b with dissolve_chr
    s "What? You don't think of her that way?"
    mc "No, I meant: Are you serious about me looking up to her?"

    show sayori 3c with dissolve_chr
    s "Well, I think it makes sense..."

    mc "You... might have a point there, but I personally think there's less to it all than you think..."
    mc "I mean, Monika has always been like this, so why would I start looking up to her just now?"

    show sayori 1r with dissolve_chr
    s "Because you're now in this club, silly. You get to see her everyday!"
    show sayori 1x with dissolve_chr
    s "And to be honest, I don't think it matters!"
    s "I think of it more as an opportunity for you two to get along!"

    mc "You know, I think we've been managing well enough so far."

    show sayori 1a with dissolve_chr
    s "That's because she's the president. She has to be nice to everyone."
    show sayori 4x with dissolve_chr
    s "But imagine if you two had more in common!"

    mc "..."
    "You have a talent for making things sound awkward, Sayori..."

    mc "You know, how about we leave this discussion for another time?"

    show sayori 1b with dissolve_chr
    s "Hmm?"
    s "Okay... If you say so..."
    show sayori 3x with dissolve_chr
    s "Actually, how about you see my poem now?"
    mc "Sounds good."
    return





label poemresponse_3_yuri:
    show yuri 1a at t11
    mc "Hey, Yuri."

    show yuri 1m with dissolve_chr
    y "[player]..."
    y "It's only our second time sharing, but it feels like we've been doing this for ages..."

    mc "I can't say I can relate, but I'm glad that you're at least more comfortable with it."

    show yuri 2u with dissolve_chr
    y "Well, yes... I hope I am..."

    mc "Don't worry. Of the two of us, you're definitely not the one who should be shy about her poems."

    show yuri 2t with dissolve_chr
    y "And what about you? Do you think your writing has improved from your previous attempt?"

    mc "In just one night? Nah."
    mc "I tried my best to take some notes, listening to all of you..."
    mc "But for someone like me, becoming at least somewhat decent will probably take months, if not ages..."

    show yuri 2v with dissolve_chr
    y "You should really be a bit more confident in your abilities..."

    "I cover my face and chuckle slightly."

    mc "Now that's ironic..."

    show yuri 3q with dissolve_chr
    y "Ehehe... y-yes, I suppose I'm really not the one to point out someone's lack of confidence, am I?"

    mc "Yes, and I'm still trying to figure out where it all comes from."

    show yuri 2A with dissolve_chr
    y "..."
    y "I... have my reasons..."
    "And there's that defensive attitude again..."

    show yuri 2w with dissolve
    y "I'm sorry, [player]. I understand that my... behavior may cause you some discomfort, but--"

    mc "Yuri, you said it yourself: 'You have your reasons.'"

    show yuri 3t with dissolve_chr
    y "Huh?"

    show yuri 1u with dissolve
    y "Y-yes... Thank you, [player]..."

    mc "How about we get to the whole... poem sharing thing? Monika said we don't have much time left."

    show yuri 1s with dissolve_chr
    y "It would be most logical."

    mc "So... ladies fi--"

    show yuri 1m with dissolve_chr
    y "[player]..."
    mc "Ahaha... Sorry, had to try it."
    "I hand her my notebook."

    scene bg club_day with wipeleft_scene
    $ renpy.call("poemresponse_3_yuri_appeal_{appeal}".format(appeal=poemwinner[1]))

    "Yuri hands me her notebook."
    "To be fair, knowing her personality, I could easily call it a private diary of sorts."

    call showpoem (poem_y_2)

    show yuri 3s with dissolve
    mc "..."
    show yuri 3t with dissolve_chr
    y "Um, did you enjoy it?"
    show yuri 3n with dissolve_chr
    y "It... d-didn't weird you out, did it?!"
    show yuri 3o with dissolve_chr
    y "Oh gosh, I--"

    mc "Yuri, is there ever a time when you're not so self-critical?"
    show yuri 3n with dissolve_chr
    y "I just... wanted to try something closer to my regular style this time..."
    show yuri 3o with dissolve_chr
    y "And I was really worried that you might find it... confusing..."
    mc "Well, it's definitely closer to what I originally expected..."
    mc "And I'm not gonna lie. I don't think I fully understand it."
    mc "It's really beautiful, though. Reminds me of what you were saying about the beauty of nature."

    show yuri 3u with dissolve_chr
    y "Yes... I personally think it's one of most gorgeous things you can possibly convey in any sort of art, especially in prose or poetry..."
    show yuri 2u with dissolve_chr
    y "I really love how some writers manage to describe a landscape... sometimes, you can almost feel that you're actually standing there."
    mc "But this poem... it's not just about nature's beauty, is it?"
    show yuri 2A with dissolve_chr
    y "..."
    show yuri 2w with dissolve_chr
    y "N-No... it's not..."
    "Yuri takes some time to collect herself. There obviously has to be some deeper meaning to her poem."
    "{i}An outcast, desperate to stay warm?{/i}"
    "{i}Whose path is nearly bare of travel?{/i}"

    mc "Yuri, mind if I take a wild guess?"
    show yuri 2B with dissolve_chr
    y "Hmm?"
    show yuri 2f with dissolve_chr
    y "O-Oh, of course."
    mc "That mysterious figure, all alone in open tundra, an outcast..."
    mc "Is... that how you see yourself?"
    show yuri 2w with dissolve_chr
    "She looks away and sighs. It seems I'm touching some really delicate topic here."
    show yuri 2A with dissolve_chr
    y "I'm afraid you don't know me well enough at this point, [player]..."

    "{i}Does anyone?{/i}"
    show yuri 2v with dissolve_chr
    y "So I can't tell you why I portray myself like this..."
    show yuri 2u with dissolve
    y "But..."
    y "If you read a bit more into it, you can see that it actually has a much deeper meaning."
    show yuri 1u with dissolve_chr
    y "Even in our most difficult moments, when we feel abandoned and all alone..."
    y "...when the very light of the world itself seems dim to your eyes..."
    show yuri 1s with dissolve_chr
    y "There's still beauty in that moment... you just need to find it."

    mc "Like here, for example? The beauty of the Northern Lights?"
    show yuri 3s with dissolve_chr
    y "Exactly. They represent the things that keep you going, things that bring joy and purpose in your life..."
    show yuri 3u with dissolve_chr
    y "Whenever you look at some random stranger passing by, you don't get to see their mind, their soul. You judge them by their looks, immediately giving them labels, jumping to conclusions..."
    y "But usually you can't even begin to imagine what world that person might actually live in..."
    show yuri 1m with dissolve_chr
    y "...what is most important for them, what those images are that drive them, those... {i}Auroras{/i} that give them hope."
    mc "{i}It is great wonder her path is nearly bare of travel.{/i}"
    show yuri 1e with dissolve_chr
    y "...?"
    show yuri 2s with dissolve_chr
    y "Y-You... you understood..."

    mc "Vaguely..."
    mc "I'll be honest with you, Yuri, I still don't get you, but whatever is this world you live in, I'm sure it's something fascinating."
    show yuri 2u with dissolve_chr
    y "T-Thank you... it's really nice to hear that coming from you."
    mc "I'm glad you shared it with me."
    mc "Okay, now I've got to go."
    show yuri 1m with dissolve_chr
    y "Y-Yes, you're right. I've already taken enough of your time."
    show yuri zorder 1 at thide
    hide yuri
    "Saying that Yuri is an unusual person would be an understatement..."
    "But I'm still glad we're making some slow, but steady progress."
    return


label poemresponse_3_yuri_appeal_sayori:
    if poemwinner[0] == "sayori":
        show yuri 2g at t11
        y "..."
        show yuri 1a with dissolve_chr
        y "Well, it seems that some things aren't meant to change..."
        mc "Like the quality of my poems?"
        show yuri 1m with dissolve_chr
        y "Not quality, but the style, I suppose."
        y "Yesterday, I didn't quite understand what you had in mind, but I think I now get the full picture."
    else:
        show yuri 2g at t11
        y "..."
        y "Hmm... now that's a bit unusual."
        mc "What is?"
        show yuri 2h with dissolve_chr
        y "You changed your style suddenly, and I'm trying to understand your reasoning behind it..."
        mc "A result of some completely spontaneous decision?"
        mc "Or just trying to experiment? I mean, that does sound like me."
        show yuri 2i with dissolve_chr
        y "It could've been that, if not for your choice of that... particular style..."
        y "..."
        show yuri 1m with dissolve_chr
        y "No, I think I know where it comes from..."

    mc "Really? Enlighten me, then."

    show yuri 1a with dissolve_chr
    y "You see, [player], a lot of writers prefer to start with something familiar in mind..."
    show yuri 1i with dissolve_chr
    y "It can be their hobby, or perhaps the place they live, or the people who surround them..."
    y "...be it their family or their friends..."

    mc "Umm... I'm not sure I follow."

    show yuri 1k with dissolve_chr
    y "How long have you been friends with Sayori?"

    mc "Oh... ummm... we've been friends since we were kids. I think we've already told you that."

    show yuri 1m with dissolve_chr
    y "Then I guess it makes sense."

    mc "What makes sense? What do you mean, Yuri? What does Sayori have to do with my poems?"

    show yuri 1a with dissolve_chr
    y "I thought it would be obvious."
    y "I've seen her poems too, you know? I can tell when people share certain traits."
    show yuri 2m with dissolve_chr
    y "And I can see those similarities expressed in the poems you both write."

    mc "Well... I guess we have to be somewhat similar... we {i}are{/i} friends, after all..."
    mc "But I still don't see how our poems fall into this."

    show yuri 2k with dissolve_chr
    y "Do you remember what I said on our first day?"
    y "{i}The truest form of writing is writing to oneself.{/i}"
    show yuri 2f with dissolve_chr
    y "In any poem you write, no matter how hard you try to conceal it, you give your reader a glance on your true nature."
    show yuri 1m with dissolve
    y "And a person with an... eye for this kind of thing can exploit it to its full potential."

    mc "Really now? And what did you manage to find out?"

    show yuri 1c with dissolve_chr
    y "That it might be... interesting to observe you two."
    mc "Wha--"

    show yuri 1k with dissolve_chr
    y "As for your writing skills, I would say that you should still work on your style."
    show yuri 1l with dissolve_chr
    y "Sayori seems far more confident in her abilities than you at this point."
    show yuri 1m with dissolve_chr
    mc "Wait, Yuri, what did you mean by-{w=0.5}{nw}"
    show yuri 2m with dissolve
    y "I'm sorry, [player], but I don't want to tell you anything I'm not sure of yet."

    mc "..."
    mc "Yuri, that's cheating!"

    show yuri 1c with dissolve
    y "Perhaps. But I'm not going to change my mind, regardless."

    mc "..."
    mc "Sigh..."
    mc "I... guess we'll just skip to your poem now?"

    y "Mhm."
    return

label poemresponse_3_yuri_appeal_natsuki:
    if poemwinner[0] == "natsuki":
        show yuri 2i at t11
        y "..."
        y "Can't say I understand your choice, but I can at least see that it's not deliberate, more or less..."
        mc "Yuri, you're a master of speaking in riddles, but I'm really not in the mood to solve them."
        show yuri 1m with dissolve_chr
        y "Well, you see, at first I assumed that your choice of that particular style was coincidental..."
        show yuri 1a with dissolve_chr
        y "...but I suppose that you indeed chose it because it... suits you."
        mc "To be fair. I still think that most of the things I do are just coincidences..."
        show yuri 1i with dissolve_chr
        y "Perhaps... but I still think that you had someone in mind while writing your poems..."
    else:
        show yuri 2g at t11
        y "..."
        y "Now that's something I certainly didn't expect..."
        show yuri 2f with dissolve_chr
        y "What inspired you to make such a drastic change?"
        mc "Ummm... I think 'inspired' is a strong word, Yuri."
        mc "And what do you mean by 'change'? Definitely not the quality, I'd wager."
        show yuri 2h with dissolve_chr
        y "It's the style, [player]... It's very different from the one you used yesterday..."
        mc "Well... I did talk to all of you, so that might've had a certain effect..."
        mc "I am trying to improve, you know? To find my style?"
        show yuri 1i with dissolve
        y "Hmm... Yes, you might have a point..."
        show yuri 1j with dissolve_chr
        y "Actually, I believe I know who had that effect on you..."

    mc "Wait, you mean someone in particular?"
    show yuri 1u with dissolve_chr
    y "Well, there's only one more person I know who shares a similar style..."
    show yuri 1v with dissolve_chr
    y "And to be fair, I still find it hard for me to understand it."

    mc "..."
    mc "W-Wait, you're talking about Natsuki, am I right?"

    show yuri 1l with dissolve_chr
    y "It was quite obvious, wasn't it?"

    mc "Not exactly... not until you mentioned that you don't understand that style."

    show yuri 3q with dissolve_chr
    y "Well, y-yes, I'm afraid it's still quite... odd for my taste..."
    show yuri 3t with dissolve_chr
    y "But I remember our talk yesterday, and I agree with Monika. We all have our own paths."

    mc "At any rate, I think my poems are still far from Natsuki's level."
    mc "Her poems... 'pack a punch,' so to speak, and I don't think mine are close to that level."

    show yuri 2q with dissolve_chr
    y "That is somewhat true, I'm afraid..."

    mc "Besides, my style still might change in the future, right? As I said before, I hardly know what I'm doing."

    show yuri 2s with dissolve_chr
    y "I'm curious to see if it will."
    show yuri 2u with dissolve_chr
    y "But please don't let my words get to you. This is just my opinion, after all, nothing more."

    mc "Noted."

    y "..."

    mc "So... can I see what you wrote for today?"

    show yuri 2f with dissolve_chr
    y "O-Oh, of course..."
    return

label poemresponse_3_yuri_appeal_yuri:
    if poemwinner[0] == "yuri":
        show yuri 2u at t11
        y "..."
        show yuri 2s with dissolve_chr
        y "[player], I see you're making certain progress."
        mc "You think so? That's a relief."
        show yuri 2u with dissolve_chr
        y "I'm serious. It's indeed better than your previous one. Still far from perfection, but you're going the right way."
        show yuri 2s with dissolve_chr
        y "Who knows, you might even have a knack for it. Not everyone can start off with such a complicated style, you know?"
        mc "Well, I'm trying my best to learn from all of you, for what it's worth..."
    else:
        show yuri 2u at t11
        y "..."
        y "I'm glad to see that my feedback helped..."
        mc "You mean... it actually got better?"
        show yuri 3s with dissolve_chr
        y "It's still rough, and that's not a big surprise. This style requires certain skill."
        y "But I definitely like this new direction you picked."
        show yuri 2m with dissolve_chr
        y "Admit it, it's so much more beautiful and profound this way, isn't it?"
        show yuri 2l with dissolve_chr
        y "Be it a beauty of nature, or a tale of a lone wanderer... there are so many exquisite words which you can use to describe it all..."
        mc "..."
        show yuri 2B with dissolve_chr
        y "...?"
        show yuri 3q with dissolve_chr
        y "S-Sorry, sorry... I know I can get carried away easily..."
        show yuri 2s with dissolve_chr
        y "The point is, I'm glad with your progress. I really think you can go far."
        mc "Well, it's good to hear you think that way."
        mc "I really hope that I'll be able to learn a thing or two from all of you."

    show yuri 4b with dissolve_chr
    y "Well... if you ever need some advice... I'm always here..."
    mc "I know, and I appreciate it, trust me."
    show yuri 4a with dissolve_chr
    y "I... might even have some good literature for you to read..."
    show yuri 4b with dissolve_chr
    y "...to, y-you know... find some inspiration..."
    mc "Still want to get me into reading, Yuri?"
    show yuri 3q with dissolve_chr
    y "Ehehe... I-I hope you don't blame me too much for trying..."

    mc "I guess I shouldn't. It {i}is{/i} weird to be a member of the Literature Club with close to no interest in literature."
    show yuri 2u with dissolve_chr
    y "My point exactly."
    y "But I'm not going to push you. I'm certain that one day you will be willing to give it a try yourself."
    mc "Everything's possible."
    show yuri 1s with dissolve_chr
    y "It would be nice to have someone to talk about it."
    mc "You know, I tried to talk to you earlier today, and you kinda alienated me..."
    show yuri 1k with dissolve_chr
    y "Well, I wouldn't want this conversation to be forced. Can you blame me for that?"
    mc "Ahaha... yeah, I guess not."
    mc "So, now that that's over, would you like to share your poem with me?"
    show yuri 3s with dissolve_chr
    y "I would love to."
    return

label poemresponse_3_yuri_appeal_monika:
    if poemwinner[0] == "monika":
        show yuri 2g at t11
        y "..."
        show yuri 2j with dissolve_chr
        y "Hmm... I see you're not someone looking for easy ways..."
        mc "Yuri, with my intelligence, I just {i}have{/i} to learn the things hard way, you know?"
        mc "Also, what are you actually talking about?"
        show yuri 1m with dissolve_chr
        y "Hmmm, when viewing it from this perspective, it might not be a bad thing, after all."
        show yuri 1a with dissolve_chr
        y "As I was saying yesterday, it's a bold approach, not something you would expect from a novice."
        y "It's a big challenge, as you constantly try to chase perfection."
        show yuri 1l with dissolve_chr
        y "Your ultimate goal in it would be to deliver every aspect of the poem on the highest level."
        show yuri 1i with dissolve_chr
        y "The problem is: not everyone's up to the task."
        mc "And I guess that includes me..."
        show yuri 2j with dissolve_chr
        y "You know, [player], I'm actually more curious about what inspired you to pick that style in the first place..."
        mc "I don't know... a love for challenge? Desire to be the best, maybe?"
        show yuri 1m with dissolve_chr
        y "Hmmm..."
        show yuri 1a with dissolve_chr
        y "Yes... that sounds plausible, indeed..."
    else:
        show yuri 2g at t11
        y "..."
        y "That's... not exactly what I meant yesterday..."
        mc "Ummm, what?"
        show yuri 2f with dissolve_chr
        y "Eh?"
        show yuri 2h with dissolve_chr
        y "O-Oh, I was saying that it's... not what I expected you to draw from my yesterday's feedback..."
        mc "C-Can you be more specific?"
        show yuri 1u with dissolve_chr
        y "Well it's... kind of what I had in mind, and at the same time... it's not."
        show yuri 1t with dissolve_chr
        y "And to be honest, I think you're biting off a bit more than you can chew..."
        mc "Okay, now I'm completely confused. What are you on about, Yuri?"
        show yuri 1v with dissolve_chr
        y "Well, you see, that style is somewhat close to mine, but it..."
        show yuri 2h with dissolve_chr
        y "...no, no, that's not the point..."
        show yuri 2t with dissolve_chr
        y "I wanted to tell you that this style... it's not a good option to start with."
        mc "Ummm... why? Is it... too complicated or what? You said I'm biting off more than I can chew."
        show yuri 1v with dissolve
        y "Yes, that's exactly what I meant. It's challenging, it's demanding, it... sets the bar quite high..."
        show yuri 1t with dissolve_chr
        y "I suppose you just got a bit overwhelmed with all our opinions yesterday and decided that you need to make everything... flawless..."
        show yuri 1h with dissolve_chr
        y "And that's not a bad thing, of course. Trying to be the best in everything is an admirable ambition..."
        y "For example, just take a look at-{w=0.5}{nw}"
        show yuri 1g with dissolve_chr
        y "Wait a minute..."
        show yuri 1h with dissolve_chr
        y "Can it be?"
        y "Hmmm..."
        show yuri 1a with dissolve_chr
        y "Well, I suppose that shouldn't be surprising."

    mc "I know that smile, Yuri, what's on your mind?"

    show yuri 1c with dissolve_chr
    y "Tell me, [player], are you looking up to Monika for guidance?"

    mc "Ehhh... come again?"

    show yuri 1b with dissolve_chr
    y "I don't know anyone else who would be better to ask for such advice."
    show yuri 1u with dissolve_chr
    y "Always ahead of everyone, always trying to reach the stars..."
    show yuri 1s with dissolve_chr
    y "It's natural for people to be drawn to her, don't you think?"

    mc "I... agree with you, Yuri, but I don't quite get what you were saying about the guidance..."

    show yuri 1m with dissolve_chr
    y "I meant that she's been somewhat of a source for you inspiration."
    show yuri 1i with dissolve_chr
    y "And I can only commend you for it: looking up to people like her, setting yourself high goals right from the start..."
    y "...it's a really good way to go. It shows your confidence and determination."

    mc "I think you're exaggerating a bit, honestly..."

    show yuri 1m with dissolve_chr
    y "Perhaps, but I'm still curious to see what will your next steps be..."

    mc "Heh... guess there's only one way to find out..."
    mc "Okay, I think it's about time for you to share your poem, don't you think?"

    show yuri 2a with dissolve_chr
    y "Of course, [player], here you go."
    return






label poemresponse_3_natsuki:
    show natsuki 3k at t11
    mc "Hey there. Everything okay?"
    show natsuki 3q with dissolve_chr
    n "Fine... I guess..."
    mc "Come on, it's not so bad, after all."
    mc "I actually thought that you would be more willing to share this time. Everyone looked so excited about it yesterday."
    show natsuki 3m with dissolve_chr
    n "Well, I don't think I have much choice..."
    n "Monika is still going to make me share, isn't she?"

    mc "Come now, Natsuki. You sound like you're afraid of Monika or something."
    show natsuki 5e with dissolve_chr
    n "I never said I was afraid, dummy!"
    mc "Then why the lack of confidence?"
    show natsuki 5q with dissolve_chr
    n "It's just... I..."
    show natsuki 5s with dissolve_chr
    n "I really don't like being pushed around, you know?"
    show natsuki 5u with dissolve_chr
    n "And Monika can sometimes be... you know, pushy..."

    mc "Like putting everyone on the spot, asking them to share their work?"
    show natsuki 5E with dissolve_chr
    n "Y-Yeah... pretty much..."
    mc "You do understand that she's doing this {i}for{/i} us?"
    mc "She's helping us with our insecurities, helps us improve our writing skills {i}and{/i} strengthen the bond of our club, all at the same time."
    show natsuki 5m with dissolve_chr
    n "Well, yeah, I know that, but that doesn't help me much..."
    show natsuki 5s with dissolve
    n "{i}(And neither do you...){/i}"

    mc "Well, if it makes you feel any better, just take a look at me..."
    mc "No clue what he's doing, no particular reason to be here, can hardly talk to anyone without making a fool of himself in the process..."
    mc "...and yet I'm still here. So you definitely shouldn't make a big deal out of it."
    show natsuki 3t with dissolve_chr
    n "Yeah... guess you're right."
    mc "Also, a little a side note..."
    mc "It's one of the first times I've gotten to talk with you without you threatening to cause me some physical harm..."
    mc "I really like it that way, you know? Let's make it a habit."
    show natsuki 4y with dissolve_chr
    n "Then I suggest you cherish these moments."
    n "Otherwise, who knows? I might accidentally find your body parts in the dough for my cupcakes..."
    mc "..."

    show natsuki 4K with dissolve
    n "..."
    show natsuki 6a with dissolve
    n "...pfffff..."
    show natsuki 6d with dissolve_chr
    n "Ahahahahahaha!"
    "{i}Phew!{/i}"
    n "You should've... ahahah... you s-should've seen your f-face, ahaha!"
    mc "Damn it, Natsuki!"
    mc "Don't say stuff like that with a straight face!"
    mc "I was ready to run for my life!"

    show natsuki 6f with dissolve
    n "Ahahaha!"
    "Soon enough, I, too, give in to Natsuki's contagious laughter."
    show natsuki 7b with dissolve
    n "Ahaha... aha... o-okay, okay..."
    show natsuki 7a with dissolve_chr
    n "Hem-hem!"
    show natsuki 4t with dissolve_chr
    n "I... think we should move on now..."
    mc "Yeah, you're right. But don't get me wrong, it's really nice to see you unwind every now and then."
    mc "Seems like there's still a human being beneath that passive-aggressive attitude of yours."

    show natsuki 4y with dissolve_chr
    n "Hah! You don't know the half of it!"
    mc "Then how about you give me your poem and let me learn a thing or two?"
    show natsuki 5d with dissolve
    n "You first! Since you were the one talking about all those insecurities we need to overcome!"
    n "We'll also see if my advice yesterday did you anything good."
    mc "Suit yourself."
    "I hand Natsuki my notebook."

    scene bg club_day with wipeleft_scene
    $ renpy.call("poemresponse_3_natsuki_appeal_{appeal}".format(appeal=poemwinner[1]))

    "Natsuki hands me a sheet with her poem."
    "Surprisingly enough, this time it's not written in pink ink. Wonder if that had something to do with her mood."

    call showpoem (poem_n_2)

    show natsuki 3c with dissolve
    mc "..."

    n "So, what do you think of this one?"
    show natsuki 5e with dissolve_chr
    n "Let me guess, you don't like it?"

    mc "Natsuki, can you please slow down for at least a minute?"
    mc "I like it! I even like it more than your previous one, it's actually so much closer to what you told me yesterday.."

    show natsuki 5q with dissolve_chr
    n "Oh, you're just saying that!"
    show natsuki 5u with dissolve_chr
    n "..."
    n "I wouldn't expect {i}you{/i} to understand..."
    show natsuki 5t with dissolve_chr
    n "Since you're the type of person that never leaves his house!"

    mc "Hey! Where did that even come from?"
    mc "Besides, I {i}do{/i} leave my house... every once in a while."

    show natsuki 4y with dissolve_chr
    n "Oh really? And where do you usually go?"

    mc "..."
    mc "The... park or something..?"

    show natsuki 3y with dissolve_chr
    n "Hah... figures..."

    mc "How is that even related, Natsuki?"

    show natsuki 3C with dissolve_chr
    n "*sigh*"
    show natsuki 3D with dissolve_chr
    n "You have to actually interact with people to understand just what jerks some of them can be."
    show natsuki 3h with dissolve_chr
    n "Not a problem you'd usually face sitting at home all day!"

    mc "Okay, at least now, I got some context to work with."
    mc "Mind if I ask you a straight question then?"

    show natsuki 5h with dissolve_chr
    n "Depends on the question..."

    mc "Is the fox in this poem actually you?"

    show natsuki 5i with dissolve_chr
    n "..."
    n "{i}Probably...{/i}"

    mc "So what you're trying to say is that our world isn't just about strength?"

    show natsuki 5s with dissolve_chr
    n "..."

    mc "And with enough skill and wit, even an underdog can come out victorious, right?"

    show natsuki 5q with dissolve_chr
    n "Uh-huh..."

    mc "But... who's the lion in this poem?"

    show natsuki 1o with dissolve_chr
    n "I-It...!"
    show natsuki 12b with dissolve_chr
    n "..."
    show natsuki 12c with dissolve_chr
    n "It doesn't matter!"
    mc "Whoa, s-sorry..."
    "Why am I apologizing?"
    n "It's okay! Are you done? Can I have it back?"
    mc "S-Sure, here you go..."

    show natsuki 12b with dissolve_chr
    "She almost tears the sheet from my hands."
    "We spend the next few seconds in a very awkward silence, until she finally calms down."

    show natsuki 12g with dissolve
    n "C-Could you please leave now?"
    show natsuki 12d with dissolve
    n "I... want to be alone for some time..."

    mc "S-Sure."
    mc "If you... well... need something, just tell me."

    show natsuki 12b with dissolve
    n "..."

    "Natsuki mumbles something in reply, but I can't figure out what."

    show natsuki zorder 1 at thide
    hide natsuki
    "That was really unexpected. I still feel like an idiot and I can't even tell why."
    "But most importantly, I feel sorry for her."
    "Because it seems that I've accidentally scratched the surface of some topic that I really shouldn't bring up."
    return

label poemresponse_3_natsuki_appeal_sayori:
    if poemwinner[0] == "sayori":
        show natsuki 3a at t11
        n "..."
        n "Well, I guess it makes some sense..."
        mc "My poem? Please. I don't recall the last time {i}I{/i} made any sense..."
        show natsuki 3d with dissolve_chr
        n "Well, I can't say I blame you for choosing that style. It's just easier this way."
        n "After all, you're only a rookie at this point."
        mc "So let me guess... still no deep, thought-provoking message and all that?"
        show natsuki 3t with dissolve_chr
        n "Well, yeah, pretty much."
        show natsuki 5y with dissolve
        n "But that's okay. After all it takes {i}skill{/i} to write something that would leave a reader in awe!"
        "And I was lecturing {i}that{/i} girl about her lack of confidence?"
        show natsuki 5t with dissolve_chr
        n "But to be fair, I don't think you're doing this just because it's easy. There's definitely more to it..."
    else:
        show natsuki 3k at t11
        n "..."
        n "Hmm, now that's some weird change..."
        mc "What do you mean?"
        show natsuki 3h with dissolve_chr
        n "Well, you switched to a pretty different style."
        n "This new poem of yours... way too carefree for my taste."
        show natsuki 4h with dissolve_chr
        n "I suppose you just understood that it's too early for you to write something complex and you decided to play it safe, huh?"
        mc "Ummm... weren't you the one who always talked about keeping things simple?"
        show natsuki 4q with dissolve_chr
        n "Well, yes, but that's not exactly what I meant."
        n "There's no point in overcomplicating, that's true..."
        show natsuki 4b with dissolve_chr
        n "But you still want your poem to have some sort of message, you know?"
        n "Making it an easy-read, just for the heck of it? That's not the way to go."
        mc "You pick some strong words, Natsuki. But I won't lie, you do have a point."
        mc "I was writing it because... well, I wanted and needed to write something, that's all."
        show natsuki 3d with dissolve_chr
        n "You know, when you put it like that, I think I finally understand why you're writing like this..."

    mc "Really? Then tell me what this is all about."
    show natsuki 5z with dissolve_chr
    "Natsuki giggles impishly."
    show natsuki 5t with dissolve_chr
    n "{i}Told her she brought you here for a reason...{/i}"
    mc "Huh? Turn the volume up just a bit, will you?"
    show natsuki 3d with dissolve_chr
    n "You and Sayori are two peas in a pod, aren't you?"
    mc "Whaaaa???"
    show natsuki 3a with dissolve_chr
    mc "Pfff! Natsuki, when was the last time you looked at us?"
    mc "A grumpy, unremarkable high schooler with an addiction to anime versus the walking incarnation of cheerfulness?"
    mc "How is that similar?"
    show natsuki 3y with dissolve_chr
    n "Well, now that you said it, I see you two together every day, you know?"

    mc "..."
    mc "...w-wait, what are you-{w=0.5}{nw}"
    show natsuki 3d with dissolve_chr
    n "But if we're talking about how you two look, then I hope you know that looks can be deceiving?"
    "You're living proof of that, Natsuki..."
    show natsuki 5d with dissolve_chr
    n "I think that you have more in common that you think. That goes for your taste in poetry at least!"
    mc "..."
    mc "Well... maybe... I don't know. I'm still not sure if that had any effect on my writing."
    show natsuki 5y with dissolve_chr
    n "Maybe, maybe not. Either way, I think we should talk about that some other time."
    mc "We can agree on that, at least. Can I see your poem now?"
    show natsuki 5t with dissolve_chr
    n "Help yourself..."
    return

label poemresponse_3_natsuki_appeal_yuri:
    if poemwinner[0] == "yuri":
        show natsuki 3s at t11
        n "..."
        show natsuki 3u with dissolve_chr
        n "Well, I guess it was foolish of me to expect something different..."
        mc "Let me guess... I once again failed to meet your expectations?"
        show natsuki 3q with dissolve_chr
        n "It's just hard for me to see so many people sticking to this style, it makes me feel like I'm doing something wrong..."
        n "...or like nobody takes me seriously."
        show natsuki 3b with dissolve_chr
        n "Tell me, did you at least listen to what I had to say yesterday?"
        mc "I listened to {i}everyone{/i}, Natsuki, including you."
        mc "And to be honest, I feel like I'm experiencing déjà vu right now."
        show natsuki 3k with dissolve_chr
        n "Ummm, what do you mean?"
        mc "This is the second day in a row that you've argued about which style is better."
        show natsuki 3m with dissolve_chr
        n "Huh?"
        show natsuki 3u with dissolve_chr
        n "Oh... {i}that{/i}..."
    else:
        show natsuki 3s at t11
        n "..."
        show natsuki 3q with dissolve_chr
        n "Jeez, that's definitely not what I wanted you to do..."
        mc "Well, excuse me. I don't recall getting any specifications."
        show natsuki 4h with dissolve_chr
        n "And I was naive enough to expect you to figure it out on your own!"
        mc "Ughhh..."
        mc "Just tell me what's wrong, Natsuki. That'll be helpful."
        show natsuki 4i with dissolve_chr
        n "You know, I'd kinda hoped that you would pay more attention to my advice."
        n "I told you, poetry isn't about fancy words. It doesn't all come down to just having a beautiful cover! It's much more than that!"
        mc "I think I heard something similar yesterday..."
        show natsuki 5b with dissolve_chr
        n "Well, yes, that's exactly what I was telling you when we shared our poems!"
        mc "That's not what I meant, Natsuki..."
        show natsuki 5c with dissolve_chr
        n "Huh?"
        show natsuki 5k with dissolve_chr
        n "..."
        show natsuki 5u with dissolve_chr
        n "Ah... y-yeah... I see what you mean..."

    mc "You and Yuri don't get along, do you?"

    show natsuki 3m with dissolve_chr
    n "Of course we do! It takes something more than just having a different taste to ruin a friendship!"
    show natsuki 5q with dissolve_chr
    n "We still argue every now and then, but that goes for everyone..."
    n "And besides, that last argument was probably the worst we had. We even managed to drag the rest of you into it..."
    mc "Well, it's like Monika said: we all have our paths. Keep that in mind and everything will be fine."
    show natsuki 5u with dissolve_chr
    n "Yeah, yeah..."
    mc "With that out of the way, can you tell me what you think of my poem? Did I make any progress, at least?"
    show natsuki 5t with dissolve_chr
    n "Heh... well, that style is definitely not my area of expertise, but I can tell you this much..."
    show natsuki 5z with dissolve_chr
    n "Your scribbles aren't even close to Yuri's poems!"
    show natsuki 5d with dissolve_chr
    n "And that's coming from me, who doesn't really like them to begin with!"
    mc "Pretty much what I expected."
    mc "Okay, your turn, Natsuki."
    show natsuki 5t with dissolve_chr
    n "Yeah, sure, let's get this over with..."
    return

label poemresponse_3_natsuki_appeal_natsuki:
    if poemwinner[0] == "natsuki":
        show natsuki 3a at t11
        n "..."
        n "Hmmm... guess I've underestimated you, [player]."
        mc "Did I... actually write something decent?"
        show natsuki 3z with dissolve_chr
        n "You wish!"
        mc "Heh, now that sounds more like the Natsuki I know."
        mc "But you did say that you underestimated me. What did you mean by that?"
        show natsuki 3d with dissolve_chr
        n "Well, you said that yesterday you wrote your poem completely by accident."
        n "But you wrote this one in a similar fashion! And I... like that..."
        n "I would even go as far as to say that you've actually improved... just a little bit."
    else:
        show natsuki 3H at t11
        n "..."
        show natsuki 4d with dissolve_chr
        n "Now that's more like it!"
        mc "Whoa, is that a positive feedback I hear?"
        mc "Who are you and what have you done with my Natsuki?"
        show natsuki 5g with dissolve_chr
        n "{i}(Don't call me yours...){/i}"
        show natsuki 5h with dissolve_chr
        n "And what I was trying to say is that I'm... glad that you listened to me..."
        show natsuki 5a with dissolve_chr
        n "I guess even someone as hopeless as you deserves a chance."
        mc "So I suppose you like it?"
        show natsuki 5d with dissolve_chr
        n "Well, I like it more than your last one, that's for sure."
        n "It could still use a lot of polishing, but at least you're on the right track now!"

    mc "What can I say? I aim to please."
    mc "Glad that you like it."
    show natsuki 5h with dissolve_chr
    n "Hey, I never said I liked it..."
    show natsuki 5s with dissolve_chr
    n "I mean, like... {i}like{/i} like..."
    "I cover my mouth, trying to supress the laughter."
    mc "Come again? I think you've just said the word \"like\" three times in a row."
    show natsuki 5w with dissolve_chr
    n "N-Never mind!"
    "Oh no, no, no, Natsuki, you're not taking away my entertainment..."
    mc "I also think you actually did say you like it. I mean, you said that my style is similar to yours."
    show natsuki 5e with dissolve_chr
    n "{i}Similar{/i}, yeah, but that's the best I can say about it so far!"
    show natsuki 5w with dissolve_chr
    n "Besides, I was just being polite! I'm just glad that you're not wasting everybody's time by coming here!"
    mc "What do you mean?"
    show natsuki 5q with dissolve_chr
    n "Well, I said that you're improving, right?"
    n "That should mean that our efforts won't go to waste, at least not completely."

    "Is she really doing that?"
    mc "It's good to see that you care about my progress."
    show natsuki 4o with dissolve_chr
    n "I-I d-don't...{w=0.5}{nw}"
    show natsuki 4x with dissolve_chr
    n "Ughhh..."
    n "I'm saying that it's... {i}nice{/i} to see that you're {i}making{/i} progress..."
    show natsuki 4e with dissolve_chr
    n "But don't expect me to actually {i}care{/i} about it!"
    show natsuki 3r with dissolve_chr
    n "And..."
    show natsuki 3o with dissolve_chr
    n "...?!"
    show natsuki 4p with dissolve_chr
    n "H-Hey, get that dumb smile off your face! What's so funny?!"
    "I wonder, how many seconds will I live if I actually call her tsundere?"
    mc "It's nothing, Natsuki. I'm just in a good mood."

    show natsuki 5x with dissolve_chr
    n "Hmph! Sure you are..."
    mc "Okay, now do I get to see your poem?"
    show natsuki 5q with dissolve
    n "Yeah, fine, go ahead..."
    return

label poemresponse_3_natsuki_appeal_monika:
    if poemwinner[0] == "monika":
        show natsuki 3k at t11
        n "..."
        n "I'm still surprised with your choice, [player]..."
        mc "Stick around, I'm full of surprises..."
        show natsuki 5h with dissolve_chr
        n "If only they were good ones..."
        mc "Okay, can you now, please, tell me what surprised you so much?"
        show natsuki 5q with dissolve_chr
        n "Well, your style hardly changed from your previous poem, and that's after all the feedback..."
        n "So I'm guessing you're seriously satisfied with it..."
        show natsuki 5w with dissolve_chr
        n 5w "But, now that I think about it, you might just be stubborn and don't care much about our opinion!"
        mc "Natsuki, you're doing it again."
        show natsuki 5b with dissolve_chr
        n "Doing what?"
        mc "Jumping to conclusions. What makes you think that I don't care about your opinion?"
        mc "At this point, it's just stupid for me to ignore what others have to say, don't you think?"
        show natsuki 4e with dissolve_chr
        n "Then explain me why are trying to be so bold? Who are you trying to impress?"
        n "I told you before, it's a tough way to start with! And yet you're still getting ahead of yourself!"
        n "What will you prove to anyone by tha-{w=0.5}{nw}"
        show natsuki 3t with dissolve_chr
        n "Waaait a second..."
        mc "Hmm?"
        show natsuki 3d with dissolve_chr
        n "Well I'll be damned..."
    else:
        show natsuki 3q at t11
        n "..."
        n "Okay, now this is just weird..."
        mc "What now?"
        show natsuki 3h with dissolve_chr
        n "Where did you get the idea for this one? Not from me, that's for sure."
        mc "I still don't think I have anything particular in mind while writing these poems, Natsuki, if that's what you're asking."
        show natsuki 5i with dissolve_chr
        n "Well, if that's the case, then I suggest you actually listen to what others have to say!"
        mc "I'm trying, but I'm afraid you aren't making much sense right now."
        show natsuki 5y with dissolve_chr
        n "Well, I mean I can get the reasoning behind this..."
        show natsuki 5t with dissolve_chr
        n "It's abstract, it looks and sounds classy and yada-yada-yada..."
        show natsuki 5h with dissolve
        n "But, besides the point that this isn't what poetry is all about..."
        n "It's also a very odd choice for a newbie!"
        mc "It was an odd choice to come here in the first place, having no interest in literature."
        mc "But I'm still trying my best, you know? No matter how mediocre my skills are, I don't want to be some sort of dead weight to the club."
        mc "There's no point in trying without setting any goals ahead of yourself..."
        show natsuki 3d with dissolve_chr
        n "Ahhh, I see..."
        n "Now that's the attitude I recognize!"

    mc "What's with the eyes, Natsuki? You look like a detective who has just solved the case of their life."
    show natsuki 5d with dissolve_chr
    n "You could say that! I think I've just found out who our dear newcomer is trying to appeal to!"
    mc "What do you mean?"
    show natsuki 5y with dissolve_chr
    n "Why, Monika, of course! She's the one with the attitude and determination of a locomotive!"
    "She's what now?"
    n "Always ahead of everyone, bashing through any obstacles..."
    n "Yep, that's definitely her."
    show natsuki 5d with dissolve_chr
    n "So tell me, are you trying to follow in her footsteps or something? Or are you just trying to get on our president's good side?"
    mc "Ughhh..."
    mc "Natsuki, it's just a freakin' poem... How do you even come up withto these conclusions?"
    show natsuki 3d with dissolve_chr
    n "Don't underestimate my intuition! I'm rarely mistaken!"
    show natsuki 3t with dissolve_chr
    n "Though it still might be just a coincidence..."
    mc "I suggest we leave it as that and move to your poem."
    show natsuki 3d with dissolve_chr
    n "Well, okay, if you insist..."
    return





label poemresponse_3_monika:
    show monika 2a at t11
    mc "So, Monika. The time has come, I suppose?"
    show monika 2j with dissolve_chr
    m "You can put it that way."
    mc "No time to waste, then?"
    show monika 4a with dissolve_chr
    m "You seem far more confident than yesterday. That's a good sign."
    m "Do you think you managed to make some progress?"
    mc "Well, I certainly hope so... I made my first step. Can't say I'm particularly proud of it..."
    mc "But I tried to keep in mind what you all had to say when writing this new one."
    show monika 2b with dissolve_chr
    m "That's also good to hear. There's nothing wrong with utilizing the experience of others."
    show monika 2k with dissolve_chr
    m "That's one of the reasons I came up with the whole poem-sharing idea, after all!"
    m "By listening to what others have to say you might find weak spots in your works, or discover some inspiration for new ones!"
    show monika 4b with dissolve_chr
    m "That's how it works, [player], and that's why there's no place for any modesty."
    show monika 2b with dissolve_chr
    m "Now, leave all of your doubts behind and let's dive right into it!"
    mc "Yes, ma'am! Locked and loaded!"
    show monika 2k with dissolve_chr
    m "Ahahaha! At ease, soldier, I don't want this club to turn into a battlezone..."
    mc "If you want, I can go and call Natsuki \"cute\" again and it will turn into a crime scene."
    show monika 2l with dissolve_chr
    m "Ahahaha! O-Okay, that was a good one..."
    mc "I aim to please."
    show monika 1m with dissolve_chr
    m "Well then, with that over, let me see your poem now."
    mc "Hey! Why am I the first one again?"
    show monika 3k with dissolve_chr
    m "Chain of command!"
    mc "...!"
    mc "I see what you did there!"
    show monika 1j with dissolve_chr
    "Monika giggles slightly as I hand her my poem."

    scene bg club_day with wipeleft_scene
    $ renpy.call("poemresponse_3_monika_appeal_{appeal}".format(appeal=poemwinner[1]))

    "Monika hands me her notebook."
    "I notice a lot of scribbles and abandoned drafts. It seems that she's been been experimenting a lot while writing this one."

    call showpoem (poem_m_2)

    show monika 2a with dissolve
    m "..."
    show monika 2j with dissolve_chr
    m "So, what do you think?"

    mc "You... got me really confused this time..."

    show monika 2k with dissolve_chr
    m "I won't lie, I expected you to find it somewhat weird."

    mc "What's with all those... spacings?"

    show monika 4b with dissolve_chr
    m "This is the style that got somewhat popular recently. I decided to experiment a bit."
    show monika 4k with dissolve_chr
    m "You're not the only one around here trying new things, you know?"
    show monika 2a with dissolve_chr
    m "Surprisingly enough, I would say it goes well with me."

    mc "Well, it's definitely different from your previous poem..."
    mc "Can you give me some sort of clue? I'm honestly lost here."
    mc "And that's coming from a person who somewhat manages to understand Yuri's poems, mind you!"

    show monika 2k with dissolve_chr
    m "Ahahaha! Yes, Yuri has a habit of keeping what she had in mind a mystery."
    show monika 3b with dissolve_chr
    m "That's why I really appreciate Natsuki's way of writing. With all their simplicity, they give you such a clear picture!"
    show monika 3n with dissolve_chr
    m "Yuri, on the other hand, is a master of making that picture as beautiful as it could possibly get..."
    show monika 1k with dissolve_chr
    m "And Sayori? Beneath that carefree, almost childish front, you can sometimes find the deepest emotions, and conveying that isn't an easy feat!"
    show monika 1b with dissolve_chr
    m "That's why I wish for you all to appreciate your uniqueness! You all excel at something, so what's the point of finding out who's better?"

    mc "Says the girl who's constantly trying to be best at everything..."

    show monika 1l at s11
    m "I-I think you're exaggerating, [player]..."

    mc "Am I? I think I pretty much nailed the point."

    show monika 3n with dissolve_chr
    m "I understand where this is coming from, but you should understand that I'm not trying to be best at everything..."
    m "...or... better than... everyone..."
    show monika 1m with dissolve_chr
    m "I'm just setting myself some goals. It's easier when you have a clear picture in front of you, rather than chasing some fleeting dream..."

    mc "Yeah, I see your point."

    show monika 1p with dissolve_chr
    m "Though I won't lie, you're not the first one who said something like this to me..."

    mc "Oh... ummm... I didn't mean to offend you in any way..."

    show monika 1l at t11
    m "I n-never said you did!"
    show monika 1n with dissolve_chr
    m "Please, [player], you need to learn to ignore my rambling sometimes..."

    mc "Riiiight..."
    mc "Okay, now how about we get back to your poem?"

    show monika 1m with dissolve_chr
    m "Yes, I promised to explain you what I had in mind, after all."
    show monika 3e with dissolve_chr
    m "You see, this whole poem is one huge metaphor for how we search for our place in this world, the way we wish to follow..."
    show monika 3a with dissolve_chr
    m "As I said, I was experimenting, looking forward to trying out something new."
    m "And I wished to convey that exact feeling into this poem."
    show monika 2a with dissolve
    m "That is why I started playing with the space I had, that is why it's so freeform and so different from my usual, methodical approach to things."
    show monika 2j with dissolve_chr
    m "I felt like I was going through notes!"
    show monika 4j with dissolve_chr
    m "{i}One-and two-and three-and...{/i}"

    mc "{i}Each genre is a note{/i}, right?"

    show monika 1b with dissolve
    m "Exactly! I felt such freedom while doing that!"
    m "I wanted to deliver that feeling that an artist experiences while creating a new piece, that moment when you feel you can do anything, be anyone!"
    m "And how if you make even the smallest change, it can have a large influence on the end result!"

    mc "Well, you wanted to convey the feeling of experimenting. And I can now tell you've succeeded."

    show monika 1j with dissolve_chr
    m "I'm glad you feel that way."
    show monika 4b with dissolve_chr
    m "But the most important lesson which I want you to learn from it is that you, first of all, have to actually {i}try.{/i}"
    m "{i}Transpose it up or down, but that experience never falls flat.{/i}"
    show monika 2b with dissolve_chr
    m "No matter whether you succeed or fail in your undertakings, you'll still get yourself some new experience!"
    show monika 2k with dissolve_chr
    m "So don't ever be afraid to try, okay?"

    mc "Will do."

    show monika 1a with dissolve_chr
    m "Okay, I think I've taken more than enough of your time."
    show monika 1j with dissolve_chr
    m "We can talk again later!"

    show monika zorder 1 at thide
    hide monika
    "I can't say I know Monika very well, but I was under the impression that she's actually quite an easy one to understand."
    "But the more I talk to her, the more complex her nature seems to me."

    return

label poemresponse_3_monika_appeal_sayori:
    if poemwinner[0] == "sayori":
        show monika 2a at t11
        m "..."
        show monika 2j with dissolve_chr
        m "Still playing it safe, I see."
        mc "I... guess? Is it good or bad?"
        show monika 4a with dissolve_chr
        m "As I said yesterday, [player], there is no \"good\" or \"bad\". There is no {i}right{/i} way, remember?"
        show monika 2a with dissolve_chr
        m "I was just pointing out that even after listening to us all you decided to keep this style."
        show monika 2j with dissolve_chr
        m "Which only makes me more certain in your reasoning behind it!"
    else:
        show monika 1a at t11
        m "..."
        m "Hmm... now that's unusually... expected..."
        mc "Did you even understand what you've just said?"
        show monika 3l with dissolve_chr
        m "Y-Yeah, I know it sounds very contradictory, but that's the best way I can describe what I'm looking at..."
        mc "What do you mean?"
        show monika 3a with dissolve_chr
        m "Well, you made a sudden change in your style, but one that I... could imagine you doing..."
        mc "You're not helping..."
        show monika 4j with dissolve_chr
        m "Allow me to explain, then."
        m "That style is, first of all, much easier to master and overall it's a better place to start for a rookie like you."
        show monika 4b with dissolve_chr
        m "But what's more interesting is that you're not the first one here to use it!"
        show monika 4j with dissolve_chr
        m "And {i}that{/i} is why I'm not actually surprised by your choice."

    mc "Not sure I follow."

    show monika 5a with dissolve_chr
    m "Tell me, you and Sayori have been friends since childhood, right?"

    mc "Ummm, well, yeah. What about it?"

    m "I think it's only natural for you two to have this in common."
    m "Her style is largely identical to yours."

    mc "You... might have a point there, but I'm afraid the same can't be said about ourselves."

    show monika 2d with dissolve_chr
    m "Hmm? And why's that?"

    mc "While we {i}are{/i} friends, we're still quite different."
    mc "I sometimes ask myself if we would even be friends if we met each other now for the first time."

    show monika 2e with dissolve_chr
    m "You know, [player], I think that there's no use in thinking of how things could've gone..."
    m "Leave those things for the past and focus on the present instead."
    show monika 4j with dissolve_chr
    m "Oh, and don't forget about the future, of course!"

    mc "I'll try."

    show monika 2m with dissolve_chr
    m "And don't read too much into what I said about Sayori, you know?"
    m "It's just my assumptions, nothing more..."

    mc "I wonder if you'll end up being right..."
    mc "Okay... Now how about we get to your poem?"

    show monika 2j with dissolve_chr
    m "Go ahead, I'm curious what you'll think of this one!"
    return

label poemresponse_3_monika_appeal_natsuki:
    if poemwinner[0] == "natsuki":
        show monika 3a at t11
        m "..."
        show monika 3b with dissolve_chr
        m "So, looks like you're getting more confident with that particular style, aren't you, [player]?"
        mc "Maybe... I don't know. Am I making any progress?"
        show monika 1b with dissolve_chr
        m "Well, it's still rough, but at least I see some hints that you now know what you're doing."
        mc "Oh no, no, no, that's where you're definitely wrong..."
        show monika 1j with dissolve_chr
        m "Perhaps that's true, but I'm more curious to find out what you have in mind while writing your poems..."
        mc "You and me both..."
        show monika 2a with dissolve_chr
        m "You see, I think I've finally managed to connect the dots."
    else:
        show monika 3e at t11
        m "..."
        m "Now that's curious..."
        mc "Is it better or worse, Monika? This is what I'd like to know..."
        show monika 3b with dissolve_chr
        m "It's slightly better in terms of quality, but I'm more surprised with your sudden change of style."
        m "You made this poem short and simplistic, but tried to put more emphasis on it's meaning."
        show monika 2a with dissolve_chr
        m "It's not an easy task, you know? Not everyone manages to pull it off."
        mc "Well, I thought it would be worth a try..."
        show monika 2m with dissolve_chr
        m "You know, the more I look at it, the more it reminds me of someone..."

    mc "Not sure what you're talking about."
    show monika 4j with dissolve_chr
    m "Tell me, [player], how much time have you been spending with Natsuki?"
    mc "As much as she lets me. You of all people should know that."
    show monika 2l with dissolve_chr
    m "Ahahaha! Yeah, I know. Natsuki isn't someone you can just come up to and have a little chat."
    mc "Why did you even bring it up?"
    show monika 2a with dissolve_chr
    m "I thought that would be obvious. Your style has started to resemble hers."
    show monika 2j with dissolve_chr
    m "I guess you understood its own unique beauty and decided to try it out for yourself!"

    mc "I... think you're exaggerating..."
    show monika 3a with dissolve_chr
    m "Perhaps I am. But honestly, I see nothing wrong with it."
    m "That style is quite uncommon, so sharing such poems for comparison would be beneficial for everyone."
    show monika 5a with dissolve
    m "Besides, Natsuki could definitely use someone who is of one mind with her..."
    m "It should also be a great opportunity for you to get on her good side..."
    mc "L-Lets not get ahead of ourselves, okay?"
    show monika 1a with dissolve
    m "No worries. I understand that you're still experimenting, trying to forge you own path."
    mc "A bit too pompous of a way to say it, but yeah... I guess you're right."
    show monika 1k with dissolve_chr
    m "I'm rarely wrong."
    mc "Heh, yeah, that you are."
    mc "Do you want to share your poem with me now?"
    show monika 1a with dissolve_chr
    m "Sure, I'm eager to hear some feedback."
    return

label poemresponse_3_monika_appeal_yuri:
    if poemwinner[0] == "yuri":
        show monika 2j at t11
        m "..."
        m "Impressive, [player]! Didn't expect you'd go on with that style."
        mc "I get what you want to say: it's challenging, it's complex and yada-yada-yada..."
        show monika 4a with dissolve_chr
        m "But that still doesn't stop you, does it?"
        "I shrug."
        mc "It works, so why should I change?"
        show monika 4j with dissolve_chr
        m "I'm not insisting on you changing it, [player]."
        m "I just want you to realize that you should take it more seriously."
        show monika 2a with dissolve_chr
        m "If you think that this is the one, then please try your best to meet certain... expectations."
        mc "A task I've been failing at so far, correct?"
        show monika 2m with dissolve_chr
        m "Yes, to be honest. It's better than your previous one, though."
    else:
        show monika 2d at t11
        m "..."
        m "You've made quite a change, haven't you, [player]?"
        mc "I suppose. As I said, I tried to listen and draw some lesson from your feedback."
        show monika 4d with dissolve_chr
        m "Well, you definitely set yourself quite a challenge."
        m "This style is quite complex, it requires a lot of skill to master the usage of imagery and metaphors..."
        m "It's definitely not something I would expect from a rookie."
        mc "Well, at least I tried."
        show monika 2e with dissolve_chr
        m "You did, and I can't say it's particularly bad for your first..."
        show monika 4n with dissolve_chr
        m "...okay, {i}second{/i} attempt. I just meant that it's the first time you're trying out that style..."
        show monika 2m with dissolve_chr
        m "But I want you to understand that it's going to be difficult path."
        mc "I'll keep it in mind."

    show monika 2m with dissolve_chr
    m "Hmmm..."
    m "I've been wondering..."
    show monika 4a with dissolve_chr
    m "Are you using Yuri's style as an example?"
    mc "Ummm... I never actually thought about that..."
    show monika 4j with dissolve_chr
    m "Well, you can't deny there are certain similarities!"
    m "She's the one who has a knack for writing her poems in such a profound way!"
    show monika 4l with dissolve_chr
    m "And no matter how much I hate it when she and Natsuki start to argue about their preferences, she indeed has some talent."
    mc "I... definitely can't argue with that, but don't you think that your... assumption is a bit far-fetched?"
    show monika 2a with dissolve_chr
    m "It might be, but I still think I have a point."
    show monika 5a with dissolve
    m "I also think that Yuri would definitely be glad to learn that we have someone who shares her vision."
    m "With her closed nature, having a similar taste in literature could be the key to getting to know her better..."
    mc "If there was any taste to begin with... I've never been into literature before, remember?"
    show monika 2a with dissolve
    m "That's true. I might also be mistaken since you're just trying everything out at this point."
    show monika 2j with dissolve_chr
    m "But I'm still glad that you keep on going."
    mc "Yeah, I guess that counts for something."
    mc "Will you let me see your poem now?"
    show monika 1a with dissolve_chr
    m "Of course! I wonder what you have to say about this one."
    return

label poemresponse_3_monika_appeal_monika:
    if poemwinner[0] == "monika":
        show monika 2m at t11
        m "..."
        m "That's certainly impressive, [player]..."
        m "It seems I underestimated you..."
        mc "Monika, hearing that from you is quite unexpected, you know?"
        show monika 4n with dissolve_chr
        m "Well, I told you yesterday that your choice of style was quite peculiar..."
        m "...and I also warned you that it might not be a best option to start with..."
        show monika 4k with dissolve_chr
        m "But you still carried on with it! I guess I should've given you more credit!"
        mc "Does my poem deserve some of that credit as well?"
        show monika 3n with dissolve_chr
        m "Y-Yes and... no, I'm afraid..."
        m "It definitely could've gone better..."
        show monika 3l with dissolve_chr
        m "But I guess that shouldn't be surprising, right? Just by seeing how far you wished to go with it..."
    else:
        show monika 3d at t11
        m "..."
        m "I... didn't expect you to take my feedback so seriously..."
        mc "Just {i}your{/i} feedback? I tried to keep in mind what everyone had to say."
        show monika 3l with dissolve_chr
        m "B-But of course! I never said you didn't!"
        show monika 3n with dissolve_chr
        m "It's just... you've really surpassed my expectations, [player]."
        m "I definitely can't call it a masterpiece, since it's still quite raw, but I like the new approach you chose..."
        mc "So you think that your feedback had the biggest impact?"
        show monika 3l with dissolve_chr
        m "Well, I... would dare to assume that, yes..."
        show monika 1e with dissolve_chr
        m "But I must warn you that it's not going to be an easy path..."
        mc "What are you talking about?"
        show monika 1m with dissolve_chr
        m "It took me quite a while to refine my style to its current shape and form, so I know the hardship that awaits you if you carry on with it..."
        m "And looking at your poem... I'm really impressed with what how far you wanted to go with just one step..."

    mc "But I didn't go anywhere, right? I don't think that qualifies as a good result."
    mc "Wanting to accomplish something and actually succeeding in it are two completely different things."
    mc "I personally prefer the latter."
    show monika 4b with dissolve_chr
    m "That's the spirit! This is something I can definitely relate to!"
    show monika 2a with dissolve_chr
    m "Never thought you had that in you, [player]."
    mc "Heh, {i}birds of a feather{/i}, huh?"
    show monika 1m with dissolve_chr
    m "Yeah, most likely..."
    mc "..."
    m "..."
    show monika 1n with dissolve_chr
    m "[player]..."
    mc "Hmm?"
    m "If there's anything I can help you with, feel free to ask me at any time, okay?"
    mc "Ummm... sure, of course."
    mc "Though I personally think you're doing quite enough for me already and same goes for everyone else."
    show monika 1l with dissolve_chr
    m "Y-Yeah, of course! I just meant... if there's anything you'd probably want to suggest or... some advice you'd like to get..."
    show monika 1e with dissolve_chr
    m "I'm here for you... all of you..."
    mc "Glad to hear it."
    mc "Can you show me your poem now?"
    show monika 1m with dissolve_chr
    m "Of course. I would love to hear your feedback on it..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
