# -------------------------------------------------------------------------------------------
# All poem responses for all four girls (with all four appeals) for day 2 (Tuesday)
# -------------------------------------------------------------------------------------------

label poemresponse_2_sayori:
    if poemsread == 0:
        "I guess it makes sense for me to start with Sayori."
        "She is my good friend, after all, so I should be most comfortable sharing my poem with her first."
        "Also, she is the one who dragged me here, after all..."

    show sayori 1x at t11
    s "Hey, [player]! Ready to share your poem with me?"
    mc "Well, yeah... I mean, do I have any alternatives?"
    show sayori 1d with dissolve_chr
    s "Awww, come on! Don't be so nervous! It's just a poem, after all. Besides, who am I to judge?"
    show sayori 4r with dissolve_chr
    s "And even if I was any good, I still wouldn't be harsh about it. You're my friend, after all!"
    s "And I am just so happy that you're here with us!"

    mc "Hehe... Yeah. Thanks, Sayori..."
    show sayori 1a with dissolve_chr
    mc "To be fair, I'm still trying to wrap my head around it."
    mc "If someone told me a week ago that I'd end up in a club dedicated to literature and that I, of all people, would be writing poems, I would laugh out loud."

    show sayori 4s with dissolve_chr
    s "Ahahah! Well, fate works in superior ways!"

    mc "I... think the word you were looking for is 'mysterious'..."

    show sayori 3l with dissolve_chr
    s "Y-Yeah, that!"
    show sayori 1x with dissolve_chr
    s "It doesn't matter! Let me see your poem now. I can't wait!"

    "I give Sayori the notebook where I wrote my poem yesterday."

    scene bg club_day with wipeleft_scene

    $ renpy.call("poemresponse_2_sayori_appeal_{appeal}".format(appeal=poemwinner[0]))

    # REJOIN:
    "Sayori hands me her poem."
    "It's written on a sheet of paper torn out from a notebook."
    "The sheet is covered in small wrinkles here and there and it--{w=0.3} Wait a minute, is that...?"
    "Yep. It's a small yet visible coffee stain, or at least something that looks like it."

    mc "Jeez, I haven't read the poem yet, but even the paper you wrote it on already reminds me of you..."

    show sayori 5c with dissolve_chr
    s "Come oooon! There's no need to be mean about it!"
    mc "Sigh..."
    mc "Never mind. Let me just read it..."


    call showpoem(poem_s_1)  # "A Day on the Ice"


    show sayori 1a with dissolve
    mc "..."
    mc "Man, that brings back memories..."

    show sayori 4r at h11
    s "I know, right?"
    show sayori 1x with dissolve_chr
    s "You see, when I checked my calendar yesterday, I realized that winter isn't that far away!"
    s "And those memories just started washing over me!"
    show sayori 1a with dissolve_chr
    s "You remember when we were both learning how to ice skate?"
    show sayori 4r with dissolve_chr
    s "That was super fun!"

    mc "Yeah, it sure was..."
    show sayori 1a with dissolve_chr
    mc "..."
    mc "Okay, before I start to get flashbacks, care to answer one question, Sayori?"

    show sayori 3x with dissolve_chr
    s "What's that?"

    mc "How was that hot chocolate?"
    show sayori 5a with dissolve
    s "Um..."
    s "What hot chocolate?"

    mc "Oh, you know, the one that supposedly left a spot riiiight here, maybe?"
    mc "The one you had with breakfast?"

    show sayori 5b with dissolve
    s "Ehehe~"

    mc "Sayori, tell me honestly..."
    mc "Did you write your poem when you were--"

    show sayori 4p at h11
    s "D-Don't say it out loud!"

    show monika 3d at l41
    m "Umm... don't say what out loud?"

    show sayori 1m with dissolve_chr
    s "Nothing!"

    show monika at lhide zorder 1
    hide monika

    mc "Heheheh..."

    show sayori 5c with dissolve_chr
    s "You're such a meanie, [player]!"
    mc "Well, excuse me, but you're the one here who's doing her homework while eating breakfast!"

    show sayori 3h with dissolve_chr
    s "Eh? Writing poems isn't 'homework,' you know?"

    mc "I know."
    mc "But I also know that this isn't the first time you've done something like this."

    show sayori 1l with dissolve_chr
    s "Okay, okay! Just don't tell Monika...?"

    mc "Oh, I don't know..."
    mc "What would I get out of it?"

    show sayori 1j at h11
    s "[player]!"
    mc "Ehehe... Okay, I'm done teasing. Relax."

    show sayori 1i with dissolve_chr
    mc "I have to say, it's a very good poem."
    show sayori 1b with dissolve_chr
    mc "It's nothing fancy, but it feels just like you, basically."
    show sayori 4x with dissolve_chr
    s "Really? How does it make you feel?"

    mc "Carefree, cheerful... It reminds me of how much fun we used to have."

    show sayori 1d with dissolve_chr
    s "Awww..."
    s "See? You're not always so grumpy and mean, after all!"
    show sayori 1r with dissolve_chr
    s "Hehe! I know that you're actually a real softie deep inside!"

    mc "Ahem! Monika, could you come o--"

    show sayori 4s at s11
    s "Okay, okay, I'll shut up now!"

    show sayori at thide zorder 1
    hide sayori
    "I chuckle to myself, giving into Sayori's contagious cheerfulness."
    "It's been a while since she and I got to playfully tease each other like this."
    "I guess bringing me here must have been for the best, after all."
    return

label poemresponse_2_sayori_appeal_sayori:
    show sayori 2n at t11
    s "..."
    show sayori 2o with dissolve_chr
    s "..."

    mc "Ahem... Sayori?"

    show sayori 1m at h11
    s "Huh? Oh, sorry! I spaced out for a second..."

    mc "Heh. After all the times you've accused me of that..."
    show sayori 3h with dissolve_chr
    s "It's not that, I just..."
    s "This is your first try? And you wrote it yourself, right?"

    mc "Wha? Of course I did, Sayori!"

    show sayori 1l with dissolve_chr
    s "Y-Yeah, you're right. Sorry about that..."
    show sayori 1c with dissolve_chr
    s "I just didn't expect it to be this good, to be honest."

    mc "Um... thanks?"

    show sayori 1q with dissolve_chr
    s "Heheh~ Don't get cocky, though. It's still pretty rough around the edges."
    show sayori 1a with dissolve_chr
    s "But I really like it anyway!"
    show sayori 4x with dissolve_chr
    s "And I guess this proves that I was right about bringing you here, after all!"
    mc "Well, as long as it's not a complete disaster, I guess I'm fine with that..."
    mc "Now... It's your turn, right?"

    show sayori 4r with dissolve_chr
    s "Yeeeep!"
    return

