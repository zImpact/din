init python:
    din_gui_path = "din/images/gui/"
    
    din_link_font = din_gui_path + "fonts/gothic.ttf"
    din_header_font = din_gui_path + "fonts/corbel.ttf"
    din_main_font = "fonts/calibri.ttf"
    din_main_menu_font = din_gui_path + "fonts/AG_Futura Regular.ttf"

    style.din_titles_style = Style(style.default)
    style.din_titles_style.font = din_link_font
    style.din_titles_style.color = "#fff"
    style.din_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.din_titles_style.drop_shadow_color = "#000"
    style.din_titles_style.italic = False
    style.din_titles_style.bold = False
    style.din_titles_style.text_align = 0.5
    style.din_titles_style.xmaximum = 0.8

    style.din_story_label = Style(style.default)
    style.din_story_label.font = din_main_menu_font
    style.din_story_label.size = 70

    style.din_story_description = Style(style.default)
    style.din_story_description.font = din_main_menu_font
    style.din_story_description.size = 55

    style.din_interlude_name = Style(style.default)
    style.din_interlude_name.font = din_main_menu_font
    style.din_interlude_name.size = 40

    style.din_button_none = Style(style.button)
    style.din_button_none.background = None
    style.din_button_none.hover_background = None
    style.din_button_none.selected_background = None
    style.din_button_none.selected_hover_background = None
    style.din_button_none.selected_idle_background = None

    style.din_text_style = Style(style.default)
    style.din_text_style.color = "#e2c778"
    style.din_text_style.drop_shadow = (2, 2)
    style.din_text_style.drop_shadow_color = "#000"

    style.din_main_menu_style = Style(style.default)
    style.din_main_menu_style.font = din_main_menu_font
    style.din_main_menu_style.size = 70
    style.din_main_menu_style.color = "#d1d1d1"
    style.din_main_menu_style.hover_color = "#ffffff"

    style.din_story_style = Style(style.default)
    style.din_story_style.font = din_main_menu_font
    style.din_story_style.size = 70
    style.din_story_style.color = "#d1d1d1"
    style.din_story_style.hover_color = "#ffffff"

    style.din_titles_style = Style(style.default)
    style.din_titles_style.font = din_link_font
    style.din_titles_style.color = "#fff"
    style.din_titles_style.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    style.din_titles_style.drop_shadow_color = "#000"
    style.din_titles_style.italic = False
    style.din_titles_style.bold = False
    style.din_titles_style.text_align = 0.5
    style.din_titles_style.xmaximum = 0.8

    style.din_log_button = Style(style.button)
    style.din_log_button.child = None
    style.din_log_button.focus_mask = None
    style.din_log_button.background = None

    style.din_save_load_button_main_menu = Style(style.button)
    style.din_save_load_button_main_menu.background = din_gui_path + "save_load/main_menu/thumbnail_idle.png"
    style.din_save_load_button_main_menu.hover_background = din_gui_path + "save_load/main_menu/thumbnail_hover.png"
    style.din_save_load_button_main_menu.selected_background = din_gui_path + "save_load/main_menu/thumbnail_selected.png"
    style.din_save_load_button_main_menu.selected_hover_background = din_gui_path + "save_load/main_menu/thumbnail_selected.png"
    style.din_save_load_button_main_menu.selected_idle_background = din_gui_path + "save_load/main_menu/thumbnail_selected.png"

    style.din_save_load_button_day = Style(style.button)
    style.din_save_load_button_day.background = din_gui_path + "save_load/day/thumbnail_idle.png"
    style.din_save_load_button_day.hover_background = din_gui_path + "save_load/day/thumbnail_hover.png"
    style.din_save_load_button_day.selected_background = din_gui_path + "save_load/day/thumbnail_selected.png"
    style.din_save_load_button_day.selected_hover_background = din_gui_path + "save_load/day/thumbnail_selected.png"
    style.din_save_load_button_day.selected_idle_background = din_gui_path + "save_load/day/thumbnail_selected.png"

    style.din_save_load_button_night = Style(style.button)
    style.din_save_load_button_night.background = din_gui_path + "save_load/night/thumbnail_idle.png"
    style.din_save_load_button_night.hover_background = din_gui_path + "save_load/night/thumbnail_hover.png"
    style.din_save_load_button_night.selected_background = din_gui_path + "save_load/night/thumbnail_selected.png"
    style.din_save_load_button_night.selected_hover_background = din_gui_path + "save_load/night/thumbnail_selected.png"
    style.din_save_load_button_night.selected_idle_background = din_gui_path + "save_load/night/thumbnail_selected.png"

    style.din_save_load_button_dungeon = Style(style.button)
    style.din_save_load_button_dungeon.background = din_gui_path + "save_load/dungeon/thumbnail_idle.png"
    style.din_save_load_button_dungeon.hover_background = din_gui_path + "save_load/dungeon/thumbnail_hover.png"
    style.din_save_load_button_dungeon.selected_background = din_gui_path + "save_load/dungeon/thumbnail_selected.png"
    style.din_save_load_button_dungeon.selected_hover_background = din_gui_path + "save_load/dungeon/thumbnail_selected.png"
    style.din_save_load_button_dungeon.selected_idle_background = din_gui_path + "save_load/dungeon/thumbnail_selected.png"

    style.din_save_load_button_sunset = Style(style.button)
    style.din_save_load_button_sunset.background = din_gui_path + "save_load/sunset/thumbnail_idle.png"
    style.din_save_load_button_sunset.hover_background = din_gui_path + "save_load/sunset/thumbnail_hover.png"
    style.din_save_load_button_sunset.selected_background = din_gui_path + "save_load/sunset/thumbnail_selected.png"
    style.din_save_load_button_sunset.selected_hover_background = din_gui_path + "save_load/sunset/thumbnail_selected.png"
    style.din_save_load_button_sunset.selected_idle_background = din_gui_path + "save_load/sunset/thumbnail_selected.png"

    style.din_base_font = Style(style.default)
    style.din_base_font.font = din_main_font
    style.din_base_font.size = 28
    style.din_base_font.line_spacing = 2

    style.din_settings_link = Style(style.din_base_font)
    style.din_settings_link.font = din_link_font
    style.din_settings_link.size = 60
    style.din_settings_link.kerning = 3
    style.din_settings_link.color = "#909ca3"
    style.din_settings_link.hover_color = "#ffffff"
    style.din_settings_link.selected_color = "#909ca3"
    style.din_settings_link.selected_idle_color = "#909ca3"
    style.din_settings_link.selected_hover_color = "#ffffff"
    style.din_settings_link.insensitive_color = "#909ca3"

    style.din_settings_link_main_menu = Style(style.din_base_font)
    style.din_settings_link_main_menu.font = din_link_font
    style.din_settings_link_main_menu.size = 60
    style.din_settings_link_main_menu.kerning = 3
    style.din_settings_link_main_menu.color = "#ffffff"
    style.din_settings_link_main_menu.hover_color = "#ffffff"
    style.din_settings_link_main_menu.selected_color = "#ffffff"
    style.din_settings_link_main_menu.selected_idle_color = "#ffffff"
    style.din_settings_link_main_menu.selected_hover_color = "#ffffff"
    style.din_settings_link_main_menu.insensitive_color = "#ffffff"

    style.din_settings_link_main_menu_preferences = Style(style.din_base_font)
    style.din_settings_link_main_menu_preferences.font = din_main_menu_font
    style.din_settings_link_main_menu_preferences.size = 60
    style.din_settings_link_main_menu_preferences.kerning = 3
    style.din_settings_link_main_menu_preferences.color = "#d1d1d1"
    style.din_settings_link_main_menu_preferences.hover_color = "#ffffff"
    style.din_settings_link_main_menu_preferences.selected_color = "#d1d1d1"
    style.din_settings_link_main_menu_preferences.selected_idle_color = "#d1d1d1"
    style.din_settings_link_main_menu_preferences.selected_hover_color = "#ffffff"
    style.din_settings_link_main_menu_preferences.insensitive_color = "#d1d1d1"

    style.din_settings_header_main_menu_preferences = Style(style.din_base_font)
    style.din_settings_header_main_menu_preferences.font = din_header_font
    style.din_settings_header_main_menu_preferences.size = 60
    style.din_settings_header_main_menu_preferences.color = "#d1d1d1"
    style.din_settings_header_main_menu_preferences.hover_color = "#ffffff"
    style.din_settings_header_main_menu_preferences.selected_color = "#ffffff"

    style.din_settings_header_main_menu_preferences_locked = Style(style.din_base_font)
    style.din_settings_header_main_menu_preferences_locked.font = din_header_font
    style.din_settings_header_main_menu_preferences_locked.size = 60
    style.din_settings_header_main_menu_preferences_locked.color = "#C0C0C0"
    style.din_settings_header_main_menu_preferences_locked.hover_color = "#C0C0C0"
    style.din_settings_header_main_menu_preferences_locked.selected_color = "#C0C0C0"

    style.din_settings_header_main_menu_quit = Style(style.din_base_font)
    style.din_settings_header_main_menu_quit.font = din_main_menu_font
    style.din_settings_header_main_menu_quit.size = 60
    style.din_settings_header_main_menu_quit.color = "#d1d1d1"
    style.din_settings_header_main_menu_quit.hover_color = "#ffffff"

    style.din_settings_header_main_menu_preferences_inverse = Style(style.din_base_font)
    style.din_settings_header_main_menu_preferences_inverse.font = din_header_font
    style.din_settings_header_main_menu_preferences_inverse.size = 60
    style.din_settings_header_main_menu_preferences_inverse.color = "#ffffff"
    style.din_settings_header_main_menu_preferences_inverse.hover_color = "#ffffff"
    style.din_settings_header_main_menu_preferences_inverse.selected_color = "#ffffff"

    style.din_main_menu = Style(style.din_base_font)
    style.din_main_menu.font = din_header_font
    style.din_main_menu.size = 60
    style.din_main_menu.kerning = 3
    style.din_main_menu.color = "#ffffff"
    style.din_main_menu.hover_color = "#ffffff"
    style.din_main_menu.selected_color = "#ffffff"
    style.din_main_menu.selected_idle_color = "#ffffff"
    style.din_main_menu.selected_hover_color = "#ffffff"
    style.din_main_menu.insensitive_color = "#ffffff"

    style.din_main_menu_locked = Style(style.din_base_font)
    style.din_main_menu_locked.font = din_header_font
    style.din_main_menu_locked.size = 60
    style.din_main_menu_locked.kerning = 3
    style.din_main_menu_locked.color = "#C0C0C0"
    style.din_main_menu_locked.hover_color = "#C0C0C0"
    style.din_main_menu_locked.selected_color = "#C0C0C0"
    style.din_main_menu_locked.selected_idle_color = "#C0C0C0"
    style.din_main_menu_locked.selected_hover_color = "#C0C0C0"
    style.din_main_menu_locked.insensitive_color = "#C0C0C0"

    style.din_settings_header_day = Style(style.din_base_font)
    style.din_settings_header_day.font = din_header_font
    style.din_settings_header_day.size = 50
    style.din_settings_header_day.color = "#4d2e19"
    style.din_settings_header_day.hover_color = "#a27146"
    
    style.din_settings_header_night = Style(style.din_base_font)
    style.din_settings_header_night.font = din_header_font
    style.din_settings_header_night.size = 50
    style.din_settings_header_night.color = "#161d3d"
    style.din_settings_header_night.hover_color = "#008193"

    style.din_settings_header_dungeon = Style(style.din_base_font)
    style.din_settings_header_dungeon.font = din_header_font
    style.din_settings_header_dungeon.size = 50
    style.din_settings_header_dungeon.color = "#161d3d"
    style.din_settings_header_dungeon.hover_color = "#008193"

    style.din_settings_header_sunset = Style(style.din_base_font)
    style.din_settings_header_sunset.font = din_header_font
    style.din_settings_header_sunset.size = 50
    style.din_settings_header_sunset.color = "#5a3525"
    style.din_settings_header_sunset.hover_color = "#636840"

    style.din_settings_text_day = Style(style.din_settings_header_day)
    style.din_settings_text_day.size = 36
    style.din_settings_text_day.selected_color = "#4d2e19"
    style.din_settings_text_day.hover_color = "#a27146"

    style.din_settings_text_night = Style(style.din_settings_header_night)
    style.din_settings_text_night.size = 36
    style.din_settings_text_night.selected_color = "#161d3d"
    style.din_settings_text_night.hover_color = "#008193"

    style.din_settings_text_dungeon = Style(style.din_settings_header_dungeon)
    style.din_settings_text_dungeon.size = 36
    style.din_settings_text_dungeon.selected_color = "#161d3d"
    style.din_settings_text_dungeon.hover_color = "#008193"

    style.din_settings_text_sunset = Style(style.din_settings_header_sunset)
    style.din_settings_text_sunset.size = 36
    style.din_settings_text_sunset.selected_color = "#5a3525"
    style.din_settings_text_sunset.hover_color = "#636840"

    style.din_text_history = Style(style.din_base_font)
    style.din_text_history.color = "#e2c778"
    style.din_text_history.drop_shadow = (2, 2)
    style.din_text_history.drop_shadow_color = "#000"