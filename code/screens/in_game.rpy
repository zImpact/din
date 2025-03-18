screen din_preferences():
    tag menu
    modal True
    
    $ din_bar_null = Frame((din_gui_path + "preferences/" + persistent.timeofday + "/din_bar_null.png"), 36, 36)
    $ din_bar_full = Frame((din_gui_path + "preferences/" + persistent.timeofday + "/din_bar_full.png"), 36, 36)

    window background din_gui_path + "preferences/" + persistent.timeofday + "/preferences_bg.jpg":
        text "Настройки": 
            style "din_settings_link"
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton "Назад": 
            style "din_log_button" 
            text_style "din_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 16 xfill True spacing 15

                text "Режим экрана":
                    style "din_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "Во весь экран": 
                            style "din_log_button"
                            text_style "din_settings_text_" + persistent.timeofday
                            action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "В окне": 
                            style "din_log_button"
                            text_style "din_settings_text_" + persistent.timeofday
                            action Preference("display", "window")

                text "Пропускать":
                    style "din_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "Всё": 
                            style "din_log_button" 
                            text_style "din_settings_text_" + persistent.timeofday
                            action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "Виденное ранее": 
                            style "din_log_button" 
                            text_style "din_settings_text_" + persistent.timeofday
                            action Preference("skip", "seen")

                text "Громкость":
                    style "din_settings_header_" + persistent.timeofday                    
                    xalign 0.5

                grid 2 1 xfill True:
                    textbutton "Музыка": 
                        style "din_log_button"
                        text_style "din_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar:
                        value Preference("music volume")
                        left_bar din_bar_full 
                        right_bar din_bar_null 
                        thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                        hover_thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton "Звуки": 
                        style "din_log_button"
                        text_style "din_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("sound volume") 
                        left_bar din_bar_full 
                        right_bar din_bar_null 
                        thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                        hover_thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36
                        xpos -0.55

                grid 2 1 xfill True:
                    textbutton "Эмбиент": 
                        style "din_log_button"
                        text_style "din_settings_text_" + persistent.timeofday
                        action NullAction()
                        xpos 0.1

                    bar: 
                        value Preference("voice volume") 
                        left_bar din_bar_full 
                        right_bar din_bar_null 
                        thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png"
                        hover_thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                        xmaximum 1.35 
                        ymaximum 36 
                        xpos -0.55

                text "Скорость текста":
                    style "din_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar: 
                    value Preference("text speed") 
                    left_bar din_bar_full 
                    right_bar din_bar_null 
                    thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                    hover_thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text "Автопереход":
                    style "din_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "Включить": 
                            style "din_log_button"
                            text_style "din_settings_text_" + persistent.timeofday
                            action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "Выключить": 
                            style "din_log_button"
                            text_style "din_settings_text_" + persistent.timeofday
                            action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text "Время автоперехода":
                    style "din_settings_header_" + persistent.timeofday
                    xalign 0.5

                bar: 
                    value Preference("auto-forward time") 
                    left_bar din_bar_full 
                    right_bar din_bar_null 
                    thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                    hover_thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_htumb.png" 
                    xalign 0.5 
                    xmaximum 0.8 
                    ymaximum 36

                text "Размер шрифта":
                    style "din_settings_header_" + persistent.timeofday
                    xalign 0.5

                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "Обычный":
                            style "din_log_button"
                            text_style "din_settings_text_" + persistent.timeofday
                            action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add din_gui_path + "preferences/" + persistent.timeofday + "/din_leaf.png" ypos 0.12

                        else:
                            null width 22

                        textbutton "Крупный": 
                            style "din_log_button"
                            text_style "din_settings_text_" + persistent.timeofday
                            action SetField(persistent, "font_size", "large")

            bar: 
                value XScrollValue("preferences") 
                left_bar "images/misc/none.png" 
                right_bar "images/misc/none.png" 
                thumb "images/misc/none.png" 
                hover_thumb "images/misc/none.png"

            vbar: 
                value YScrollValue("preferences") 
                bottom_bar "images/misc/none.png" 
                top_bar "images/misc/none.png" 
                thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_vthumb.png" 
                thumb_offset -12