label poemresponse_2_sayori_appeal_natsuki:
    show sayori 1q at t11
    s "..."
    s "Eheheh..."

    mc "Hey! I know it's bad, but you could at least try not to laugh at it!"
    show sayori 3r with dissolve_chr
    s "I'm not laughing at it, [player]. It just reminded me of someone..."

    mc "Could you be any more vague?"

    show sayori 1l with dissolve_chr
    s "Well, it's a bit short... and simple..."

    mc "Heh. Now that's a bit ironic, don't you think?"

    show sayori 5d with dissolve_chr
    s "H-Hey! I'm not only about cute and happy stuff and... you know..."

    mc "..."
    mc "Really??"

    show sayori 5b with dissolve_chr
    s "Well... at least not all the time..."

    mc "Uh-huh, sure..."
    mc "Okay, just tell me. How bad is it?"

    show sayori 1a with dissolve_chr
    s "It's not bad, really! It's different from what I expected, but it's not bad at all!"
    show sayori 1x with dissolve_chr
    s "You have a long way to go, that's for sure, but you've got potential!"
    show sayori 1q with dissolve_chr
    s "I'm super curious what your next poems will look like."

    mc "Well, I guess we'll see soon enough. Mind if I read your poem now?"

    show sayori 1x at h11
    s "Okay!"
    return

label poemresponse_2_sayori_appeal_yuri:
    show sayori 1n at t11
    s "..."
    s "Whoa..."
    show sayori 1o with dissolve_chr
    s "[player], did you really write this yourself?"

    mc "Sayori, come on! I thought you, of all people, would give me at least some credit."

    show sayori 1l with dissolve_chr
    s "Oh, sorry..."
    show sayori 1g with dissolve_chr
    s "It's just... not what I was expecting from you..."
    show sayori 1i with dissolve_chr
    s "It's just so deep and... complicated."
    show sayori 3j with dissolve_chr
    s "Did you just find this somewhere online?"

    mc "Sayori, you do get how ridiculous that sounds, right?"
    mc "I know that I'm not any good at writing yet, but could you at least try to give me some actual feedback?"
    mc "You know, instead of accusing me of cheating?"

    show sayori 4e with dissolve_chr
    s "Sorry... I really didn't mean it that way."
    show sayori 4k with dissolve_chr
    s "I just think it's weird for you to start off with something like this."
    show sayori 1o with dissolve_chr
    s "Seriously though, I have no idea what you wrote about in your poem!"

    show sayori 3x with dissolve_chr
    s  "But maybe that's not a bad thing! Poems don't always need to have a clear message, right?"
    s "If you just want to say exactly what you mean, then what's the point of writing a poem?"

    mc "Yeah, I guess you might be right..."

    show sayori 1a with dissolve_chr
    mc "Okay then. Care to share your poem with me?"

    show sayori 4r at h11
    s "Sure!"
    return

label poemresponse_2_sayori_appeal_monika:
    show sayori 1b at t11
    s "..."
    show sayori 1c with dissolve_chr
    s "Wow, [player], this is actually pretty... nice..."

    mc "Wait, really?"

    show sayori 3r with dissolve_chr
    s "Okay, it's not amazing or anything, but it'is better than what I expected!"

    mc "...implying that you expected it to be way worse?"

    show sayori 3x with dissolve_chr
    s "Well, it's way more abstract and... organized than I thought it would be."
    show sayori 3g with dissolve_chr
    s "And what makes you think I would expect it to be bad?"

    mc "Well, you said it yourself. You obviously had lower expectations."

    show sayori 3h with dissolve_chr
    s "Yeah, but... I never said I expected to be, like, 'bad' bad..."
    show sayori 1x with dissolve_chr
    s "But you know what?"
    show sayori 4r with dissolve_chr
    s "You're taking your first steps, and I think that's what really matters!"

    mc "Yeah, I guess you're right."
    mc "So... Is this the part where you share your poem with me?"

    show sayori 1n at h11
    s "Oh! Yeah! I totally forgot!"
    show sayori 1q with dissolve_chr
    s "Here you go!"
    return

# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================

