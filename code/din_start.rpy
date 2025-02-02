init python:
    mods["din_start"] = u"{font=din/images/gui/fonts/AG_Futura Regular.ttf}{size=50}Дни нигде{/font}{/size}"

    try:
        modsImages["din_start"] = ("din/images/gui/misc/din_tabular_list_preview.png", False)

    except:
        pass

label din_start:
    $ din_onload("lock")
    $ din_screens_save_act()
    $ din_set_main_menu_cursor()
    scene bg black with Dissolve(2)
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
    $ persistent.timeofday = "day"
    $ din_set_mode_adv()

    label din_after_intro:
        $ din_onload("unlock")
        stop sound
        $ renpy.transition(Dissolve(2))