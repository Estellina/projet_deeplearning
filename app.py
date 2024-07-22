from init import LineWorld, GridWorld, RockPaperScissors, MontyHall, print_environment

# Exemple d'utilisation de LineWorld
env = LineWorld(10)
state = env.reset()
done = False
while not done:
    action = 1  # Toujours aller à droite pour cet exemple
    state, reward, done = env.step(action)
    print_environment(env)
print(f"Final reward: {reward}")

# Exemple d'utilisation de GridWorld
env = GridWorld(5, 5)
state = env.reset()
done = False
while not done:
    action = 1  # Toujours aller en bas pour cet exemple
    state, reward, done = env.step(action)
    print_environment(env)
print(f"Final reward: {reward}")

# Exemple d'utilisation de RockPaperScissors
env = RockPaperScissors()
state = env.reset()
done = False
while not done:
    action = 'rock'  # Toujours jouer 'rock' pour cet exemple
    state, reward, done = env.step(action)
    print_environment(env)
print(f"Final reward: {reward}")

# Exemple d'utilisation de MontyHall
env = MontyHall()
state = env.reset()
done = False
while not done:
    if env.chosen_door is None:
        action = 0  # Choisir la première porte
    else:
        action = 1  # Changer de porte
    state, reward, done = env.step(action)
    print_environment(env)
print(f"Final reward: {reward}")
