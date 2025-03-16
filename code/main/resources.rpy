init python:
    import time
    from os import path
    
    din_mod_name = "din"
    din_prefix = din_mod_name + "_"

    for file_name in renpy.list_files():
        if din_mod_name in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith(din_mod_name + "/images/bg/"):
                renpy.image("bg " + din_prefix + file_path, file_name)

            elif file_name.startswith(din_mod_name + "/images/sprites/"):
                renpy.image(
                    din_prefix + file_path, 
                    ConditionSwitch(
                        "persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)),
                        "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), 
                        True, file_name
                    )
                )

            elif file_name.startswith(din_mod_name + "/sounds/"):
                globals()[din_prefix + file_path] = file_name
    
    din_std_set_for_preview = {}
    din_std_set = {}
    store.din_colors = {}
    store.din_names = {}
    store.din_names_list = []
    din_speaker_color = "speaker_color"

    store.din_names_list.append("din_narrator")

    store.din_names_list.append("din_th")

    din_colors["din_third_i"] = {"speaker_color": "#004979"}
    din_names["din_third_i"] = "Я"
    store.din_names_list.append("din_third_i")

    din_colors["din_third"] = {"speaker_color": "#004979"}
    din_names["din_third"] = "Третий"
    store.din_names_list.append("din_third")

    din_colors["din_nit_he"] = {"speaker_color": "#9f9393"}
    din_names["din_nit_he"] = "Он"
    store.din_names_list.append("din_nit_he")

    din_colors["din_nit_guest"] = {"speaker_color": "#9f9393"}
    din_names["din_nit_guest"] = "Гость"
    store.din_names_list.append("din_nit_guest")

    din_colors["din_nit"] = {"speaker_color": "#9f9393"}
    din_names["din_nit"] = "Ниточник"
    store.din_names_list.append("din_nit")

    din_colors["din_pi_teapot"] = {"speaker_color": "#551313"}
    din_names["din_pi_teapot"] = "Пионер"
    store.din_names_list.append("din_pi_teapot")

    din_colors["din_teapot"] = {"speaker_color": "#551313"}
    din_names["din_teapot"] = "Чайник"
    store.din_names_list.append("din_teapot")

    din_colors["din_gensek"] = {"speaker_color": "#d1d141"}
    din_names["din_gensek"] = "Генсек"
    store.din_names_list.append("din_gensek")

    din_colors["din_pi1"] = {"speaker_color": "#cccc00"}
    din_names["din_pi1"] = "Пионер"
    store.din_names_list.append("din_pi1")

    din_colors["din_pi2"] = {"speaker_color": "#666699"}
    din_names["din_pi2"] = "Пионер"
    store.din_names_list.append("din_pi2")

    din_colors["din_pi3"] = {"speaker_color": "#1873b9"}
    din_names["din_pi3"] = "Пионер"
    store.din_names_list.append("din_pi3")

    din_colors["din_pi_listener"] = {"speaker_color": "#5e5b5a"}
    din_names["din_pi_listener"] = "Пионер"
    store.din_names_list.append("din_pi_listener")

    din_colors["din_pacifist"] = {"speaker_color": "#088010"}
    din_names["din_pacifist"] = "Пацифист"
    store.din_names_list.append("din_pacifist")

    din_colors["din_dv"] = {"speaker_color": "#ffaa00"}
    din_names["din_dv"] = "Алиса"
    store.din_names_list.append("din_dv")

    din_colors["din_sl"] = {"speaker_color": "#ffd200"}
    din_names["din_sl"] = "Славяна"
    store.din_names_list.append("din_sl")

    din_colors["din_un"] = {"speaker_color": "#aa64d9"}
    din_names["din_un"] = "Лена"
    store.din_names_list.append("din_un")

    class DinTimingMemorization():
        def __init__(self, channel, fade):
            self.channel = channel
            self.fade = fade            

        def pause(self):
            self.file_name = renpy.music.get_playing(self.channel)
            self.pause_time = renpy.music.get_pos(self.channel)
            renpy.music.stop(self.channel, fadeout=self.fade)

        def resume(self):
            self.resume_params = "<from 0>" + self.file_name if self.pause_time == None else "<from {}>".format(self.pause_time) + self.file_name
            renpy.music.play(self.resume_params, channel=self.channel, fadein=self.fade)

    class DinBlackRectangle(renpy.Displayable):
        def __init__(self, width, height, alpha, **kwargs):
            super(DinBlackRectangle, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.alpha = alpha
            self.frame = Solid("#000000", xsize=self.width, ysize=self.height)

        def render(self, width, height, st, at):
            t = Transform(child=self.frame, alpha=self.alpha)
            obj = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(obj, (0, 0))
            return render

    def din_shrinking_text_tag(tag, argument, contents):
        if persistent.font_size == "large":
            start_size = 32

        elif persistent.font_size == "small":
            start_size = 28
        
        modified_contents = []
        current_size = start_size
        
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    size_tag = "size={}".format(current_size)
                    modified_contents.append((renpy.TEXT_TAG, size_tag))
                    modified_contents.append((renpy.TEXT_TEXT, char))
                    modified_contents.append((renpy.TEXT_TAG, "/size"))
                    
                    current_size -= 1

        return modified_contents

    def din_char_define(character_name, is_nvl=False):
        global DynamicCharacter
        global nvl
        global din_store
        global din_speaker_color
        din_gl = globals()
        
        if character_name == "din_narrator":
            if is_nvl:
                din_gl["din_narrator"] = Character(None, kind=nvl, what_style="din_text_style")
            
            else:
                din_gl["din_narrator"] = Character(None, what_style="din_text_style")
            
            return
        
        if character_name == "din_th":
            if is_nvl:
                din_gl["din_th"] = Character(None, kind = nvl, what_style = "din_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            else:
                din_gl["din_th"] = Character(None, what_style = "din_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            return
        
        if is_nvl:
            din_gl[character_name] = DynamicCharacter("%s_name" % character_name, color=store.din_colors[character_name][din_speaker_color], kind=nvl, what_style="din_text_style", who_suffix=":")
            din_gl["%s_name" % character_name] = store.din_names[character_name]
        
        else:
            din_gl[character_name] = DynamicCharacter("%s_name" % character_name, color=store.din_colors[character_name][din_speaker_color], what_style="din_text_style")
            din_gl["%s_name" % character_name] = store.din_names[character_name]

    def din_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name)

    def din_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global din_narrator
        global din_th
        din_narrator_nvl = din_narrator
        th_nvl = din_th
        
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name, True)

    def din_reload_names():
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name)

    din_reload_names()

    if persistent.din_flags == None:
        persistent.din_flags = {}

    persistent.din_flags.setdefault("din_intro_completed", False)
    persistent.din_flags.setdefault("din_ikarus_story_completed", False)
    persistent.din_flags.setdefault("din_winterlong_story_completed", False)
    persistent.din_flags.setdefault("din_rolegame_story_completed", False)
    persistent.din_flags.setdefault("din_nit_info_received", False)
    persistent.din_flags.setdefault("din_hall_info_received", False)
    persistent.din_flags.setdefault("din_third_info_received", False)
    persistent.din_flags.setdefault("din_gensek_info_received", False)
    persistent.din_flags.setdefault("din_pacifist_info_received", False)

    def din_get_char_sprites(char):
        sprite_names = []

        for image in renpy.list_images():
            if image.startswith("din_{} ".format(char)):
                sprite_names.append(image)

        return sprite_names

    def din_page_counter(n, k):
        l = float(n) / float(k)
        
        if l - int(l) > 0:
            return int(l) + 1

        else:
            return l

    def din_frame_animation(image_name, frames_quantity, retention, loop, transition, start=1, **properties):
        anim_args = []
        
        for i in xrange(start, start + frames_quantity):
            anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))
            
            if loop:
                anim_args.append(retention)
                anim_args.append(transition)
        
        return anim.TransitionAnimation(*anim_args, **properties)

    def din_blink(blink_pause):
        renpy.show("blink")
        renpy.pause(blink_pause, hard=True)

    def din_unblink(scene_name, unblink_pause):
        renpy.hide("blink")
        renpy.scene()
        renpy.show(scene_name)
        renpy.show("unblink")
        renpy.pause(unblink_pause, hard=True)

    def din_portal_using(after_portal_use_bg):
        before_portal_use_bg = renpy.get_attributes("bg")[0]
        renpy.play(din_portal_use, channel="sound")
        renpy.scene()
        renpy.show(before_portal_use_bg, at_list=[din_portal_using_zoom])
        renpy.pause(0.035, hard=True)
        renpy.scene()
        renpy.show("bg white")
        renpy.transition(din_portal_use_transition)
        renpy.pause(1.2, hard=True)
        renpy.show(after_portal_use_bg)
        renpy.transition(flash)
        renpy.pause(1.3, hard=True)

    def din_story_intro(_save_name, daytime, background, sprite, lbl, desc, amb):
        global save_name

        renpy.block_rollback()
        save_name = _save_name
        persistent.timeofday = daytime
        persistent.sprite_time = daytime
        renpy.music.play("sound/ambiences/{}.ogg".format(amb), "ambience", fadein=2)
        renpy.scene()
        renpy.show(background)
        renpy.show(sprite)
        renpy.show("din_story_frame", at_list=[Transform(xalign=0.5, yalign=0.85)])
        renpy.show("text", what=Text(lbl, xalign=0.5, yalign=0.75, style=style.din_story_label), tag="lbl")
        renpy.show("text", what=Text(desc, xalign=0.5, yalign=0.85, style=style.din_story_description), tag="desc")
        renpy.with_statement(Dissolve(1.5))
        renpy.pause(3.0, hard=True)
        renpy.music.stop("ambience", 2)
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(Dissolve(1.5))

    def din_interlude_intro(interlude_name):
        global save_name

        renpy.block_rollback()
        save_name = "Интерлюдия.\nНиточник и Третий.\n{}".format(interlude_name)
        persistent.timeofday = "sunset"
        persistent.sprite_time = "sunset"
        renpy.music.play("sound/ambiences/ext_road_evening.ogg", "ambience", fadein=2)
        renpy.scene()
        renpy.show("bg din_ext_camp_plain_sight_sunset")
        renpy.show("din_nit normal_r", at_list=[Transform(xalign=0.1, yalign=0.5)])
        renpy.show("din_third normal", at_list=[Transform(xalign=0.9, yalign=0.5)])
        renpy.show("din_interlude_frame", at_list=[Transform(xalign=0.5, yalign=0.85)])
        renpy.show("text", what=Text("Интерлюдия", xalign=0.5, yalign=0.7, style=style.din_story_label), tag="lbl")
        renpy.show("text", what=Text("Ниточник и Третий", xalign=0.5, yalign=0.775, style=style.din_story_description), tag="desc")
        renpy.show("text", what=Text(interlude_name, xalign=0.5, yalign=0.85, style=style.din_interlude_name), tag="interl_name")
        renpy.with_statement(Dissolve(1.5))
        renpy.pause(3.0, hard=True)
        renpy.music.stop("ambience", 2)
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(Dissolve(1.5))
        
    def din_onload(type):
        global din_lock_quit
        global din_lock_quick_menu

        if type == "lock":
            renpy.config.skipping = None
            din_lock_quit = True
            din_lock_quick_menu = True
            config.allow_skipping = False

        elif type == "unlock":
            din_lock_quit = False
            din_lock_quick_menu = False
            config.allow_skipping = True

    def din_current_time():
        hours = {
            "morning": [7, 8],
            "day": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            "sunset": [20, 21],
            "night": [22, 23, 24, 0, 1, 2, 3, 4, 5, 6]            
        }
        
        current_time = time.strftime("%H:%M:%S", time.localtime())
        hour, minute, sec = current_time.split(":")

        for timeofday, hours in hours.items():
            if int(hour) in hours:
                return timeofday

    def din_show_titles():
        renpy.show("din_titles_frame")
        renpy.with_statement(dissolve)
        renpy.show_screen("din_titles_overlay", _layer="overlay")
        renpy.show("din_titles_style din_titles", at_list=[din_titles_anim])
        renpy.pause(30, hard=True)
        renpy.hide("din_titles_frame")
        renpy.with_statement(dissolve)
        renpy.hide_screen("din_titles_overlay", layer="overlay")

    def din_set_timeofday_cursor():
        config.mouse_displayable = MouseDisplayable(din_gui_path + "cursors/" + persistent.timeofday + "/cursor.png", 0, 0)

    def din_set_dynamic_cursor(state):
        if din_set_timeofday_cursor in config.overlay_functions:
            config.overlay_functions.remove(din_set_timeofday_cursor)

        if state == "timeofday":
            config.overlay_functions.append(din_set_timeofday_cursor)

        elif state == "main_menu":
            config.mouse_displayable = MouseDisplayable(din_gui_path + "cursors/main_menu/cursor.png", 0, 0)

        elif state == "null":
            config.mouse_displayable = MouseDisplayable(Null(0, 0), 0, 0)

    def din_set_time(timeofday, sprite_time=None):
        if sprite_time is None:
            sprite_time = timeofday
        
        renpy.block_rollback()
        persistent.timeofday = timeofday
        persistent.sprite_time = sprite_time

    config.custom_text_tags["din_shrinking_text"] = din_shrinking_text_tag

