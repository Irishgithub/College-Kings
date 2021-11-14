screen spoiler2():
    modal True

    add "images/darker.webp"

    use endfrTemplate:
        text "Warning: The path builder contains spoilers for the story of the game. Are you sure you want to continue?":
            style "endfree"
            xalign 0.5

        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("spoiler2"), Show("pathBuilder")]

            textbutton "No":
                action Hide("spoiler2")

screen pathBuilder():
    tag menu
    modal True

    add "gui/path builder/path_builder_background.png"

    text "PATH BUILDER":
        size 50
        align (0.5, 0.1)

    vbox:
        spacing 50
        pos (200,300)

        text "Step 1: Pick a fraternity"

        hbox:
            spacing 75

            vbox:
                imagebutton:
                    if joinwolves:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("joinwolves", True)

                text "Wolves":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if not joinwolves:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("joinwolves", False)

                text "Apes":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

        hbox: 
            yoffset -30
            spacing 200

            textbutton "BACK":        
                xalign 0
                action ShowMenu("main_menu")

            textbutton "NEXT":          
                xalign 1.0
                action Show ("pathBuilder2")

screen pathBuilder2():
    tag menu
    modal True

    add "gui/path builder/path_builder_background.png"

    text "PATH BUILDER":
        size 50
        align (0.5, 0.1)

    vbox:
        spacing 50
        pos (200,300)

        text "Step 2: Pick your starting KCT"

        hbox:
            spacing 75

            vbox:
                imagebutton:
                    if kct == "loyal":
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("kct", "loyal")

                text "Loyal":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if kct == "popular":
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("kct", "popular")

                text "Popular":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if kct == "confident":
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("kct", "confident")

                text "Confident":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

        hbox:
            spacing 20
            yoffset -30
            imagebutton:
                idle "gui/path builder/pb_tick.png"

            text "Lock KCT (Prevent it from changing)":
                yoffset -7


        hbox: 
            yoffset -30
            spacing 200

            textbutton "BACK":        
                xalign 0
                action Show ("pathBuilder")

            textbutton "NEXT":          
                xalign 1.0
                action Show ("pathBuilder3")

screen pathBuilder3():
    tag menu
    modal True

    add "gui/path builder/path_builder_background.png"

    text "PATH BUILDER":
        size 50
        align (0.5, 0.1)

    vbox:
        pos (200,300)
        spacing 50

        text "Step 3: Pick which girls you want to be romantically involved with"

        vpgrid:
            cols 4
            xspacing 50
            yspacing 20
            ysize 700
        
            


            vbox:
                imagebutton:
                    if chloegf:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("chloegf", True)

                text "Chloe":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if norars:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("norars", True)

                text "Nora":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if aubreyrs:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("aubreyrs", True)

                text "Aubrey":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if rileyrs:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("rileyrs", True)

                text "Riley":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"


            vbox:
                imagebutton:
                    if laurenrs:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("laurenrs", True)

                text "Lauren":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"


            vbox:
                imagebutton:
                    if penelopers:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("penelopers", True)

                text "Penelope":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"


            vbox:
                imagebutton:
                    if amberrs:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("amberrs", True)

                text "Amber":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"


            vbox:
                imagebutton:
                    if lindseyrs:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("lindseyrs", True)

                text "Lindsey":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"


            vbox:
                imagebutton:
                    if msrosers:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("msrosers", True)

                text "Ms. Rose":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if v11_samantha_spa:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("v11_samantha_spa", True)

                text "Samantha":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if jennyrs:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("jennyrs", True)

                text "Jenny":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"


            vbox:
                imagebutton:
                    if emilyrs:
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action ToggleVariable("emilyrs", True)

                text "Emily":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"
        
        hbox: 
            yoffset -300
            spacing 200

            textbutton "BACK":        
                xalign 0
                action Show ("pathBuilder2")

            textbutton "NEXT":          
                xalign 1.0
                action Show ("pathBuilder4")

screen pathBuilder4():
    tag menu
    modal True

    add "gui/path builder/path_builder_background.png"

    text "PATH BUILDER":
        size 50
        align (0.5, 0.1)

    vbox:
        spacing 50
        pos (200,300)

        text "Step 4: Pick your starting location"

        hbox:
            spacing 75

            vbox:
                imagebutton:
                    if start_location == "v8start":
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("start_location", "v8start")

                text "Start of Act 2":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if start_location == "v11_start":
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("start_location", "v11_start")

                text "Start of Act 3":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

            vbox:
                imagebutton:
                    if start_location == "v14_start":
                        idle "gui/path builder/pb_selected.png"
                    else:
                        idle "gui/path builder/pb_button.png"
                    hover "gui/path builder/pb_selected.png"
                    action SetVariable("start_location", "v14_start")

                text "Start of Act 4":
                    align (0.5, 0.5)
                    yoffset -70
                    color "#000"

        hbox: 
            yoffset -30
            spacing 200

            textbutton "BACK":        
                xalign 0
                action Show ("pathBuilder3")

            textbutton "Start Game":          
                xalign 1.0
                action Start (start_location)