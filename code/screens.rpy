init python:
    din_g = Gallery()
    din_page = 0
    din_g.transition = fade
    din_g.locked_button = din_gui_path + "save_load/main_menu/thumbnail_idle.png"
    din_g.navigation = False

    din_rows = 4
    din_cols = 3
    din_cells  = din_rows * din_cols

    din_gallery_bg_list = [
        "din_ext_camp_plain_sight_sunset", "din_ext_power_line_day",
        "din_ext_power_line_sunset", "din_int_dining_hall_sunset",
        "din_food_normal_sunset", "din_int_dining_hall_people_sunset", 
        "din_int_dining_hall_sunset_crashed", "din_int_rpg_dungeon", 
        "din_ext_bar_night", "din_ext_scene_night",
        "din_ext_camp_entrance_night", "din_ext_camp_entrance_old",
        "din_ext_clubs_sunset", "din_ext_musclub_sunset",
        "din_space"
    ]

    for bg in din_gallery_bg_list:
        din_g.button(bg)
        din_g.image("bg " + bg)
        din_g.unlock("bg " + bg)

    din_gallery_animated_bg_list = [
        "din_fireplace_winterlong_anim", "din_stars_bush_anim"
    ]

    for animated_bg in din_gallery_animated_bg_list:
        din_g.button(animated_bg)
        din_g.image("bg " + animated_bg)
        din_g.unlock("bg " + animated_bg)

    din_music_box = {
        "God Is An Astronaut — Tempus Horizon": din_god_is_an_astronaut_tempus_horizon,
        "The last days — The Time Will Never Come Back": din_the_last_days_the_time_will_never_come_back,
        "Argsound — Night": din_argsound_night,
        "DWTD — Eyes Of Madness": din_dance_with_the_dead_eyes_of_madness,
        "El Huervo — Daisuke": din_el_huervo_daisuke,
        "Experia — Smoke And Ashes": din_experia_smoke_and_ashes,
        "Explosions In The Sky — Your Hand In Mine": din_explosions_in_the_sky_your_hand_in_mine,
        "God Is An Astronaut — Falling Leaves": din_god_is_an_astronaut_falling_leaves,
        "God Is An Astronaut — First Day Of Sun": din_god_is_an_astronaut_first_day_of_sun,
        "God Is An Astronaut — Suicide By Star": din_god_is_an_astronaut_suicide_by_star,
        "H.1 — Timeless": din_h1_timeless,
        "Higurashi When They Cry — Chiyouraiki No Sora": din_higurashi_when_they_cry_chiyouraiki_no_sora,
        "Out Of Sight — Reasons": din_out_of_sight_reasons,
        "Pillars Of Eternity — Elmshore": din_pillars_of_eternity_elmshore
    }

    din_mr = MusicRoom(fadeout=1.0)

    for music_name in din_music_box.values():
        din_mr.add(music_name)

screen din_main_menu():
    tag menu
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "din_main_menu_" + din_current_time() + "_anim"

    if din_main_menu_var:
        add "din_main_menu_frame" xalign 0.5 yalign 0.5

        text "Дни нигде":
            size 135
            font din_main_menu_font
            text_align 0.5
            xalign 0.5
            yalign 0.045
            antialias True
            kerning 2

        add "din_main_menu_underline" xalign 0.5 ypos 191

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

        textbutton "Загрузить" at din_buttons_atl():
            style "din_main_menu_style"
            text_style "din_main_menu_style"
            xalign 0.5
            ypos 433
            action [
                SetVariable("din_main_menu_var", False),
                ShowMenu("din_load_main_menu")
            ]

        textbutton "Дополнительно" at din_buttons_atl():
            style "din_main_menu_style"
            text_style "din_main_menu_style"
            xalign 0.5
            ypos 556
            action [
                SetVariable("din_main_menu_var", False),
                ShowMenu("din_extra")
            ]

        textbutton "Настройки" at din_buttons_atl():
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
            auto din_gui_path + "misc/logowhite_%s.png"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")

