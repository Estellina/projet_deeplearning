import random

class MontyHall:
    def __init__(self, num_doors=3):
        self.num_doors = num_doors
        self.reset()

    def reset(self):
        self.doors = ['goat'] * self.num_doors
        self.car = random.randint(0, self.num_doors - 1)
        self.doors[self.car] = 'car'
        self.chosen_door = None
        self.opened_door = None
        self.final_choice = None
        return self.doors

    def step(self, action):
        if self.chosen_door is None:
            self.chosen_door = action
            self.opened_door = self.open_other_door()
            return self.doors, 0, False
        else:
            self.final_choice = action
            reward = 1 if self.doors[self.final_choice] == 'car' else 0
            done = True
            return self.doors, reward, done

    def open_other_door(self):
        available_doors = [i for i in range(self.num_doors) if i != self.chosen_door and i != self.car]
        return random.choice(available_doors)

    def render(self):
        print(f"Doors: {self.doors}")
        print(f"Chosen door: {self.chosen_door}")
        print(f"Opened door: {self.opened_door}")
