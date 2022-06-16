# show_input_kivy
A simple Input showing software for streamers

This software allows you to show your inputs to people watching your stream without having to go through an OBS plugin.

{
    "keys": {
        "a": [0, 0.43, 1, 1],
        "z": [0.95 , 0, 0, 1]
    },
    "cols_nb": 1
}

This config file would for example create an overlay capturing the A and Z keys, with the A in blue and the Z in red. The keys would be on top of each other as the cols_nb has a value of 1.

Available keys are the following :

space
up
left
down
right
ctrl_l
alt_l
cmd
tab
caps_lock
shift
backspace
enter
shift_r
page_up
page_down
ctrl_l

and obviously all the latin letters
