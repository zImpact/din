screen din_main_menu():
    tag menu
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "din_main_menu_" + din_current_time() + "_anim"

    if din_main_menu_var:
        add "din_main_menu_frame":
            xalign 0.5
            yalign 0.5

        text "Дни нигде":
            size 135
            font din_main_menu_font
            text_align 0.5
            xalign 0.5
            yalign 0.045
            antialias True
            kerning 2

        add "din_main_menu_underline":
            xalign 0.5
            ypos 191

        $ din_start_button_text = "Выбрать историю" if persistent.din_flags["din_intro_completed"] else "Начать игру"

        textbutton "[din_start_button_text]" at din_buttons_atl():
            style "din_main_menu_style"
            text_style "din_main_menu_style"
            xalign 0.5
            ypos 300

            if persistent.din_flags["din_intro_completed"]:
                action [
                    Hide("din_main_menu"),
                    ShowMenu("din_story_choice",
                    _transition=fade)
                ]

            else:
                action [
                    Hide("din_main_menu", Dissolve(1.5)),
                    Start("din_intro")
                ]

        textbutton "[DIN_LOAD_TEXT]" at din_buttons_atl():
            style "din_main_menu_style"
            text_style "din_main_menu_style"
            xalign 0.5
            ypos 433
            action [
                SetVariable("din_main_menu_var", False),
                ShowMenu("din_load_main_menu")
            ]

        textbutton "[DIN_EXTRA_TEXT]" at din_buttons_atl():
            style "din_main_menu_style"
            text_style "din_main_menu_style"
            xalign 0.5
            ypos 556
            action [
                SetVariable("din_main_menu_var", False),
                ShowMenu("din_extra")
            ]

        textbutton "[DIN_PREFERENCES_TEXT]" at din_buttons_atl():
            style "din_main_menu_style"
            text_style "din_main_menu_style"
            xalign 0.5
            ypos 680
            action [
                SetVariable("din_main_menu_var", False),
                ShowMenu("din_preferences_main_menu")
            ]

        textbutton "Выход" at din_buttons_atl():
            style "din_main_menu_style"
            text_style "din_main_menu_style"
            xalign 0.5
            ypos 803
            action [
                SetVariable("din_main_menu_var", False),
                ShowMenu("din_quit_main_menu")
            ]

        imagebutton:
            auto DIN_GUI_PATH + "misc/logowhite_%s.png"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")

screen din_story_choice():
    tag menu
    modal True

    add DIN_GUI_PATH + "main_menu/stories_all_closed.png"

    imagebutton:
        auto DIN_GUI_PATH + "main_menu/ikarus_story_%s.png"
        focus_mask True
        action [
            Hide("din_story_choice", Dissolve(1.5)),
            Start("din_ikarus_story")
        ]

    if persistent.din_flags["din_ikarus_story_completed"]:
        imagebutton:
            auto DIN_GUI_PATH + "main_menu/winterlong_story_%s.png"
            focus_mask True
            xpos 470
            action [
                Hide("din_story_choice", Dissolve(1.5)),
                Start("din_winterlong_story")
            ]

    if persistent.din_flags["din_winterlong_story_completed"]:
        imagebutton:
            auto DIN_GUI_PATH + "main_menu/rolegame_story_%s.png" 
            focus_mask True
            xpos 980
            action [
                Hide("din_story_choice", Dissolve(1.5)),
                Start("din_rolegame_story")
            ]

    if persistent.din_flags["din_rolegame_story_completed"]:
        imagebutton:
            auto DIN_GUI_PATH + "main_menu/lost_peace_story_%s.png"
            focus_mask True
            xpos 1405
            action [
                Hide("din_story_choice", Dissolve(1.5)),
                Start("din_lost_peace_story")
            ]

    add DIN_GUI_PATH + "main_menu/stories_borders.png"

    imagebutton:
        auto DIN_GUI_PATH + "main_menu/back_%s.png"
        xpos 1800
        ypos 1000
        action [
            Hide("din_story_choice"),
            ShowMenu("din_main_menu", _transition=fade)
        ]

screen din_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not din_main_menu_var: 
        add "din_main_menu_options_frame":
            xalign 0.5
            yalign 0.5
        
        text "[DIN_EXTRA_TEXT]":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "Музыка":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.3
            action [
                Hide("din_extra"),
                ShowMenu("din_music_room")
            ]

        textbutton "Галерея":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.5
            action [
                Hide("din_extra"),
                ShowMenu("din_background_gallery")
            ]

        textbutton "Персонажи":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.7
            action [
                Hide("din_extra"),
                ShowMenu("din_characters")
            ]

        textbutton "[DIN_RETURN_TEXT]":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [
                SetVariable("din_main_menu_var", True),
                Hide("din_extra"), 
                ShowMenu("din_main_menu")
            ]

