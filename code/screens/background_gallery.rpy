init python:
    din_gallery = Gallery()
    din_page = 0
    din_gallery.transition = fade
    din_gallery.locked_button = DIN_GUI_PATH + "save_load/main_menu/thumbnail_idle.png"
    din_gallery.navigation = False

    din_rows = 4
    din_cols = 3
    din_cells = din_rows * din_cols

    def din_page_counter(n, k):
        l = float(n) / float(k)

        if l - int(l) > 0:
            return int(l) + 1

        else:
            return l

    din_gallery_bg_list = [
        "din_ext_camp_plain_sight_sunset",
        "din_ext_power_line_day",
        "din_ext_power_line_sunset",
        "din_int_dining_hall_sunset",
        "din_food_normal_sunset",
        "din_int_dining_hall_people_sunset",
        "din_int_dining_hall_sunset_crashed",
        "din_int_rpg_dungeon",
        "din_ext_bar_night",
        "din_ext_scene_night",
        "din_ext_camp_entrance_night",
        "din_ext_camp_entrance_old",
        "din_ext_clubs_sunset",
        "din_ext_musclub_sunset",
        "din_space",
        "din_ext_camp_plain_sight_night",
        "din_ext_road_night_without_lep"
    ]

    for bg in din_gallery_bg_list:
        din_gallery.button(bg)
        din_gallery.image("bg " + bg)
        din_gallery.unlock("bg " + bg)

    din_gallery_animated_bg_list = [
        "din_fireplace_winterlong_anim",
        "din_stars_bush_anim"
    ]

    for animated_bg in din_gallery_animated_bg_list:
        din_gallery.button(animated_bg)
        din_gallery.image("bg " + animated_bg)
        din_gallery.unlock("bg " + animated_bg)

screen din_background_gallery():
    modal True

    if not din_main_menu_var:
        add "din_main_menu_options_frame":
            xalign 0.5
            yalign 0.5

        $ din_gallery_table = din_gallery_bg_list + din_gallery_animated_bg_list

        $ din_len_table = len(din_gallery_table)

        text "Галерея":
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
                            "din/images/bg/" + din_gallery_table[n][len(DIN_PREFIX):] + "/" + din_gallery_table[n][len(DIN_PREFIX):-4] + "1.png",
                            (0, 0, 1920, 1080)
                        )

                    else:
                        $ _din_t = im.Crop(
                            "din/images/bg/" + din_gallery_table[n][len(DIN_PREFIX):] + ".png",
                            (0, 0, 1920, 1080)
                        )

                    $ _din_img_scaled = im.Scale(_din_t, 320, 180)

                    $ din_img = im.Composite(
                        (336, 196),
                        (8, 8),
                        im.Alpha(_din_img_scaled, 0.9),
                        (0, 0),
                        im.Image(DIN_GUI_PATH + "save_load/main_menu/thumbnail_idle.png")
                    )

                    $ din_imgh = im.Composite(
                        (336, 196),
                        (8, 8),
                        _din_img_scaled,
                        (0, 0),
                        im.Image(DIN_GUI_PATH + "save_load/main_menu/thumbnail_hover.png")
                    )

                    add din_gallery.make_button(
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
                auto DIN_GUI_PATH + "misc/gallery_previous_%s.png"
                yalign 0.5
                xalign 0.04
                action [
                    SetVariable("din_page", din_page - 1),
                    ShowMenu("din_background_gallery")
                ]

        if din_page != int(din_page_counter(din_len_table, din_cells)) - 1:
            imagebutton:
                auto DIN_GUI_PATH + "misc/gallery_next_%s.png"
                yalign 0.5
                xalign 0.96
                action [
                    SetVariable("din_page", din_next_page),
                    ShowMenu("din_background_gallery")
                ]
