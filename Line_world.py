import numpy as np

class LineWorld:
    def __init__(self, size):
        self.size = size
        self.reset()

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == 0:
            self.state = max(0, self.state - 1)
        elif action == 1:
            self.state = min(self.size - 1, self.state + 1)
        reward = 1 if self.state == self.size - 1 else 0
        done = self.state == self.size - 1
        return self.state, reward, done

    def render(self):
        print('-' * self.size)
        print(' ' * self.state + 'A' + ' ' * (self.size - self.state - 1))
        print('-' * self.size)

# Example usage
env = LineWorld(10)

env.render()
