#!/usr/bin/env python
import numpy
from vizdoom import DoomGame, KILLCOUNT
from matplotlib import pyplot as plt
import random
import time

game = DoomGame()
# game.load_config("./Alectronic/alec.cfg")
game.load_config("./Alectronic/alec1.cfg")
game.init()

shoot = [1, 0, 0, 1]
turn_left = [0, 1, 0,0]
turn_right = [0, 0, 1,0]
actions = [shoot, turn_left,turn_left,turn_left, turn_right,turn_right,turn_right]

episodes = 10
resultplot = []
resultplotkill = []
for i in range(episodes):
    game.new_episode()
    misc = []
    while not game.is_episode_finished():
        state = game.get_state()
        #img = state.screen_buffer
        misc = state.game_variables
        reward = game.make_action(random.choice(actions))
        print(
            "reward:", game.get_total_reward(), misc
        )
        # print(state)
        time.sleep(0.0000002)
    print("Result:", game.get_total_reward(),
          " Time:", game.get_episode_timeout())
    time.sleep(2)

    resultplot.append(game.get_total_reward())
    resultplotkill.append(misc[2]*10)
    # time.sleep(2)


"""Plots the results using matplotlib"""
"""Converts the global result lists into numpy arrays for use in matplotlib"""
resultnpy = numpy.array(resultplot)
resultnpykill = numpy.array(resultplotkill)

x = numpy.linspace(0, len(resultnpy), len(resultnpy))
y = numpy.linspace(0, len(resultnpykill), len(resultnpykill))

with plt.style.context('fivethirtyeight'):
    """Graph for average fitness over time"""
    fig = plt.figure()
    fig.suptitle('Results Over Time', fontsize=14, fontweight='bold')
    plt.plot(x, resultnpy)
    plt.plot(y, resultnpykill)
    plt.show()

