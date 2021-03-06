# window width/height
win_width =  1000
win_height = int(win_width * 1 / 1.3)

# scene width/height, regardless of window width/height
scene_width = 800
scene_height = 600

# use these stuff to calculate things between window and scene easily
factor_width = float(win_width) / float(scene_width)
factor_height = float(win_height) / float(scene_height)

clear_color = (120, 200, 255)
message_size = 24

images = 'images/'
fonts = 'fonts/'

gravity = 2000 # something with inc_y of things

class monkey():
    dimensions = (160, 240)

    mouth_timeout = 150 # ms before mouth opens again after closed

    move_factor = 0.1

    class mouth_tweak():
        amount = 65
        direction = -65


class arm():
    dimensions = (150, 40)
    position_factor = 0.4

    top_angle = 120
    bottom_angle = 260
    throw_angle =  170
    prepare_factor = 4
    throw_factor = 10
    rotation_error = 5

    # pixels to move the fruit so it fits inside the palm
    class fruit_tweak():
        amount = 25
        direction = -110

class fruit():
    dimensions = (60, 60)
    rot_inc_max = 360

    min_inc_x = -100
    max_inc_x = -1000
    max_init_inc_y = -550

    shrink = 2 # it shrinks from 1 to 0 when eaten. this parameter is the rate.
    rot_inc_extra = 5 # when shrinking, rotate faster by this factor

class collision():
    fruit_monkey = 40**2

class cloud():
    max_width = 300
    max_height = 140
    min_circles = 2
    max_circles = 6
    radius_factor = 0.21 # final radius is = max_width * radius_factor
    max_ix = 20
    delta = (100, 600) # width between clouds

class tree():
    dimensions = (140, 200)
    max_trees = 3

class yousuck(): # "you suck!" CoolZoom values
    rotation_count_range = (-1, 1)
    rotation_count_out_factor = 0.07
    zoom_times = (0.3, 0.65)
    color = (255, 90, 0)
    size = 100

class pause():
    background_image = 'food.jpg'
    font_family = "Tahoma"
    font_size = int(win_width / 32)
    font_color = (255, 0, 0)