label poemresponse_2_yuri:
    if poemsread == 0:
        "If I'm going to be practical about this, then my first choice should probably be Yuri."
        "Out of all the members, she seems like the one with the most experience, at least when it comes to literature."
        "Besides, knowing her shyness, I hardly expect her to be too harsh to me..."
        "..."
        "If anything, she probably expects me to be harsh to her, instead."

    show yuri 2t at t11
    y "Oh, h-hello, [player]..."

    mc "Hey, Yuri. Is everything okay?"
    y "Yes... I believe it is.:
    show yuri 3w with dissolve_chr
    y "So... I assume you would like us to share our poems?"

    "Well, at least I'm not the only one embarrassed about this whole... 'activity' Monika came up with."

    show yuri 3n with dissolve_chr
    y "W-Why are you smiling?"
    show yuri 3p with dissolve_chr
    y "Is it something I said?"

    mc "Yuri, take it easy, okay?"
    show yuri 3o with dissolve_chr
    mc "This is just as new to me as it is to you."
    mc "And unlike me, you probably know a thing or two about poetry."

    show yuri 3q with dissolve_chr
    y "I'm... not that good, to be honest..."

    mc "Oh, come on, don't be shy. You left me speechless when you were talking about your passion for literature yesterday."
    mc "And impressing me with literature as a topic? That counts for something."

    show yuri 4b with dissolve_chr
    y "Yes, I suppose it does..."

    mc "Also, if I remember correctly, you promised to make me feel as comfortable here as possible."
    mc "And I don't think spending the rest of the meeting just sitting here, too embarrassed to share our work, qualifies as 'comfortable.'"

    show yuri 2w with dissolve
    y "Sigh..."
    show yuri 2u with dissolve_chr
    y "You're right... Please excuse my modesty. This is a new experience for me, after all."

    mc "For both of us."
    mc "So... ladies first, then?"

    show yuri 1k with dissolve_chr
    y "Tsk-tsk-tsk! [player], you do know that this is the type of trick a {i}real{/i} gentleman would never use?"

    mc "Haha... well, you can't blame me for trying..."

    show yuri 1c with dissolve_chr
    y "I know, but I still appreciate you trying to act like one."

    "..."
    "I... don't exactly know what to make out of that last line, but I'm guessing that everything that Yuri says has some sort of double meaning to it."
    "I hand her a notebook with my poem in it."

    scene bg club_day with wipeleft_scene
    $ renpy.call("poemresponse_2_yuri_appeal_{appeal}".format(appeal=poemwinner[0]))

    # REJOIN:
    "Yuri hands me her notebook."
    "When I touch it, it takes just a little more effort to get it out of her hand than I expected. She's obviously still having second thoughts about all this."
    "I tug on it slightly, and she hesitantly releases it. Opening the notebook, I start reading through her latest poem."
    "Her handwriting is beautiful, almost calligraphic..."

    call showpoem(poem_y_1)  # "Fading Light"

    show yuri 4a with dissolve

    mc "..."

    y "So? What do you think?"

    mc "It's very beautiful. But I'm a bit surprised. I expected you to make it more... mysterious."

    show yuri 4C with dissolve_chr
    y "Oh, um... I'm sorry to disappoint you..."

    mc "Huh? What?! No! That's not what I..."
    mc "Ughhh..."
    "{i}Why does everything I say come out so wrong?{/i}"
    mc "It's not disappointing at all. I was just under the impression that you would make the message more concealed."

    show yuri 2v with dissolve
    y "Well, I wouldn't exactly call you misguided."
    y "I do tend to... overcomplicate things..."
    show yuri 2w with dissolve_chr
    y "My usual style revolves around the idea of having the reader ponder for a bit, to make him try to understand my way of thinking..."
    show yuri 2h with dissolve_chr
    y "...or to instead find some new meaning to it, one that initially evaded my gaze, to see my work from a completely new perspective..."

    mc "Yuri..."

    show yuri 3q with dissolve_chr
    y "O-Oh! Y-Yes... Excuse my rambling..."

    "{i}No offense, Yuri, but if I let you go on about literature any more, we'd probably be stuck here for hours...{/i}"

    show yuri 1u with dissolve_chr
    y "I just thought that for the first time sharing poems, it would be logical to start with something more... plain."
    show yuri 3t with dissolve_chr
    y "Do you think it was a poor choice?"

    mc "Wha- no! Yuri, please, you really worry too much about this!"

    show yuri 3s with dissolve_chr
    y "I'm afraid that's not very easy for me to change... I hope it doesn't cause you all much trouble..."
    show yuri 4a with dissolve_chr
    y "So... You said that you found the message in this poem quite obvious?"

    mc "I wouldn't say 'obvious,' but I think I sort of understood it."

    show yuri 4b with dissolve
    y "And what does it make you think of... me?"

    mc "Ah, so you're saying that the speaker in this poem is you?"

    show yuri 3o with dissolve
    y "Um... Well, I..."

    mc "What can I say, then? I think I'm starting to understand why you like literature so much."

    show yuri 3f with dissolve_chr
    y "Huh?"
    y "You... you do?"

    mc "This poem... It's about you reading, right? Exploring the world in your books?"
    
    show yuri 3q with dissolve_chr
    y "Well, y-yes..."
    mc "It's a really beautiful poem. And if you can make reading sound beautiful, then that's really impressive."
    mc "Especially to someone who's not really into literature."
    
    show yuri 2u with dissolve
    y "..."
    y "Do you really think so?"
    mc "I do."
    mc "Wait... Does that mean I was right about your poem?"
    
    y "Um... There's a bit more to it, but..."
    
    y "I'm glad you understand, though, even if it's just slightly..."
    y "It's comforting to see that there are people who I can talk to about things like this..."

    mc "Please. You mean to tell me that you had no one to discuss this with before I came here? In a Literature Club, no less?"
    mc "That doesn't make sense, does it?"

    show yuri 1c with dissolve_chr
    y "I don't think there's much sense in a Literature Club member with no interest in literature, either."

    mc "Huh?"
    mc "...Oh."
    mc "Yeah, you got me there."

    show yuri 1c with dissolve
    "Yuri giggles softly."

    show yuri 1s with dissolve
    y "At any rate, I think I shouldn't keep you here any longer, but..."

    mc "But?"

    show yuri 1u with dissolve_chr
    y "I..."
    show yuri 3s with dissolve_chr
    y "I just want to thank you, [player]... I really needed someone to help me make the first step."

    mc "Yeah... I think we both did..."

    show yuri 3c with dissolve_chr
    $ renpy.pause(0.7)
    show yuri at thide zorder 1
    hide yuri
    "Yuri gives me a sweet smile and then turns away. I guess that's it for our conversation."
    return

label poemresponse_2_yuri_appeal_sayori:
    show yuri 2g at t11
    y "..."
    show yuri 1i with dissolve_chr
    y "..."
    show yuri 1m with dissolve_chr
    y "Well, this is fairly in line with what I expected."
    show yuri 1a with dissolve_chr
    y "This is your first time, correct?"

    mc "Well, yeah. Why?"

    show yuri 1c with dissolve_chr
    y "It's nothing, really. I'm just familiar with the more common mistakes of inexperienced writers."
    show yuri 1m with dissolve_chr
    y "In your particular case, I suppose you decided to start with something simple. Am I right?"
    show yuri 1k with dissolve_chr
    y "You didn't want to oversaturate your poem with metaphors or make any strong message in it, but rather give it a calm, soothing mood."
    show yuri 1a with dissolve_chr
    y "It's not a bad thing at all. Sometimes, even I require something to vent my thoughts instead of holding onto them."

    mc "..."
    mc "Yuri, I'm going to be honest with you..."

    show yuri 1e with dissolve_chr
    y "Oh?"

    mc "I was just writing something, anything... I honestly don't know what I had in mind."

    show yuri 1d with dissolve_chr
    y "And that only further confirms my assumption!"

    mc "Assumption? What assumption?"

    show yuri 2m with dissolve_chr
    y "All in good time, [player]."
    show yuri 3u with dissolve_chr
    y "Besides, I'm actually curious if your style will change as you go..."

    mc "At this point, I'd be happy if I made any progress at all, let alone find any particular 'style' of my own."

    show yuri 3u with dissolve_chr
    y "I am certain you will succeed."
    show yuri 2l with dissolve_chr
    y "So..."
    y "I guess now it's only natural for me to share my poem as well?"

    mc "I'm looking forward to it."
    return

label poemresponse_2_yuri_appeal_natsuki:
    show yuri 2h at t11
    y "..."
    show yuri 2j with dissolve_chr
    y "That's not what I was expecting, frankly."

    mc "Wow, you actually had some specific expectations?"

    show yuri 2i with dissolve_chr
    y "Well, I understand that this is your first attempt, but I had hoped that you would choose a different approach..."

    mc "Care to elaborate? I barely knew what I was doing at all."

    show yuri 1i with dissolve_chr
    y "You see, it's not a particularly bad idea to focus your attention on the message..."
    show yuri 1l with dissolve_chr
    y "...but there really is no need to limit yourself."
    show yuri 2v with dissolve_chr
    y "There are so many beautiful words, so many beautiful ways to convey your thoughts and your feelings..."
    show yuri 2t with dissolve_chr
    y "In the hands of a writer, language is a tool to deliver his or her message in a profound way, which can leave people in awe."

    mc "Okay! I get it. It's horrible! There's really no need in trying so hard to spare my feelings, Yuri."

    show yuri 3p at h11
    y "N-No! I never said that!"
    show yuri 3o with dissolve_chr
    y "I just meant that it's a little..."

    mc "A little...?"
    show yuri 3p with dissolve_chr
    y "Simplistic!"
    show yuri 3o with dissolve_chr
    y "Yeah... That's the word."
    mc "Uh-huh..."
    mc "You know, I think I'm fine with that feedback."
    mc "Thank you."
    show yuri 3q with dissolve_chr
    y "Y-You're welcome..."
    mc "Mind if I take a look at your poem now?"
    show yuri 2s with dissolve_chr
    y "Oh, yes. Sure."
    return

