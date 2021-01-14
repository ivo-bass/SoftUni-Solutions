from collections import deque
from datetime import datetime, timedelta

END_COMMAND = 'End'


class Robot:
    def __init__(self, n, pr_t):
        self.name = n
        self.production_time = pr_t
        self.is_working = False
        self.time_left = pr_t

    # ____ For debugging ____
    # def __repr__(self):
    #     return f'{self.name}|{self.production_time}|{self.time_left}|{self.is_working}'


def get_data():
    robots_input = input().split(';')
    robots_queue = deque()
    for r in robots_input:
        name, production_time = r.split('-')
        production_time = int(production_time)
        robots_queue.append(Robot(name, production_time))

    time = datetime.strptime(input(), '%H:%M:%S')

    product_queue = deque()
    while True:
        product_input = input()
        if product_input == END_COMMAND:
            break
        product_queue.append(product_input)
    return robots_queue, time, product_queue


def main():
    robots, time, products = get_data()
    free_robots = robots.copy()
    busy_robots = []
    list_to_remove = []

    while products:
        time = time + timedelta(seconds=1)
        product = products.popleft()

        if free_robots:
            working_robot = free_robots.popleft()
            working_robot.is_working = True
            busy_robots.append(working_robot)
            print(
                f'{working_robot.name} - {product} [{time.strftime("%H:%M:%S")}]')
        elif not free_robots:
            products.append(product)

        for rob in busy_robots:
            rob.time_left -= 1
            if rob.time_left <= 0:
                rob.is_working = False
                rob.time_left = rob.production_time
                free_robots.append(rob)
                list_to_remove.append(rob)

        for r in robots:
            if not r.is_working and r in busy_robots:
                busy_robots.remove(r)


if __name__ == '__main__':
    main()