screen din_story_choice():
    tag menu
    modal True

    add din_gui_path + "main_menu/stories_all_closed.png"

    imagebutton:
        idle din_gui_path + "main_menu/ikarus_story_hover.png"
        hover din_gui_path + "main_menu/ikarus_story_hover.png"
        focus_mask True
        action [
            Hide("din_story_choice", Dissolve(1.5)),
            Start("din_ikarus_story")
        ]

    if persistent.din_flags["din_ikarus_story_completed"]:
        imagebutton:
            idle din_gui_path + "main_menu/winterlong_story_hover.png"
            hover din_gui_path + "main_menu/winterlong_story_hover.png"
            focus_mask True
            xpos 470
            action [
                Hide("din_story_choice", Dissolve(1.5)),
                Start("din_winterlong_story")
            ]

    if persistent.din_flags["din_winterlong_story_completed"]:
        imagebutton:
            idle din_gui_path + "main_menu/rolegame_story_hover.png" 
            hover din_gui_path + "main_menu/rolegame_story_hover.png"
            focus_mask True
            xpos 980
            action [
                Hide("din_story_choice", Dissolve(1.5)),
                Start("din_rolegame_story")
            ]

    if persistent.din_flags["din_rolegame_story_completed"]:
        imagebutton:
            idle din_gui_path + "main_menu/lost_peace_story_idle.png" 
            hover din_gui_path + "main_menu/lost_peace_story_hover.png"
            focus_mask True
            xpos 1405
            action [
                Hide("din_story_choice", Dissolve(1.5)),
                Start("din_lost_peace_story")
            ]

    add din_gui_path + "main_menu/stories_borders.png"

    imagebutton:
        auto din_gui_path + "main_menu/back_%s.png"
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
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5
        
        text "Дополнительно":
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

        textbutton "Назад":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [
                SetVariable("din_main_menu_var", True),
                Hide("din_extra"), 
                ShowMenu("din_main_menu")
            ]

screen din_characters():
    modal True

    if not din_main_menu_var:
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5

        text "Персонажи":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        for char, info in din_characters_info.items():
            if persistent.din_flags["din_" + char + "_info_received"]:
                imagebutton:
                    auto "din_" + char + "_button_info" + "_%s"
                    xalign info["button_pos"]
                    yalign 0.5
                    action [
                        Hide("din_characters"),
                        SetField(persistent, "sprite_time", info["sprite_time"]),
                        ShowMenu("din_character_info", char=char)
                    ]
            
            else:
                add "din_button_info_locked" xalign info["button_pos"] yalign 0.5

        textbutton "Назад":
            style "din_log_button"
            text_style "din_settings_link_main_menu_preferences"
            xalign 0.1
            ypos 970
            action [
                Hide("din_characters"),
                ShowMenu("din_extra")
            ]

screen din_character_info(char):
    modal True

    add din_characters_info[char]["bg"]

    add "din_" + char + "_char_name_frame" xalign 0.5 yalign 0.031

    text din_characters_info[char]["name"]:
        font din_main_menu_font
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2

    add "din_char_description_frame" xpos 58 ypos 135

    imagebutton:
        idle Transform(din_characters_info[char]["main_sprite"], alpha=0.9)
        hover din_characters_info[char]["main_sprite"]
        focus_mask True
        xalign 1.05
        action [
            Hide("din_character_info"),
            ShowMenu("din_character_sprites", char=char, sprite=din_characters_info[char]["main_sprite"])
        ]

    text din_characters_info[char]["description"]:
        font din_main_menu_font
        line_spacing 10
        size 55
        xpos 77
        ypos 172

    imagebutton:
        auto "din_back_%s"
        xpos 1800
        ypos 1000
        action [
            Hide("din_character_info"),
            ShowMenu("din_characters")
        ]

