# -------------------------------------------------------------------------------------------
# All poem responses for all four girls (with all four appeals) for day 2 (Tuesday)
# -------------------------------------------------------------------------------------------

label poemresponse_2_sayori:
    if poemsread == 0:
        "I guess it makes sense for me to start with Sayori."
        "She is my good friend, after all, so I should be most comfortable sharing my poem with her first."
        "Also, she was the one who dragged me here..."

    show sayori 1x at t11
    s "Hey, [player]! Ready to share your poem with me?"
    mc "Well, yeah... I mean, do I have any alternatives?"
    show sayori 1d with dissolve_chr
    s "Awww, come on! Don't be so nervous! It's just a poem, after all. Besides, who am I to judge?"
    show sayori 4r with dissolve_chr
    s "And even if I was any good, I still wouldn't be harsh about it. You're my friend, after all!"
    s "And I am just so happy that you're here with us!"

    mc "Hehe... yeah, thanks, Sayori..."
    show sayori 1a with dissolve_chr
    mc "To be fair, I'm still trying to wrap my mind around it."
    mc "If someone told me a week ago that I'd end up in a club dedicated to literature and that {i}I,{/i} of all people, would be writing poems, I would laugh out loud."

    show sayori 4s with dissolve_chr
    s "Ahahah! Well, fate works in superior ways!"

    mc "I... think the word you were looking for is \"mysterious...\""

    show sayori 3l with dissolve_chr
    s "Y-Yeah, that!"
    show sayori 1x with dissolve_chr
    s "It doesn't matter! Let me see your poem now. I can't wait!"

    "I give Sayori the notebook where I wrote my poem yesterday."

    scene bg club_day with wipeleft_scene

    $ renpy.call("poemresponse_2_sayori_appeal_{appeal}".format(appeal=poemwinner[0]))

    # REJOIN:
    "Sayori hands me her poem."
    "It's written on a sheet of paper, torn out from a notebook."
    "The sheet is covered in small wrinkles here and there and it~... wait a minute, is that...?"
    "Yep. It's a small yet visible coffee stain, or at least something that looks like it."

    mc "Jeez, I haven't read the poem yet, but even the paper you wrote it on already reminds me of you, Sayori..."

    show sayori 5c with dissolve_chr
    s "Come oooon! There's no need to be mean about it!"
    mc "Ughhh..."
    mc "Nevermind, let me just read it..."


    call showpoem(poem_s_1)  # "A Day on the Ice"


    show sayori 1a with dissolve
    mc "..."
    mc "Man, that brings back memories..."

    show sayori 4r at h11
    s "I know, right?"
    show sayori 1x with dissolve_chr
    s "You see, when I checked my calendar yesterday, I suddenly realized that winter isn't that far away!"
    s "And those memories just started washing over me!"
    show sayori 1a with dissolve_chr
    s "You remember how we were both learning how to ice-skate?"
    show sayori 4r with dissolve_chr
    s "That was super fun!"

    mc "Yeah... it sure was..."
    show sayori 1a with dissolve_chr
    mc "..."
    mc "Okay, before I start to get flashbacks, care to answer one question, Sayori?"

    show sayori 3x with dissolve_chr
    s "What's that?"

    mc "How was that hot chocolate?"
    show sayori 5a with dissolve
    s "Ehehe~ What do you mean?"

    mc "Oh, you know, the one that supposedly left a spot riiiight here, maybe?"
    mc "The one I assume you had with breakfast?"

    show sayori 5b with dissolve
    s "Ehehe~"

    mc "Sayori, tell me, {i}honestly...{/i}"
    mc "Did you write your poem when you were-{w=0.5}{nw}"

    show sayori 4p at h11
    s "D-Don't say it out loud!"

    show monika 3d at l41
    m "Umm... don't say {i}what{/i} out loud?"

    show sayori 1m with dissolve_chr
    s "Nothing!"

    show monika at lhide zorder 1
    hide monika

    mc "Heheheh..."

    show sayori 5c with dissolve_chr
    s "{i}You're such a meanie, [player]!"
    mc "{i}Well, excuse me, but you're the one around here who does her homework while eating breakfast!{/i}"

    show sayori 3h with dissolve_chr
    s "Eh? Writing poems isn't just {i}homework{/i}, you know?"

    mc "I know."
    mc "But I also know that this isn't the first time you've done something like this."

    show sayori 1l with dissolve_chr
    s "Okay, okay! Just don't tell Monika...?"

    mc "Oh, I don't know..."
    mc "What would I get out of it?"

    show sayori 1j at h11
    s "[player]!"
    mc "Ehehe... Okay, I'm done teasing, relax."

    show sayori 1i with dissolve_chr
    mc "I have to say, it's a very good poem."
    show sayori 1b with dissolve_chr
    mc "It's nothing fancy, but it feels just like you, basically."
    show sayori 4x with dissolve_chr
    s "Really? And how does it make you feel?"

    mc "Carefree, cheerful... It reminds me of how much fun we used to have."

    show sayori 1d with dissolve_chr
    s "Awww..."
    s "See? You're not always so grumpy and mean, after all!"
    show sayori 1r with dissolve_chr
    s "Hehe! I know that you're actually a real softie deep inside!"

    mc "Ahem! Monika, could you come ov-{w=0.5}{nw}"

    show sayori 4s at s11
    s "Okay, okay, I'll shut up now!"

    show sayori at thide zorder 1
    hide sayori
    "I chuckle to myself, unable to keep a straight face while watching Sayori's mood swings."
    "Yeah, I guess me being here is really for the best, after all."
    return

label poemresponse_2_sayori_appeal_sayori:
    show sayori 2n at t11
    s "..."
    show sayori 2o with dissolve_chr
    s "..."

    mc "Ahem... Sayori?"

    show sayori 1m at h11
    s "Huh? Oh, sorry! I spaced out for a second..."

    mc "Hah! After all the times {i}you{/i} accuse {i}me{/i} of that..."
    show sayori 3h with dissolve_chr
    s "It's not that, I just..."
    s "This is... your first try? And you wrote it yourself, right?"

    mc "Sayori, are you serious right now?!"

    show sayori 1l with dissolve_chr
    s "Y-Yeah, you're right. Sorry about that."
    show sayori 1c with dissolve_chr
    s "I just didn't expect it to be that good, to be honest."

    mc "Ummm... thanks?"

    show sayori 1q with dissolve_chr
    s "Heheh~ Don't get cocky, though. It's still pretty rough around the edges..."
    show sayori 1a with dissolve_chr
    s "But I really like it anyway!"
    show sayori 4x with dissolve_chr
    s "And if there's anything that proves that I was right about bringing you here, then this is definitely it!"
    mc "Well, as long as it's not a complete disaster, I guess I'm fine with that..."
    mc "Now... it's your turn, right?"

    show sayori 4r with dissolve_chr
    s "Yeeeep!"
    return

