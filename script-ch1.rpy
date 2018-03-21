label ch1:
    $ config.skipping = True
    $ config.allow_skipping = True
    $ allow_skipping == True


    window hide(None)
    $ quick_menu = True
    stop music fadeout 2.0
    $ renpy.pause(4.0)
    play music alarm

    $ renpy.pause(2.0)
    "..."
    "...!"
    "...!!"
    mc "!!!"
    play sound "sfx/alarm-hit.ogg"
    stop music

    window show
    $ renpy.pause(2.0)
    mc "Ughh..."
    mc "I hate Mondays..."

    scene bg bedroom with open_eyes
    play music morning

    "I muffle those words into my pillow, before lifting my head slowly."
    "My eyelids protest as I try to open them, letting my eyes see the sunlight permeating into my room."
    "I probably look ridiculous as I grimace from the light."
    "..."
    "I bet I look like a cat right now, woken from its nap..."
    "Because I squint my eyes, yawn eagerly, and I can barely suppress an urge to start hissing spitefully at everyone and everything."
    mc "Uuugh..."

    play sound pillow

    "I let my head hit the pillow, pressing it in as deep as possible..."

    play sound pillow
    mc "Need to..."

    play sound pillow
    mc "...stop..."

    play sound pillow
    mc "...staying..."

    play sound pillow
    mc "...up..."

    play sound pillow
    mc "...late!"

    "I hit my head against the pillow several times."
    "Oddly enough, it eventually helps me to feel at least somewhat awake."

    if persistent.playthrough == 0:
        "...and with it, a strange thought comes to my mind..."
        "Did I even stay up late yesterday?"
        "And if I didn't, then I should have at least gotten enough sleep, right?"
        "Unfortunately, my mind's library appears to still be closed, since I'm unable to even recall the events of last night."

        "It's either me having some weird amnesia, or just being unnaturally sleepy..."

    mc "*yawn*"

    if persistent.playthrough == 0:
        "...must have been the latter after all."

    "Finally, after mustering enough strength, I push myself off from the bed, letting my feet find the floor."

    if persistent.playthrough == 0:
        "...to sit and stare at the window."
        "..."
        "For some reason I feel like I've been doing the exact same thing just recently..."

    mc "School..."

    "While my mind is clearly not in condition to form up any coherent thoughts..."
    "It seems that at least my self-preservation instincts are still functioning, capable of prioritizing my tasks..."

    play sound stand_up

    "I finally let my body stand up, acting purely on instinct, the real \"me\" still laying on the bed, trying to fall back to sleep."
    "I start with my morning routine..."
    "Getting dressed..."
    "Brushing my teeth..."
    "And while I'm, like, 50%% positive that if I were offered to exchange my soul for at least one extra hour of sleep, I would give an enthusiastic “yes”..."
    "Being tired after midterms is clearly not an excuse for skipping classes afterwards..."

    if persistent.playthrough == 0:
        "And besides..."
        "For some reason... I feel like I..."
        "{i}Need{/i} to go there..."
        "..."

    "I'd better get ready fast since I'm already running late..."



    window hide(None)                                   
    scene white with dissolve_cg
    stop music fadeout 2.0
    $ renpy.pause(2.0)

    scene expression "bg/sky_bg.png" with dissolve_cg
    show clouds
    play music t1                                       
    $ renpy.pause(0.5)


    show expression "bg/splash1.png" as msg at truecenter with dissolve_cg

    $ renpy.pause(2.0)


    hide msg with dissolve_cg
    show expression "bg/splash2.png" as msg2 at truecenter with dissolve_cg

    $ renpy.pause(2.0)


    hide msg2 with dissolve_cg
    show expression "gui/logo.png" as logo at truecenter with dissolve_cg

    $ renpy.pause(5.0)


    hide logo with dissolve_cg
    scene white with dissolve_cg

    scene bg residential_day with dissolve_cg
    window auto



    "Despite the fact that I'm already walking down the street, I'm fairly certain my consciousness fell asleep somewhere on the sofa back at home..."
    "And while I'm used to starting my school weeks like this, my tiredness seems to be amplified tenfold this time."

    mc "*yawn*"

    "Well, let's just hope that my inner GPS still works and I don't wander into a completely different part of the city."

    $ s_name = "???"
    s "Hey! [player]!"

    "Wha??"
    "Nooo-no-no-no..."
    "I am in neither the condition nor the mood for any form of socializing..."
    "So, whoever this is..."
    "Please...{w=0.5} just ignore me..."
    "Pretend that I'm some sort of glitch or something..."

    s "[player]!!!"

    "The voice is getting closer. It's starting to sound more irritated..."
    "...and familiar?"

    mc "Oh no..."

    "As I rub my eyes, barely holding myself from letting out yet another yawn, I turn around to meet my annoying pursuer."

    if persistent.playthrough == 0:
        $ renpy.say(narrator, "I see an ann8ying girl rrunning toWard me f--rom the dIIStance, wavi-" + base64encode("nope, we are not rehashing the original script") + "{nw}")
        show screen tear(20, 0.1, 0.1, 1, 40)
        play sound glitch
        $ renpy.pause(0.25)
        stop sound
        hide screen tear

    "Yep, that's definitely her."
    "Your one and only..."

    $ s_name = "Sayori"
    show sayori 4j zorder 2 at t11
    s "Hey, what was {i}that{/i} all about?!"
    show sayori 2j with dissolve_chr
    s "Did you seriously just try to ignore me and walk away?"
    s "...pretending that you didn't hear me?"
    show sayori 6i with dissolve
    s "That is {i}super{/i} mean, [player]!"

    "Her accusing gaze and her hands on her hips don't go well with her otherwise cute appearance and extremely (sometimes even ridiculously) cheerful personality."

    mc "I'm sorry, Sayori, I ju-{w=0.5}{nw}"
    mc "*yawn*"

    show sayori 1g with dissolve_chr
    "As I yawn, Sayori's expression quickly shifts from irritated to concerned."

    show sayori 1h with dissolve_chr
    s "Whoa, did you even sleep last night?"
    show sayori 2j with dissolve_chr
    s "Please don't tell me you stayed up late again just to watch some anime!"

    "...and then it's back to accusations again."

    mc "Wow, look who's talking..."
    show sayori 1h with dissolve_chr
    s "Eh?"

    "Sayori is almost taken aback by my sudden retaliation."

    mc "Sayori, this is the first time in, like, I don't even remember how long..."
    mc "But it's been a {i}while{/i} since we last met each other before school, and would you like to know why?"
    show sayori 1l with dissolve_chr
    s "Eheheh... Well..."
    mc "Because whenever I pass by your house, {i}you're{/i} the one who's still sleeping!"
    mc "Seriously, I can almost hear you snoring. Right here, from the street!"
    show sayori 4p with dissolve_chr
    s "Awww! Okay! Okay!"
    show sayori 5d with dissolve_chr
    s "You win..."

    "She pouts a little and starts twiddling her forefingers."
    "It's her typical gesture whenever she feels embarrassed or guilty..."
    "...or gets busted."

    show sayori 5b zorder 2 with dissolve_chr
    s "I just had a... problem with getting up recently..."
    show sayori 2h with dissolve_chr
    s "A-And that still doesn't get {i}you{/i} off the hook!"
    s "Seriously, you should always get enough sleep! You look like you've been hit by a truck!"

    show sayori 1d at f11
    "She suddenly comes closer and holds me by my wrist, looking into my eyes like a hurt puppy."

    show sayori 1e with dissolve_chr
    s "Please, promise me you won't do it anymore, okay?"

    "I chuckle slightly as I pull back from her and put my hand on my heart."

    mc "Of course, my {i}darling{/i}, whatever you say."
    show sayori 1l at hf11
    s "H-Hey!"
    show sayori at t11
    s "D-Don't call me that..."

    show sayori 1y with dissolve
    "A small blush starts appearing on her face."
    s "You make it sound like we're... a couple or something..."
    "As I turn around and start walking away, I let out another chuckle."
    mc "Pff! Not in a million years..."

    show sayori 3j at h11
    s "Hey!!!"

    "She hits my back with the bottom of her fist."

    s "Now what was {i}that{/i} supposed to mean?!"
    mc "Heheh... Sorry, I guess I'm just a bit grumpy this morning..."

    show sayori 1d with dissolve_chr
    "Sayori catches up, walking (or rather, skipping) right next to me."

    show sayori zorder 1 at thide
    hide sayori
    "We start off a typical, insignificant morning chat, which my mind doesn't even record, keeping up the conversation completely autonomously."
    "Sayori and I have been good friends since we were children. And to be quite honest, I couldn't even imagine befriending her now, if I hadn't already known her for so long."
    "I mean, while I'm just being your stereotypical, unremarkable high-schooler..."
    "...whose interests are limited mostly (if not exclusively) to only the most refined and sophisticated form of media..."
    "...(in other words, video games and anime)..."
    "Sayori, on the other hand is..."
    "Well..."
    "Let's just say that the first thing I would compare her to is the Energizer Bunny, with two huge light bulbs instead of eyes."
    "Even on the most boring and uneventful day, this little girl can remain cheerful, capable of finding joy in the smallest of things."
    "It's quite adorable, contagious even. Not that I mind it..."
    "The point is, with us being almost complete opposites, it's funny that we've managed to even preserve our friendship through so many years..."
    "...let alone care for each other's well being."
    "I guess there {i}are{/i} some things in this world that you just accept the way the are, without looking for some explanation..."



    scene bg school_day with wipeleft_scene

    "I barely notice that we've almost reached the school..."

    show sayori 2j zorder 2 at f11
    s "Helloooo!"
    play sound "sfx/finger_snap2.ogg"
    $ renpy.pause(0.5)
    play sound "sfx/finger_snap.ogg"
    $ renpy.pause(0.5)
    play sound "sfx/finger_snap2.ogg"
    "Huh?"
    "Sayori snaps her fingers in front of my face several times, trying to get my attention."

    mc "Huh? What is it?"

    show sayori 1j at t11
    s "Quit spacing out, will you?"

    mc "S-Sorry, guess I am still- {w=0.5}*yawn*"

    show sayori 4c with dissolve_chr
    s "Oh, come on, you sleepyhead! We're almost at the school!"
    show sayori 4r at h11
    s "Cheer up!"

    "Sayori runs in front of me, twirling as she goes."

    show sayori 1x with dissolve_chr
    s "There is a whole new, sunny day ahead of you! And you get to hang out with people, maybe meet some new friends..."
    s "..."
    show sayori 1b with dissolve_chr
    s "..."
    show sayori 1i with dissolve
    s "..."

    "She slowly falls silent, watching a sour grimace appearing on my face."
    "There is no need for me to even say anything to show how skeptical I am."
    show sayori 6j with dissolve
    s "Jeez, you're getting less and less sociable every year!"
    s "Please don't tell me that you still spend all of your free time playing games!"
    show sayori 6i with dissolve_chr
    s "How can you even live like this?"

    "Sure, go ahead, wound my pride even more..."

    mc "Sayori, I appreciate your concern, but trust me, I'm fine the way I am."
    show sayori 4h with dissolve_chr
    s "Come oooon, [player]! You really need to have something else to brighten up your everyday life!"
    s "You know, something to look forward to whenever you go to school!"

    "Look forward to going to school? Now that's a joke to remember..."

    show sayori 1n with dissolve
    "As I keep myself immersed in my thoughts, Sayori's face suddenly changes as if she's remembered something important."

    s "..."

    show sayori 1o with dissolve
    "Her eyes light up as if she's come to some sort of realization."
    s "By the way, [player]..."

    "For some reason, I find that tone somewhat familiar...{w=0.3} and suspicious..."

    show sayori 2c with dissolve_chr
    s "Have you considered joining a club?"

    "..."
    "Oh, no..."
    "Not this again..."

    mc "Sayori..."
    mc "We've been through this..."
    show sayori 4h with dissolve_chr
    s "Exactly! I'm always trying to convince you to join some club..."
    show sayori 1j with dissolve_chr
    s "And I keep doing so until you say something like..."
    show sayori 1o with dissolve_chr
    s "{i}I'll think about it...{/i}"
    show sayori 1j with dissolve_chr
    s "...and then you do nothing!"
    show sayori 2h with dissolve_chr
    s "And then it keeps happening over and over again!"
    mc "Heh... sounds like a plan to me..."
    show sayori 1e with dissolve_chr
    s "Oh, come oooon! Pleeeease?"

    show sayori at f11
    "She once again comes closer, trying to give me the puppy eyes..."

    show sayori 4e with dissolve_chr
    s "Pretty-pretty please??"

    "Nuh-uh. Not this time around."
    "I put my hand on her head, shielding her eyes, then use my other hand to delicately get her out of my way."

    show sayori 4m at hf11
    s "H-Huh?!"

    "As I pass her, I can barely hold myself from laughing at her stupefied expression."

    show sayori 4p at t11
    $ renpy.say(s, "YOU'RE SUCH A MEANIE, {name}!".format(name=persistent.playername.upper()))

    show sayori zorder 1 at thide
    hide sayori

    "I chuckle to myself and wave her goodbye, without even turning back."
    "I have to admit, I feel kinda bad for alienating her like that, especially considering that she's just trying to help..."
    "But I'm really not in the mood right now..."

    mc "*sigh*"
    mc "Sorry, Sayori, but I'm better off this way..."

    "I adjust the straps of my backpack and finally enter the building."


    stop music fadeout 2.0
    scene bg class_day with wipeleft_scene
    play music t2  

    "I spend most of the school day trying to finally shake off the remnants of my sleepiness."
    "Other than that, it's as ordinary as ever, and it's over before I know it."
    "I wave goodbye to some of my classmates as they leave the classroom."
    "Meanwhile, I'm still sitting at my desk, lazily packing up my things."
    "No matter what I do, Sayori's upset face still haunts me."

    mc "Ughhh..."
    mc "Maybe I should consider joining some club, after all..."

    "I mean, I understand that it's not obligatory..."
    "But the main purpose of those clubs (at least in theory) is to help people sharing the same interests become more social and get involved in something they all enjoy."
    "Alas, I'm definitely not the type of guy suited for any major commitments..."
    "Besides, based on my interests, where would I even go? The Anime Club?"

    mc "Pfff... Yeah, sure..."

    "Despite the fact that it sounds like something right up my alley, I don't think it's such a good idea after all..."

    $ s_name = "???"
    s "Huh? [player]?"

    "...?"

    show sayori 1b zorder 2 at t11
    "My solitude is suddenly interrupted by a familiar, cheerful voice."

    mc "Sayori? What are you doing here?"

    $ s_name = "Sayori"
    show sayori 1c with dissolve_chr
    s "It's funny, I was going to ask you the same thing..."

    mc "Huh? Why would y-{w=0.5}{nw}"
    mc "Oh."

    show sayori 1b with dissolve_chr
    "I realize that I'm the only person left in the classroom."
    "Well... apart from Sayori, that is."

    mc "Yeah, I just kinda spaced out for a moment..."
    mc "But you still haven't answered my question -- why are {i}you{/i} here?"

    show sayori 2c with dissolve_chr
    s "Well, I was planning to catch you coming out of the classroom, but then I saw you just sitting here, and so I came in."
    show sayori 1k with dissolve_chr
    s "You know..."
    s "I kept thinking about our conversation the whole day..."

    mc "Sayori, please..."
    mc "I promise I'll find some time to check out some clubs..."
    mc "Just... n-not now..."

    show sayori 4j with dissolve_chr
    s 4j "Oh, come oooon! That's the exact same excuse you {i}always{/i} give me!"

    "{i}Well, it's been working so far...{/i}"

    show sayori 1x with dissolve_chr
    s "Heeeeey..."
    show sayori 4r with dissolve_chr
    s "I've just got a brilliant idea!"

    "I highly doubt it's even close to being brilliant..."
    "But I guess I have no choice but to hear her out..."

    mc "I'm all ears..."

    show sayori 1l with dissolve_chr
    s "Ehehehe..."
    s "Well..."

    "She's clearly having a hard time telling me what's on her mind, which makes it all look even more suspicious."

    show sayori 1y with dissolve
    s "[player]..."

    "I raise my eyebrow questioningly."

    s "You wouldn't...{w=0.3} want to make a cute girl upset, right??"

    "..."
    "No..."
    "NO! You can't be serious!"
    "You don't get to pull {i}that{/i} trick on me!"

    mc "Seriously, Sayori?"
    mc "You're {i}seriously{/i} trying to get me into {i}your{/i} club just by guilt-tripping me?"

    show sayori 5b with dissolve_chr
    s "Ehehehe..."

    "During our morning chat, I completely forgot that Sayori is the vice president of the Literature Club."
    "To be honest, I can hardly see how Sayori and literature even mix..."
    "But I guess that every club just needs someone as passionate and proactive as her every now and then."
    "Besides, I'm pretty sure the main reason for her being so enthusiastic about it was just the opportunity to help start start a new club."

    show sayori 5a with dissolve_chr
    s "I just thought that it could help you make up your mind..."
    s "And I've already told everyone that I will bring a new member with me..."

    "Huh?"

    show sayori 5b with dissolve_chr
    s "Natsuki even brought her cupcakes, so the timing was perfect..."

    "Wait, WHAT?!"

    mc "Sayori, are you being serious right now?!"

    show sayori at s11
    s "Ehehehe..."

    mc "So after having just {i}one{/i} conversation with me, and without even inviting me to join {i}your{/i} club in particular..."
    mc "You've already told your clubmates that I'd definitely join?!"

    s "Ehehe..."
    show sayori 5a with dissolve_chr
    s "Ummm...{w=0.2} please?"

    "I roll my eyes and bury my face in my hands."

    mc "No..."

    show sayori 1e with dissolve_chr
    s "Pleeeease?"

    "Don't you dare..."

    mc "No, Sayori!"

    show sayori 4e at f11
    s "Pretty-pretty pleeeeeeeeeaaase???"

    "Don'tgivemethepuppyeyesdon'tgivemethepupp-{w=0.2} ahh, she's giving me the puppy eyes..."
    "AGAIN!"
    "THIRD TIME IN A ROW!"
    "She's perfectly aware that it's a dirty trick to use, but that doesn't stop her from constantly using it."

    mc "Sayori, this is just unfair!"
    mc "Besides, you know I hardly have any interest in literature!"

    show sayori 3r at t11
    s "Oh, don't worry, it's much easier to get into than you think, trust me!"
    show sayori 1x with dissolve_chr
    s "What {i}is{/i} important, however, is that you get to hang out with us!"
    show sayori 4r with dissolve_chr
    s "We'll make you feel right at home!"

    mc "Ughhhh..."

    scene black with close_eyes

    "I cover my face with my hands for a few seconds, hoping that this annoying girl will simply vanish if I stop looking at her."
    "..."

    scene bg class_day with open_eyes
    show sayori 1b at t11


    "Nope, she's still there..."
    mc "*sigh*"
    mc "{i}Fine{/i}..."
    mc "I'll do it...."


    show sayori 4r at hf11
    s "YAY!"

    "Sayori suddenly hugs me, almost making me fall from my chair."

    show sayori 4s with dissolve_chr
    s "Thank you, thank you, thank you!"

    "I want to say that I'm only stopping by, and that I have no intention of actually joining her club..."
    "But... I just don't have the guts to say that out loud."
    "I realize that it's been quite a while since I last got to hang out with Sayori."
    "For the past few months, we've almost never even seen each other."
    "Yet there once was a time when we used to walk to school together every morning."
    "Or just wander around, trying to kill time..."
    "Man, we even had sleepovers..."
    "At her place, mostly, since an airhead like herself would usually keep her house a complete mess and she'd constantly rely on my help."
    "And that's where my caring personality comes in handy..."
    "Even if it {i}is{/i} buried deep below layers upon layers of cynicism."
    "..."
    "Well, guess there's no use in denying that I... missed her."
    "I let out a chuckle and finally hug her back."

    mc "Okay, okay..."
    mc "If it makes you happy, I'll give it a try..."

    show sayori 1a at t11
    "She lets go of me, and then takes my hand, eager to lead the way."

    show sayori 2x with dissolve_chr
    s 2x "Come on, then! You won't be disappointed, I promise!"
    s "You'll get along with everyone just fine! And you'll also like our room, and our president..."

    s "And-{w=0.3}{nw}"
    show sayori 4n with dissolve_chr
    s "OOOOOOOH!{w=0.7}{nw}"
    show sayori 4x with dissolve_chr
    s "Did I tell you about the cupcakes?!"

    mc "Ummm, yes, you mentioned them... Something about the perfect timing..."

    show sayori 4r with dissolve_chr
    s "They are to {i}die{/i} for! Seriously! Natsuki is {i}super{/i} good at baking!"
    show sayori 1x with dissolve_chr
    s "You're lucky that she decided to bring them today!"

    show sayori 1a at d11
    "As I stand up, Sayori grabs my backpack and hands it to me."

    show sayori 1r with dissolve_chr
    s 1r "Come on! I can't wait!"

    show sayori zorder 1 at thide
    hide sayori
    "Almost skipping with joy, she leads me out of the classroom."
    "Well, as long as I get a free snack, I guess it's not a complete waste of my time..."



    scene bg corridor with wipeleft_scene

    "As we leave the classroom, one of my classmates, Kenji, notices us."
    show kenji p1 at t11

    k "Oh, hey, [player]! You're still here?"

    "To be fair, having that weirdo as my company isn't exactly my cup of tea."
    "Despite being in the same class, we almost never talk. I always found him to be a person...{w=0.5} {i}not of this world{/i}...{w=0.5} I can't put my finger on why..."
    "It might be his looks... {w=0.5}or his behavior... {w=0.5}or both, I don't know."

    mc "Yeah, sort of. I'm just being taken to an eternal servitude in some club..."

    show sayori 3j at t21
    show kenji at t22
    s "[player], stop it!"
    show kenji p3 with dissolve_chr
    k "Ahahah! Really? And what cl-{w=0.7}{nw}"
    show kenji p2 with dissolve_chr
    k "Wait a minute..."

    "He turns his head to Sayori, obviously remembering her from somewhere."

    k "You're from the Literature Club, aren't you?"
    show sayori 1a with dissolve_chr

    "Sayori's face lights up as he mentions her club."

    show sayori 1x at f21
    show kenji at t22
    s "Yeah! I'm the vice president, actually!"
    show sayori 4x with dissolve_chr
    s "Would you like to join? We are always happy to see new faces!"

    show kenji p3 with dissolve_chr
    k "Nah, I... think I'll pass on that one, thanks."
    show sayori 1k at t21
    s "Awwww..."
    show kenji p4 with dissolve_chr
    k "Either way, I've gotta go! Rest in peace, [player]!"
    mc "Yeah, sure. When they ask for my epitaph, tell them to write something like... I don't know..."
    mc "{i}Here lies [player], who sold his soul for a cupcake.{/i}"
    show sayori 1j with dissolve_chr
    show kenji at t22
    s "[player]!"
    show sayori
    show kenji p5 with dissolve_chr
    k "Hah! Will do! See ya later, pal!"
    mc "Later."

    show kenji zorder 1 at thide
    hide kenji
    $ renpy.pause(0.5)
    show sayori 1i at t11
    "Finally leaving Kenji behind, I dejectedly follow Sayori, still hoping to myself that the ordeal I'm about to go through will be over before it starts to get dangerous."
    show sayori zorder 1 at thide
    hide sayori
    "{i}Remember: get in, get the cupcake, and get out before Sayori gets a chance to sink her puppy teeth into you...{i}"

    stop music fadeout 7.0
    scene bg corridor with wipeleft_scene

    "I can barely keep up with Sayori, who is clearly far more enthusiastic about this whole situation."
    "I follow her across the school and upstairs, to the section of the school that is generally used for third-year classes and activities."
    "Eventually, she leads me to a door of yet another completely unremarkable classroom."

    show sayori 1x at t11
    s "We're here!"
    show sayori 4r at h11
    s "Come on in, I can't wait!"

    show sayori zorder 1 at thide
    hide sayori

    play sound closet_open


    if persistent.playthrough == 0:
        "As she swings open the classroom door, I feel some fleeting and extremely weird feeling."
        "A feeling of..."
        "{i}Déjà vu...{/i}"
        "..."
        "Still oblivious to the reason of {i}why{/i} all of it feels so familiar, I follow Sayori into the clubroom."
    else:
        "Sayori swings open the classroom door with such enthusiasm as if she's entering a candy store."
        "She leaves it wide open, though, and I guess that implies that I have to follow her."

        mc "*sigh*"
        mc "Well..."
        mc "Cupcakes, here I come..."

    scene bg club_day with wipeleft_scene
    play music t3  

    show sayori 4r at l31
    s "Hey, everyone! I'd like you all to meet [player], our newest member!"
    mc "What?!"
    mc "Sayori, I'm only..."
    mc "...?"

    show sayori zorder 1 at thide
    hide sayori
    "I fall silent as I take a glance around the room."

    $ y_name = "Girl 1"
    show yuri 2t at t11
    y "Oh... I-It's a pleasure meeting you."

    "The first member I see is a tall girl with long purple hair, sitting at a desk near the window."
    "She appears to have been reading a book, and by looking at her behaviour, I can clearly see that she's not entirely comfortable with me being here."

    show yuri 2A at t33
    $ n_name = "Girl 2"
    n "*pant* *pant*"
    n "Seriously, Sayori?"

    "That other voice comes from a closet in the far corner of the room."
    "And soon enough, I get to see its source, and she's visibly annoyed."
    show natsuki 4g at t32
    "She has short pink hair, and her equally short and small figure makes me think she's probably a first year."
    show natsuki 4b with dissolve_chr
    n "You know, when you said you were going to bring a new member, I certainly didn't expect you to bring your boyfriend!"

    show natsuki at t32
    show sayori 1l at t31

    s "H-Hey! I never said he was my boyfriend!"
    show natsuki 5e with dissolve_chr
    n "Oh, so it's just some random boy, then? Great! Way to ruin the atmosphere, Sayori!"
    "The atmosphere...?"
    "..."
    "Wait..."
    "Does that imply that the members of this club..."
    "Are {i}all{/i} girls?"

    $ m_name = "???"
    m "[player]?"

    show sayori 1b with dissolve_chr
    show natsuki 5k with dissolve_chr
    show yuri 2B with dissolve_chr
    mc "...?"

    "Okay, now {i}that's{/i} a voice I didn't expect to hear."
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide natsuki
    hide yuri
    "But as I turn to the teacher's desk, my assumptions are confirmed."

    $ m_name = "Monika"
    show monika 2b at t11
    m "Oh my gosh, I did not expect it to be you!"
    show monika 2k with dissolve_chr
    m 2k "What a nice surprise!"

    "Yep, that's definitely her..."
    "Monika, probably one of the most popular girls in the entire school."

    mc "H-Hi there, Monika. I can say that I'm quite surprised as well."

    show sayori 2c at t21
    show monika 2a at t22

    s "Whoa, you two know each other?"
    mc "Yeah, we... were kinda in the same class some time ago."
    mc "We didn't get to talk much, though..."
    show monika 1n with dissolve_chr
    m 1n "Yeah... that's true..."

    "Monika looks away, almost apologetically."

    show monika 1m with dissolve_chr
    show sayori 1b with dissolve_chr
    "To be honest, it feels a bit awkward to talk to her even now."
    "We almost never talked, despite being in the same class."




    "Ever since the day she transferred here, Monika started climbing the popularity ranks rapidly, gaining favor among both the teachers and the other students."
    "Her confidence, charisma and trademark smile quickly earned her certain recognition."
    "Add her intelligence, good looks, and athletic ability into the mix, and you'll get the full picture."
    "..."
    "...a picture of a girl, who is completely out of my league; hence our scarce communication."

    show monika 4k with dissolve_chr
    m "But I guess that's about to change, now that you're here!"

    show monika 2a with dissolve_chr
    "Monika gives me the sweetest smile I've ever seen, making me feel even more uncomfortable."

    show sayori 3x with dissolve_chr
    s "Well, I see there's no need to introduce you to our president, then."

    show monika zorder 1 at thide
    hide monika
    show sayori 2q at t31

    s "Buuuuut..."

    "Sayori grabs my arm and turns me around to face the two girls I didn't recognize."

    show natsuki 2A at t32
    show yuri 4C at t33

    "...who are already standing right in front of me."
    "...I can also hear Monika behind me, standing up from the teacher desk."

    mc "*gulp*"

    "I'm standing in the middle of the classroom, surrounded by four..."
    show sayori 1a with dissolve_chr
    "{i}Incredibly...{/i}"
    show natsuki 5i with dissolve_chr
    "{i}Cute...{/i}"
    show yuri 4D with dissolve_chr
    "{i}Girls!{/i}"

    show sayori 1q at f31
    s "So, everyone, this is a good friend of mine, [player]!"
    show sayori 2x with dissolve_chr
    s "[player], I would like you to meet our dear Natsuki, always full of energy!"

    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    $ n_name = "Natsuki"
    show natsuki 5t2 at t32
    n "Hmph!"

    "Ah, so {i}that's{/i} Natsuki, the one who supposedly brought some cupcakes today, according to Sayori..."
    "She's quite short, and that's coming from a guy who's...{w=0.3} not exactly towering, himself."
    "And I'm pretty sure she's the youngest here as well, though I could be wrong."
    "Looks can be deceiving, after all..."

    mc "Nice to meet you."

    show natsuki 5A with dissolve_chr
    "Natsuki looks at me with a distrusting expression for a few seconds."
    "The way she's staring makes me think she's trying to analyze me."
    show natsuki 5B with dissolve_chr
    "She eventually looks away, barely muttering her response."
    n "Likewise."


    show sayori 1q at f31
    "Sayori leans closer to me before whispering in my ear."

    s "Just ignore her when she gets all moody, okay?"

    show sayori 1q at t31
    "I may have known Natsuki for just a few minutes, but her sour attitude is something you can't help but notice."
    "Though it seems quite jarring against her outwardly cute appearance..."
    "I have to admit, it's hard to keep myself from smiling when I look at her pouting like this."
    "Heh..."
    "I guess there's far more to her than she lets on..."

    show natsuki zorder 1 at thide
    hide natsuki

    show sayori 3x with dissolve_chr
    s "And, of course, Yuri, the smartest in our club!"

    $ y_name = "Yuri"
    show sayori zorder 1 at thide
    hide sayori
    show yuri 4C at t32
    y "D-Don't say things like that..."


    "Yuri, on the other hand, seems to be the complete opposite of Natsuki (and in stark contrast with Sayori, for that matter)..."
    "She appears to be quite shy and more mature, compared to the others."
    "And to be honest, she is, by far, the only one who I could easily imagine being a member of the Literature Club."
    "Even after taking just a small glance at her, I can tell that she's a real bookworm."
    "And I don't think you need a degree in psychology to figure that out."
    "As for her looks..."
    "Well..."

    show yuri 4D with dissolve_chr
    "Let's just say when I call her \"mature,\" I mean it on... {i}many{/i} levels..."

    mc "My pleasure..."

    "I try my best to say it with a straight face and not look at any of them in particular."

    show sayori 1a at t31
    show natsuki 2A at t32
    show yuri 2u at t33

    y "S-So, [player]..."

    "Yuri seems to have calmed down, a shy smile appearing on her face."

    show yuri 2s with dissolve_chr
    y "What made you consider joining the Literature Club?"

    "Oops..."
    "Yuri, while I appreciate you taking a more straightforward approach, you've managed to step on a landmine right off the bat..."

    mc "Y-Yeah... About that..."
    mc "I d-don't mean to be a killjoy, but I kinda..."

    show sayori 1g with dissolve_chr
    show natsuki 1c with dissolve_chr
    show yuri 2f with dissolve_chr

    "I glance at Sayori, who is getting more upset with every second."

    show sayori 1k with dissolve_chr
    s "[player]..."

    mc "I'm kinda just... stopping by... Nothing more..."

    mc "Sayori really wanted me to try joining some club, but I... never made any actual decision..."
    show yuri 3v with dissolve_chr
    y "O-Oh... Um... I see..."
    show natsuki 5x with dissolve_chr
    n "Pfff..."
    show natsuki 5w with dissolve_chr
    n "Told you about killing the atmosphere..."

    mc "{i}Plus I was in the mood for some cupcakes...{/i}"
    show natsuki 5C with dissolve_chr
    "I say that under my breath. Luckily, none of them seems to have heard it."
    "I lower my eyes, feeling as if I had just confessed to some heinous crime."
    "..."
    "Wait a minute, why should I even feel guilty? I was literally dragged here by Sayori!"
    "It was never my intention to join any club in the first place!"
    "But just by looking at the upset faces of these girls..."
    "..."
    "This is {i}not{/i} good."
    "I really can't make any clear-headed decisions in a situation like this..."

    show monika 4l zorder 3 at f41
    show sayori 1b zorder 2 at t42
    show natsuki 5c zorder 2 at t43
    show yuri 3e zorder 2 at t44

    m "Well, anyway, let's not get distracted!"
    show monika 4b with dissolve_chr
    m "We have a guest after all, so the least we can do is to make him feel at home, right everyone?"

    "Monika is obviously trying to lighten the mood, which isn't surprising."
    "She's the president, after all. She should be used to dealing with situations like these."

    show sayori 1o zorder 3 at f42
    show monika 2a at t41
    s "Oh, wait! I almost forgot!"
    show sayori 4x with dissolve_chr
    s "[player], I promised you some cupcakes, right?"
    show sayori 1x zorder 2 at t42
    show natsuki 1p zorder 3 at f43
    n "E-Eh?!"
    n "Hey, I didn't make them just for some random-{w=0.7}{nw}"
    show yuri 2l zorder 3 at f44
    show natsuki 1p zorder 2 at t43
    y "Natsuki..."
    show yuri 1k with dissolve_chr
    y "You're really not helping us make a good first impression."
    show sayori 1a with dissolve_chr
    show natsuki 1r zorder 3 at f43
    show yuri 1k zorder 2 at t44
    n "...!"
    show natsuki 5s with dissolve_chr
    n "*sigh*"
    show natsuki 5u with dissolve_chr
    n "Yeah, yeah, I know..."
    n "I'll... go grab them, then..."
    show natsuki zorder 2 at t43
    show yuri 1c zorder 3 at f44
    y "And I'll make some tea, if everyone's okay with that."
    show yuri at t44
    show monika 1b at f41
    m "That'd be great! Meanwhile, we'll organize the desks."

    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    $ renpy.pause(0.25)
    show monika 1a at t21
    show sayori 1a at t22

    "Em, define \"we\"..."

    show sayori 2x with dissolve_chr
    "Yeah! Come on, [player], we can arrange the desks to form a table, so that everyone can take a seat!"

    show sayori zorder 1 at thide
    hide sayori
    $ renpy.pause(0.25)
    show monika 1j at t11
    "Before I'm even able to say anything, I feel a pair of hands grabbing my shoulders from behind."

    show monika 1k with dissolve_chr
    m "We could really use some help with that."

    show monika 1a with dissolve_chr
    "With that said, Monika starts pushing me forward."
    show monika 5a with dissolve
    "As we go, I feel her leaning slightly closer to my ear, her voice almost turning into a whisper."
    m "A gentleman like yourself wouldn't possibly want to make four beautiful girls any {i}more{/i} upset, right?"

    "Out of the corner of my eye, I see Monika's expression becoming more flirtatious, her emerald eyes almost drilling into me."
    "With every minute I spend here, I lose more of my ability to think clearly..."



    scene bg club_day with wipeleft_scene

    "Shortly after, we form a table with enough space for all of us."
    show yuri 1a at t11
    "I see Yuri coming back, carrying a tray with a kettle and several cups."

    mc "Do you keep a whole tea set here?"
    show yuri 1c with dissolve_chr
    y "Mhm."

    "Yuri smiles sweetly."

    y "It took some time to convince the teachers, but they allowed us to keep it in the clubroom."

    show sayori 3x at t21
    show yuri 1a at t22

    s "Yeah! Thankfully we have Monika as our president, so we basically have all the teaching staff on our side, no matter what!"

    show yuri 2u with dissolve_chr
    y "I agree, we couldn't have asked for a better president."

    show monika 1l at t31
    show sayori 1x at t32
    show yuri 2u at t33

    m "Ahahah..."

    m "Please, girls, you're embarrassing me..."

    show yuri 1a with dissolve_chr
    show sayori 1a with dissolve_chr

    "Monika getting embarrassed? Now that's something you don't see every day..."

    show monika 1m with dissolve_chr
    "As Yuri sets everything on the table, I take a seat between Monika and Sayori."
    "I instinctively move my chair a bit closer to Sayori, though, since she is the one I feel most comfortable being around."

    show monika zorder 2 at t41
    show sayori zorder 2 at t42
    show natsuki 3z zorder 3 at f43
    show yuri zorder 2 at t44

    "As I raise my eyes, I see Natsuki, proudly marching back to the table. In her hands is a tray covered with tin foil."

    n "Okay... everybody ready?"
    show natsuki 3l with dissolve_chr
    n "...Ta-daa!"

    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."

    show monika 1d with dissolve_chr
    show sayori 1n with dissolve_chr
    show yuri 2e with dissolve_chr

    "Their whiskers are drawn with icing, and little pieces of chocolate were used to make the ears."

    show sayori 1c zorder 3 at f42
    show natsuki zorder 2 at t43
    s "Uwooooah!"
    show sayori 4r at hf42
    s "They're soooo cuuuuute!"

    show monika 1a with dissolve_chr
    show natsuki 1j with dissolve_chr
    show yuri 1m with dissolve_chr

    if persistent.playthrough == 0:
        "For some reason I feel like I've {i}seen{/i} them somewhere before..."
        "..."
        "...must've been in a recipe or an advertisement somewhere online, most likely..."

    show monika 2b zorder 3 at f41
    show sayori 1a zorder 2 at t42
    m "Wow, I knew you were good at baking, Natsuki, but I never expected something on this scale!"
    show monika zorder 2 at t41
    show natsuki 3t zorder 3 at f43
    n "Ehehe. Well, the more you know..."
    show natsuki 3l with dissolve_chr
    n 3l "Don't just sit there. Grab one already!"

    show natsuki zorder 2 at t43
    show monika 1a zorder 2 with dissolve_chr
    show sayori 1r zorder 3 at d42
    show yuri 1a with dissolve_chr

    "You don't have to tell Sayori twice..."
    "She grabs one and takes a huge bite."

    show sayori 1q with dissolve_chr
    s "Shhooo goooood!"

    show natsuki 3a with dissolve_chr

    "Without even chewing it all down, she starts talking, her voice muffled, and some icing already smudged over her nose."

    show monika 1j at d41
    $ renpy.pause(0.25)
    show yuri 1m at d44
    "Monika takes one cupcake for herself, and Yuri follows."
    "I finally take one as well and start turning it around in my fingers, looking for the best angle to take a bite."

    show natsuki 3k with dissolve_chr

    "Natsuki is the only one who still hasn't touched the cupcakes, and I can see her sneaking glances in my direction."
    "Is she waiting for me to try it?"
    "After finally finding an angle I'm satisfied with, I take a bite."
    "..."
    "The icing is sweet and full of flavor."
    "Whether she made them herself or had some help, it's still really impressive!"

    mc "This is really delicious."
    mc "Thank you, Natsuki."
    show monika 1a with dissolve_chr
    show natsuki 4p zorder 3 at f43
    n "W-Why are you thanking me? It's not like I..."

    show natsuki 5q with dissolve
    n "...made them just for you or anything!"

    show natsuki at t43
    show sayori 1a with dissolve_chr

    if persistent.playthrough == 0:
        "I swear I've heard that somewhere before..."
    else:
        "Yeah, sure, whatever."

    "I decide to ignore her and just enjoy my cupcake."

    show yuri 1i with dissolve_chr

    "Meanwhile, Yuri has finished pouring tea into four cups and begins carefully placing them in front of everyone."

    show natsuki zorder 2
    show yuri 1k zorder 3 at f44
    y "So, [player], what do you usually like to read?"
    mc "..."

    "I hoped that we could avoid topics like that, since I've just recently said that I am not joining their club."
    "But I guess I can't blame them for hoping that I'll change my decision."

    mc "Well... um..."

    "Besides, considering how little I've read these past few years, I don't really have a good way of answering that."

    mc "Manga..."

    "I mutter quietly to myself, half-joking."

    show yuri zorder 2
    show natsuki 5c zorder 3 with dissolve_chr
    "Natsuki's head suddenly perks up."

    show natsuki 5B with dissolve_chr
    "My words clearly piqued her interest, but she keeps quiet."

    show natsuki zorder 2
    show yuri 2u zorder 3 with dissolve_chr
    y 2u "N-Not much of a reader, I guess..."

    "Yuri, on the other hand, obviously had some higher expectations."

    show natsuki 1p zorder 3 at f43
    show yuri zorder 2 at t44
    n "H-Hey! Don't say that like it's a bad thing or something!"
    show natsuki zorder 2 at t43
    show yuri 1f zorder 3 at f44
    y "Oh?"
    show yuri 3q with dissolve_chr
    y "Ah, uhm, s-sorry... I didn't mean it that way..."

    show yuri zorder 2 at t44
    show monika 1j at f41
    "Monika leans to me, half-whispering."

    m "Natsuki keeps her entire manga collection in the clubroom..."

    show yuri 3A with dissolve_chr
    show monika zorder 2 at t41
    show natsuki 1p zorder 2 at s43
    n 1o "...!"

    show sayori 1q at f42

    "Sayori lets out a giggle, snorting in her teacup."

    show sayori 1r zorder 3 with dissolve_chr
    s "Yeah, she's always saying that it's literature as well!"
    show sayori zorder 2 at t42
    show yuri 3e with dissolve_chr
    show natsuki 1x zorder 3 at f43
    n "Gnnnn!!"

    "Now you did it, Sayori..."

    show natsuki 4v at hf43
    n "Manga IS literature!!!"

    show sayori 1r with dissolve_chr
    show monika 1k with dissolve_chr
    show yuri 3d with dissolve_chr

    "We all laugh, unable to keep it together while looking at Natsuki's quickly reddening face."



    stop music fadeout 4.0
    scene bg club_day with wipeleft_scene
    play music t8  

    "With the atmosphere finally getting less tense, we spend the next few minutes just chatting and drinking tea."
    "Natsuki's cupcakes fade away with alarming speed."

    show monika 2b at t32
    m "So, [player], I take it that you're enjoying your stay here so far?"

    "I reach out to grab the last cupcake from the tray."

    mc "Well, I'd be lying if I said I wasn't."

    show monika 2j with dissolve_chr
    "I mean, what sane guy would say no to that question?"
    "And besides, those sweet smiles that answer earns from Monika, Yuri, Sayori, and even Natsuki are definitely worth it."

    mc "By the way, Monika, I wanted to ask you..."
    show monika 2c with dissolve_chr
    mc "How come you decided to start your own club?"
    mc "You could easily be a board member for any of the major clubs."
    mc "Actually, weren't you a leader of the debate club last year?"

    show monika 2C with dissolve_chr
    "Monika smiles and takes a sip of tea."

    show monika 2B with dissolve_chr
    m "I knew you would bring it up sooner or later..."
    show monika 4B with dissolve_chr
    m "You see, to be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    show monika 2b with dissolve_chr
    m "I'd much rather take something I personally enjoy and make something special out of it."
    show monika 1k with dissolve_chr
    m "And if it encourages others to get into literature, then I'm fulfilling that dream!"

    show yuri 3m at t33
    y "That is indeed an admirable cause."
    show yuri at t33
    show sayori 4x at t31

    s "And that's why we're here to help you with it!"

    show sayori 1a with dissolve_chr
    show monika 1m with dissolve_chr
    show yuri 3a with dissolve_chr
    "The girls are clearly fond of Monika. Nothing surprising about that, to be honest."
    "After all, she always succeeds, regardless of what she decides to take on."
    "What's not to admire about that?"

    mc "I'm actually surprised there aren't more people in the club yet..."

    show monika 2A with dissolve_chr

    "Monika's expression changes. A smirk appears on her face and she raises her eyebrow teasingly."
    "..."
    "Damn it."
    "I shouldn't have said that..."
    "Now I've cornered myself..."
    show monika 2j with dissolve_chr
    "Meanwhile, Monika continues, pretending that she didn't notice my little slip-up there."

    show monika 4b at f32
    m "Well, you see, not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it comes to something that doesn't grab your attention, like literature."
    show monika 2b with dissolve_chr
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    show monika 2k with dissolve_chr
    m "So I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    show monika at t32
    show sayori 4r at hf31
    s "Yeah!"
    show sayori at t31
    show yuri 2c at f33
    y "We'll do our best."

    show sayori 4x zorder 2 at t41
    show monika 2k zorder 2 at t42
    show natsuki 3z zorder 3 at f43
    show yuri 2c zorder 2 at t44

    n "You know it!"
    show natsuki 3z at t43

    show sayori 1a with dissolve_chr
    show monika 2B with dissolve_chr
    show natsuki 3a with dissolve_chr
    show yuri 2a with dissolve_chr
    "Such different girls, all interested in the same goal..."
    "Monika must have worked really hard just to find these three."
    "Maybe that's why they were all so delighted by the idea of a new member joining."
    "Though I still don't know if I can keep up with their level of enthusiasm about literature..."
    show sayori zorder 1 at thide
    hide sayori

    show monika zorder 1 at thide
    hide monika

    show natsuki zorder 1 at thide
    hide natsuki

    show yuri zorder 1 at thide
    hide yuri


    if persistent.playthrough == 0:
        "However..."
        "There is one thing that's particularly bugging me..."
        "Sayori is the only one of these girls I really know..."
        "I mean, I've hardly ever talked to Monika and I've only just met Yuri and Natsuki today..."
        "But for some reason, I can't help but feel like I've known them {i}all{/i} for a while."
        "..."
        "I should probably quit spacing out and try to keep up the conversation, otherwise they'll think I'm getting bored."
    else:
        "Hmmm..."
        "But maybe it's really not that big of a deal, after all..."
        "I mean, Sayori's a member. And I don't recall {i}her{/i} being fond of literature either."
        "Hell, she's the vice president, for crying out loud. So me becoming a member, even if I have close to no interest in literature..."
        "..."
        "Wait, am I actually considering this?"
        "I'm telling you, there's got to be something in that tea...{w=0.5} or those cupcakes..."
        "Some sort of drug that makes people more willing to join their club."
        "Although, with members like these, I don't think they need to try that hard to grab someone's attention."
        "..."
        "At least as long as that \"someone\" is a single guy like me..."
        "At any rate, I should probably quit spacing out and try to keep up the conversation, otherwise they'll think I'm getting bored."

    show yuri 1c at t11

    mc "So, Yuri, what do you like to read?"

    show yuri 3n at h11
    y "H-Huh?!"
    show yuri 3o with dissolve_chr
    y "Um, m-me?"

    "Man, could you have possibly picked someone even {i}more{/i} difficult to talk to?"
    "While she is trying her best to act natural, she's obviously still not used to having me around."

    y "W-Well, I suppose there's no simple answer to that question..."

    show yuri 3q with dissolve_chr
    y "But perhaps the best way to describe my preferences is something that is truly... {i}immersive{/i}."
    show yuri 2j with dissolve_chr
    y "I really love it when the book acts like a guide, taking you on a journey, making you feel like you're actually entering that beautifully described world, so different from our own..."
    show yuri 2l with dissolve_chr
    y "...helping you to get involved into the story, relate to its characters, allowing you to experience all that this new world has to offer..."

    "I don't know what I find more interesting, listening to Yuri's little speech or just watching that seemingly timid girl speaking with such confidence in her voice all of the sudden."
    "I have to admit, I've never met someone so passionate about literature in my life."
    "As she goes on, I look back into my memory, trying my best to find at least something I can relate to."

    mc "I'm impressed, Yuri. You truly make it sound so interesting."

    show yuri 4b with dissolve_chr
    "Yuri stops in her tracks, blushing a little."

    y "I'm... glad you feel that way..."
    mc "To be honest, the only thing I can remember that got me so immersed was a horror novel I had read... a really long time ago."
    show yuri 2f with dissolve
    y "Oh? Really?"

    "Surprisingly enough, my words seem to pique Yuri's interest."

    show yuri 2g with dissolve_chr
    y "I've actually been reading a lot of different horror stories as well..."

    "Okay... that was unexpected..."

    show yuri 3p at h11
    y "N-Not that I am f-fond of horror! It's just that..."
    show yuri 3o with dissolve_chr
    y "You see, stories with deep psychological elements is something I particularly enjoy."
    show yuri 2v with dissolve_chr
    y "They make you feel all those emotions that characters have to experience... Their shock, their anxiety..."
    show yuri 1w with dissolve_chr
    y 1w "...and quite often, these stories can even make you ponder about your own ideology, changing the way you look at the world."

    show monika 3d at t21
    show yuri 1w at t22

    m "Honestly, I would never have expected that from you, Yuri."
    show monika 1d with dissolve_chr
    show yuri 1A with dissolve_chr
    m "For someone as gentle as you..."
    show monika 1e with dissolve
    m "To take interest in something so... unique."

    show yuri 3q with dissolve_chr
    y "W-Well, I guess we all have our own little demons inside us..."

    show natsuki 3q at t31
    show monika at t32
    show yuri 3q at t33

    n "Ugh, I hate horror..."
    show yuri 2f with dissolve_chr
    show monika 1a with dissolve_chr
    y "Oh? Why's that?"
    show natsuki 3s with dissolve_chr
    n "Well, I just..."

    show natsuki 3n with dissolve_chr
    "Natsuki's eyes dart over to me for a split second."

    show natsuki 5s with dissolve_chr
    n "Never mind."

    show natsuki at t31
    show monika 4k at f32
    m "That's right, you usually like to write about cute things, don't you, Natsuki?"

    show monika at t32
    show natsuki 1o at f31
    n "W-What?!"
    show yuri 1m with dissolve_chr
    show natsuki 4o with dissolve_chr
    n "What gives you that idea?!"

    show natsuki at t31
    show monika 2j at f32
    m "You left a piece of scrap paper behind last club meeting."

    show natsuki 1r at s31
    n "Mmmm!!!"

    show monika 3b with dissolve_chr
    m "It looked like you were working on a poem called-{w=0.5}{nw}"

    show natsuki 1p at hf31
    show monika at t32
    n "Don't say it out loud!"
    n "And give it back!"

    show monika 1l with dissolve_chr
    m "Fine, fine~"

    show natsuki 5s with dissolve_chr
    "Natsuki snatches the sheet of paper from Monika's hands."

    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    $ renpy.pause(0.5)
    show sayori 1q zorder 3 at t31
    show natsuki zorder 2 at t32
    s "Ehehe, your cupcakes, your poems..."
    show sayori 4r at h31
    s "Everything you do is just as cute as you are~"

    show sayori 4q zorder 1 at t42
    "Sayori sidles up behind Natsuki and puts her hands on her shoulders, almost hugging her."
    show natsuki 1x with dissolve_chr
    n "Grrr!"

    show natsuki 1v at h32
    $ renpy.pause(0.25)
    show natsuki 1v at h32
    n "I'm not cute!!!"

    "Are you sure about that?"

    mc "Natsuki, you write your own poems?"

    show sayori zorder 1 at thide
    hide sayori

    show natsuki 3m at t11
    n "Eh? Well, yeah... sometimes."
    show natsuki 4h with dissolve_chr
    n "Why do you care?"
    mc "I... think that's really impressive."
    mc "Why don't you share them sometime?"
    show natsuki 1o at h11
    n 1o "N-No!"

    show natsuki 5r with dissolve_chr
    "Natsuki averts her eyes."

    show natsuki 5s with dissolve
    n "You wouldn't... like them..."
    mc "Ah... not a very confident writer yet?"

    show natsuki 5s at t21
    show yuri 2t at t22

    y "I can understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    show natsuki 5u with dissolve_chr
    show yuri 2w with dissolve_chr
    y "The truest form of writing is writing to oneself."
    show natsuki 5n with dissolve_chr
    show yuri 1l with dissolve_chr
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."

    show natsuki at t31
    show yuri at t32
    show monika 1a at t33

    m "I take it that you have some writing experience too, Yuri?"
    show monika 3b with dissolve_chr
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri 3o at s32
    y "U-Ummm..."
    mc "I guess it's the same for Yuri..."

    show sayori 4h zorder 3 at t41
    show natsuki at t42
    show yuri at t43
    show monika 1c at t44

    s "Aww... But I wanted to read everyone's poems..."

    "We all sit in silence for a moment until it's broken by Monika snapping her fingers."
    play sound "sfx/finger_snap2.ogg"

    show sayori at t41
    show monika 4k zorder 3 at hf44
    m "Okay!"
    m "I have an idea, everyone!"

    show sayori 1b with dissolve_chr
    show natsuki 1c with dissolve_chr
    show yuri 1e at t43

    "All of us look at her quizzically."
    show monika 4b with dissolve_chr
    m "Let's all go home and write a poem of our own!"
    show monika 2b with dissolve_chr
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"

    "The reaction follows shortly after."
    show monika zorder 2 at t44
    show natsuki 1p zorder 3 at f42
    n "What?!"
    show natsuki zorder 2 at t42
    show yuri 3o zorder 3 at f43
    y "U-Um..."

    show yuri zorder 2 at t43
    show sayori 4r zorder 3 at f41
    s 4r "Yay! Let's do it!"


    show sayori zorder 2 at t41
    show monika 3b zorder 3 at f44
    m "Besides, since we have a new member now, I think it'll help us all get a little more comfortable with each other, and strengthen the bond of our club."

    "...?!"

    mc "Ahem..."
    mc "Umm, Monika?"

    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    show monika 7r with dissolve_chr
    $ renpy.pause(0.5)

    show monika at t11
    "Monika rolls her eyes and lets out a sigh, turning to me."

    "There's no malevolence on her face, but she definitely looks annoyed by my stubbornness."

    show monika 7C with dissolve_chr
    m "[player]..."

    "Well, here it goes..."

    m "I know it's all a bit overwhelming, and you never intended to do this..."
    show monika 7n with dissolve_chr
    m "...and that Sayori bit off more than she could chew, telling us that you would definitely join..."

    show sayori 1l zorder 2 at l31
    s "Ehehe~"

    show sayori zorder 1 at lhide
    hide sayori

    show monika 3e with dissolve_chr
    m "But I would like to be straightforward with you and ask you this one question..."

    show monika 1C with dissolve
    "She takes a short pause, inhaling before saying the words I knew she would say sooner or later..."

    show monika 1j with dissolve_chr
    m "Would you like to join the Literature Club?"
    mc "..."

    "I can't remember the last time I'd been so conflicted."

    show monika zorder 1 at thide
    hide monika

    "On one hand, it's just like Monika said. I never intended to come here in the first place..."
    "But on the other..."
    "I take a look at those four beautiful girls, surrounding me..."
    "They all stare at me, their eyes full of hope, the corners of their mouth slowly moving downwards with each passing second..."

    show sayori 1d at t41
    "Sayori, the good childhood friend of mine, a little lump of sunshine in this grey, boring world..."

    show natsuki 5n at t42
    "Natsuki, a cute, fragile girl, hidden beneath that harsh exterior..."

    show yuri 3t at t43
    "Yuri, a maiden of mystery, covering her true self behind that timid facade..."

    show monika 2e at t44
    "And Monika, a girl who had always impressed me and who is now giving me the most genuine smile, hoping to hear \"yes\" for an answer..."

    "..."
    "What was that about making clear-headed decisions?"
    "Ah, who cares? Being logical is overrated..."

    mc "Okay."

    show sayori 1c with dissolve_chr
    show natsuki 5k with dissolve_chr
    show yuri 3f with dissolve_chr
    show monika 2d with dissolve_chr
    "One by one, the girls' eyes light up."

    mc "I won't lie. I really enjoyed spending time with you all, and..."
    mc "...while I still can't believe I'm saying this, I've made a decision."

    show sayori 4t at s41
    "Sayori is almost ready to explode at this point."

    mc "I'll join the Literature Club!"

    "With that said, I brace myself for impact."

    show sayori 4s at hf41
    $ renpy.pause(0.3)
    show sayori 4s at hf41
    s "Yaaaaaaay! I'm so happyyyy~"

    "Sayori wraps her arms around me, jumping up and down."

    mc "H-Hey, easy there..."

    show sayori 1q at t41
    show natsuki zorder 2
    show monika zorder 2
    show yuri 1u zorder 3 at f43
    y "I was honestly worried that you would just... leave at the end..."

    show monika zorder 2
    show yuri zorder 2 at t43
    show natsuki 3h zorder 3 at f42
    n "Yeah! If you really came here just for the cupcakes, I would be super pissed!"

    show yuri zorder 2
    show natsuki zorder 2 at t42
    show monika 2e zorder 3 at f44
    m "I'm so glad that you've finally made up your mind."
    show monika 2k with dissolve_chr
    m 2k "And... I guess that makes it official!"

    show sayori zorder 1 at thide
    hide sayori

    show natsuki zorder 1 at thide
    hide natsuki

    show yuri zorder 1 at thide
    hide yuri

    show monika 2j at t11
    m "[player]."



    "Monika reaches out her hand for a handshake."

    show monika 2b with dissolve_chr

    m "Welcome to the Literature Club!"

    "I smile and delicately shake her hand."

    show monika zorder 1 at thide
    hide monika


    if persistent.playthrough == 0:
        "I still can't get rid of the feeling that everyone and everything here seems so familiar."
        "Maybe it's just a hint to me that this is where I belong."
        "Honestly, it doesn't matter."
        "I've made up my mind."
        "And I'm ready for whatever the future has in store for me."
    else:
        "That might be my weirdest decision in my entire life."
        "But honestly, I don't care."
        "My life has been a mess for quite a while at this point."
        "No actual friends, no particular plans or dreams..."
        "Every single day is already a chore."
        "But here...{w=0.3} I have a feeling that I might even achieve something new."
        "And let's be honest..."
        "Who could possibly reject an opportunity of spending so much time with these adorable girls?"
        "So in case all it takes for me is to just give literature a try..."
        "...I'm okay with it."



    show monika 2b at t11
    m "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    show monika 4b with dissolve_chr
    m "Everyone remember tonight's assignment!"
    m "Write a poem to bring to the next meeting, so we can all share!"

    "Monika looks over at me once more."

    show monika 5a with dissolve_chr
    m "That's especially important in your case, [player]! I'm really looking forward to see how you express yourself."

    "I chuckle as I jokingly salute her."

    mc "Yes, ma'am."

    show monika 2j with dissolve_chr
    "Monika smiles sweetly and heads towards the teacher's desk."

    show monika zorder 1 at thide
    hide monika

    "Soon, the girls have cleaned up all the tableware and packed up their things, ready to leave."

    show sayori 2x at t11
    s "Hey, [player], since we're already here, do you want to walk home together?"
    mc "Sure, why not? It's been a while since we last did it, after all."
    show sayori 1y with dissolve_chr
    s "Yeah, it really has..."



    scene bg residential_day with wipeleft_scene

    "Today was a complete surprise for me."
    "A very good one, to be honest."
    "I'm still unsure if it was all just some weird dream."
    "But it doesn't matter."
    "Right now, I'm happy how things have turned out."
    "And I'm ready for whatever I'll have to face."

    if persistent.playthrough == 0:
        "Because this time..."
        "{i}I'll set things right.{/i}"
        "..."
        "What am I even on about?"

    show sayori 2i at t11
    s "Helloooooo?"
    mc "Huh?"
    show sayori 1j with dissolve_chr
    s 1j "Oh, come on, don't tell me you're spacing out again!"
    s "[player], promise me that you'll get enough sleep tonight, okay?"
    mc "I will."
    mc "Seriously, Sayori, you worry about me too much."

    show sayori 1d with dissolve_chr
    s "Well, who else would worry about you, if not your best friend?"

    "I smile back, unable to find any good way to answer that question."
    "It's only a matter of minutes before we reach Sayori's house."

    show sayori 1q with dissolve_chr
    s "Ahhh... I'm so glad you joined us, [player]!"
    show sayori 4r with dissolve_chr
    s "I still can't wrap my mind around it, I'm just so happy!"
    mc "Yeah, I'm still making sense of it myself, to be honest..."
    show sayori 2x with dissolve_chr
    s "Don't worry! I promise you won't regret it!"
    s "Now, go home and get some sleep! I'd like to walk to school with you again tomorrow morning!"
    show sayori 1a with dissolve_chr
    s "And I don't want you to be all sleepy and grumpy again..."
    mc "Hahah... Noted."
    show sayori 4c at h11
    s "Oh! But before you go to sleep, don't forget to write your poem today!"
    show sayori 1c with dissolve_chr
    s 1c "It's really important, and we'll all be upset if you just forgot about it..."

    show sayori 7a with dissolve_chr
    "She pouts falsely, looking me straight in the eyes."

    s "You wouldn't want to make us upset, right?"

    mc "Don't worry, I'll do my best, I promise."

    show sayori 1x with dissolve_chr
    s "Great!"
    s "Well, I'll see you tomorrow, then!"
    show sayori 1r with dissolve_chr
    s "Have a good night!"
    mc "Night."

    show sayori zorder 1 at thide
    hide sayori
    "As I walk away, I see Sayori skipping to her house."
    "..."
    "Yes."
    "It was indeed a good day."

    stop music fadeout 10.0
    scene bg bedroom with wipeleft_scene

    "The first thing I do when I enter my room is happily throw my backpack somewhere in my bed's direction."
    mc "Ughhh... It's finally over..."
    "..."
    "Oh, who am I kidding, {i}it{/i} has only just begun..."
    "Yet another school week, yet another term..."
    "And {i}now{/i} I'm also a member of a club to boot!"
    mc "I can't believe Sayori managed to talk me into this..."
    "As I lay on my bed, staring blankly into the ceiling, I keep thinking on what I could possibly write about."
    "I really have {i}zero{/i} experience when it comes to poetry, so where should I even start?"
    "Oh well, I guess the best option is to just try actually {i}writing{/i} something..."
    "It certainly sounds better than just laying around, doing nothing..."
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