label poemresponse_2_yuri_appeal_yuri:
    show yuri 2u at t11
    y "..."
    y "This is... really impressive, [player]."

    mc "..."
    mc "Yuri, that's the textbook definition of 'flattery' right there."

    show yuri 3t with dissolve_chr
    y "What makes you say that?"

    mc "Because I can hardly expect someone with as much experience as you to find my first poem ever 'impressive.'"

    show yuri 2e with dissolve
    y "Um, this is... your first time?"

    mc "I'll... take that as a compliment."
    mc "And yeah, it is. I thought that would be obvious."

    show yuri 2f with dissolve_chr
    $ renpy.pause(0.5)
    show yuri 1g with dissolve_chr
    y "..."

    "Yuri starts rereading my poem, tracing her finger along the words, as if it helps her analyze it more thoroughly."

    show yuri 1j with dissolve_chr
    y "Ah, yes. That makes sense."
    show yuri 1l with dissolve_chr
    y "Well, I won't lie. It's far from perfection."

    "{i}Oh, so now, it's suddenly not so impressive?{/i}"

    y "You've made a few mistakes common among beginners..."
    show yuri 1k with dissolve
    y "And while you certainly have some skill in usage of imagery and metaphors..."
    show yuri 1i with dissolve_chr
    y "...I hardly think I'm ready to call you an author with his unique and well-defined style."
    show yuri 1c with dissolve_chr
    y "But, nevertheless, you certainly have a lot of potential!"

    mc "Hah. Well, I guess I did almost trick you into thinking that this isn't my first attempt at writing."
    mc "So that counts for something."

    show yuri 4b with dissolve_chr
    y "Yes, I suppose you're right about that..."

    "I really didn't expect Yuri, of all people, to like my poem that much."
    "And I hope that it's not just her being polite."

    mc "So, I think it's only fair for me to see your poem now?"

    show yuri 3s with dissolve_chr
    y "Of course! I would be glad to share."

    "Well, at least she's more enthusiastic about it now."
    return

label poemresponse_2_yuri_appeal_monika:
    show yuri 2i at t11
    y "..."

    y "Not bad, [player]."
    show yuri 1a with dissolve_chr
    y "This is your first attempt, correct?"

    mc "Well, yes... I'm pretty sure that wasn't hard to figure out..."

    show yuri 1m with dissolve_chr
    y "Well, at any rate, I would say you've chosen quite a peculiar approach."

    mc "How so?"

    show yuri 1c with dissolve_chr
    y "It's quite daring, even. Definitely not something I would expect a novice to choose as his starting point."

    mc "Yuri, you're not making it any more clear, I'm afraid."

    show yuri 3q with dissolve_chr
    y "Oh! Please, excuse me. I got a little distracted..."
    show yuri 3s with dissolve_chr
    y "What I mean to say is that it's not my preferred style, but I still love it."
    y "It's fine-tuned and it pays enough attention to every aspect of writing a poem, as if you were trying your best to make it meet the highest of standards."

    mc "And that's... good, right?"

    show yuri 3q with dissolve_chr
    y "Yes... in theory..."

    mc "Heh... Right. Guess that's one way to say that I didn't pull it off."

    show yuri 3o with dissolve_chr
    y "Um... well..."

    "Yuri obviously can't just bring down the hammer and tell me that I tried to reach for the stars and failed miserably."

    show yuri 3q with dissolve_chr
    y "A-Anyway, as I was saying..."
    y "People who choose this style are usually confident and straightforward. Yet in their works, they tend to focus on abstractions..."
    show yuri 3u with dissolve_chr
    y "...on images which convey the hardships of their everyday lives..."
    show yuri 2g with dissolve_chr
    y "Hmm..."
    show yuri 2j with dissolve_chr
    y "So I'm guessing that you, too, have a story to tell."

    mc "Too?"

    show yuri 3q with dissolve
    y "Well... Yes, I believe that everyone has their own story..."

    mc "I guess?"

    show yuri 2t with dissolve_chr
    y "So... Would you like to read my poem now?"
    mc "Hmm? Sure."
    return

# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================

