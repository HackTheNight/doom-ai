#!/usr/bin/env python

from vizdoom import DoomGame
from matplotlib import pyplot as plt
import random, time, numpy

game = DoomGame()
game.load_config("./custom-basic.cfg")
game.init()

shoot = [1, 0, 0, 0, 0, 0, 0, 0]
left = [0, 1, 0, 0, 0, 0, 0, 0]
right = [0, 0, 1, 0, 0, 0, 0, 0]
forward = [0, 0, 0, 1, 0, 0, 0, 0]
backward = [0, 0, 0, 0, 1, 0, 0, 0]
turn_left = [0, 0, 0, 0, 0, 1, 0, 0]
turn_right = [0, 0, 0, 0, 0, 0, 1, 0]
jump = [0, 0, 0, 0, 0, 0, 0, 1]
actions = [shoot, left, right, forward, backward, turn_left, turn_right, jump]

episodes = 10
resultplot = []

for i in range(episodes):
    game.new_episode()
    while not game.is_episode_finished():
        state = game.get_state()
        img = state.screen_buffer
        misc = state.game_variables
        reward = game.make_action(random.choice(actions))
        print("reward:", reward)
        time.sleep(0.02)
    print("Result:", game.get_total_reward())
    resultplot.append(game.get_total_reward())
    time.sleep(2)


"""Plots the results using matplotlib"""
"""Converts the global result lists into numpy arrays for use in matplotlib"""
resultnpy = numpy.array(resultplot)

x = numpy.linspace(0, len(resultnpy), len(resultnpy))

with plt.style.context('fivethirtyeight'):
    """Graph for average fitness over time"""
    fig = plt.figure()
    fig.suptitle('Results Over Time', fontsize=14, fontweight='bold')
    plt.plot(x, resultnpy, color='red')
    plt.show()