label poemresponse_2_sayori_appeal_natsuki:
    show sayori 1q at t11
    s "..."
    s "Eheheh..."

    mc "Hey! I know it's bad, but you could at least {i}try{/i} not to laugh at it!"
    show sayori 3r with dissolve_chr
    s "I'm not laughing {i}at{/i} it, [player], it just reminded me of someone..."

    mc "Could you be any more vague?"

    show sayori 1l with dissolve_chr
    s "Well... it's a bit... blunt... and simple..."

    mc "Coming from you, I don't know if I should feel insulted or amused."

    show sayori 5d with dissolve_chr
    s "H-Hey! I'm not only about cute and... happy stuff and... you know..."

    mc "..."
    mc "Really???"

    show sayori 5b with dissolve_chr
    s "W-Well... at least not all the time..."

    mc "Uh-huh, sure..."
    mc "Okay, just tell me. How bad is it?"

    show sayori 1a with dissolve_chr
    s "It's not bad, actually! It's different from what I expected, but it's definitely not bad!"
    show sayori 1x with dissolve_chr
    s "You have a long way to go, that's for sure, but you've got potential!"
    show sayori 1q with dissolve_chr
    s "I'm really curious what your next poems will look like."

    mc "Well, it's a bit too early for that. Mind if I read your poem now?"

    show sayori 1x at h11
    s "Okay!"
    return

label poemresponse_2_sayori_appeal_yuri:
    show sayori 1n at t11
    s "..."
    s "Whoa..."
    show sayori 1o with dissolve_chr
    s "[player], did you really write this yourself?"

    mc "Sayori, come on! I thought you of all people would give me at least {i}some{/i} credit here!"

    show sayori 1l with dissolve_chr
    s "Yeah, sorry about that."
    show sayori 1g with dissolve_chr
    s "It's just... not what I was expecting from you..."
    show sayori 1i with dissolve_chr
    s "It's just so deep... and complicated..."
    show sayori 3j with dissolve_chr
    s "Did you just find this somewhere online?"

    mc "Sayori, you do get how ridiculous that sounds, right?"
    mc "And I know that I'm not any good at writing yet, but still... you've could at least given me some {i}actual{/i} feedback!"
    mc "You know, something other than your baseless accusations!"

    show sayori 4e with dissolve_chr
    s "Sorry... I really didn't mean it that way."
    show sayori 4k with dissolve_chr
    s "I just think it's weird for you to start off with something like... {i}this{/i}..."
    show sayori 1o with dissolve_chr
    s "In all seriousness, I really have no idea what you wrote about in your poem!"

    "How did you even manage to say the word \"seriousness?\""
    show sayori 3x with dissolve_chr
    s  "But maybe that's not a bad thing! Poems don't always need to have a clear message, right?"
    s "If you just want to say exactly what you mean, then what's the point of writing a poem, right?"

    mc "Yeah, I... you're probably right..."

    show sayori 1a with dissolve_chr
    mc "Okay then... care to share your poem with me?"

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
    s "Well, okay it's not {i}very{/i} good, but it sure is better than what I expected!"

    mc "..."
    mc "...implying that you expected it to suck far more?"

    show sayori 3x with dissolve_chr
    s "Well, it's way more abstract and... organized than I thought it would be!"
    show sayori 3g with dissolve_chr
    s "And what makes you think I would expect it to su-... {i}be bad{/i}?"

    mc "Well, you said it yourself. You obviously had lower expectations."

    show sayori 3h with dissolve_chr
    s "Yeah, but... I never said I expected to be, like, \"bad\" bad..."
    show sayori 1x with dissolve_chr
    s "You know what? I think what matters most right now is that you're taking your first steps!"
    show sayori 4r with dissolve_chr
    s "And quite nice ones, for that matter!"

    mc "Haha... well, yeah, thanks..."
    mc "So... is this the part where {i}you{/i} share your poem with me?"

    show sayori 1n at h11
    s "Oh! Yeah! I completely forgot!"
    show sayori 1q with dissolve_chr
    s "Here you go, [player]!"
    return

# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================

