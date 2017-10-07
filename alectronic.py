#!/usr/bin/env python

from vizdoom import DoomGame
import random
import time

game = DoomGame()
# game.load_config("./Alectronic/alec.cfg")
game.load_config("./Alectronic/alec1.cfg")
game.init()

shoot = [1, 0, 0, ]
turn_left = [0, 1, 0]
turn_right = [0, 0, 1]
actions = [shoot, turn_left, turn_right]

episodes = 100
# for i in range(episodes):
while True:
    game.new_episode()
    while not game.is_episode_finished():
        state = game.get_state()
        #img = state.screen_buffer
        misc = state.game_variables
        reward = game.make_action(random.choice(actions))
        # print("reward:", reward)
        # print(state)
        time.sleep(0.002)
    print("Result:", game.get_total_reward(),
          " Time:", game.get_episode_timeout())
    time.sleep(2)
