label end_demo:
    stop music fadeout 2.0
    scene black with dissolve_cg
    "End of demo"
call endgame from _call_endgame
scene black with dissolve_cg
label end_demo_loop:
    $ persistent.autoload = "end_demo_loop"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen dialog(message="You have finished the Demo. Please wait for the Public Release!", ok_action=Quit(confirm=False))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