label poemresponse_2_yuri:
    if poemsread == 0:
        "If I'm to be pragmatic about this, then my first choice should definitely be Yuri."
        "Out of all members, she's clearly the one with the most experience, at least when it comes to literature."
        "Besides, knowing her shyness, I hardly expect her to be too harsh to me..."
        "..."
        "Who am I kidding? That girl probably expects {i}me{/i} to be harsh to {i}her.{/i}"

    show yuri 2t at t11
    y "Oh, h-hi, [player]..."

    mc "..."
    mc "We've... already seen each other today, Yuri."

    show yuri 3q with dissolve_chr
    y "Ahaha.... yeah... silly me..."
    y "..."
    show yuri 3w with dissolve_chr
    y "So... I assume you would like us to... s-share our poems?"

    "I can't help but smile. At least I'm not the only one embarrassed about this whole... activity Monika came up with."

    show yuri 3n with dissolve_chr
    y "W-Why are you s-smiling?"
    show yuri 3p with dissolve_chr
    y "I-Is it something I said?"

    mc "Yuri, take it easy, okay?"
    show yuri 3o with dissolve_chr
    mc "This is just as new to me as it is to you."
    mc "And unlike me, you at least know your way around poetry."

    show yuri 3q with dissolve_chr
    y "I'm... not that good, to be honest..."

    mc "Oh, come on, don't be shy. You left me speechless when you were talking about your passion for literature just yesterday."
    mc "And impressing {i}me,{/i} with literature as a topic? That counts for something."

    show yuri 4b with dissolve_chr
    y "Yeah... I suppose it does..."

    mc "Also, if I remember correctly, you promised to make me feel as comfortable here as possible."
    mc "And... I don't think us spending the rest of the meeting just sitting here, too embarrassed to share our work, qualifies as \"comfortable.\""

    show yuri 2w with dissolve
    y "*sigh*"
    show yuri 2u with dissolve_chr
    y "You're right... please excuse my modesty. This is... a new experience for me, after all."

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
    "Nevertheless, I finally get my hands on it and start leafing through the pages, looking for her latest poem."
    "Her handwriting is beautiful, almost calligraphic..."

    call showpoem(poem_y_1)  # "Fading Light"

    show yuri 4a with dissolve

    mc "..."

    y "S-So? What do you think?"

    mc "It's very beautiful. And to be fair, it's quite clear. I would've expected you to make it more... mysterious..."

    show yuri 4C with dissolve_chr
    y "Oh, ummm... I'm... sorry to disappoint you..."

    mc "Hu- What?! No! No-no-no, that's not what I..."
    mc "Ughhh..."
    mc "{i}Why does everything I say come out so wrong?{/i}"
    mc "I never said it was bad in any way. I was just under the impression that you would make the message more concealed, more... challenging to uncover..."

    show yuri 2v with dissolve
    y "Well... I wouldn't exactly call you misguided..."
    y "I {i}do{/i} tend to... overcomplicate things a bit..."
    show yuri 2w with dissolve_chr
    y "My usual style revolves around the idea of trying to make the reader ponder for a bit, to make him try to understand {i}my{/i} way of thinking..."
    show yuri 2h with dissolve_chr
    y "Or to instead find some new meaning to it, one that initially evaded my gaze, to see my work from a completely new perspective..."

    mc "Ahem..."

    show yuri 3q with dissolve_chr
    y "O-Oh! Y-Yes... excuse my rambling..."

    "No offense, Yuri, but if I let you talk, we'll most likely be stuck here until tomorrow..."

    show yuri 1u with dissolve_chr
    y "I just thought that for the first time it would be logical to start with something more... plain..."
    show yuri 3t with dissolve_chr
    y "D-Do you think it was a wrong move?"

    mc "Wha- no! Yuri, please, you really think too much about this!"

    show yuri 3s with dissolve_chr
    y "Well, I'm afraid that's just the way I am. I hope it doesn't cause you all much trouble..."
    show yuri 4a with dissolve_chr
    y "S-So... you've said that you found the message in this poem quite... obvious?"

    mc "Well, yeah... at least I think so."

    show yuri 4b with dissolve
    y "And... what does it make you think of m-me?"

    mc "Ah, so you confirm that the character of this poem is indeed you?"

    show yuri 3o with dissolve
    y "Eh... well, I-I..."

    mc "What can I say, then? I'm beginning to understand your interest in literature a bit more."

    show yuri 3f with dissolve_chr
    y "Huh?"
    y "Y-You... you do?"

    mc "Well, if it paints such a beautiful image in your mind that even the description of that process..."
    mc "..."
    mc "You {i}were{/i} describing yourself reading, right? The other worlds you wander off to? How the time passes, unnoticed?"

    show yuri 3q with dissolve_chr
    y "Well, y-yes..."
    mc "Then... as I was saying, if you manage to make the mere description of that process sound so beautiful, I can hardly imagine what you must experience during it."
    mc "...not that I can fully comprehend your passion towards it."

    show yuri 2u with dissolve
    y "..."
    y "I'm still glad you understand, even if it's just slightly..."
    y "It's good to see that there are people who I can talk to about things like this..."

    mc "Pfff! So you mean to tell me that you had no such people before I came here? In a Literature Club, no less?"
    mc "Now I know you're pulling my leg..."

    show yuri 1c with dissolve_chr
    y "And that's coming from a person who claimed he had no interest in literature whatsoever..."

    mc "Heh? Well... I wasn't lying!"

    show yuri 1a with dissolve_chr
    y "Do you even believe that, yourself?"

    mc "..."
    mc "I... don't think I have a straight answer to that question yet..."

    show yuri 1c with dissolve
    "Yuri giggles softly."

    show yuri 1s with dissolve
    y "At any rate, I think I shouldn't hold you off any longer, but..."

    mc "But?"

    show yuri 1u with dissolve_chr
    y "I..."
    show yuri 3s with dissolve_chr
    y "I just wanted to thank you, [player]... I really needed someone to help me make the first step."

    mc "Yeah... we both did..."

    show yuri 3c with dissolve_chr
    $ renpy.pause(0.7)
    show yuri at thide zorder 1
    hide yuri
    "Yuri gives me a sweet smile and then turns away; I guess our conversation is over..."
    return

label poemresponse_2_yuri_appeal_sayori:
    show yuri 2g at t11
    y "..."
    show yuri 1i with dissolve_chr
    y "..."
    show yuri 1m with dissolve_chr
    y "Well, it's pretty much the way I expected it to be."
    show yuri 1a with dissolve_chr
    y "This is your first time, correct?"

    mc "..."

    "{i}I really hope that this is the first and the last time I hear those two sentences in THAT particular order coming from a girl...{/i}"

    mc "Y-Yes. Why?"

    show yuri 1c with dissolve_chr
    y "It's nothing, really. I'm just rather familiar with the common mistakes of inexperienced writers."
    show yuri 1m with dissolve_chr
    y "In your particular case, I suppose you decided to start with something simple. Am I right?"
    show yuri 1k with dissolve_chr
    y "You didn't want to oversaturate your poem with metaphors or make any strong message in it, but rather give it a calm, soothing mood."
    show yuri 1a with dissolve_chr
    y "It's not a bad thing at all. Sometimes, even I require something to vent my thoughts instead of holding onto them in constant pondering..."

    mc "..."
    mc "Yuri, I'm going to be honest with you..."

    show yuri 1e with dissolve_chr
    y "Oh?"

    mc "I was just writing something, {i}anything...{/i} I honestly don't know what I had in mind during that."

    show yuri 1d with dissolve_chr
    y "And that only further confirms my assumption!"

    mc "Assumption? What assumption?"

    show yuri 2m with dissolve_chr
    y "All in good time, [player]."
    show yuri 3u with dissolve_chr
    y "Besides, I'm actually curious if your style changes as you go..."

    mc "At this point, I'd be happy if I made any progress at all, let alone find any particular \"style\" of my own."

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
    y "T-That's..."
    y "...not something I was expecting, to be honest."

    mc "Wow, you actually had some specific expectations at all?"

    show yuri 2i with dissolve_chr
    y "Well, I understand that this is your first attempt, but I hoped that you would pick... a {i}different{/i} approach..."

    mc "C-Care to elaborate? Because I barely knew what I was doing at all."

    show yuri 1i with dissolve_chr
    y "You see, it's not particularly a bad idea to focus your attention on the message..."
    show yuri 1l with dissolve_chr
    y 1l "...but there's really no need to limit yourself."
    show yuri 2v with dissolve_chr
    y "There are so many beautiful words, so many beautiful ways to convey your thoughts and your feelings..."
    show yuri 2t with dissolve_chr
    y "In the hands of a writer, language is a tool to deliver his or her message in a profound way, which would leave people in awe."

    mc "Okay! I get it, it sucks! There's really no need in trying so hard to spare my feelings, Yuri."

    show yuri 3p at h11
    y "N-No! I never said that!"
    show yuri 3o with dissolve_chr
    y "I-I just meant that it's s..."
    y "S-S...."

    "I can barely contain my laughter at this point."
    mc "S...?"
    show yuri 3p with dissolve_chr
    y "S-Simplistic!"
    show yuri 3o with dissolve_chr
    y "Y-Yeah... that's the... word..."
    mc "Ahaha..."
    mc "Okay, I think I'm fine with that feedback."
    mc "Thank you."
    show yuri 3q with dissolve_chr
    y "Y-You... you're welcome..."
    mc "Okay, mind if I take a look at your poem now?"
    show yuri 2s with dissolve_chr
    y "Oh, y-yes, sure..."
    return

