init python:
    corridors = {
        2: (0.35, 0.65),
        3: (0.2, 0.8),
    }

    current_page = 0
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

screen din_music_room():
    modal True

    if not din_main_menu_var:
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5

        add din_gui_path + "main_menu/music_room_frame.png"

        frame:
            background None

            has side "c r":
                area (0.15, 0.22, 0.79, 0.73)

            viewport:
                id "din_music_box"
                draggable True
                mousewheel True
                scrollbars None

                has grid 1 len(din_music_box)
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
