win_width =  800
win_height = 600

clear_color = (120, 200, 255)

images = 'images/'

class monkey():
    dimensions = (160, 240)

class arm():
    dimensions = (150, 40)
    factor = 0.4

    # pixels to move the fruit so it fits inside the palm
    class fruit_tweak():
        ammount = 25
        direction = -110

class fruit():
    dimensions = (60, 60)
    rot_inc_max = 360