label poemresponse_2_yuri_appeal_yuri:
    show yuri 2u at t11
    y "..."
    y "T-That's... really impressive, [player]"

    mc "..."
    mc "Yuri, that's like... the textbook definition of \"flattery\" right there."

    show yuri 3t with dissolve_chr
    y "W-What makes you say that?"

    mc "Because I can hardly expect someone with as much experience as you to find my first poem ever {i}impressive!{/i}"

    show yuri 2e with dissolve
    y 2e "Ummm, this is... your first time?"

    mc "..."
    mc "I'll... take that as a compliment."
    mc "And yes, it {i}is.{/i} I kinda thought that would be obvious."

    show yuri 2f with dissolve_chr
    $ renpy.pause(0.5)
    show yuri 1g with dissolve_chr
    y "..."

    "Yuri starts rereading my poem, tracing her finger along the words, as if it helps her analyze it more thoroughly."

    show yuri 1j with dissolve_chr
    y "Ah, yeah, t-that makes sense."
    show yuri 1l with dissolve_chr
    y "Well, I won't lie. It's far from perfection."

    "Oh, so {i}now{/i} it's suddenly not so impressive?"

    y "You've managed to make a couple of mistakes, common among the beginners..."
    show yuri 1k with dissolve
    y "And while you certainly have {i}some{/i} skill in usage of imagery and metaphors..."
    show yuri 1i with dissolve_chr
    y "...I hardly think I'm ready to call you an author with his unique and well-defined style."
    show yuri 1c with dissolve_chr
    y "But nevertheless, you certainly have a lot of potential!"

    mc "Hah... well... I guess I {i}did{/i} almost trick you into thinking that this isn't my first attempt at writing..."
    mc "So that counts for something."

    show yuri 4b with dissolve_chr
    y "Yes... I suppose you're correct about that..."

    "I really didn't expect Yuri of all people to like my poem that much."
    "And I also hope that it's not just her being polite."

    mc "So, I think it's only fair for me to see your poem now?"

    show yuri 3s with dissolve_chr
    y "O-of course! I would be... g-glad to share."

    "Well, at least she's more enthusiastic about it now."
    return

label poemresponse_2_yuri_appeal_monika:
    show yuri 2i at t11
    y "..."

    y "Not bad, [player]."
    show yuri 1a with dissolve_chr
    y "This is your first attempt, correct?"

    mc "Well, yes... I'm pretty sure that wasn't hard to deduce..."

    show yuri 1m with dissolve_chr
    y "Well, if I had to give some feedback, then I would say you've picked quite a peculiar approach."

    mc "Going to need some details..."

    show yuri 1c with dissolve_chr
    y "It's actually quite daring, even. Definitely not something I would expect a novice to choose as his starting point."

    mc "Yuri! The details!"

    show yuri 3q with dissolve_chr
    y "Oh! S-Sorry, I just got a little distracted..."
    show yuri 3s with dissolve_chr
    y "The point is, it's not exactly my style, but I still love it."
    y "It's fine-tuned and it pays enough attention to every aspect of writing a poem, as if you were trying your best to make it... {i}flawless{/i}..."

    mc "And that's... good, right?"

    show yuri 3q with dissolve_chr
    y "Y-Yes... in theory..."

    mc "Ahah... right... guess that's one way to say that I didn't succeed..."

    show yuri 3o with dissolve_chr
    y "Ummm... well..."

    "Yuri obviously can't just bring the hammer down and tell me that I tried to reach for the stars and failed miserably..."

    show yuri 3q with dissolve_chr
    y "A-Anyway, as I was saying..."
    y "People who choose this style are usually confident and straightforward. Yet in their works, they tend to focus on abstractions..."
    show yuri 3u with dissolve_chr
    y "...on images which convey the hardships of their everyday lives..."
    show yuri 2g with dissolve_chr
    y "Hmmm..."
    show yuri 2j with dissolve_chr
    y "So I'm guessing you, too, have a story to tell..."

    mc "Too?"

    show yuri 3q with dissolve
    y "Ehehe... well, yeah... we all have our... stories..."

    mc "Okay..."

    show yuri 1q with dissolve
    y "Y-Yeah..."

    mc "..."

    show yuri 2t with dissolve_chr
    y "W-Would you like to read my poem now?"
    mc "Hmm? Well, yeah, sure."
    return

# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================

