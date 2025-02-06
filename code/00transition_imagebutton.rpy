python early:
    renpy.register_sl_statement("din_transition_imagebutton", children=0) \
        .add_property("idle") \
        .add_property("hover") \
        .add_property("xpos") \
        .add_property("ypos") \
        .add_property("transition") \
        .add_property("action")

screen din_transition_imagebutton(idle, hover, transition, action, xpos=0, ypos=0, **properties):
    imagebutton:
        idle idle
        xpos xpos
        ypos ypos
        hovered ShowTransient("din_transition_imagebutton_hovered", transition=transition, img=hover, pos=(xpos, ypos))
        unhovered Hide("din_transition_imagebutton_hovered", transition=transition)
        action action
        properties properties

screen din_transition_imagebutton_hovered(img, pos):
    add img xpos pos[0] ypos pos[1]