label poemresponse_2_natsuki:
    if poemsread == 0:
        "While the whole idea of sharing our poems obviously belongs to Monika..."
        "...I was the one who gave her the idea, and I, in turn, have Natsuki to thank for that."
        "So I guess it would be smart to start with her. I did tell her that I'd like to see her poems, after all."
        "Besides, I'm pretty curious what sort of poems a girl like her would write..."

    show natsuki 3c at t11
    mc "Hey, Natsuki."
    show natsuki 4w with dissolve_chr
    n "..."
    n "You're here to share your poem with me, I guess..."
    mc "Well, yeah. Anything wrong with that?"
    n "N-No..."
    mc "..."
    "I can tell she's not exactly thrilled about this."
    
    mc "Natsuki..."

    show natsuki 5h with dissolve_chr
    mc "I know you don't particularly like me, but..."
    n "Huh?"

    show natsuki 1p with dissolve_chr
    n "W-What? 'Like' you?!"
    n "Why would you expect me to like you in the first place?!"
    mc "Yeah, that didn't come out as planned..."
    mc "I meant to say, ' you don't particularly like me being around here,' Natsuki..."

    show natsuki 5q with dissolve_chr
    n "Oh... Hmph..."
    show natsuki 5w with dissolve_chr
    n "Well, it still doesn't change much!"

    "Oh boy..."
    n "Of course I'm not okay with it! I'm not used to it!"
    n "How can you expect me to feel good about it when Sayori just brought you here all of a sudden and not a minute later, you're already a new member!"
    mc "Natsuki..."
    n "It was just the four of us for quite a while, and I didn't expect anyone new barging in like this, let alone a boy!"
    show natsuki 5e with dissolve_chr
    n "And here you are! Roaming around our club, eating my cupcakes and..."
    mc "Ughhhh..."

    # add screen shake effect
    play sound "sfx/table_hit.ogg"
    show natsuki 1p at h11
    "..."
    "I let my head hit the desk. Not one of my brightest ideas, to be fair..."
    show natsuki 4I with dissolve_chr
    n "Hey, what do you think you're doing?!"

    "...but I need to get her attention somehow."

    mc "Natsuki, we're not making any progress..."

    show natsuki 4w with dissolve_chr
    n "Well, hitting your head against school furniture won't help, either!"
    show natsuki 3y with dissolve_chr
    n "Besides, if you want to do it so badly, you should get some professional help!"
    show natsuki 3z with dissolve_chr
    n "I'd be more than happy to give you a hand! Who knows? It might even make you smarter!"
    "I raise my head, rubbing my forehead and chuckling."
    mc "Whatever it takes, Natsuki. Whatever it takes..."

    show natsuki 3t with dissolve_chr
    n "Hehehe~"
    n "Okay, you do have a point, though. We really should get this over with..."
    mc "As long as it doesn't involve any more physical harm to me, I'm all for it."

    show natsuki 1l with dissolve_chr
    n "Hey! It was your idea, not mine!"
    mc "Sigh..."
    mc "Let me guess. Still don't feel like sharing?"
    n "And you do?"

    mc "Not really, to be honest."
    mc "On one heand, it's my first time, so I don't have to worry about ruining my image or anything..."
    mc "But on the other..."
    mc "...yeah, I still feel you."
    mc "So don't worry. You're not in this alone."
    n "I-I'm not worried! I'm just... not used to it, that's all."
    mc "Figures..."
    mc "Either way, I think I owe you an apology."

    show natsuki 5k with dissolve_chr
    n "An apology? For what?"
    mc "Well, if I wasn't so curious about your poem yesterday, Monika wouldn't have come up with all this."

    show natsuki 5m with dissolve_chr
    n "Hmm..."
    n "Yeah, you're totally right on that one."
    show natsuki 5y with dissolve_chr
    n "Thanks for pointing that out, actually! Now I at least know who to blame!"

    mc "Natsuki..."

    show natsuki 6c with dissolve
    n "Hehehe... Okay, okay..."
    show natsuki 7a with dissolve
    n "I'll let you off the hook for now."
    mc "Just let me know when we're finally done with this roleplaying, okay?"
    n "Huh? What do you mean?"
    mc "Well, it just feels like we're in the military or something."
    mc "You know, with you being some sort of 'veteran' here, hazing a new recruit on his first day..."
    
    n "Heh... I guess you could put it that way."
    n "Okay, then! Let's get to the drill!"
    n "Hurry up and give me those scribbles you call a 'poem,' maggot!"
    "I chuckle and hand her my notebook."
    mc "You have no idea how perfectly you summed it up..."

    scene bg club_day with wipeleft_scene

    $ renpy.call("poemresponse_2_natsuki_appeal_{appeal}".format(appeal=poemwinner[0]))

    # REJOIN:
    "Natsuki hands me a sheet of paper with her poem."
    "It's... written in pink ink."
    "Seriously, how can she expect people to not consider her cute when she acts this way for even with the smallest things?"

    call showpoem(poem_n_1)  # "Not Your Cupcakes!"

    show natsuki 5s with dissolve
    mc "..."

    show natsuki 5u with dissolve_chr
    n "I knew you wouldn't like it..."

    mc "Eh? I haven't even said anything yet..."

    show natsuki 4w with dissolve_chr
    n "There's no need to! I can already tell!"

    mc "You sure do like jumping to conclusions, don't you?"

    show natsuki 4e with dissolve_chr
    n "Well... That's because I'm usually right, you know?"

    mc "Well, not this time..."

    show natsuki 5e with dissolve_chr
    n "Really now? So you mean you actually like it?"

    mc "Yeah, and now I think I get what you were saying just a minute ago..."
    mc "It's brief, but it still carries a strong message without getting too cluttered."

    show natsuki 2h with dissolve_chr
    n "Well, yeah... More or less..."

    mc "So... Let me take a wild guess: Did you use me as an inspiration for your poem?"
    show natsuki 1o with dissolve_chr
    n "Excuse me?!"

    "Here we go again..."

    show natsuki 1e with dissolve_chr
    n "What exactly are you trying to say?!"

    mc "It just sounds like you might have based this poem off of me coming in here and taking your cupcakes without a second thought."

    show natsuki 1o with dissolve_chr
    n "..."
    show natsuki 1r with dissolve_chr
    n "..."
    show natsuki 1o with dissolve_chr
    n "W-Well... Yeah! So?!"
    n "Maybe I just don't like being taken for granted!"

    show natsuki 1h with dissolve
    mc "Seems like most people don't take you seriously, do they?"
    n "Um... Maybe..."
    mc "An the cupcakes represent how you wish people would notice you for more than just your appearance?"

    show natsuki 1m with dissolve
    n "Um... uh-huh..."
    mc "...but most of them won't even try to look past that cover? Won't even try to see your personality through that shell of yours?"

    show natsuki 1k with dissolve_chr
    n "..."
    show natsuki 1q with dissolve_chr
    n "..."
    show natsuki 1s with dissolve_chr
    n "..."

    mc "Umm, hello? Earth to Natsuki?"

    show natsuki 2x with dissolve
    n "Grrr! W-Well, yeah! That's... pretty much what I meant..."
    show natsuki 2s with dissolve
    n "Still surprised you actually understood anything..."

    mc "I did, and I'm sorry you see me that way."

    show natsuki 1m with dissolve_chr
    n "...?"

    mc "I get that I just showed up here, seemingly out of nowhere, and that I'm making you uncomfortable..."
    mc "But I think we got off on the wrong foot."
    mc "I know there's no reason for you to trust me yet, but I promise I'll try my best not to be a jerk..."

    show natsuki 1o with dissolve_chr
    n "...!"
    show natsuki 1r with dissolve_chr
    n "..."
    show natsuki 5u with dissolve
    n "..."

    "Hmm, I guess Natsuki just isn't used to being treated kindly. Especially when she's acting so irritated herself."

    mc "You going to be okay there?"

    n "J-Just... go already..."

    show natsuki zorder 1 at thide
    hide natsuki

    "I heave a sigh and stand up, feeling a bit upset. Guess it really is best to leave her alone for the time being."

    return

label poemresponse_2_natsuki_appeal_sayori:
    show natsuki 3c at t11
    n "..."
    show natsuki 3d with dissolve_chr
    n "Well, that's pretty much what I expected from you."

    mc "I oubt there's any hidden compliment there, huh?"

    show natsuki 4y with dissolve_chr
    n "Pfff! You wish!"

    mc "Haha..."
    mc "Okay, then. So what exactly did you expect from me?"

    show natsuki 5y with dissolve_chr
    n "Well, for starters, it's pretty bland. I expected you to have at least some message in it."
    n "I mean, that's what poetry's all about!"

    mc "Yep, 'bland' sounds just like me."

    show natsuki 5t with dissolve_chr
    n "But on the other hand, at least you're not in over your head."
    show natsuki 5q with dissolve_chr
    n "You didn't try to go all 'sophisticated,' like some people..."

    mc "Hmm? What do you mean?"

    show natsuki 4w with dissolve_chr
    n "Never mind!"
    show natsuki 4h with dissolve_chr
    n "The point is, until you get some skill, don't even bother trying to write some real poetry!"

    mc "Oh? I guess you can show me how it's done, then?"

    show natsuki 1e with dissolve_chr
    n "Wha? Well, yes I can! Are you doubting my writing skills?!"

    mc "No, but I think that for someone who turned as red as a tomato the last time--"

    show natsuki 4w with dissolve_chr
    n "Stop quoting Monika, will you? At least have the decency of coming up with something on your own!"

    mc "Sigh..."
    mc "Can I just read your poem already?"

    show natsuki 5s with dissolve_chr
    n "Hmph!"
    return