label poemresponse_2_natsuki:
    if poemsread == 0:
        "While the whole idea of poem-sharing obviously belongs to Monika..."
        "...I was the one who gave her the idea, and {i}I,{/i} in turn, should thank Natsuki for that."
        "So I guess it would be wise to start with her. I told her that I'd like to see her poems, after all."
        "Besides, I'm actually curious what sort of poems a girl like her would write..."

    show natsuki 3c at t11
    mc "Hey, Natsuki."
    show natsuki 4w with dissolve_chr
    n "Let me guess, you're here to see my poem?"
    mc "Bravo, Mr. Holmes! I never doubted your deductive skills!"

    show natsuki 5w with dissolve_chr
    n "Okay, listen here, funny guy, I don't know wha-{w=0.7}{nw}"
    mc "Natsuki..."

    show natsuki 5h with dissolve_chr
    n "Huh?"
    mc "I know that you don't particularly like me..."

    show natsuki 1p with dissolve_chr
    n "W-Whaa?!"
    n "Why would you expect me to {i}like{/i} you at all in the first place?!"
    mc "I meant \"don't particularly like me being around here\", Natsuki..."

    show natsuki 5q with dissolve_chr
    n "Ah? O-Oh... hmph..."
    show natsuki 5w with dissolve_chr
    n "Well it still doesn't change much!"

    "Oh boy..."

    n "How can you expect me to feel good about it when Sayori just brought you here all of a sudden and not a minute later, you are already a new member!"
    show natsuki 5e with dissolve_chr
    n "And here you are! Roaming around {i}our{/i} club, eating {i}my{/i} cupcakes and..."
    mc "Ughhhh...{w=0.3}{nw}"

    # add screen shake effect
    play sound "sfx/table_hit.ogg"
    show natsuki 1p at h11
    "*SLAM!*"

    show natsuki 4I with dissolve_chr
    n "Hey, what do you think you're doing?!"

    "Desperate to get through that wall of stubbornness, I let my head hit the desk... Not one of my best ideas, to be fair, but I'm just helpless at this point."

    mc "{i}Natsuki, we're not making any progress...{/i}"

    show natsuki 4w with dissolve_chr
    n "Well, hitting your dumb head against school furniture won't help, either!"
    show natsuki 3y with dissolve_chr
    n "Besides, if you want to hit your head so badly, you should get some {i}professional{/i} help!"
    show natsuki 3z with dissolve_chr
    n "I'd be more than happy to give you a hand! Who knows? It might even make you smarter!"
    "I raise my head, rubbing my forehead and chuckling."
    mc "Whatever it takes, Natsuki, whatever it takes..."

    show natsuki 3t with dissolve_chr
    n "Hahaha..."
    n "Haaah... okay, you do have a point, though. We should really get this over with..."
    mc "As long as it doesn't involve any more physical harm to me, I'm all for it."

    show natsuki 1l with dissolve_chr
    n "Well, that depends on you!"
    mc "Let me guess. Still uncomfortable about sharing poems?"

    show natsuki 5q with dissolve
    n "Well, not exactly... I mean, I'm not Yuri, after all..."
    mc "Yeah, that you are. Still, I think I owe you an apology."

    show natsuki 5k with dissolve_chr
    n "An apology? For what?"
    mc "Well... if I wasn't so curious about your poem, Monika wouldn't have come up with all this..."

    show natsuki 5m with dissolve_chr
    n "Yeah... I guess you're right about that."
    show natsuki 5y with dissolve_chr
    n "Thanks for pointing that out, actually! Now I know who to bla-{w=0.7}{nw}"

    mc "Natsuki..."
    mc "Don't you even start..."

    show natsuki 6c with dissolve
    n "Hehehe... okay, okay, I'm done."
    show natsuki 7a with dissolve
    n "I think you've met your quota for today."
    mc "Just let me know when when you're done with this hazing, will you?"

    show natsuki 4y with dissolve_chr
    n "Call it an \"initiation\". And don't think you're getting away with just one day!"

    mc "Figured as much..."

    show natsuki 3a with dissolve_chr
    mc "So... are we going to pull straws or..."
    show natsuki 5w with dissolve_chr
    n "Oh, just cut to the chase and give me those scribbles of yours already!"

    "You don't even realize how perfectly you nailed the description of my poem..."
    "I finally give Natsuki my notebook, which she takes with a look which you'd expect from someone grabbing a live cockroach..."

    scene bg club_day with wipeleft_scene

    $ renpy.call("poemresponse_2_natsuki_appeal_{appeal}".format(appeal=poemwinner[0]))

    # REJOIN:
    "Natsuki hands me a sheet of paper with her poem."
    "It's... written in pink ink..."
    "Seriously, how can she expect someone {i}not{/i} to consider her cute when she acts like this even with the smallest things?"

    call showpoem(poem_n_1)  # "Not Your Cupcakes!"

    show natsuki 5s with dissolve
    mc "..."

    show natsuki 5u with dissolve_chr
    n "I knew you wouldn't like it..."

    mc "Eh? I haven't even said anything yet..."

    show natsuki 4w with dissolve_chr
    n "There's no need to! I can already see it!"

    mc "Sheesh... You sure enjoy jumping to conclusions, don't you?"

    show natsuki 4e with dissolve_chr
    n "That's only because I'm usually right!"

    mc "Well, not this time around..."

    show natsuki 5e with dissolve_chr
    n "Really now? So you mean to tell me you actually like it?"

    mc "Yes, and I'm pretty sure I get what you were talking about just a minute ago..."
    mc "Brief format, with little show-off and a clear message. Simple and efficient."

    show natsuki 2h with dissolve_chr
    n "W-Well... yeah... roughly speaking..."

    mc "So... let me take a wild guess, did you use me as an inspiration for your poem?"
    show natsuki 1o with dissolve_chr
    n "...?!"

    "{i}Fire in the hole!{/i}"

    show natsuki 1v at h11
    n "WWWWHAT?!?!?!"

    mc "I {i}meant{/i} that {i}I{/i} am that hypothetical person who takes your cupcakes without paying you any mind, correct?"

    show natsuki 1o with dissolve_chr
    n "..."
    show natsuki 1r with dissolve_chr
    n "..."
    show natsuki 1o with dissolve_chr
    n "W-Well... y-yeah! So?!"

    mc "So I guess you really don't like being taken for granted, same goes for people not taking you seriously."

    show natsuki 1h with dissolve
    n "Y-Yeah... kinda..."

    mc "And the cupcakes represent what you are and what you want to share with other people, all of it made presentable just to get people's attention..."

    show natsuki 1m with dissolve
    n "Ummm... uh-huh..."
    mc "...but most of those people won't even try to look behind that cover? Won't even try to get the meaning to all this? To see the heart and soul put into it?"

    show natsuki 1k with dissolve_chr
    n "..."
    show natsuki 1q with dissolve_chr
    n "..."
    show natsuki 1s with dissolve_chr
    n "..."

    mc "Umm, hello? Earth to Natsuki!"

    show natsuki 2x with dissolve
    n "Grrr! W-Well, yeah! That's... pretty much what I meant..."
    show natsuki 2s with dissolve
    n "Still surprised you actually understood at least something..."

    mc "I did, and I'm sorry you see me that way."

    show natsuki 1m with dissolve_chr
    n "...?"

    mc "I understand that I just popped up here, seemingly out of nowhere, and that I'm kinda making you uncomfortable..."
    mc "But I didn't come here to make enemies, and I think you and I... kinda got off on the wrong foot."
    mc "I know there's no reason for you to trust me at this point, but I assure you I'll try my best not to be a jerk..."

    show natsuki 1o with dissolve_chr
    n "...!"
    show natsuki 1r with dissolve_chr
    n "..."
    show natsuki 5u with dissolve
    n "..."

    "Ughhh... another side note to myself: Approaching Natsuki kindly when she's pissed (actually, is there a time when she's not pissed?) seems to cause her to malfunction..."

    mc "You're going to be okay here?"

    n "J-Just... go already..."

    show natsuki zorder 1 at thide
    hide natsuki

    "I shrug and stand up. Guess it's really best to leave her alone for the time being."

    return

label poemresponse_2_natsuki_appeal_sayori:
    show natsuki 3c at t11
    n "..."
    show natsuki 3d with dissolve_chr
    n "Well, that's pretty much what I expected from you."

    mc "I don't think there's any hidden compliment there, right?"

    show natsuki 4y with dissolve_chr
    n "Pfff! You wish!"

    mc "Haha..."
    mc "Okay, then. So what exactly did you expect from me?"

    show natsuki 5y with dissolve_chr
    n "Well, for starters, it's pretty bland! It hardly has any message in it."

    mc "Yep, sounds just like me."

    show natsuki 5t with dissolve_chr
    n "But on the other hand, at least you're not over your head."
    show natsuki 5q with dissolve_chr
    n "You didn't try to go all {i}sophisticated{/i} and stuff... like some people..."

    mc "Hmm? What do you mean?"

    show natsuki 4w with dissolve_chr
    n "Never mind!"
    show natsuki 4h with dissolve_chr
    n "The point is, until you get some skill, don't even bother trying to write some {i}real{/i} poetry!"

    mc "Oh? I guess {i}you{/i} can show me how it's done, huh?"

    show natsuki 1e with dissolve_chr
    n "Wha?? Well y-yes I can! Are you doubting my writing skills?!"

    mc "No, but I think that for someone who got as red as a tomato the last time-{w=0.7}{nw}"

    show natsuki 4w with dissolve_chr
    n "Stop quoting Monika, will you? At least have the decency of coming up with something on your own!"

    mc "*sigh*"
    mc "Can I just see your poem already?"

    show natsuki 5s with dissolve_chr
    n "Hmph!"
    return

