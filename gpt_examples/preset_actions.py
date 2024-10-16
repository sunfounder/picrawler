
from time import sleep

BODY_LENGTH = 77
BODY_WIDTH = 77
BODY_DIAGONAL = 108.9
DELTA = 45 

def sit(spider):
    spider.do_action('sit', speed=60)


def stand(spider):
    spider.do_action('stand', speed=60)


def look_up(spider):
    # spider.do_action('look_up', speed=60)
    coords = [
        # stand
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -76], [45, 0, -76], [45, 0, -38], [45, 45, -30]],
    ]

    for coord in coords:
        spider.do_step(coord, 60)


def look_down(spider):
    # spider.do_action('look_down', speed=60)
    coords = [
        # stand
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -28], [45, 0, -40], [45, 0, -68], [45, 45, -76]],
    ]
    for coord in coords:
        spider.do_step(coord, 60)


def dance(spider):
    spider.do_action('dance', speed=95)



def wave_hand(spider):
    stand = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    wave_hand = [
        [[45, 45, -70], [50, 40, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [-20, 60, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [50, 40, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [-20, 60, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [50, 40, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [-20, 60, 120], [45, 0, -60], [45, 45, -30]],
    ]

    return_stand = [
        [[45, 45, -50], [45, 0, -30], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -40], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in stand:
        spider.do_step(coord, 80)
    for coord in wave_hand:
        spider.do_step(coord, 90)
    for coord in return_stand:
        spider.do_step(coord, 80)

def beckon(spider):
    stand = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    beckon = [
        [[45, 45, -70], [10, 60, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [10, 60, 50], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [10, 60, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [10, 60, 50], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [10, 60, 120], [45, 0, -60], [45, 45, -30]],
        [[45, 45, -70], [10, 60, 50], [45, 0, -60], [45, 45, -30]],
    ]

    return_stand = [
        [[45, 45, -50], [45, 0, -30], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -40], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in stand:
        spider.do_step(coord, 80)
    for coord in beckon:
        spider.do_step(coord, 90)
    for coord in return_stand:
        spider.do_step(coord, 80)


def shake_hand(spider):
    ready = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -65], [5, 280, 80], [45, 0, -60], [45, 45, -40]],
    ]

    shake_hand = [
        [[45, 45, -65], [5, 280, 100], [45, 0, -60], [45, 45, -40]],
        [[45, 45, -65], [5, 280, -10], [45, 0, -60], [45, 45, -40]],
        [[45, 45, -65], [5, 280, 100], [45, 0, -60], [45, 45, -40]],
        [[45, 45, -65], [5, 280, -10], [45, 0, -60], [45, 45, -40]],
        [[45, 45, -65], [5, 280, 100], [45, 0, -60], [45, 45, -40]],
        [[45, 45, -65], [5, 280, -10], [45, 0, -60], [45, 45, -40]],
        [[45, 45, -65], [5, 100, 10], [45, 0, -60], [45, 45, -40]],
        [[45, 45, -65], [5, 100, 10], [45, 0, -60], [45, 45, -40]],
    ]

    return_stand = [
        [[45, 45, -50], [45, 0, -30], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -40], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in ready:
        spider.do_step(coord, 80)
    sleep(.2)
    for coord in shake_hand:
        spider.do_step(coord, 82)
    for coord in return_stand:
        spider.do_step(coord, 80)


def fighting(spider):
    ready = [
        # stand
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        # fighting ready
        [[45, 45, -40], [45, 0, -40], [50, 20, -20], [45, 45, -50]],
        [[45, 45, -40], [45, 0, -40], [40, 20, -45], [45, 45, -50]],
        [[45, 45, -40], [45, 0, -40], [60, 40, -60], [45, 45, -40]],
        #
        [[45, 45, -40], [45, 30, -30], [60, 40, -60], [45, 45, -40]],
        [[45, 45, -30], [45, 30, -30], [60, 40, -60], [60, 40, -60]],
    ]

    twist_butt = [
        # twist butt
        [[55, 7, -30], [19, 48, -30], [77, 12, -60], [36, 63, -60]],
        [[19, 48, -30], [55, 7, -30], [36, 63, -60], [77, 12, -60]],
        #
        [[55, 7, -30], [19, 48, -30], [77, 12, -60], [36, 63, -60]],
        [[19, 48, -30], [55, 7, -30], [36, 63, -60], [77, 12, -60]],
        #      
        [[40, 30, -30], [40, 30, -30], [60, 40, -60], [60, 40, -60]],
        # shrink
        [[40, 60, -30], [40, 60, -30], [60, 10, -60], [60, 10, -60]],
    ]

    pounce_bite = [
        [[40, 40, -60], [20, 60, 110], [60, 60, -60], [60, 60, -60]],
        [[40, 40, -40], [20, 30, -40], [60, 60, -60], [60, 60, -60]],
        [[20, 60, 110], [20, 30, -60], [60, 60, -60], [60, 60, -60]],
        [[20, 30, -40], [20, 30, -40], [60, 60, -60], [60, 60, -60]],
    ]

    return_stand = [
        [[45, 45, -50], [45, 0, -30], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -40], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in ready:
        spider.do_step(coord, 80)
    for coord in twist_butt:
        spider.do_step(coord, 82)
    sleep(0.2)
    for coord in pounce_bite:
        spider.do_step(coord, 100)
    sleep(1)
    for coord in return_stand:
        spider.do_step(coord, 82)


def excited(spider):
    stand = [
        # stand
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    up_down = [
        # [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
        # [[45, 45, -80], [45, 0, -80], [45, 0, -80], [45, 45, -80]],
        # [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
        # [[45, 45, -80], [45, 0, -80], [45, 0, -80], [45, 45, -80]],
        # [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
        # [[45, 45, -80], [45, 0, -80], [45, 0, -80], [45, 45, -80]],

        [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
        [[45, 45, -65], [45, 0, -65], [45, 0, -65], [45, 45, -65]],
        [[45, 45, -70], [45, 0, -70], [45, 0, -70], [45, 45, -70]],

        [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
        [[45, 45, -65], [45, 0, -65], [45, 0, -65], [45, 45, -65]],
        [[45, 45, -75], [45, 0, -75], [45, 0, -75], [45, 45, -75]],

        [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
        [[45, 45, -65], [45, 0, -65], [45, 0, -65], [45, 45, -65]],
        [[45, 45, -80], [45, 0, -80], [45, 0, -80], [45, 45, -80]],
    ]

    return_stand = [
        [[45, 45, -30], [45, 0, -30], [45, 0, -30], [45, 45, -30]],
        [[45, 45, -65], [45, 0, -65], [45, 0, -65], [45, 45, -65]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in stand:
        spider.do_step(coord, 80)
    for coord in up_down:
        spider.do_step(coord, 95)
    for coord in return_stand:
        spider.do_step(coord, 80)

def play_dead(spider):
    sit = [
        # stand
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        #
        [[45, 45, -10], [45, 0, -10], [45, 0, -10], [45, 45, -10]],
    ]

    play_dead = [
        [[45, 45, 100], [45, 45, 100], [45, 45, 100], [45, 45, 100]],
        #
        [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
        [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
        [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
        [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
        [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
        [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
        [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
        [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
        [[45, 35, 60], [35, 45, 80], [35, 45, 80], [45, 35, 60]],
        [[35, 45, 80], [45, 35, 60], [45, 35, 60], [35, 45, 80]],
        #
        [[45, 45, 100], [45, 45, 100], [45, 45, 100], [45, 45, 100]],
    ]

    return_stand = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in sit:
        spider.do_step(coord, 60)
    for coord in play_dead:
        spider.do_step(coord, 85)
    for coord in return_stand:
        spider.do_step(coord, 60)


def nod(spider):
    stand = [
        # stand
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    nod = [
        [[45, 45, -80], [45, 0, -50], [45, 0, -20], [45, 45, -30]],
        [[45, 45, -20], [45, 0, -36], [45, 20, -52], [40, 20, -80]],
        [[45, 45, -80], [45, 0, -50], [45, 0, -20], [45, 45, -30]],
        [[45, 45, -20], [45, 0, -36], [45, 20, -52], [40, 20, -80]],
        [[45, 45, -80], [45, 0, -50], [45, 0, -20], [45, 45, -30]],
    ]

    return_stand = [
        [[45, 45, -80], [45, 0, -50], [45, 0, -40], [45, 45, -40]],
        [[45, 45, -60], [45, 0, -50], [45, 0, -40], [45, 45, -40]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in stand:
        spider.do_step(coord, 60)
    for coord in nod:
        spider.do_step(coord, 70)
    sleep(.2)
    for coord in return_stand:
        spider.do_step(coord, 80)
    sleep(1)


def shake_head(spider):
    ready = [
        # stand
        # [[45, 45, -50], [45, 0, -50], [45, 20, -50], [45, 45, -50]],
        # [[45, 45, -50], [45, 20, -30], [45, 20, -50], [45, 45, -50]],
        # [[45, 45, -50], [45, 45, -50], [45, 20, -50], [45, 45, -50]],

        [[45, 45, -50], [45, 20, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 20, -50], [45, 20, -30], [45, 45, -50]],
        [[45, 45, -50], [45, 20, -50], [45, 45, -50], [45, 45, -50]],
    ]

    twist_butt = [
        # twist butt
        [[55, 7, -50], [19, 48, -50], [77, 12, -50], [36, 63, -50]],
        [[19, 48, -50], [55, 7, -50], [36, 63, -50], [77, 12, -50]],
        #
        [[51, 15, -50], [27, 43, -50], [72, 22, -50], [45, 56, -50]],
        [[27, 43, -50], [51, 15, -50], [45, 56, -50], [72, 22, -50]],
        #
        [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
    ]

    return_stand = [
        # [[45, 45, -50], [45, 20, -30], [45, 0, -50], [45, 45, -50]],
        # [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],

        [[45, 45, -50], [45, 0, -50], [45, 20, -30], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in ready:
        spider.do_step(coord, 80)
    for coord in twist_butt:
        spider.do_step(coord, 90)
    sleep(.5)
    for coord in return_stand:
        spider.do_step(coord, 82)


def look_left(spider):
    stand = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    look_left = [
        [[45, 0, -50], [45, 45, -50], [45, 45, -50], [45, 0, -50]],
        [[0, 45, -50], [45, 45, -50], [45, 45, -50], [45, 0, -50]],
        [[0, 45, -50], [45, 45, -35], [45, 45, -50], [45, 0, -50]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in stand:
        spider.do_step(coord, 80)
    for coord in look_left:
        spider.do_step(coord, 80)


def look_right(spider):
    stand = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    look_right = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [0, 45, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -35], [0, 45, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 0, -50], [45, 45, -50], [45, 45, -50], [45, 0, -50]],
    ]

    for coord in stand:
        spider.do_step(coord, 80)
    for coord in look_right:
        spider.do_step(coord, 80)


def warm_up(spider):
    stand = [
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
    ]

    # left_right.append(spider.move_list.rotate_body_absolute_x(-25))
    left_right = [
        [[45, 37, -85], [45, 37, -14], [45, 37, -14], [45, 37, -85]],
        [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
        [[45, 37, -85], [45, 37, -14], [45, 37, -14], [45, 37, -85]],
        [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
        #
        [[45, 37, -14], [45, 37, -85], [45, 37, -85], [45, 37, -14]],
        [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
        [[45, 37, -14], [45, 37, -85], [45, 37, -85], [45, 37, -14]],
        [[45, 45, -50], [45, 45, -50], [45, 45, -50], [45, 45, -50]],
    ]

    clockwise = []
    clockwise.append(spider.move_list.move_body_absolute(0, 25, 10))
    clockwise.append(spider.move_list.move_body_absolute(12.5, 21.65, 10))
    clockwise.append(spider.move_list.move_body_absolute(21.65, 12.5, 10))
    clockwise.append(spider.move_list.move_body_absolute(25, 0, 10))
    clockwise.append(spider.move_list.move_body_absolute(21.65, -12.5, 10))
    clockwise.append(spider.move_list.move_body_absolute(12.5, -21.65, 10))
    clockwise.append(spider.move_list.move_body_absolute(0, -25, 10))
    clockwise.append(spider.move_list.move_body_absolute(-12.5, -21.65, 10))
    clockwise.append(spider.move_list.move_body_absolute(-21.65, -12.5, 10))
    clockwise.append(spider.move_list.move_body_absolute(-25, 0, 10))
    clockwise.append(spider.move_list.move_body_absolute(-21.65, 12.5, 10))
    clockwise.append(spider.move_list.move_body_absolute(-12.5, 21.65, 10))
    clockwise.append(spider.move_list.move_body_absolute(0, 25, 10))

    anticlockwise = []
    anticlockwise.append(spider.move_list.move_body_absolute(0, 25, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(-12.5, 21.65, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(-21.65, 12.5, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(-25, 0, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(-21.65, -12.5, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(-12.5, -21.65, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(0, -25, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(12.5, -21.65, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(21.65, -12.5, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(25, 0, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(21.65, 12.5, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(12.5, 21.65, 10))
    anticlockwise.append(spider.move_list.move_body_absolute(0, 25, 10))

    return_stand = [
        [[45, 45, -50], [45, 45, -40], [45, 0, -50], [45, 45, -50]],
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
    ]

    for coord in stand:
        spider.do_step(coord, 80)
    sleep(0.5)
    for coord in left_right:
        spider.do_step(coord, 75)
    sleep(.3)
    for coord in clockwise:
        spider.do_step(coord, 90)
    sleep(.3)
    for coord in anticlockwise:
        spider.do_step(coord, 90)
    sleep(.3)
    for coord in return_stand:
        spider.do_step(coord, 80)


def push_up(spider):
    ready = [
        # stand
        [[45, 45, -50], [45, 0, -50], [45, 0, -50], [45, 45, -50]],
        # 
        [[60, 10, -60], [60, 0, -60], [20, 60, 10], [10, 65, -40]],
        [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
    ]

    push_up = [
        [[70, 0, -40], [70, 0, -40], [0, 130, -40], [0, 130, -40]],
        [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
        [[70, 0, -40], [70, 0, -40], [0, 130, -40], [0, 130, -40]],
        [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
        [[70, 0, -40], [70, 0, -40], [0, 130, -40], [0, 130, -40]],
        [[70, 0, -76], [70, 0, -76], [0, 130, -40], [0, 130, -40]],
    ]

    for coord in ready:
        spider.do_step(coord,70)
    for coord in push_up:
        spider.do_step(coord, 80)


actions_dict = {
    "sit": sit,
    "stand": stand,
    # "turn_left": turn_left_angle,
    # "turn_right": turn_right_angle,
    # "dance": dance,
    "wave_hand": wave_hand,
    "beckon": beckon,
    "shake_hand": shake_hand,
    "fighting": fighting,
    "excited": excited,
    "play_dead": play_dead,
    "nod": nod,
    "shake_head": shake_head,
    # "look_left": look_left,
    # "look_right": look_right,
    "look_up": look_up,
    "look_down": look_down,
    "warm_up": warm_up,
    "push_up": push_up,
}


sounds_dict = {

}

if __name__ == "__main__":
    from picrawler import Picrawler

    my_spider = Picrawler()

    actions = list(actions_dict.keys())
    for i, key in enumerate(actions_dict):
        print(f'{i} {key}')

    last_key = None

    try:
        while True:
            key = input()

            if key == '':
                print(actions[last_key])
                actions_dict[actions[last_key]](my_spider)
            else:
                key = int(key)
                if key > (len(actions) - 1):
                    print("Invalid key")
                else:
                    last_key = key
                    print(actions[key])
                    actions_dict[actions[key]](my_spider)

            # sleep(2)
            # wave_hand(my_spider)
            # shake_hand(my_spider)
            # fighting(my_spider)
            # excited(my_spider)
            # play_dead(my_spider)
            # nod(my_spider)
            # shake_head(my_spider)
            # look_left(my_spider)
            # look_right(my_spider)
            # look_up(my_spider)
            # look_down(my_spider)
            # warm_up(my_spider)
            # push_up(my_spider)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f'Error:\n {e}')
    finally:
        my_spider.do_action("sit", speed=60)
        sleep(.1)




