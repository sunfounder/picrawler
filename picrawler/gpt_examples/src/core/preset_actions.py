from time import sleep
import time

BODY_LENGTH = 77
BODY_WIDTH = 77
BODY_DIAGONAL = 108.9
DELTA = 45


def sit(spider, speed=40):
    spider.do_action("sit", speed=speed)


def stand(spider, speed=40):
    spider.do_action("stand", speed=speed)


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
    spider.do_action("dance", speed=95)


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
    sleep(0.2)
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
    sleep(0.2)
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
    sleep(0.5)
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
    sleep(0.3)
    for coord in clockwise:
        spider.do_step(coord, 90)
    sleep(0.3)
    for coord in anticlockwise:
        spider.do_step(coord, 90)
    sleep(0.3)
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
        spider.do_step(coord, 70)
    for coord in push_up:
        spider.do_step(coord, 80)


def walk_forward(spider, steps=3, speed=40):
    """Walk forward a few steps"""
    print("Walking forward...")
    try:
        for _ in range(steps):
            spider.do_action("forward", speed=speed)
            sleep(0.2)
        return True
    except Exception as e:
        print(f"Error walking forward: {e}")
        return False


def walk_backward(spider, steps=3, speed=40):
    """Walk backward a few steps"""
    print("Walking backward...")
    try:
        for _ in range(steps):
            spider.do_action("backward", speed=speed)
            sleep(0.2)
        return True
    except Exception as e:
        print(f"Error walking backward: {e}")
        return False


def move_closer(spider, steps=2, speed=40):
    """Move closer to something (walk forward)"""
    print("Moving closer...")
    walk_forward(spider, steps, speed)
    return True


def explore(spider, speed=40):
    """Execute a simple exploration pattern"""
    print("Exploring the environment...")
    try:
        walk_forward(spider, 2, speed)
        look_up(spider)
        sleep(0.5)
        look_down(spider)
        sleep(0.5)
        walk_forward(spider, 1, speed)
        return True
    except Exception as e:
        print(f"Error during exploration: {e}")
        return False


def turn_left(spider, degrees=45, speed=40):
    """Turn the robot left by the specified degrees"""
    print(f"Turning left {degrees} degrees...")
    try:
        spider.do_action("turn_left", speed=speed)
        return True
    except Exception as e:
        print(f"Error turning left: {e}")
        return False


def turn_right(spider, degrees=45, speed=40):
    """Turn the robot right by the specified degrees"""
    print(f"Turning right {degrees} degrees...")
    try:
        spider.do_action("turn_right", speed=speed)
        return True
    except Exception as e:
        print(f"Error turning right: {e}")
        return False


def zigzag(spider, steps=3, speed=40):
    """Move in a zigzag pattern"""
    print("Moving in zigzag pattern...")
    try:
        for i in range(steps):
            walk_forward(spider, 2, speed)
            if i % 2 == 0:
                turn_left(spider)
            else:
                turn_right(spider)
        return True
    except Exception as e:
        print(f"Error during zigzag: {e}")
        return False


def circle(spider, speed=40):
    """Move in a circular pattern"""
    print("Moving in a circle...")
    try:
        walk_forward(spider, 1, speed)
        for _ in range(8):  # 8 segments to make a full circle
            turn_right(spider, 45)
            walk_forward(spider, 1, speed)
        return True
    except Exception as e:
        print(f"Error during circle movement: {e}")
        return False


def patrol(spider, iterations=2, speed=40):
    """Patrol a rectangular area"""
    print("Starting patrol...")
    try:
        for _ in range(iterations):
            walk_forward(spider, 3, speed)
            turn_right(spider, 90)
            walk_forward(spider, 2, speed)
            turn_right(spider, 90)
            walk_forward(spider, 3, speed)
            turn_right(spider, 90)
            walk_forward(spider, 2, speed)
            turn_right(spider, 90)
        return True
    except Exception as e:
        print(f"Error during patrol: {e}")
        return False


def random_explore(spider, moves=5, speed=40):
    """Move randomly to explore the environment"""
    import random

    print("Starting random exploration...")
    try:
        for _ in range(moves):
            # Choose a random action
            action = random.choice(
                ["forward", "turn_left", "turn_right", "look_up", "look_down"]
            )
            if action == "forward":
                walk_forward(spider, random.randint(1, 3), speed)
            elif action == "turn_left":
                turn_left(spider, random.randint(15, 90))
            elif action == "turn_right":
                turn_right(spider, random.randint(15, 90))
            elif action == "look_up":
                look_up(spider)
            elif action == "look_down":
                look_down(spider)
            sleep(0.5)
        return True
    except Exception as e:
        print(f"Error during random exploration: {e}")
        return False


def curious(spider, speed=40):
    """Act curious about something"""
    print("Acting curious...")
    try:
        # Look around with excitement
        look_up(spider)
        sleep(0.3)
        look_down(spider)
        sleep(0.3)
        # Approach carefully
        move_closer(spider, 1, speed)
        sleep(0.2)
        # Tilt head and look
        look_up(spider)
        sleep(0.2)
        # Show excitement
        excited(spider)
        return True
    except Exception as e:
        print(f"Error during curious behavior: {e}")
        return False


