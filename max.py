__author__ = 'max'


#!/usr/bin/env python

from vizdoom import DoomGame
import random
import time

game = DoomGame()
game.load_config("Max/basic.cfg")
#game.load_config('scenario-configs/deadly_corridor.wad')
game.init()

left = [1,0,0 ,0 , 0, 1, 0, 0]
right = [0,1,0 ,0 , 0, 1, 0, 0]
forward = [0,0,1 ,0 , 0, 1, 0, 0]
backward = [0,0,0 ,1 , 0, 1, 0, 0]
jump = [0,0,0 ,0 , 1, 1, 0, 0]
attack=[0,0,0 ,0 , 0, 1, 0, 0]
tleft=[0,0,1 ,0 , 0, 0, 1, 0]
tright=[0,0,1 ,0 , 0, 0, 0, 1]
actions = [left, right, forward, backward, jump, attack, tleft, tright]

episodes = 300
for i in range(episodes):
    game.new_episode()
    while not game.is_episode_finished():
        state = game.get_state()
        img = state.screen_buffer
        misc = state.game_variables
        reward = game.make_action(random.choice(actions))
        print("reward:", reward)
        time.sleep(0.02)
        print(state)
    print("Result:", game.get_total_reward())
    time.sleep(2)
