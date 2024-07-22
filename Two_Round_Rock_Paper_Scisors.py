import random


class RockPaperScissors:
    def __init__(self):
        self.actions = ['rock', 'paper', 'scissors']
        self.reset()

    def reset(self):
        self.round = 1
        self.history = []
        return self.history

    def step(self, action):
        if self.round == 1:
            opponent_action = random.choice(self.actions)
        else:
            opponent_action = self.history[0]

        self.history.append((action, opponent_action))
        reward = self.get_reward(action, opponent_action)
        self.round += 1
        done = self.round > 2
        return self.history, reward, done

    def get_reward(self, action, opponent_action):
        if action == opponent_action:
            return 0
        elif (action == 'rock' and opponent_action == 'scissors') or \
                (action == 'paper' and opponent_action == 'rock') or \
                (action == 'scissors' and opponent_action == 'paper'):
            return 1
        else:
            return -1

    def render(self):
        print(f"Round {self.round - 1}: {self.history[-1]}")
