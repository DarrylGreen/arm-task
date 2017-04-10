from collections import deque
from random import randint


class Worker(object):
    """This class tracks what a worker is holding and
     how much time has been spent assembling the product"""
    def __init__(self):
        super(Worker, self).__init__()
        self.items = set([])
        self.assembly_count_time = 0

    def assemble_product(self):
        if self.items == set(['A', 'B']):
            self.assembly_count_time += 1
        if self.assembly_count_time >= 4:
            self.items = set(['F'])
            self.assembly_count_time = 0


class Conveyor(object):
    """This class tracks the conveyor belt and the workers on the belt"""
    def __init__(self, belt_length):
        super(Conveyor, self).__init__()
        self.belt_length = belt_length
        self.belt = deque([' ' for i in range(belt_length + 1)],
                          maxlen=belt_length + 1)
        self.top_workers = [Worker() for i in range(belt_length)]
        self.bottom_workers = [Worker() for i in range(belt_length)]
        self.finished_items = 0
        self.untouched_A_components = 0
        self.untouched_B_components = 0

    def add_random_item_to_belt(self):
        random_number = randint(0,2)
        if random_number == 0:
            self.belt.appendleft('A')
        elif random_number == 1:
            self.belt.appendleft('B')
        else:
            self.belt.appendleft(' ')

    def handle_component_at_position(self, position, component, other_component):
        if self.top_workers[position].items == set([other_component]):
            self.belt[position] = ' '
            self.top_workers[position].items.add(component)
        elif self.bottom_workers[position].items == set([other_component]):
            self.belt[position] = ' '
            self.bottom_workers[position].items.add(component)
        elif len(self.top_workers[position].items) == 0:
            self.belt[position] = ' '
            self.top_workers[position].items.add(component)
        elif len(self.bottom_workers[position].items) == 0:
            self.belt[position] = ' '
            self.bottom_workers[position].items.add(component)

    def handle_empty_space_at_position(self, position):
        if 'F' in self.top_workers[position].items:
            self.belt[position] = 'F'
            self.top_workers[position].items.discard('F')
        elif 'F' in self.bottom_workers[position].items:
            self.belt[position] = 'F'
            self.bottom_workers[position].items.discard('F')

    def handle_belt_position(self, position):
        if self.belt[position] == ' ':
            self.handle_empty_space_at_position(position)
        elif self.belt[position] == 'A':
            self.handle_component_at_position(position, 'A', 'B')
        elif self.belt[position] == 'B':
            self.handle_component_at_position(position, 'B', 'A')

    def check_end_of_belt(self):
        if self.belt[-1] == 'F':
            self.finished_items += 1
        elif self.belt[-1] == 'A':
            self.untouched_A_components += 1
        elif self.belt[-1] == 'B':
            self.untouched_B_components += 1

    def advance_belt_one_step(self):
        self.add_random_item_to_belt()
        for i in range(self.belt_length):
            self.handle_belt_position(i)
            self.top_workers[i].assemble_product()
            self.bottom_workers[i].assemble_product()
        self.check_end_of_belt()


if __name__ == "__main__":
    conveyor = Conveyor(3)
    for j in range(100):
        conveyor.advance_belt_one_step()
    print('Finished products: {}'.format(conveyor.finished_items))
    print('Untouched A components: {}'.format(conveyor.untouched_A_components))
    print('Untouched B components: {}'.format(conveyor.untouched_B_components))