def search_around(spider):
    """Search around the environment systematically."""
    # First look up
    look_up(spider)
    time.sleep(0.5)

    # Then look left
    turn_left(spider)
    time.sleep(0.5)

    # Then look right (back to center and then right)
    turn_right(spider)
    time.sleep(0.5)
    turn_right(spider)
    time.sleep(0.5)

    # Back to center
    turn_left(spider)
    time.sleep(0.5)

    # Finally look down
    look_down(spider)
    time.sleep(0.5)

    # Return to normal position
    spider.do_action("stand", speed=40)


def look_around(spider):
    """Look around in different directions to observe surroundings."""
    # Look up first
    look_up(spider)
    time.sleep(0.8)

    # Look down
    look_down(spider)
    time.sleep(0.8)

    # Look left
    turn_left(spider)
    time.sleep(0.8)

    # Look right (turning from left position requires two right turns to look right)
    turn_right(spider)
    time.sleep(0.5)
    turn_right(spider)
    time.sleep(0.8)

    # Return to center
    turn_left(spider)
    time.sleep(0.5)

    # Return to normal position
    spider.do_action("stand", speed=40)


def idle_motion(spider, duration=5, speed=30):
    """Subtle movements to appear more alive when idle"""
    print("Performing idle motions...")
    import random, time

    try:
        start_time = time.time()
        while time.time() - start_time < duration:
            action = random.choice(
                ["slight_look_up", "slight_look_down", "slight_turn"]
            )
            if action == "slight_look_up":
                # Just a tiny movement upward
                spider.do_action("body_up", speed=speed)
            elif action == "slight_look_down":
                # Just a tiny movement downward
                spider.do_action("body_down", speed=speed)
            elif action == "slight_turn":
                # Small rotation
                if random.choice([True, False]):
                    turn_left(spider, 10, speed)
                else:
                    turn_right(spider, 10, speed)
            sleep(random.uniform(0.5, 1.5))
        return True
    except Exception as e:
        print(f"Error during idle motion: {e}")
        return False


def greeting(spider, speed=40):
    """Perform a friendly greeting"""
    print("Greeting...")
    try:
        # Stand tall
        stand(spider, speed)
        sleep(0.3)

        # Wave hello
        wave_hand(spider)
        sleep(0.5)

        # Show excitement
        excited(spider)

        return True
    except Exception as e:
        print(f"Error during greeting: {e}")
        return False


def smile(spider):
    """
    Simulates a smiling action by performing a happy motion.
    Since the robot doesn't have a face to smile, this uses head movement to simulate happiness.
    """
    try:
        # Use only spider.do_action which is safer than direct servo control
        # First stand properly
        spider.do_action("stand", speed=40)
        time.sleep(0.3)

        # Look up slightly (like a happy expression)
        spider.do_action("look_up", speed=30)
        time.sleep(0.4)

        # Return to center position
        spider.do_action("stand", speed=40)
        time.sleep(0.2)

        # Do a little excited wiggle
        spider.do_action("body_right", speed=30)
        time.sleep(0.2)
        spider.do_action("body_left", speed=30)
        time.sleep(0.2)

        # Return to standard position
        spider.do_action("stand", speed=40)

        # Briefly show excitement
        try:
            excited(spider)
        except Exception as e:
            print(f"Error executing excited() during smile: {e}")

        # Make sure we end in a standing position
        spider.do_action("stand", speed=40)
        return True
    except Exception as e:
        print(f"Error processing action smile: {e}")
        # Make sure we're in a safe state
        try:
            spider.do_action("stand", speed=40)
        except:
            pass
        return False


actions_dict = {
    "sit": sit,
    "stand": stand,
    "wave_hand": wave_hand,
    "beckon": beckon,
    "shake_hand": shake_hand,
    "fighting": fighting,
    "excited": excited,
    "play_dead": play_dead,
    "nod": nod,
    "shake_head": shake_head,
    "look_up": look_up,
    "look_down": look_down,
    "warm_up": warm_up,
    "push_up": push_up,
    "walk_forward": walk_forward,
    "walk_backward": walk_backward,
    "move_closer": move_closer,
    "explore": explore,
    "turn_left": turn_left,
    "turn_right": turn_right,
    "zigzag": zigzag,
    "circle": circle,
    "patrol": patrol,
    "random_explore": random_explore,
    "curious": curious,
    "search_around": search_around,
    "idle_motion": idle_motion,
    "greeting": greeting,
    "look_around": look_around,
    "smile": smile,
}


sounds_dict = {}

if __name__ == "__main__":
    from picrawler import Picrawler

    my_spider = Picrawler()

    actions = list(actions_dict.keys())
    for i, key in enumerate(actions_dict):
        print(f"{i} {key}")

    last_key = None

    try:
        while True:
            key = input()

            if key == "":
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
        print(f"Error:\n {e}")
    finally:
        my_spider.do_action("sit", speed=60)
        sleep(0.1)