label poemresponse_2_natsuki_appeal_natsuki:
    show natsuki 3k at t11
    n "..."
    n "D-Did..."
    n "Did somebody tell you..."

    mc "Um... did somebody tell me what?"

    show natsuki 1r with dissolve_chr
    n 1r "D-Doesn't matter!"
    show natsuki 4w with dissolve_chr
    n "And now that I think of it, did you even write it yourself?!"

    mc "Whoa, now that's a pretty harsh accusation, even for you."
    mc "Care to explain what made you so mad?"

    show natsuki 1p with dissolve_chr
    n "I-I'm not mad! What makes you say-{w=0.5}{nw}"

    mc "Natsuki, you're really confusing me right now. I didn't expect my poem to make you act like this."

    show natsuki 2s with dissolve_chr
    n "*sigh*"
    show natsuki 2q with dissolve_chr
    n "Well, it's just... weird..."
    n "I didn't expect you to write anything like this..."

    mc "So... does that mean you actually like it?"

    show natsuki 5w with dissolve_chr
    n 5w "Don't get full of yourself! It's obviously still lacking!"

    show natsuki 5s with dissolve_chr
    "Natsuki starts looking through my poem once again."

    show natsuki 5q with dissolve
    n "This part could be better... and this one is kinda \"meh\" too..."

    show natsuki 5r with dissolve_chr
    "She's starting to get more irritated, as if she's forcing herself to find imperfections in my poem..."
    "...which really shouldn't be hard to do, to be fair."

    show natsuki 2w with dissolve_chr
    n "Well, as I said, it's still far from perfect!"
    show natsuki 2e with dissolve
    n "And I'm still not sure if you wrote it like this on purpose or just by accident!"
    mc "If it makes things easier, I suggest we stick to the latter."
    mc "It actually sounds more plausible. I hardly know what I'm doing at this point..."

    show natsuki 2b with dissolve_chr
    n "Then I suggest you figure it out. The sooner, the better!"
    n "You need to learn how to make a poem brief but also carry a strong message! Short and sweet, you know?"

    "I start snickering."

    mc "{i}Short{/i} and {i}sweet{/i}, huh?"

    show natsuki 4w with dissolve_chr
    n "Dont even start, you wannabe-comedian!"

    "I raise my hands in defeat and show that I zip my mouth."

    show natsuki 3w with dissolve_chr
    n "Anyway, as I was saying..."

    show natsuki 3c with dissolve_chr
    n "Writing poetry isn't just some game! You need to have a clear picture in front of you and a clear, trademark style to your work!"

    mc "I'm pretty sure it's way too early for that."
    mc "But, tell you what? Why don't you show me your poem now? You're obviously the one here who has things figured out."

    show natsuki 3q with dissolve_chr
    n "Well... yeah... I guess you could say that..."
    return

label poemresponse_2_natsuki_appeal_yuri:
    show natsuki 5g at t11
    n "..."
    show natsuki 5w with dissolve_chr
    n "Ughhh... jeez, you too?"

    mc "Ummm, what?"

    show natsuki 5q with dissolve_chr
    n "Why does everyone think that poetry always have to be so complicated?!"

    mc "Um... Natsuki?"

    show natsuki 5r with dissolve_chr
    n "Seriously, it's like no one even understands what it's about! They're all just going for those fancy words, as if it makes the poem good by default!"

    mc "Natsuki!"

    show natsuki 1o with dissolve_chr
    n "What?!"

    mc "You kinda lost me there a few seconds ago. Don't mean to interrupt your rant, but I could use some {i}actual{/i} feedback, you know?"

    show natsuki 3w with dissolve_chr
    n "Ughhh... fine!"
    n "Well, first of all... you don't even have the skill to write things {i}that{/i} way!"

    mc "{i}Which{/i} way, Natsuki?"

    show natsuki 4e with dissolve_chr
    n "Oh, you know... the way people like you overcomplicate stuff, always making it sound so metaphorical and completely confusing the reader!"

    mc "Well, what's the point of making it plain and straightforward? That's hardly poetic in any way."
    mc "I mean, how would it make it any different from a casual chat?"

    show natsuki 4w with dissolve_chr
    n "And {i}there{/i} is that point of view I've been talking about!"
    show natsuki 4e with dissolve_chr
    n "Don't you understand, [player]? It's not about putting up this... \"front...\" It's about the message you're trying to deliver!"
    show natsuki 4b with dissolve_chr
    n "You need to make your point clear and strong, not force the reader to guess what you even had in your mind while writing all this!"
    show natsuki 3q with dissolve_chr
    n "And you need more than just some fancy words to nail that..."

    mc "I... think I get what you mean..."

    show natsuki 5C with dissolve_chr
    n "You'd better... or else you won't appreciate my poems..."

    "She mumbles that last part so I can barely hear what she says."

    mc "Well, we'll never know unless I try, right?"

    show natsuki 5w with dissolve_chr
    n "Yeah, yeah, here you go..."
    return

label poemresponse_2_natsuki_appeal_monika:
    show natsuki 3h at t11
    n "..."
    n "Ughhh... why do you all make things so difficult?"
    mc "Um... going to need some context."

    show natsuki 5h with dissolve_chr
    n "It's just the way you're... overcomplicating things, making it so abstract, so... weird and confusing..."
    show natsuki 5s with dissolve_chr
    n "You're not going completely overboard... {i}thankfully{/i}..."
    show natsuki 5h with dissolve_chr
    n "But I still think it's a very weird starting point! I mean, you {i}are{/i} a complete newbie when it comes to poetry, right?"

    mc "You're sitting in the presence of the walking definition of \"newbie\", Natsuki..."
    mc "As for my poem... well... I honestly don't even know how it turned out the way it did. I was just writing... {i}something...{/i}"

    show natsuki 3g with dissolve_chr
    n  "Well, just so you know, it's very rough around the edges! And that's not surprising, given your skill level..."
    n "That's why I'm telling you that this is a very tough way to start!"
    show natsuki 3h with dissolve_chr
    n "Besides, poetry isn't about making things classy, it's about having a clear message! A simple but deep one!"
    n "People don't read poems to fall asleep trying to figure out what the writer had in mind!"

    mc "Okay, okay, I understand. Keep it simple, fewer words, but more meaning to them. Got it."
    mc "Could you show me your poem now? I'm pretty sure I'll understand you better with a clear example in front of me."

    show natsuki 3s with dissolve_chr
    n "Hmph... okay... guess it's worth a shot..."
    return

# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================
# ======================================================================================================================================================================================================