label poemresponse_2_natsuki_appeal_natsuki:
    show natsuki 3k at t11
    n "..."
    n "D-Did..."
    n "Did somebody tell you..."

    mc "Um... Did somebody tell me what?"

    show natsuki 1r with dissolve_chr
    n "I-It doesn't matter!"
    show natsuki 4w with dissolve_chr
    n "And now that I think of it, did you even write this yourself?!"

    mc "Whoa. Now where's this coming from?"
    mc "What about it made you so mad?"

    show natsuki 1p with dissolve_chr
    n "I-I'm not mad! What makes you say--"

    mc "Natsuki, I'm completely confused at this point. Could you, please, explain what made you react like this?"

    show natsuki 2s with dissolve_chr
    n "Sigh..."
    show natsuki 2q with dissolve_chr
    n "Well, it's just... weird..."
    n "I didn't expect you to write anything like this..."

    mc "So... does that mean you actually like it?"

    show natsuki 5w with dissolve_chr
    n "Don't get full of yourself! It's obviously still lacking!"

    show natsuki 5s with dissolve_chr
    "Natsuki starts looking through my poem once again."

    show natsuki 5q with dissolve
    n "This part could be better... and this one is also kinda 'meh'..."

    show natsuki 5r with dissolve_chr
    "She's starting to get more irritated, as if she's forcing herself to find imperfections in my poem..."
    "...which shouldn't be hard very to do."

    show natsuki 2w with dissolve_chr
    n "Well, like I said, it's still nowhere near perfect!"
    show natsuki 2e with dissolve
    n "And I still can't tell if you wrote it like this on purpose or just by accident!"
    mc "If it makes things easier, it's likely the second one."
    mc "I hardly know what I'm doing at this point, after all."

    show natsuki 2b with dissolve_chr
    n "Then you'd better figure it out. And soon!"
    n "You need to learn how to make a poem short but also have a strong message! Short, sweet, and to the point!"

    "I laugh to myself."

    mc "'Short' and 'sweet,' huh?"

    show natsuki 4w with dissolve_chr
    n "Don't you even start!"

    "I raise my hands in defeat."

    show natsuki 3w with dissolve_chr
    n "Anyway, as I was saying..."

    show natsuki 3c with dissolve_chr
    n "Writing poetry isn't just some game! You need to have clear plan in mind! There's no point in just writing some random stuff!"

    mc "I'll try to keep it in mind."
    mc "Tell you what, how about you show me your poem now? You're obviously the one here who has things figured out."

    show natsuki 3q with dissolve_chr
    n "Well, yeah. Obviously!"
    return

label poemresponse_2_natsuki_appeal_yuri:
    show natsuki 5g at t11
    n "..."
    show natsuki 5w with dissolve_chr
    n "Jeez... You too...?"

    mc "What?"

    show natsuki 5q with dissolve_chr
    n "Why does everyone think poetry always has to be so complicated?!"

    mc "Huh?"

    show natsuki 5r with dissolve_chr
    n "Seriously, it's like no one even understands what it's about! You all just go for those fancy words, as if it's all you need for a good poem!"

    mc "Natsuki, hold up. What's going on?"

    show natsuki 3w with dissolve_chr
    n "Sigh..."
    n "Well, first of all... you don't even have the skill to write things this way..."

    mc "Which way, Natsuki?"

    show natsuki 4e with dissolve_chr
    n "The way you all overcomplicate stuff, always making it sound so metaphorical. You're just confusing the reader!"

    mc "Well, poetry shouldn't just be completely plain, should it? Otherwise, wouldn't you be just as well off in a normal conversation?"

    show natsuki 4w with dissolve_chr
    n "Oh, come on, [player]!"
    show natsuki 4e with dissolve_chr
    n "Don't you understand? It's not about making it look or sound pretty... It's about the message you're trying to deliver!"
    show natsuki 4b with dissolve_chr
    n "You need to make your point clear and strong, not force the reader to guess what you had in your mind!"
    show natsuki 3q with dissolve_chr
    n "And you need more than just some fancy words for that..."

    mc "Hmmm, I... think I get what you mean..."

    show natsuki 5C with dissolve_chr
    n "You'd better... or else you'll never understand my poems..."

    "She mumbles that last part so I can barely hear what she says."

    mc "Well, we'll never know unless I try, right?"

    show natsuki 5w with dissolve_chr
    n "Yeah, I guess. Here you go..."
    return

label poemresponse_2_natsuki_appeal_monika:
    show natsuki 3h at t11
    n "..."
    n "Sigh..."
    mc "Um... Is something wrong?"

    show natsuki 5h with dissolve_chr
    n "It's just the way you're... overcomplicating things and making it so abstract..."
    n "It makes it more confusing than it needs to be..."
    show natsuki 5s with dissolve_chr
    n "You're not going completely overboard, thankfully..."
    show natsuki 5h with dissolve_chr
    n "But I still think it's a weird starting point! I mean, you are a complete newbie when it comes to poetry, right?"

    mc "You're sitting in the presence of the walking definition of 'newbie,' Natsuki..."
    mc "As for my poem... I honestly don't even know how it turned out the way it did. I was just writing, well, something..."

    show natsuki 3g with dissolve_chr
    n  "Well, just so you know, it's very rough around the edges! And that's not surprising, given your skill level."
    n "That's why I'm saying that this is a very tough way to start!"
    show natsuki 3h with dissolve_chr
    n "Besides, poetry isn't about making things fancy, it's about having a clear message. A simple but deep one!"
    n "People don't read poems just to get a headache trying to figure out what the writer had in mind!"

    mc "Okay, okay, I understand. Keep it simple, fewer words, but more meaning to them. Got it."
    mc "Could you show me your poem now? I'll probably understand you better with a clear example in front of me."

    show natsuki 3s with dissolve_chr
    n "Hmph... Okay, I guess it's worth a shot..."
    return

# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================