screen din_save():
    tag menu
    modal True
    
    window background din_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text "Сохранение": 
            style "din_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton "Назад": 
            style "din_log_button" 
            text_style "din_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton "Сохранить": 
            style "din_log_button" 
            text_style "din_settings_link"
            yalign 0.92 
            xalign 0.5 
            action [
                DinFunctionCallback(din_on_save_callback, selected_slot),
                FileSave(selected_slot)
            ]

        textbutton "Удалить": 
            style "din_log_button" 
            text_style "din_settings_link" 
            yalign 0.92 
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "din_save_load_button_" + persistent.timeofday
                        has fixed
                        text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" +FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15
    
screen din_load():
    tag menu
    modal True
    
    window background din_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png":
        text "Загрузка": 
            style "din_settings_link" 
            xalign 0.5 
            yalign 0.08 
            color "#ffffff"

        textbutton "Назад": 
            style "din_log_button" 
            text_style "din_settings_link" 
            xalign 0.015 
            yalign 0.92 
            action Return()

        textbutton "Загрузить": 
            style "din_log_button" 
            text_style "din_settings_link" 
            yalign 0.92 
            xalign 0.5 
            action [
                DinFunctionCallback(din_on_load_callback,selected_slot),
                FileLoad(selected_slot, confirm = False)
            ]
        
        textbutton "Удалить": 
            style "din_log_button" 
            text_style "din_settings_link"
            yalign 0.92
            xalign 0.97 
            action FileDelete(selected_slot)

        grid 4 3 xpos 0.108 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "din_save_load_button_" + persistent.timeofday
                        has fixed
                        text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" + FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15                  
                                
screen din_say(what, who):    
    window background None id "window":
        if persistent.font_size == "large":
            add din_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box_large.png" xpos 174 ypos 866

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/hide_%s.png" 
                xpos 1508 
                ypos 883 
                action HideInterface()

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/save_%s.png"
                xpos 1567
                ypos 883
                action ShowMenu("din_save")

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/menu_%s.png"
                xpos 1625 
                ypos 883 
                action ShowMenu("din_game_menu_selector")

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/load_%s.png"
                xpos 1682 
                ypos 883 
                action ShowMenu("din_load")

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png" 
                xpos 38 
                ypos 924 
                action ShowMenu("din_text_history")

            if not config.skipping:
                imagebutton:
                    auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            else:
                imagebutton: 
                    auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
                    xpos 1768 
                    ypos 924 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 914 
                xmaximum 1541 
                size 30
                line_spacing 1

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 877 
                    size 35 
                    line_spacing 1

        elif persistent.font_size == "small":
            add din_gui_path + "dialogue_box/" + persistent.timeofday + "/dialogue_box.png" xpos 174 ypos 916

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/hide_%s.png"
                xpos 1508
                ypos 933
                action HideInterface()

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday+"/save_%s.png"
                xpos 1567
                ypos 933
                action ShowMenu("din_save")

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday+"/menu_%s.png"
                xpos 1625
                ypos 933
                action ShowMenu("din_game_menu_selector")

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday+"/load_%s.png"
                xpos 1682
                ypos 933
                action ShowMenu("din_load")

            imagebutton:
                auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png" 
                xpos 38 
                ypos 949 
                action ShowMenu("din_text_history")

            if not config.skipping:
                imagebutton:
                    auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            else:
                imagebutton:
                    auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
                    xpos 1768 
                    ypos 949 
                    action Skip()

            text what:
                id "what" 
                xpos 194 
                ypos 964 
                xmaximum 1541 
                size 25
                line_spacing 2

            if who:
                text who:
                    id "who" 
                    xpos 194 
                    ypos 931 
                    size 28 
                    line_spacing 2