screen din_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not din_main_menu_var:
        add "din_main_menu_options_frame":
            xalign 0.5
            yalign 0.5
        
        text "[DIN_LOADING_TEXT]":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "[DIN_RETURN_TEXT]":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [
                SetVariable("din_main_menu_var", True),
                Hide("din_load_main_menu"), 
                ShowMenu("din_main_menu")
            ]
                    
        textbutton "Загрузить игру":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.5
            ypos 970
            action [
                DinFunctionCallback(din_on_load_callback, selected_slot),
                FileLoad(selected_slot, confirm=False)
            ]
                 
        textbutton "[DIN_DELETE_TEXT]":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.9
            ypos 970
            action FileDelete(selected_slot, confirm=False)
            
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "din_save_load_button_main_menu"

                        fixed:
                            text "%s." % i + FileTime(i, format=DIN_SAVE_LOAD_FORMAT, empty=DIN_SAVE_LOAD_EMPTY_LABEL) + "\n" + FileSaveName(i):
                                style "din_text_save_load_main_menu"
                                xpos 15
                                ypos 15

screen din_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not din_main_menu_var:
        add "din_main_menu_options_frame":
            xalign 0.5
            yalign 0.5
        
        text "[DIN_PREFERENCES_TEXT]":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        text "[DIN_DISPLAY_PREFERENCES_TEXT]":
            font din_header_font
            size 60
            xalign 0.5
            ypos 200
            
        textbutton "[DIN_DISPLAY_PREFERENCES_FULLSCREEN_TEXT]":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")
            
        textbutton "[DIN_DISPLAY_PREFERENCES_WINDOW_TEXT]":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 280

            if not _preferences.fullscreen:
                text_style "din_settings_header_main_menu_preferences_inverse"

            else:
                text_style "din_settings_header_main_menu_preferences"

            action Preference("display", "window")

        text "[DIN_FONT_SIZE_PREFERENCES_TEXT]":
            font din_header_font
            size 60
            xalign 0.5
            ypos 360
                
        textbutton "[DIN_FONT_SIZE_PREFERENCES_SMALL_TEXT]":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton "[DIN_FONT_SIZE_PREFERENCES_LARGE_TEXT]":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "[DIN_SKIP_PREFERENCES_TEXT]":
            font din_header_font
            size 60
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton "[DIN_SKIP_PREFERENCES_SEEN_TEXT]":
                style "din_button_none"
                text_style "din_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "[DIN_SKIP_PREFERENCES_ALL_TEXT]":
                style "din_button_none"
                text_style "din_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton "[DIN_SKIP_PREFERENCES_SEEN_TEXT]":
                style "din_button_none"
                text_style "din_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "[DIN_SKIP_PREFERENCES_ALL_TEXT]":
                style "din_button_none"
                text_style "din_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")    
            
        text "Громкость музыки":
            font din_header_font
            size 60
            xpos 430
            ypos 820

        bar:
            value Preference("music volume")
            right_bar DIN_GUI_PATH + "preferences/main_menu/bar_null.png"
            left_bar DIN_GUI_PATH + "preferences/main_menu/bar_full.png"
            thumb DIN_GUI_PATH + "preferences/main_menu/htumb.png"
            xpos 975
            ypos 813
            xmaximum 400
            ymaximum 85

        textbutton "[DIN_RETURN_TEXT]":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [
                SetVariable("din_main_menu_var", True),
                Hide("din_preferences_main_menu"),
                ShowMenu("din_main_menu")
            ]
    
screen din_quit_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not din_main_menu_var:
        add "din_main_menu_options_frame":
            xalign 0.5
            yalign 0.5
        
        text "Вы действительно хотите выйти?":
            font din_main_menu_font
            size 80
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            
        textbutton "[DIN_YES_TEXT]":
            style "din_settings_header_main_menu_quit"
            text_style "din_settings_header_main_menu_quit"
            xpos 493
            ypos 600
            action [
                Hide("din_quit_main_menu"),
                Function(din_screens_diact),
                ShowMenu("main_menu")
            ]
            
        textbutton "[DIN_NO_TEXT]":
            style "din_settings_header_main_menu_quit"
            text_style "din_settings_header_main_menu_quit"
            xpos 1230
            ypos 600
            action [
                SetVariable("din_main_menu_var", True),
                Hide("din_quit_main_menu"),
                ShowMenu("din_main_menu")
            ]