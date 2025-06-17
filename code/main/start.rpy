init python:
    mods["din_start"] = u"{font=din/images/gui/fonts/AG_Futura Regular.ttf}{size=50}Дни нигде{/font}{/size}"

    try:
        modsImages["din_start"] = (DIN_GUI_PATH + "misc/tabular_list_preview.png", False)

    except:
        pass

label din_start:
    $ din_set_dynamic_cursor("null")
    $ renpy.pause(3, hard=True)
    $ din_onload("lock")
    $ din_screens_save_act()
    $ din_set_dynamic_cursor("main_menu")
    $ din_set_time("day")
    $ renpy.scene()
    $ renpy.show("din_ext_camp_entrance_" + din_current_time())
    show din_intro_frame at truecenter
    show din_intro_logo at truecenter
    show din_blank_skip
    with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    play sound din_intro_sample
    $ renpy.pause(8, hard=True)
    scene bg black with Dissolve(2)
    $ renpy.pause(2, hard=True)

    label din_after_intro:
        $ din_onload("unlock")
        stop sound
        $ renpy.transition(Dissolve(2))
