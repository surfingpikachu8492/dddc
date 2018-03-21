init python:
    def shorten(string, length, terminator='...'):
        if len(string) <= length:
            return string
        else:
            s = string
            while len(s + terminator) > length:
                s = s[:-1]
            return s + terminator

    def chunk(iterable, length):
        result = []
        for i in range(0, len(iterable), length):
            result.append(iterable[i:i+length])
        return result

image console_bg:
    "#333"
    topleft
    alpha 0.75 size (480,180)

style console_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []


style console_text_console is console_text:
    slow_cps 30

default consolehistory = []
image console_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=30, ypos=10)
image console_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=30, ypos=50)
image console_caret = Text(">", style="console_text", anchor=(0,0), xpos=5, ypos=10)

label updateconsole(text="", history="", delay=0.5, wraplength=35):
    show console_bg zorder 1
    show console_caret zorder 1
    show console_text "_" as ctext zorder 1
    show console_text "[text]" as ctext zorder 1
    $ pause(len(text) / 30.0 + 0.5)
    hide ctext
    show console_text "_" as ctext zorder 1

    $ lines = chunk(history, wraplength)
    while lines:
        python:
            line, lines = lines[0], lines[1:]
            consolehistory.insert(0, line)
            if len(consolehistory) > 5:
                del consolehistory[5:]
            consolehistorydisplay = '\n'.join(str(h).replace('\r\n', '') for h in consolehistory)
            renpy.pause(0.05)
        show console_history "[consolehistorydisplay]" as chistory zorder 1

    $ renpy.pause(delay)
    return

label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)

    return

label updateconsole_old(text="", history=""):
    $ starttime = datetime.datetime.now()
    $ textlength = len(text)
    $ textcount = 0
    show console_bg zorder 1
    show console_caret zorder 1
    show console_text "_" as ctext zorder 1
    label updateconsole_loop:
        $ currenttext = text[:textcount]
        call drawconsole (drawtext=currenttext) from _call_drawconsole
        $ pause_duration = 0.08 - (datetime.datetime.now() - starttime).microseconds / 1000.0 / 1000.0
        $ starttime = datetime.datetime.now()
        if pause_duration > 0:
            $ renpy.pause(pause_duration / 2)
        $ textcount += 1
        if textcount <= textlength:
            jump updateconsole_loop

    pause 0.5
    hide ctext
    show console_text "_" as ctext zorder 1
    call updateconsolehistory (history) from _call_updateconsolehistory_1
    pause 0.5
    return

    label drawconsole(drawtext=""):

        show console_text "[drawtext]_" as ctext zorder 1

        return











label hideconsole:
    hide console_bg
    hide console_caret

    hide ctext
    hide chistory
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