init:
    $ din_titles = """{b}Спасибо, что снова читаете мод нашей команды!{/b}
    Не смотря ни на что, мы хотим создавать что-то новое, непохожее и нетипичное для мастерской.\n\nЭкспериментировать, воплощать и развивать идеи, которые откликаются людям. И если наш мод как-то в вас откликнулся, то дайте нам знать!\n\nВаша поддержка, даже в форме простого комментария ""Хороший мод, жду нового!"" действительно очень помогает нам. Каждый раз, когда мы видим подобное, в наших чатах случается подъем боевого духа и желания сворачивать горы)\n\nНад модом работали:\nSeeker - автор идеи, сценарист.\n\npaych3ck - основой код, дизайн интерфейса.\n\nДаниил Бухичевский - помощь с текстом.\n\nЕгорыч - работа над визуальной составляющей.\n\ndigreen17 - помощь с визуальной составляющей и вычитка текста.\n\nD_SMILE - художник фонов.\n\nCloudy - художник спрайтов.\n\nДанила Маклаков - помощь с улучшением спрайтов.\n\nБлагодарим тех, кто поддерживал нас финансово:\nГригорий Григорьев\n\nНикита Берлов\n\nИлья Можайкин\n\nМаксим Куттер\n\nПионер Пионерович\n\nРуслан Власов\n\nТак или иначе, спасибо за уделённое нам время! Этот мод - далеко не конец. Мы не собираемся останавливаться. Следите за анонсами. С уважением, Zero Impact."""

    $ din_main_menu_var = True
    $ din_lock_quit_game_main_menu_var = True
    $ din_lock_quit = False
    $ din_lock_quick_menu = False

    $ din_take_torch = False
    $ din_take_clock = False
    $ din_choice_clock = False
    $ din_choice_wait = False
    $ din_take_everything = False

    $ din_wiperight = CropMove(.5, "wiperight")
    $ din_wipeleft = CropMove(.5, "wipeleft")

    $ din_set_timeofday_cursor_var = False

    $ din_rolegame_ambience_memorization = DinTimingMemorization("ambience", 2)
    $ din_rolegame_music_memorization = DinTimingMemorization("music", 2)

    $ din_portal_use_transition = ImageDissolve("din/images/gui/misc/din_transition2.png", 0.3, 16)

    image din_main_menu_frame = DinBlackRectangle(width=720, height=1080, alpha=0.6)
    image din_main_menu_options_frame = DinBlackRectangle(width=1804, height=1028, alpha=0.6)
    image din_intro_frame = DinBlackRectangle(width=1920, height=689, alpha=0.6)
    image din_char_description_frame = DinBlackRectangle(width=1150, height=915, alpha=0.6)
    image din_hall_char_name_frame = DinBlackRectangle(width=180, height=70, alpha=0.6)
    image din_gensek_char_name_frame = DinBlackRectangle(width=250, height=70, alpha=0.6)
    image din_nit_char_name_frame = DinBlackRectangle(width=330, height=70, alpha=0.6)
    image din_third_char_name_frame = DinBlackRectangle(width=240, height=90, alpha=0.6)

    image din_story_frame = DinBlackRectangle(width=630, height=240, alpha=0.5)
    image din_interlude_frame = DinBlackRectangle(width=630, height=290, alpha=0.5)
    
    image bg din_fireplace_anim = din_frame_animation("din/images/bg/fireplace_anim/fireplace", 10, 1.8, True, Dissolve(1.2))
    image bg din_fireplace_winterlong_anim = din_frame_animation("din/images/bg/fireplace_winterlong_anim/fireplace_winterlong", 10, 1.8, True, Dissolve(1.2))
    image bg din_stars_bush_anim = din_frame_animation("din/images/bg/stars_bush_anim/stars_bush", 15, 1.8, True, Dissolve(1.2))
    image din_main_menu_day_anim = din_frame_animation("din/images/gui/main_menu/day/day", 5, 4, True, Dissolve(2))
    image din_main_menu_night_anim = din_frame_animation("din/images/gui/main_menu/night/night", 5, 4, True, Dissolve(2))
    image din_main_menu_sunset_anim = din_frame_animation("din/images/gui/main_menu/sunset/sunset", 5, 4, True, Dissolve(2))
    image din_main_menu_morning_anim = din_frame_animation("din/images/gui/main_menu/morning/morning", 5, 4, True, Dissolve(2))
    image din_main_menu_underline = din_gui_path + "main_menu/underline.png"

    image din_intro_logo = din_gui_path + "misc/intro_logo.png"

    image din_ext_camp_entrance_day = din_gui_path + "misc/ext_camp_entrance_day.png"
    image din_ext_camp_entrance_night = din_gui_path + "misc/ext_camp_entrance_night.png"
    image din_ext_camp_entrance_sunset = din_gui_path + "misc/ext_camp_entrance_sunset.png"
    image din_ext_camp_entrance_morning = din_gui_path + "misc/ext_camp_entrance_morning.png"

    image bg din_ext_polyana_night_blurred = im.Blur("images/bg/ext_polyana_night.jpg", 1.5)

    image din_gensek silhouette normal = im.MatrixColor("din/images/sprites/gensek/normal/gensek stay normal.png", im.matrix.tint(0, 0, 0))
    image din_nuts silhouette normal = im.MatrixColor("din/images/sprites/nuts/normal/nuts normal.png", im.matrix.tint(0, 0, 0))
    image din_pi silhouette normal = im.MatrixColor("din/images/sprites/pi/normal/pi normal.png", im.matrix.tint(0, 0, 0))
    image din_nit silhouette normal = im.MatrixColor("din/images/sprites/nit/normal/nit bulging3_r.png", im.matrix.tint(0, 0, 0))
    image din_nit silhouette normal_r = im.MatrixColor("din/images/sprites/nit/normal/nit normal_r.png", im.matrix.tint(0, 0, 0))

    image din_blank_skip = renpy.display.behavior.ImageButton(Null(1920, 1080), Null(1920, 1080), clicked=[Jump("din_after_intro")])

    image din_titles_style = ParameterizedText(style="din_titles_style", size=40, xalign=0.5)

    image din_note = "din/images/effects/note.png"

    image din_nit_alpha_anim:
        "din_nit normal_r"
        pause 0.5
        linear 0.8 alpha 1.0
        pause 0.2
        linear 1.0 alpha 0.0
        repeat

    image din_nit_darklight_anim:
        "din_nit normal_r"
        pause 0.8
        "din_nit silhouette normal_r" with Dissolve(0.4)
        pause 0.8
        "din_nit normal_r" with Dissolve(0.4)
        pause 0.8
        repeat

    transform din_buttons_atl():
        on idle:
            linear 0.5 zoom 1.0

        on hover:
            linear 0.5 zoom 1.025

    transform din_buttons_transition():
        on hover:
            alpha 1.0
            linear 0.5 alpha 0.0
            
        on idle:
            alpha 0.0
            linear 0.5 alpha 1.0

    transform din_portal_using_zoom():
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.5 zoom 2 xalign 0.5 yalign 0.5

    transform din_titles_anim():
        xalign 0.5
        ypos 1.1
        linear 48 ypos -4.0

    transform din_moveinbottom():
        linear 0.5 ypos 1300

    transform din_zoom_in_center():
        xalign 0.5 yalign 0.5 zoom 1.0
        pause 2.0
        linear 20 zoom 2.0 xalign 0.5 yalign 0.5

    transform din_auto_moving():
        subpixel True
        truecenter
        zoom 1.03

        parallel:
            linear 0.2 xoffset -2
            linear 0.3 xoffset 3
            linear 0.2 xoffset -1
            linear 0.3 xoffset 2
            repeat

        parallel:
            linear 0.2 yoffset -1
            linear 0.25 yoffset 2
            linear 0.2 yoffset -1
            repeat