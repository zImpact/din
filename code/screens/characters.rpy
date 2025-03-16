init python:
    from collections import OrderedDict

    din_characters_info = OrderedDict([
        ("hall", {
            "name": "Халл",
            "main_sprite": "din_hall pos2 normal",
            "sprite_time": "night",
            "bg": "bg din_ext_scene_night",
            "description": "Если для многих жизнь в лагере стала\nпыткой и мучением, Халл явное исключение\nиз правила. Только в критические моменты\nза его рассеянностью и спонтанностью\nможно разглядеть опасного долгожителя.\nЖажда знаний и экспериментов завоевала\nему устойчивое место среди\nисследователей лагеря. Хоть девять из\nдесяти его изобретений - нерабочая груда\nхлама, десятое часто может стать\nпредметом мысли всех в Общем Лагере\nна многие смены.",
            "sprites": din_get_char_sprites("hall")
        }),
        ("third", {
            "name": "Третий",
            "main_sprite": "din_third normal",
            "sprite_time": "sunset",
            "bg": "bg din_int_dining_hall_sunset_crashed",
            "description": "Среди верхушки лагеря каждый так или\nиначе пытается прогнуть мир под себя,\nподстроить лагерь под свои идеалы. Тем\nудивительнее выглядит Третий, о котором\nмногие рядовые Пионеры могли только\nслышать. Взяв себе имя за место в\nТурнире, победив почти всех один на один,\nТретий всегда занимает роли второго\nплана в лагере. Хоть такое отсутствие\nамбиций поначалу удивляло Пионеров, они\nбыстро смекнули, что Третий может стать \nбесценным подспорьем в любой идее.",
            "sprites": din_get_char_sprites("third")
        }),
        ("nit", {
            "name": "Ниточник",
            "main_sprite": "din_nit normal_r",
            "sprite_time": "day",
            "bg": "bg din_ext_camp_plain_sight_day",
            "description": "Сдержанный оптимизм и лидерские навыки\nсделали Ниточника уважаемым и желанным\nгостем в любой компании даже несмотря\nна не самую большую опасность в бою.\nКрасноречие и сдержанность позволяют\nему служить отличным мостом между и\nстарыми, и довольно «молодыми»\nПионерами, а большие амбиции не\nпозволят ему сидеть на месте. Он - один\nиз немногих старших Пионеров, кто может\nоткрыто верить во Внешний Мир и не быть\nосмеянным.",
            "sprites": din_get_char_sprites("nit")
        }),
        ("gensek", {
            "name": "Генсек",
            "main_sprite": "din_gensek stay normal",
            "sprite_time": "night",
            "bg": "bg din_ext_bar_night",
            "description": "Очень деятельный и крайне опасный, этот\nПионер мало похож на других из первой\nдесятки. Если остальные скорее молча\nуживаются с лагерем, то Генсек\nперестраивает жизнь в лагере под себя.\nИменно он когда-то давно превратил\nскромное сборище пары Пионеров в\nсердце лагерей, Общую столовую.\nГенсек намеревается построить удобное\nдля него общество и, благодаря таланту к\nманипуляции и умению заводить друзей, он\nтак или иначе добьется своего.",
            "sprites": din_get_char_sprites("gensek")
        }),
        ("pacifist", {
            "name": "Пацифист",
            "main_sprite": "din_gensek stay normal",
            "sprite_time": "sunset",
            "bg": "bg din_ext_bar_night",
            "description": "Помимо завсегдатаев и новичков, в Лагере иногда можно встретить и тех, кто еще не выбрал себе дорогу. Пацифист, довольно молодой Пионер в Лагере, все еще ищет своё место. И если старые Пионеры уже давно себя показали, то среди таких, как Пацифист, еще могут таиться сюрпризы. Кто знает, может, именно в нём сокрыт огромный потенциал?",
            "sprites": din_get_char_sprites("pacifist")
        })
    ])

    din_characters_corridors = {
        2: (0.35, 0.65),
        3: (0.2, 0.8),
    }

    din_characters_current_page = 0
    din_characters_per_page = 3
    din_characters_all = list(din_characters_info.items())
    din_characters_total = len(din_characters_all)
    din_characters_pages = (din_characters_total + din_characters_per_page - 1) // din_characters_per_page

screen din_characters():
    modal True

    $ din_characters_start_index = din_characters_current_page * din_characters_per_page
    $ din_characters_end_index = min(din_characters_start_index + din_characters_per_page, din_characters_total)
    $ din_characters_on_page = din_characters_all[din_characters_start_index:din_characters_end_index]

    if not din_main_menu_var:
        add "din_main_menu_options_frame" xalign 0.5 yalign 0.5

        text "Персонажи":
            font din_main_menu_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        $ din_characters_current_number = len(din_characters_on_page)

        for i, (char, info) in enumerate(din_characters_on_page):
            $ din_characters_left_border, din_characters_right_border = din_characters_corridors.get(din_characters_current_number, (0.2, 0.8))
            $ din_characters_xalign = din_characters_left_border + (i * (din_characters_right_border - din_characters_left_border) / (din_characters_current_number - 1)) if din_characters_current_number > 1 else 0.5

            if persistent.din_flags["din_" + char + "_info_received"]:
                imagebutton:
                    auto din_gui_path + "main_menu/" + char + "_button_info" + "_%s.png"
                    xalign din_characters_xalign
                    yalign 0.5
                    action [
                        Hide("din_characters"),
                        SetField(persistent, "sprite_time", info["sprite_time"]),
                        ShowMenu("din_character_info", char=char)
                    ]
            
            else:
                add din_gui_path + "main_menu/button_info_locked.png" xalign din_characters_xalign yalign 0.5

        if din_characters_pages > 1:
            if din_characters_current_page < din_characters_pages - 1:
                imagebutton:
                    auto din_gui_path + "misc/gallery_next_%s.png"
                    xalign 0.96
                    yalign 0.5
                    action [
                        SetVariable("din_characters_current_page", din_characters_current_page + 1),
                        ShowMenu("din_characters")
                    ]

            if din_characters_current_page > 0:
                imagebutton:
                    auto din_gui_path + "misc/gallery_previous_%s.png"
                    xalign 0.04
                    yalign 0.5
                    action [
                        SetVariable("din_characters_current_page", din_characters_current_page - 1),
                        ShowMenu("din_characters")
                    ]

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