screen din_character_sprites(char, sprite):
    modal True

    $ din_char_sprites = din_characters_info[char]["sprites"]
    $ din_current_sprite_index = din_char_sprites.index(sprite)
    $ din_next_sprite_index = (din_current_sprite_index + 1) % len(din_char_sprites)
    $ din_prev_sprite_index = (din_current_sprite_index - 1) % len(din_char_sprites)
    $ din_next_sprite = din_char_sprites[din_next_sprite_index]
    $ din_prev_sprite = din_char_sprites[din_prev_sprite_index]

    add din_characters_info[char]["bg"]

    add sprite xalign 0.5

    imagebutton:
        auto din_gui_path + "misc/gallery_next_%s.png"
        xalign 0.8
        yalign 0.5
        action ShowMenu("din_character_sprites", char=char, sprite=din_next_sprite)

    imagebutton:
        auto din_gui_path + "misc/gallery_previous_%s.png"
        xalign 0.2
        yalign 0.5
        action ShowMenu("din_character_sprites", char=char, sprite=din_prev_sprite)

    imagebutton:
        auto "din_back_%s"
        xpos 1800
        ypos 1000
        action [
            Hide("din_character_sprites"),
            ShowMenu("din_character_info", char=char)
        ]

screen din_music_room():
    modal True

    if not din_main_menu_var:
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5

        add din_gui_path + "main_menu/music_room_frame.png"

        frame:
            background None

            side "c r":
                area (0.15, 0.22, 0.79, 0.73)

                viewport:
                    id "din_music_box"
                    draggable True
                    mousewheel True
                    scrollbars None
                    
                    grid 1 len(din_music_box):
                        for name, track in sorted(din_music_box.iteritems()):
                            textbutton name:
                                style "din_button_none"
                                text_style "music_link"
                                xalign 0.5
                                action din_mr.Play(track)

                vbar:
                    value YScrollValue("din_music_box")
                    bottom_bar din_gui_path + "main_menu/vbar_null.png"
                    top_bar din_gui_path + "main_menu/vbar_full.png"
                    thumb None
                    xmaximum 52

        text "Музыка":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "Назад":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences"
            xalign 0.1
            ypos 970
            action [
                Hide("din_music_room"),
                ShowMenu("din_extra")
            ]

        on "replaced" action Play("music", din_god_is_an_astronaut_tempus_horizon)

screen din_background_gallery():
    modal True

    if not din_main_menu_var:
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5

        $ din_gallery_table = din_gallery_bg_list + din_gallery_animated_bg_list

        $ din_len_table = len(din_gallery_table)

        text "Галерея":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "Назад":
            style "din_log_button" 
            text_style "din_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [
                Hide("din_background_gallery"),
                ShowMenu("din_extra")
            ]

        grid din_rows din_cols xpos 0.1 ypos 0.18:
            $ din_bg_displayed = 0
            $ din_next_page = din_page + 1

            if din_next_page > int(din_len_table / din_cells):
                $ din_next_page = 0

            for n in range(din_len_table):
                if n < (din_page + 1) * din_cells and n >= din_page * din_cells:
                    if din_gallery_table[n] in din_gallery_animated_bg_list:
                        $ _din_t = im.Crop(
                            "din/images/bg/" + din_gallery_table[n][len(din_prefix):] + "/" + din_gallery_table[n][len(din_prefix):-4] + "1.png", 
                            (0, 0, 1920, 1080)
                        )

                    else:
                        $ _din_t = im.Crop(
                            "din/images/bg/" + din_gallery_table[n][len(din_prefix):] + ".png",
                            (0, 0, 1920, 1080)
                        )

                    $ _din_img_scaled = im.Scale(_din_t, 320, 180)

                    $ din_img = im.Composite(
                        (336, 196),
                        (8, 8),
                        im.Alpha(_din_img_scaled, 0.9), (0, 0),
                        im.Image(din_gui_path + "save_load/main_menu/thumbnail_idle.png")
                    )

                    $ din_imgh = im.Composite(
                        (336, 196),
                        (8, 8),
                        _din_img_scaled,
                        (0, 0),
                        im.Image(din_gui_path + "save_load/main_menu/thumbnail_hover.png")
                    )

                    add din_g.make_button(
                        din_gallery_table[n],
                        get_image("gui/gallery/blank.png"),
                        None,
                        din_imgh,
                        din_img,
                        style="blank_button",
                        bottom_margin=50,
                        right_margin=50
                    )

                    $ din_bg_displayed += 1

                    if n + 1 == din_len_table:
                        $ din_next_page = 0

            for j in range(0, din_cells - din_bg_displayed):
                null

        if din_page != 0:
            imagebutton:
                auto din_gui_path + "misc/gallery_previous_%s.png"
                yalign 0.5 
                xalign 0.04 
                action [
                    SetVariable("din_page", din_page - 1),
                    ShowMenu("din_background_gallery")
                ]

        if din_page != int(din_page_counter(din_len_table, din_cells)) - 1:
            imagebutton: 
                auto din_gui_path + "misc/gallery_next_%s.png"
                yalign 0.5 
                xalign 0.96 
                action [
                    SetVariable("din_page", din_next_page),
                    ShowMenu("din_background_gallery")
                ]

