import numpy as np

class GridWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.state = (0, 0)
        return self.state

    def step(self, action):
        x, y = self.state
        if action == 0 and y > 0:
            y -= 1
        elif action == 1 and y < self.height - 1:
            y += 1
        elif action == 2 and x > 0:
            x -= 1
        elif action == 3 and x < self.width - 1:
            x += 1
        self.state = (x, y)
        reward = 1 if self.state == (self.width - 1, self.height - 1) else 0
        done = self.state == (self.width - 1, self.height - 1)
        return self.state, reward, done

    def render(self):
        grid = np.zeros((self.height, self.width), dtype=str)
        grid[:] = '-'
        x, y = self.state
        grid[y, x] = 'A'
        print('\n'.join([''.join(row) for row in grid]))