label poemresponse_2_monika:
    if poemsread == 0:
        "I think I'm going to start with Monika..."
        "First of all, she was the one who came up with this idea, and she looked somewhat eager to seeing my poem in particular."
        "Second, she's the president here. I would even call her some sort of a mentor figure for others."
        "So I hope she won't judge me too hard, especially since it's my first time..."

    show monika 2j at t11
    m "So, [player], ready to share your poem with me?"

    mc "Do I at least get a last wish?"

    show monika 2r with dissolve_chr
    m "*sigh*"
    show monika 4i with dissolve_chr
    m "[player], you should really ease up a little..."
    show monika 4e with dissolve_chr
    m "I mean, you're in the club already. The toughest part is over!"
    show monika 2e with dissolve_chr
    m "Seriously, I didn't expect you to have any problems with fitting in. Everyone seems to like you!"
    show monika 4n with dissolve_chr
    m "Well, okay, Yuri and Natsuki might not look like they're... exactly happy to see you..."
    show monika 4k with dissolve_chr
    m "...but I assure you that they're actually really glad that you're now with us! I saw their smiles yesterday. I know what I'm talking about!"

    mc "So you mean to tell me that you expected a person who never wanted to join any clubs..."
    mc"...to fit right into one just like that? Especially with members like these..."

    show monika 3d with dissolve_chr
    m "Huh? What do you mean?"

    mc "...!"

    "Damn it, I {i}really{/i} shouldn't have said that..."

    mc "W-What are you talking about, Monika?"

    show monika 2a with dissolve_chr
    m "Wait a minute..."
    show monika 5a with dissolve
    m "[player]..."

    "Please... don't..."

    m "That last line of yours..."

    "Don't make me go through this!"

    m "You do understand that there are two ways to interpret it?"
    m "With the first one implying that you don't like it here, because of us..."
    show monika 5b with dissolve_chr
    m "Which, in turn, implies that you don't like {i}us...{/i}"

    "Mercy!"

    show monika 5a with dissolve_chr
    m "While the second..."

    mc "Monika, please!"

    show monika 4k with dissolve
    m "Uh-uh-uh! Now you're in for it, [player]. I won't leave you alone until you spit it all out!"

    mc "Ughhh..."
    mc "{i}Damn my blabbering mouth...{/i}"

    show monika 2j with dissolve_chr
    m "Say it."

    mc "Monika... please..."

    show monika 4j with dissolve_chr
    m "Not until you say it!"

    mc "*sigh*"
    mc "Alright, fine... it's hard for me to fit in right from the start because... this club is full of... girls..."

    show monika 2A with dissolve_chr
    m "...?"

    mc "..."
    mc "...{i}very cute and interesting girls...{/i}"

    show monika 2j with dissolve_chr
    m "That's better!"
    show monika 5a with dissolve
    m "See, it wasn't so hard, right?"

    "I glance around the clubroom. It seems that the others neither saw nor heard what Monika just made me go through, thankfully..."

    mc "Can we... just get back to the poem sharing now?"

    show monika 4j with dissolve
    m "And now you're also eager to share!"
    show monika 2b with dissolve_chr
    m "Now you see that I never do anything without a reason, and encouraging the members of my club to be more open is one of my direct responsibilities..."
    show monika 2k with dissolve_chr
    m "Even if it involves putting them on the spot for a second..."

    "I just hope that you're not going to make me your test subject of sorts..."

    show monika 3a with dissolve
    m "Okay. Now, let's get back to the topic at hand."

    mc "Yeah... my thoughts exactly..."

    "I give Monika my poem, still avoiding eye contact."

    scene bg club_day with wipeleft_scene
    $ renpy.call("poemresponse_2_monika_appeal_{appeal}".format(appeal=poemwinner[0]))

    # REJOIN:
    "Monika hands me her notebook."
    "As I leaf through the pages, I can see her pristine handwriting..."
    "It makes sense: she never settles for second-best. Whenever she does something, it's always going to be top-class."

    call showpoem(poem_m_1)  # "Just Another World"

    show monika 4a with dissolve
    m "So, [player], I think it's time {i}I{/i} get some feedback from {i}you.{/i}"

    mc "Well... I'm no expert, obviously, but I can definitely tell you have skill."

    show monika 2a with dissolve_chr
    m "Can you be a bit more... specific?"

    mc "It really is a beautiful poem -- the style, the meaning, the mood... all of it is so fine-tuned..."
    mc "Mind if I ask you what you had in mind while writing it?"

    show monika 3p with dissolve_chr
    m "It's hard to tell, to be honest... you see, I had a weird dream yesterday..."
    show monika 3D with dissolve_chr
    m "Or wait... was it the day before yesterday?"
    show monika 1r with dissolve_chr
    m "N-Never mind..."
    show monika 3m with dissolve_chr
    m "I can hardly remember what it was about, but it left me wondering..."
    show monika 3e with dissolve_chr
    m "...thinking about our lives and the question \"Are we even in control?\""
    m "Is everything really up to us, as most people say? Or have our fates been predetermined from the very beginning?"

    mc "I get what you're saying. Sometimes I also feel like I'm just some puppet in some stupid play..."

    show monika 2d with dissolve_chr
    m "You do? Hmmm... interesting..."
    mc "And now that you've mentioned it, I also had a weird dream recently... but I'm pretty sure it was just me being extremely tired from midterms..."

    show monika 2k with dissolve_chr
    m "Ahaha! Yeah, yeah, you're definitely right. That does sound plausible. Pretty sure I can relate to that as well."
    mc "Yeah... okay. I guess that's it, right?"

    show monika 2j with dissolve_chr
    m "Yep! Thank you very much for sharing with me, [player]. I really hope you enjoy spending your time here!"
    mc "You really seem worried about this, don't you?"

    show monika 2e with dissolve_chr
    m "But of course I am, [player]! Sayori might have brought you here, but it was I who put the question point-blank and asked you to join us..."
    show monika 4b with dissolve_chr
    m "Besides, it's my responsibility as president to make sure everyone feels comfortable around here!"

    mc "I appreciate that, Monika. And please don't worry. It might seem like I'm having a hard time, but it's actually been a lot of fun so far..."

    show monika 2j with dissolve_chr
    m "It's a relief to hear that. Honestly, I'm {i}very{/i} glad."
    show monika 1b with dissolve_chr
    m "Okay, now I'm afraid I have some work to do, but I'll chat with you later!"
    mc "Sure."

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

    mc "Still not an exactly detailed answer..."

    show monika 3a with dissolve_chr
    m "Well, I might be mistaken, of course. It's only your first attempt, after all. You could've written it that way completely unintentionally..."

    mc "Whoa, I was supposed to have some intentions? To be fair, I was just kinda... writing whatever popped up in my mind and that's all..."

    show monika 1j with dissolve_chr
    m "Once again, just the way I expected..."
    show monika 1a with dissolve_chr
    m "Okay, let me give you some actual feedback. It's a {i}start,{/i} and it's quite a simple one..."
    m "...you decided to play it safe, to utilize something which is at least slightly familiar, without any bold experiments."
    show monika 3j with dissolve_chr
    m "Don't get me wrong. It's not bad. Nobody said that poetry should always have a deep, thought-provoking message or a beautiful, extravagant style..."
    show monika 3a with dissolve_chr
    m "Sometimes, it's the simple things that can end up being the most heartwarming {i}or{/i} heartbreaking..."
    m "And making the reader feel the emotions you had while writing this? It's a huge challenge, actually..."

    mc "..."
    mc "You know, I feel like you're my psychiatrist right now, and you're explaining the problems I didn't even know I had..."

    show monika 2k with dissolve_chr
    m "Ahaha! Well, then I hope you have your insurance because my services aren't cheap, you know?"

    mc "Ahaha... yeah, I got it covered, no worries..."

    show monika 2j with dissolve_chr
    m "Yeah..."
    show monika 2a with dissolve_chr
    m "Okay, we're getting a little distracted here. You've shown me your poem, now it's my turn."

    mc "Go ahead, then. I'm pretty sure that unlike me, you have nothing to embarrassed about..."
    return