label poemresponse_2_monika:
    if poemsread == 0:
        "I think I'm going to start with Monika..."
        "After all, she was the one who came up with this idea, and she did say yesterday that she was eager to see my poem in particular."
        "Besides, she's the president here. I would even call her a sort of mentor figure for the others."
        "So I hope she won't judge me too harshly, especially since it's my first time..."

    show monika 2j at t11
    m "So, [player], ready to share your poem with me?"

    mc "Um... Sure, I guess?"

    show monika 2r with dissolve_chr
    m "Sigh..."
    show monika 4i with dissolve_chr
    m "[player], you really should ease up a little..."
    show monika 4e with dissolve_chr
    m "I mean, you're in the club already. The toughest part is over!"
    show monika 2e with dissolve_chr
    m "Seriously, I never expected you to have any problems fitting in. I mean, everyone seems to like you already!"
    show monika 4n with dissolve_chr
    m "Well, okay, Yuri and Natsuki might not look like they're exactly happy to see you..."
    show monika 4k with dissolve_chr
    m "But I assure you that they're actually glad that you joined the club! Trust me. I saw their smiles yesterday."

    mc "Wait, you really expected a person who never wanted to join any clubs to fit right in just like that?"
    mc "Especially with members like these..."

    show monika 3d with dissolve_chr
    m "Huh? What do you mean?"

    mc "...!"

    "{i}Damn it, I really shouldn't have said that...{/i}"

    mc "W-Well, I..."

    show monika 2a with dissolve_chr
    m "Wait a minute..."
    show monika 5a with dissolve
    m "[player]..."

    "{i}Please don't...{/i}"

    m "What you just said..."

    "{i}Don't make me go through this!{/i}"

    m "You know that there are two ways to interpret it?"
    m "That could either imply that you don't like it here, because of us..."
    show monika 5b with dissolve_chr
    m "Which, in turn, implies that you don't like us..."

    show monika 5a with dissolve_chr
    m "Or..."

    mc "Monika, please!"

    show monika 4k with dissolve
    m "Uh-uh-uh! Now you're in for it, [player]. I won't leave you alone until you spit it all out!"

    mc "Ughhh..."
    "{i}Curse my blabbering mouth...{/i}"

    show monika 2j with dissolve_chr
    m "Say it."

    mc "Monika, please..."

    show monika 4j with dissolve_chr
    m "Not until you say it!"

    mc "Sigh..."
    mc "Alright, fine. it's hard for me to fit in right from the start because... this club is full of... girls..."

    show monika 2A with dissolve_chr
    m "...?"

    mc "..."
    mc "...very cute and interesting girls..."

    show monika 2j with dissolve_chr
    m "That's better!"
    show monika 5a with dissolve
    m "See, it wasn't so hard, right?"

    "I glance around the clubroom. It seems that the others thankfully didn't hear Monika just made me go through."

    mc "Can we... just get back to the poem sharing now?"

    show monika 4j with dissolve
    m "And now you're also eager to share!"
    show monika 2b with dissolve_chr
    m "You see, encouraging the members of my club to be more open is one of my direct responsibilities."
    show monika 2k with dissolve_chr
    m "Even if it does involve putting them on the spot for a second..."

    "{i}I just hope that you're not going to make me your test subject of sorts...{/i}"

    show monika 3a with dissolve
    m "Okay. Now, let's get back to the topic at hand."

    mc "Yeah... That's a great idea..."

    "I give Monika my poem, avoiding eye contact."

    scene bg club_day with wipeleft_scene
    $ renpy.call("poemresponse_2_monika_appeal_{appeal}".format(appeal=poemwinner[0]))

    # REJOIN:
    "Monika hands me her notebook."
    "Looking at her poem, I can see her pristine handwriting..."
    "It makes sense: She never settles for second-best. Whenever she does something, it's always going to be top-notch."

    if persistent.playthrough == 0:
        call showpoem(poem_m_1a)  # "Just Another World"

        show monika 4a with dissolve
        m "So, [player], I think it's time I get some feedback from you."

        mc "Well, I'm no expert, obviously, but I can definitely tell that you have skill."

        show monika 2a with dissolve_chr
        m "Can you be a bit more... specific?"

        mc "It really is a beautiful poem -- the style, the meaning, the mood... all of it is very fine-tuned..."
        mc "But I'm not sure I really understand what it's about."

        show monika 3p with dissolve_chr
        m "Well, you see, I had a weird dream a few days ago..."

        show monika 3m with dissolve_chr
        m "I can hardly remember what it was about, but it left me wondering..."
        show monika 3e with dissolve_chr
        m "It made me think about our lives and wonder, 'Are we even in control?'"
        m "Is anything really up to us, as people seem to think? Or were our fates predetermined from the very beginning?"

        mc "I get what you're saying. Sometimes I also feel like I don't have any real control over what happens."

        show monika 2d with dissolve_chr
        m "You do? Hmm... Interesting..."
        mc "And now that you've mentioned it, I also had a weird dream the other day, but I'm pretty sure it was just me being extremely tired from midterms."
        mc "Stress and exhaustion do cause weird dreams at times, right?"

        show monika 2k with dissolve_chr
        m "Ahaha! Yeah, you might be right. Pretty sure I can relate to that as well."
        mc "Yeah... Okay. I guess that's it, right?"
    else:
        call showpoem(poem_m_1b) # This is a Place of Happiness
        # rest of call, still waiting to be approved

    show monika 2j with dissolve_chr
    m "Yep! Thank you very much for sharing with me. I really hope you enjoy your time here!"
    mc "You really seem worried about me, don't you?"

    show monika 2e with dissolve_chr
    m "Of course I am! Sayori might have brought you here, but I was the one who put the question point-blank and asked you to join us."
    show monika 4b with dissolve_chr
    m "Besides, it's my responsibility as president to make sure everyone feels comfortable around here!"

    mc "I appreciate that, Monika. Don't worry, it's actually been a lot of fun so far."

    show monika 2j with dissolve_chr
    m "It's a relief to hear that. Honestly, I'm glad."
    show monika 1b with dissolve_chr
    m "Anyway, we should move on now. I'll chat with you later, okay?"
    mc "Okay."

    show monika zorder 1 at thide
    hide monika
    "Well, that certainly went better than I expected."
    return