screen din_nvl(items, dialogue):
    window background Frame((din_gui_path + "choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox

        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10

                if persistent.font_size == "large":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 39

                    text what:
                        id what_id 
                        size 32

                elif persistent.font_size == "small":
                    if who is not None:
                        text who: 
                            id who_id 
                            size 35

                    text what:
                        id what_id 
                        size 28
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"

                    else:
                        text caption style "nvl_dialogue"

    imagebutton:
        auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/backward_%s.png"
        xpos 38 
        ypos 924
        action ShowMenu("din_text_history")

    if not config.skipping:
        imagebutton:
            auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

    else:
        imagebutton:
            auto din_gui_path + "dialogue_box/" + persistent.timeofday + "/fast_forward_%s.png"
            xpos 1768
            ypos 949
            action Skip()

screen din_game_menu_selector():
    tag menu
    modal True

    if din_lock_quick_menu:
        timer 0.01 action Return()

    else:
        button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

        add din_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_ground.png" xalign 0.5 yalign 0.5

        imagemap:
            auto din_gui_path + "quick_menu/" + persistent.timeofday + "/quick_menu_%s.png" xalign 0.5 yalign 0.5

            hotspot (0, 83, 660, 65) focus_mask None clicked [
                Function(din_set_dynamic_cursor, "main_menu"),
                MainMenu(confirm=False)
            ]

            hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu("din_save")

            hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu("din_load")

            hotspot (0, 278, 660, 65) focus_mask None clicked ShowMenu("din_preferences")

            hotspot (0, 343, 660, 65) focus_mask None action [
                Function(din_screens_diact),
                ShowMenu("main_menu")
            ]    

screen din_quit():
    tag menu
    modal True

    if din_lock_quit:
        timer 0.01 action Return()

    elif din_lock_quit_game_main_menu_var:
        timer 0.01 action Quit(confirm = False)

    else:    
        add din_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
            
        text "Вы действительно \nхотите выйти?":
            font din_link_font
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            
        textbutton "Да":
            style "din_settings_header_main_menu_quit"
            text_style "din_settings_header_main_menu_quit"
            xpos 493
            ypos 600
            action [
                Function(din_screens_diact),
                ShowMenu("main_menu")
            ]
            
        textbutton "Нет":
            style "din_settings_header_main_menu_quit"
            text_style "din_settings_header_main_menu_quit"
            xpos 1230
            ypos 600
            action [
                Hide("din_quit"),
                Return()
            ]

screen din_yesno_prompt(yes_action, message, no_action):
    modal True

    add din_gui_path + "yes_no/" + persistent.timeofday + "/yes_no.png"

    text _(message): 
        text_align 0.5 
        yalign 0.46 
        xalign 0.5

        if persistent.timeofday == "day":
            color "#64483c"

        elif persistent.timeofday == "night":
            color "#161d3d"

        elif persistent.timeofday == "prologue":
            color "#008193"

        elif persistent.timeofday == "sunset":
            color "#5a3525"

        font din_header_font 
        size 30

    textbutton "Да": 
        text_size 60 
        style "din_log_button" 
        text_style "din_settings_link" 
        yalign 0.65 
        xalign 0.3 
        action yes_action

    textbutton "Нет": 
        text_size 60 
        style "din_log_button" 
        text_style "din_settings_link" 
        yalign 0.65 
        xalign 0.7 
        action no_action

screen din_text_history():
    tag menu

    predict False

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "small":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "large":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame(din_gui_path + "choice/" + persistent.timeofday + "/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "din_text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0

            has vbox

            for h in _history_list:
                if h.who:
                    text h.who:
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size

                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what:
                    text_size history_text_size
                    style "din_log_button" 
                    text_style "din_text_history" 
                    xpos 100                    
                    xmaximum xmax

                    if persistent.timeofday == "day":
                        text_hover_color "#40e138"

                    elif persistent.timeofday == "night":
                        text_hover_color "#008193"

                    elif persistent.timeofday == "sunset":
                        text_hover_color "#636840"

                    elif persistent.timeofday == "dungeon":
                        text_hover_color "#636840"
                    
                    action RollbackToIdentifier(h.rollback_identifier)
        
        vbar:
            value YScrollValue("din_text_history_screen")
            bottom_bar "images/misc/none.png"
            top_bar "images/misc/none.png"
            thumb din_gui_path + "preferences/" + persistent.timeofday + "/din_vthumb.png"
            xoffset 1700  

screen din_choice(items):
    modal True
    
    python:
        din_choice_colors_hover = {                        
        "day": "#9dcd55",
        "night": "#3ccfa2",
        "sunset": "#dcd168",
        "dungeon": "#98d8da"
                            }

        din_choice_colors = {
        "day": "#466123",
        "night": "#145644",
        "sunset": "#69652f",
        "dungeon": "#496463"
                            }

        din_choice_colors_selected = {                        
        "day": "#2a3b15",
        "night": "#0b3027",
        "sunset": "#42401e",
        "dungeon": "#2d3d3d"
                            }

    window background Frame(("din/images/gui/choice/" + persistent.timeofday + "/choice_box.png"), 50, 50) xfill True yalign 0.5 left_padding 75 right_padding 75 bottom_padding 50 top_padding 50:
        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:
                button background None:
                    xalign 0.5
                    action action

                    if persistent.licensed:
                        if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right" and caption != "Ir a la izquierda" and caption != "Ir a la derecha":
                            text caption font header_font size 37 hover_size 37 color din_choice_colors_selected[persistent.timeofday] hover_color din_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5

                        else:
                            text caption font header_font size 37 hover_size 37 color din_choice_colors[persistent.timeofday] hover_color din_choice_colors_hover[persistent.timeofday] xcenter 0.5 text_align 0.5

                    else:
                        text caption font header_font size 37 hover_size 37 color din_choice_colors[persistent.timeofday] hover_color din_choice_colors_hover[persistent.timeofday] xalign 0.5

            else:
                if persistent.licensed:
                    text caption font header_font size 60 color din_choice_colors[persistent.timeofday] text_align 0.5 xcenter 0.5

                else:
                    text caption font header_font size 40 color din_choice_colors[persistent.timeofday] xalign 0.5 text_align 0.5 xcenter 0.5

screen din_help():
    tag menu
    modal True
    
    add din_gui_path + "save_load/" + persistent.timeofday + "/load_bg.png"
    
    text "Информация":
        font din_link_font
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2
            
    textbutton "Группа VK":
        style "din_log_button" 
        text_style "din_settings_header_main_menu_quit"
        xalign 0.5
        ypos 350
        action OpenURL("https://vk.com/public176281709")
            
    textbutton "Бессонница":
        style "din_log_button" 
        text_style "din_settings_header_main_menu_quit"
        xalign 0.5
        ypos 500
        action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=1636163628")    
            
    textbutton "Петля времени":
        style "din_log_button" 
        text_style "din_settings_header_main_menu_quit"
        xalign 0.5
        ypos 650
        action OpenURL("https://youtu.be/x2KBAuBKWL8")        
            
    add din_gui_path + "logowhite_hover.png" xpos 1520 ypos 890

    textbutton "Назад": 
        style "din_log_button" 
        text_style "din_settings_link" 
        xalign 0.015 
        yalign 0.92 
        action Return()

screen din_ignore_button():
    key "game_menu" action NullAction()

screen din_titles_overlay():
    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()
        
    key "K_SCROLLOCK":
        action NullAction()
        
    key "mouseup_3":
        action NullAction()
        
    key "mouseup_4":
        action NullAction()
        
    key "K_PAGEUP":
        action NullAction()
    
    key "repeat_K_PAGEUP":
        action NullAction()
    
    key "K_AC_BACK":
        action NullAction()

    key "mouseup_2":
        action NullAction()

    key "h":
        action NullAction()

    key "mouseup_1":
        action NullAction()

    key "K_RETURN":
        action NullAction()

    key "K_SPACE":
        action NullAction()

    key "K_KP_ENTER":
        action NullAction()

    key "K_SELECT":
        action NullAction()

    key "K_LCTRL":
        action NullAction()

    key "K_RCTRL":
        action NullAction() 
        
    key "joy_holdskip":
        action NullAction()

    key "K_TAB":
        action NullAction() 
        
    key "joy_toggleskip":
        action NullAction()

    key ">":
        action NullAction()