screen din_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not din_main_menu_var:
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5
        
        text "Загрузка":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "Назад":
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
                 
        textbutton "Удалить":
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
                            text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=" Пусто") + "\n" + FileSaveName(i)):
                                style "din_text_save_load_main_menu"
                                xpos 15
                                ypos 15

screen din_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not din_main_menu_var:
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5
        
        text "Настройки":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        text "Режим экрана":
            font din_header_font
            size 60
            xalign 0.5
            ypos 200
            
        textbutton "Во весь экран":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")
            
        textbutton "В окне":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 280

            if not _preferences.fullscreen:
                text_style "din_settings_header_main_menu_preferences_inverse"

            else:
                text_style "din_settings_header_main_menu_preferences"

            action Preference("display", "window")

        text "Размер шрифта":
            font din_header_font
            size 60
            xalign 0.5
            ypos 360
                
        textbutton "Обычный":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton "Крупный":
            style "din_button_none"
            text_style "din_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "Пропускать":
            font din_header_font
            size 60
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "din_button_none"
                text_style "din_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Всё":
                style "din_button_none"
                text_style "din_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton "Виденное ранее":
                style "din_button_none"
                text_style "din_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "Всё":
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
            right_bar din_gui_path + "preferences/main_menu/bar_null.png"
            left_bar din_gui_path + "preferences/main_menu/bar_full.png"
            thumb din_gui_path + "preferences/main_menu/htumb.png"
            xpos 975
            ypos 813
            xmaximum 400
            ymaximum 85

        textbutton "Назад":
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
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5
        
        text "Вы действительно хотите выйти?":
            font din_main_menu_font
            size 80
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
                Hide("din_quit_main_menu"),
                Function(din_screens_diact),
                ShowMenu("main_menu")
            ]
            
        textbutton "Нет":
            style "din_settings_header_main_menu_quit"
            text_style "din_settings_header_main_menu_quit"
            xpos 1230
            ypos 600
            action [
                SetVariable("din_main_menu_var", True),
                Hide("din_quit_main_menu"),
                ShowMenu("din_main_menu")
            ]
        
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

            hotspot (0, 83, 660, 65) focus_mask None clicked [din_set_main_menu_cursor_curried(), MainMenu(confirm=False)]

            hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu("din_save")

            hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu("din_load")

            hotspot (0, 278, 660, 65) focus_mask None clicked ShowMenu("din_preferences")

            hotspot (0, 343, 660, 65) focus_mask None action [Function(din_screens_diact), ShowMenu("main_menu")]    

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