label poemresponse_2_monika_appeal_sayori:
    show monika 2a at t11
    m "..."
    show monika 2m with dissolve_chr
    m "Predictable..."

    mc "Hmm?"

    show monika 4j with dissolve_chr
    m "I'm saying that it's very close to what I expected from you, [player]."

    mc "Realy? And what exactly did you expect?"

    show monika 3a with dissolve_chr
    m "Well, I might be mistaken, of course. It's only your first attempt, after all. You could've written it this way completely unintentionally..."

    mc "To be fair, I was just quite honest, I was just writing whatever popped up in my mind. That's all..."

    show monika 1j with dissolve_chr
    m "Once again, just the way I expected."
    show monika 1a with dissolve_chr
    m "Okay, let me give you some actual feedback. It's a start, and it's quite a simple one..."
    m "...It looks like you decided to play it safe, to use a method that's at least slightly familiar, without any bold experiments."
    show monika 3j with dissolve_chr
    m "Don't get me wrong. It's not bad. Not all poetry needs to have a deep, thought-provoking message or a beautiful, extravagant style..."
    show monika 3a with dissolve_chr
    m "Sometimes, it's the simple things that can end up being the most heartwarming. Or heartbreaking, for that matter."
    m "And making the reader feel the emotions you had while writing this? It's a huge challenge."

    mc "..."
    mc "You know, I feel like you're my psychiatrist right now, and you're explaining the problems I didn't even know I had..."

    show monika 2j with dissolve_chr
    m "Ahaha! Yeah, sorry about that..."
    show monika 2a with dissolve_chr
    m "Anyway, we're getting a little distracted here. You've shown me your poem, so now it's my turn."

    mc "Go ahead, then. I doubt you'll have to be as embarrassed as I was."
    return

label poemresponse_2_monika_appeal_yuri:
    show monika 3c at t11
    m "..."
    show monika 3d with dissolve_chr
    m "A bold choice, [player]..."
    m "Definitely not something I'd expect from someone's first attempt..."

    mc "Is that a good thing or a bad thing?"
    show monika 3d with dissolve_chr
    m "Well, it's a bit of both. First of all, you've made quite a bold choice, [player]."
    m "I understand that you may have taken inspiration from the works of some well-known authors, but trying to write something while keeping this style..."
    show monika 4d with dissolve_chr
    m "...can be very challenging for a rookie!"

    mc "I'm not sure I follow..."

    show monika 4e with dissolve_chr
    m "Using metaphors and complex figures of speech takes skill and right now, you're setting yourself a very high standard that you may or not be able to meet yet."

    mc "Honestly, Monika, at this point, I don't have a slightest clue what I'm even doing."

    show monika 3j with dissolve_chr
    m "I'm sure you'll figure it out soon enough! And, please, don't let my words get to you. I never meant to discourage you!"
    show monika 3b with dissolve_chr
    m "We all have our own paths to take, and in case you feel this is the one you for you, then go for it! I just want you to know that it won't be an easy one..."
    mc "You're probably right. Maybe I'll try this again. Who knows?"

    show monika 2j with dissolve_chr
    m "That's fine by me! Okay, now I think it's my turn to share!"

    mc "Go ahead, then. I bet you hand more luck with your poem."
    m "Well, I guess we're about to find out."
    return

label poemresponse_2_monika_appeal_natsuki:
    show monika 2j at t11
    m "..."
    show monika 2k with dissolve_chr
    m "Awww... Now this just adorable!"

    mc "Ahem! I'm not exactly used to hearing that word when it's about me, you know?"

    show monika 3a with dissolve_chr
    m "Well, I was talking about your poem, rather than you..."
    show monika 5a with dissolve_chr
    m "But you know, now that I think about it..."
    m "I guess it could be used to describe you as well, to a certain degree!"

    mc "Um... Thanks, I suppose..."

    show monika 2l with dissolve_chr
    m "Ahahah! Sorry, teasing you just never gets old, does it?"

    "I roll my eyes."

    show monika 3a with dissolve_chr
    m "Okay, now let's get back to business."
    m "The path you chose might seem easy at first, but trust me, it's actually far more challenging than you think."
    show monika 3b with dissolve_chr
    m "Focusing all of your efforts on delivering the message and emotions you have while writing this can be difficult in itself."
    m "But if you also sacrifice the style and overall length of the poem, you might leave yourself vulnerable."
    show monika 3d with dissolve_chr
    m "You know, those things usually serve to paint a picture or set a mood, or..."
    mc "Well, can't they serve different purposes depending on the poem?"
    m "They can, but if you ignore all of that completely, you risk failing to make the message hit the reader hard enough..."
    show monika 3n with dissolve_chr
    m "Which is what happened here in this poem of yours..."

    mc "Ha! Man, that's a long way of telling someone that their work is disappointing."

    show monika 2e with dissolve_chr
    m "My job isn't to rub your nose into your mistakes, but rather, to help you realize them and find a possible way of improving yourself."
    show monika 4j with dissolve_chr
    m "Besides, I never said your poem was bad!"
    m "Rough and unpolished, maybe, but definitely not bad."
    m "And if you put forth the effort, I'm certain you'll go far!"

    mc "Well... Thanks, I guess..."

    show monika 2a with dissolve_chr
    m "Right, now I think it's about time you read my poem, don't you think?"

    mc "Sure, why not?"
    return

label poemresponse_2_monika_appeal_monika:
    show monika 3d at t11
    m "..."
    m "A peculiar choice... to say the least..."

    mc "That isn't the way you pronounce 'completely random and unconscious,' Monika."

    show monika 5a with dissolve_chr
    m "Is that so? So, you really had no idea what you were doing while writing this?"

    mc "Well... Pretty much, yeah..."

    "{i}Why is she giving me that look?{/i}"

    show monika 2j with dissolve_chr
    m "Hmm... Okay, if you say so..."

    mc "..."
    mc "So... do I get any feedback or anything?"

    show monika 4a with dissolve_chr
    m "Well, for a moment, I had a feeling that there was something more to it..."
    show monika 2o with dissolve_chr
    m "But then you just shattered all those hopes in an instant..."

    mc "Um... 'Hopes'...? What do you mean?"

    show monika 2k with dissolve_chr
    m "Ahaha! Don't read so much into it!"
    show monika 3m with dissolve_chr
    m "Okay, so... about your poem..."
    m "It's... definitely not what I expected from you."
    m "You're raising the bar quite high, right off the bat..."
    show monika 4n with dissolve_chr
    m "I'm not saying that's a bad thing, but I'm just worried that if you fail to meet your own expectations, you'll lose your drive and give up on it completely."

    mc "I would be able to give you a clear answer if I knew what you're even talking about..."

    show monika 2e with dissolve_chr
    m "You're... How should I put this?"
    m "You're trying your best to maintain the balance of everything in your poem, to keep everything beautiful, meaningful and, yet, still simple enough to understand."
    show monika 1m with dissolve_chr
    m "You're trying to make things, well, perfect... to satisfy every possible taste..."

    mc "Okay... but isn't that a good thing?"

    show monika 1l with dissolve_chr
    m "I never said it's not! It's just... challenging. Especially for a beginner..."

    mc "Well..."

    show monika 1n with dissolve_chr
    m "Yeah..."

    "This feels really strange. I think this is the first time I've ever seen Monika act like this..."

    mc "So..."

    show monika 3l with dissolve_chr
    m "Would you like to see my poem now?"

    mc "Well, sure, I mean... It's your turn now, after all..."
    return
