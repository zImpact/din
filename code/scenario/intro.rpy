label din_intro:
    $ din_set_mode_adv()
    stop music fadeout 3
    $ renpy.pause(2, hard=True)
    $ renpy.block_rollback()
    $ din_set_time("sunset")
    $ din_set_dynamic_cursor("timeofday")
    scene bg din_ext_camp_plain_sight_sunset with Dissolve(2)
    play ambience ambience_ext_road_evening fadein 2
    play music din_explosions_in_the_sky_your_hand_in_mine fadein 5
    din_narrator "В тихом мире закатного горизонта давно уже ничего не происходит."
    din_narrator "То, что когда-то было лагерем, сейчас — лишь бескрайняя пустошь."
    din_narrator "Разве что одинокая дорога рассекает пейзаж."
    din_narrator "Когда-то она не смотрелась так одиноко."
    din_narrator "Да и жизнь здесь была иной."
    din_narrator "Десятки Пионеров существовали, смирившись с данной им безальтернативной вечностью."
    din_narrator "Каждого из них я знал. По именам, характерам, привычкам, страхам."
    din_narrator "Мог не задумываясь сказать кто как проводит своё время и сколько ему осталось до сумасшествия."
    din_narrator "Я видел, как Пионеры менялись, развивались или застывали во времени, отказываясь двигаться дальше."
    din_narrator "А сейчас эта память медленно утекает, как песок сквозь ладони."
    din_narrator "А потом произошла случайность."
    stop ambience fadeout 2
    $ din_set_time("night")
    scene bg din_int_dining_hall_damaged
    show prologue_dream
    with flash
    din_narrator "Странная смена со странными событиями."
    din_narrator "Ниточник, кажется так его тогда звали, предпринял новую попытку выхода."
    din_narrator "Эти события я еще помнил хорошо."
    show din_hall pos2 normal_burns at left behind prologue_dream
    show din_nit bulging3_l at right behind prologue_dream
    with dissolve
    din_narrator "Игра в карты..."
    scene bg din_fireplace_anim
    show din_nit normal_r at left
    show prologue_dream
    with flash
    din_narrator "«Разговор» у костра..."
    $ renpy.block_rollback()
    scene bg ext_camp_entrance_day
    $ din_set_time("day")
    show din_nit normal_r at center
    show prologue_dream
    with flash
    din_narrator "И самое невероятное — его план сработал!"
    din_narrator "Мир, в котором мы провели больше смен, чем есть звезд на холодном небе, дрогнул."
    scene bg din_ext_camp_plain_sight_sunset with flash
    $ renpy.block_rollback()
    $ din_set_time("sunset")
    din_narrator "Исчез лагерь."
    din_narrator "Исчезло время."
    din_narrator "Исчезли перемены."
    din_narrator "И исчезли Пионеры."
    din_narrator "И только две куклы до сих пор бродят по этой пустыне. {w}Неприкаянные и всеми забытые."
    din_narrator "Я и Ниточник."
    din_narrator "Я поднял взгляд к солнцу."
    din_narrator "Забавно, оно теперь не греет и не слепит, можно смотреть на него сколько угодно."
    din_narrator "Но когда-то дни в лагере были совсем другими."
    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ persistent.din_flags["din_intro_completed"] = True
    $ renpy.pause(2, hard=True)
    jump din_ikarus_story
