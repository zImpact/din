init python:
    din_screens_list = [
        "main_menu",
        "quit",
        "say",
        "nvl",
        "game_menu_selector",
        "yesno_prompt", 
        "choice",
        "help"
    ]

    din_sound_channels = [
        "ambience",
        "music",
        "sound", 
        "sound_loop"
    ]

    class DinFunctionCallback(Action):
        def __init__(self,function, *arguments):
            self.function = function
            self.arguments = arguments

        def __call__(self):
            return self.function(self.arguments)
    
    def din_on_load_callback(slot):
        try:
            if persistent.din_on_save_timeofday[slot]:
                persistent.timeofday = persistent.din_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.din_on_save_timeofday[slot][1]
                persistent.font_size = persistent.din_on_save_timeofday[slot][2]
                _preferences.volumes["music"] = persistent.din_on_save_timeofday[slot][3]
                _preferences.volumes["sfx"] = persistent.din_on_save_timeofday[slot][4]
                _preferences.volumes["voice"] = persistent.din_on_save_timeofday[slot][5]
        
        except:
            pass
    
    def din_on_save_callback(slot):
        if not persistent.din_on_save_timeofday:
            persistent.din_on_save_timeofday = {}

        persistent.din_on_save_timeofday[slot] = (
            persistent.timeofday,
            persistent.sprite_time,
            persistent.font_size,
            _preferences.volumes["music"],
            _preferences.volumes["sfx"],
            _preferences.volumes["voice"]
        )
        
    def din_screens_save():
        for screen_name in din_screens_list:
            renpy.display.screen.screens[("din_old_" + screen_name, None)] = renpy.display.screen.screens[(screen_name, None)]
        
    def din_screens_act():
        persistent.timeofday = "day"
        config.window_title = u"Дни нигде"
        config.name = "Days_In_Nowhere"
        config.version = "1.1"

        for screen_name in din_screens_list:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("din_" + screen_name, None)]

        layout.LOADING = "Потерять несохраненые данные?"
        
        config.overlay_functions.append(din_set_timeofday_cursor)
        config.main_menu_music = din_god_is_an_astronaut_tempus_horizon
        config.linear_saves_page_size = None
        persistent._file_page = "din_FilePage_1"  

    def din_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"

        for screen_name in din_screens_list:
            renpy.display.screen.screens[(screen_name, None)] = renpy.display.screen.screens[("din_old_" + screen_name, None)]
         
        layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
        renpy.free_memory()
        persistent.timeofday = "day"
        config.mouse_displayable = MouseDisplayable("images/misc/mouse/1.png", 0, 0)
        config.main_menu_music = music_list["blow_with_the_fires"]

        persistent._file_page = 1
        
        for channel in din_sound_channels:
            renpy.music.stop(channel)

        renpy.play(music_list["blow_with_the_fires"], channel="music")

    def din_screens_save_act():
        din_screens_save()
        din_screens_act()