label poemresponse_2_monika_appeal_yuri:
    show monika 3c at t11
    m "..."
    show monika 3d with dissolve_chr
    m "A bold choice, [player]..."
    m "Definitely not something I'd expect from someone's first attempt..."

    mc "Context, Monika? My telepathic abilities are still lacking."

    show monika 4k with dissolve_chr
    m "Ahaha, you're so funny, [player]!"

    mc "Ummm... well..."

    show monika 2e with dissolve_chr
    m "Sorry, I was just being sarcastic..."

    mc "H-Hey! Come on, my sense of humour can't be {i}that{/i} bad!"

    show monika 2j with dissolve_chr
    m "I'm {i}still{/i} being sarcastic, [player]."

    mc "..."
    mc "Monika, please, quit it... I feel like a child right now..."

    show monika 4a with dissolve_chr
    m "I'm sorry, but sometimes I just can't help myself."
    show monika 4j with dissolve_chr
    m "When it's you, in particular. Your reactions are way too funny to miss out on!"

    mc "Ughhh... can we go back to the whole poem feedback thing?"

    show monika 2c with dissolve_chr
    m "Right..."
    show monika 3d with dissolve_chr
    m "Well, first of all, as I was saying, you've made quite a bold choice, [player]..."
    m "I understand that you most likely took inspiration from the works of some well-known authors, but trying to write something while keeping this style..."
    show monika 4d with dissolve_chr
    m "...it can be very challenging for a rookie!"

    mc "Still not sure I follow..."

    show monika 4e with dissolve_chr
    m "You see, using metaphors and complex figures of speech takes skill and right now, you're setting yourself a very high standard even if you're certainly not ready to meet it yet."
    show monika 2e with dissolve_chr
    m "Are you sure you don't want to start with something more... simple?"

    mc "Honestly, Monika, I don't have a slightest clue to what I'm even doing..."

    show monika 3j with dissolve_chr
    m "I'm sure you'll figure it out soon enough! And please don't let my words get to you. I never meant to discourage you!"
    show monika 3b with dissolve_chr
    m "We all have our ways, and in case you feel this is the one you should take, go for it! I'm just warning you that it won't be an easy one..."

    mc "Thanks, I'll try my best to make more... conscious choices from now on."

    show monika 2j with dissolve_chr
    m "That's good with me! Okay, now I think it's my turn to share!"

    mc "You're the boss..."
    return

label poemresponse_2_monika_appeal_natsuki:
    show monika 2j at t11
    m "..."
    show monika 2k with dissolve_chr
    m "Awww... now this just adorable!"

    mc "Ahem! Not... quite used to hearing that word when it's about me, you know?"

    show monika 3a with dissolve_chr
    m "Well, I was talking about your poem, rather than you..."
    show monika 5a with dissolve_chr
    m "But you know, now that I think about it..."
    m "I guess that word {i}can{/i} be used to describe you as well, to a certain degree!"

    mc "Monika, enough is enough..."

    show monika 2l with dissolve_chr
    m "Ahahah! S-Sorry, it just never gets old, does it?"

    "I roll my eyes, not wanting to continue that discussion."

    show monika 3a with dissolve_chr
    m "Okay, now let's get back to business..."
    m "The path you chose might seem easy at first, but trust me, it's actually far more complicated than you think."
    show monika 3b with dissolve_chr
    m "Focusing all of your efforts on delivering the message and emotions you have while writing this is challenging on it's own..."
    m "...but if you also sacrifice the style and overall length of the poem... you might leave yourself vulnerable."
    show monika 3d with dissolve_chr
    m "You know, those things usually serve as some sort of distraction, a way to dull people's attention..."
    m "And in case you ignore all of that completely, you'd also risk failing to make the message hit them hard enough..."
    show monika 3n with dissolve_chr
    m "Which has been... exactly the issue here, in that poem of yours..."

    mc "Ahahah! Man, that's a long way of telling someone that their work is subpar."

    show monika 2e with dissolve_chr
    m "My job is not to rub your nose into your mistakes, but rather help you realize them and find a possible way of improving yourself."
    show monika 4j with dissolve_chr
    m "Besides, I never said your poem was bad!"
    m "Rough, unpolished? Yes. But bad?"
    m "No, definitely not. And I'm certain you'll go far!"

    mc "Well... thanks, I guess..."

    show monika 2a with dissolve_chr
    m "Right, now I think it's high time you read my poem, don't you think?"

    mc "Sure, why not?"
    return

label poemresponse_2_monika_appeal_monika:
    show monika 3d at t11
    m "..."
    m "A p-peculiar choice... to say the least..."

    mc "That isn't the way you pronounce \"completely random and unconscious\", Monika."

    show monika 5a with dissolve_chr
    m "Is that so? So you mean to tell me... you had {i}no{/i} idea what you were doing while writing this?"

    mc "Well... p-pretty much, yeah..."

    "Why is she giving me that look?"

    show monika 2j with dissolve_chr
    m "Hmmm, okay, if you say so..."

    mc "..."
    mc "S-So... do I get any feedback or something?"

    show monika 4a with dissolve_chr
    m "Well, for a moment I got a feeling that there's actually something more to it..."
    show monika 2o with dissolve_chr
    m "But then... alas, you've shattered all those hopes in an instant..."

    mc "Um.... hopes? I s-shattered... What are you even talking about?"

    show monika 2k with dissolve_chr
    m "Ahaha! Don't read much into it!"
    show monika 3m with dissolve_chr
    m "Okay, so... about your poem..."
    m "It's... definitely not the thing I expected from you..."
    m "You're raising the bar quite high, right from the start..."
    show monika 4n with dissolve_chr
    m "I'm not saying it's a bad thing, but I'm just worried that if you fail to meet your own expectations, you'll lose your drive and give up on it completely..."

    mc "I would be able to give you a clear answer if I had any clue what you're even on about..."

    show monika 2e with dissolve_chr
    m "You're... how should I put this?"
    m "You're trying your best to maintain the balance, to keep everything beautiful, meaningful and still simple enough to understand, all at the same time..."
    show monika 1m with dissolve_chr
    m "You're trying to make things... {i}perfect{/i}... to satisfy every potential taste..."

    mc "Okaaay... isn't it a good thing?"

    show monika 1l with dissolve_chr
    m "I n-never said it's not! It's just... challenging... especially for a beginner..."

    mc "Well..."

    show monika 1n with dissolve_chr
    m "Yeah..."

    "This is really getting awkward. I think it's the first time I've seen Monika acting like this..."

    mc "So..."

    show monika 3l with dissolve_chr
    m "W-Would you like to see my poem now?"

    mc "Well, sure, I mean... it's your turn now, after all..."
    return
