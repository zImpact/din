init python:
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