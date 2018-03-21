init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3
        
        @property
        def num_words(self):
            replaced = self.text.replace("\n", " ").replace("-", "")
            words = [word for word in replaced.split(" ") if word]
            return len(words)
        
        def read(self, character):
            for line in self.text.split("\n"):
                if line:
                    renpy.say(character, "{i}" + line + "{/i}")


    poem_m_1 = Poem(author="monika", title="Just Another World", text="""\
Life that idles
Swiftly floats into the abyss,
The dark abyss known as stagnation.
Within it, life decays, bringing but pain and sorrow.
It tears through us, in a slow, endless torment,
Through the mind, body, and soul.

Life that storms
Leaves a scar,
The one that scarred another world.
The air of this new world flows through us -
A breeze that brings purpose and satisfaction
Through the mind, body, and soul.

We long for a revelation,
An answer we shall bring ourselves to accept.
The reality between us and the world we dream of -
None of it is real.
This world isn't ours -
Only our lives are.

Our world is just another world.""")

    poem_m_2 = Poem(author="monika", title="Quaver", text="""\
Half a beat.
One-and
       Two-and
              Three-and
                       Four.

Or a beat itself.
One-two-three
             Four-five-six.

The same, yet different.
Both in form and feel.

Listen to the music
Synthesizing your emotions.
Let yourself explore.

Each genre is a note, each note with its place in the piece
Transpose it up or down,
But that experience never falls flat.""")

    poem_y_1 = Poem(author="yuri", title="Fading Light", text="""\
The setting sun’s amber stream casts now elongated shadows.
Paying it no mind, I lose myself in the expansive worlds beside me,
No - inside me, now, as I explore them.

The light’s hue changes from yellow to orange to black to white,
The only indication of passing time,
Imperceptible at first.

But it is only as that hue fades back again
That I make any observation.

I must now return to exploring my own.""")

    poem_y_2 = Poem(author="yuri", title="Aurora", text="""\
Far from everything she finds herself,
A lone, hooded figure traversing the open tundra,
An outcast, desperate to stay warm.
The harsh winds of winter strike at her frame –
Behind little shelter she cowers, almost whimpering.
It is little wonder her path is nearly bare of travel.

She perseveres, placing one foot forward, mechanically,
The burdens she carries, neglected by others, ignored at last.
The vibrant blurs of green and pink dare her to look at the once-dark sky above.
The harsh winds of winter match not the wild flare of solar winds.
With these brilliant colors from a conflict born,
It is great wonder her path is nearly bare of travel.""")

    poem_n_1 = Poem(author="natsuki", title="{color=#FF1493}Not Your Cupcakes!{/color}", text="""\
{color=#FF1493}I like baking cupcakes,
Mixing the batter...
Watching them in the oven...
Making the frosting…
Decorating...
They look so good!

I like when people want my cupcakes,
It makes me feel quite proud.
But when people try to take them
And don’t pay me any mind,
It makes me feel like they don’t care,
So I won’t share - They’re mine!{/color}""")

    poem_n_2 = Poem(author="natsuki", title="The Fox", text="""\
The lion was proud
And its prey feared its strength.
The birds hid in fear.
The rabbits hid in fear.
The zebras hid in fear.
But the fox didn’t hide.
The fox ran.
The lion chased.
The fox and lion ran around a corner.
And the lion fell in a trap.
And the fox didn’t need to run anymore.""")

    poem_s_1 = Poem(author="sayori", title="A Day on the Ice", text="""\
I stand out in the rink, a giant ring of ice,
Bundled up in my favorite coat and hat.
I'm kinda scared that I'll fall and get hurt,
So I’m gonna stay close to the wall.

I skate --
Around and around,
Around and around.

I decide to move away from the wall,
Still a little afraid I'll fall down.

...I fall down.

I'm fine: My coat softens the blow.
I get up again and dust myself off
And start off towards the end of the rink.

Left foot, right foot, left foot, right.
I laugh as I skate around.
My fear left me long ago.

I'm almost sad when it's time to go home,
I wish I could stay forever.
But I can come back another day.

And besides...

I'm cold.
I want hot chocolate.""")

    poem_s_2 = Poem(author="sayori", title="It's Just a Little Raincloud", text="""\
It's a beautiful day --
The sun is shining bright,
The birds are singing,
The breeze blows through the trees.

It's a lazy day --
I sit in the park, barefoot in the grass,
Leaning against the trunk of a large oak tree.
I watch the patterns in the white cotton clouds.

This one looks like a dolphin,
This one's a feather,
This one's a smiling face,
This is a heart.

But that dark gray one might ruin my game,
I'd have to go back inside.
No more watching clouds.

But, hey, it's just a little raincloud.
It's the only one.
And even if it rains today,
There'll be puddles to jump in tomorrow.""")

image paper = "images/bg/poem.jpg"
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "images/bg/poem-glitch1.png"
image paper_glitch2:
    "images/bg/poem-glitch2.png"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat


transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            if currentpoem.yuri_2:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.yuri_3:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
            else:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
        elif currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        elif currentpoem.author == "natsuki":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
        elif currentpoem.author == "monika":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"



style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700





style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style yuri_text_2:
    font "gui/font/y2.ttf"
    size 40
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return
    play sound page_turn
    if music:
        $ currentpos = get_pos()
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "gui/poem_dismiss.png" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
