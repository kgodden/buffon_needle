__author__ = 'Kevin Godden'

import matplotlib.pyplot as plt
from random import *
import sys
from math import *
import numpy as np

def draw_board(fig, d, gwidth, gheight):
    # Draw the board onto which the needles will be thrown
    # we will draw 3 vertical lines at a distance of d apart
    #

    x_off = 0

    plt.plot(0, 0)
    plt.plot(gwidth, 0)

    plt.plot([x_off, x_off], [0, gheight], 'k-', lw=1)
    plt.plot([x_off + d, x_off + d], [0, gheight], 'k-', lw=1)
    plt.plot([x_off + 2 * d, x_off + 2 * d], [0, gheight], 'k-', lw=1)

    
def pick_random_point_on_unit_circle():
    # Randomly pick a point on a unit circle
    # This function deliberately does not use
    # the value of Pi or any of the trig. functions.
    # (as I reckon that's cheating if your trying to
    # estimate Pi in the first place!!)
    #
    # see: http://mathworld.wolfram.com/CirclePointPicking.html
    #

    x1 = 0
    x2 = 0
    s = 1

    # Find a point on the unit circle centred at the origin.
    #
    # We need s < 1 before we can use
    # the values of x1 and x2
    while s >= 1:
        x1 = np.random.uniform(low=-1.0, high=1.0 + sys.float_info.epsilon)
        x2 = np.random.uniform(low=-1.0, high=1.0 + sys.float_info.epsilon)

        s = x1 * x1 + x2 * x2

    # now, calculate point on circle
    x = (x1 ** 2 - x2 ** 2) / (x1 ** 2 + x2 ** 2)
    y = (2 * x1 * x2) / (x1 ** 2 + x2 ** 2)

    return x, y


def pick_point_on_circle(ox, oy, r):

    ux, uy = pick_random_point_on_unit_circle()

    # Now we want to map this point onto a circle
    # of radius r

    # Calculate slope of line from
    # centre/origin to point
    m = uy / ux

    # And extend out the point along this slope
    # onto the larger circle
    x1 = sqrt((r ** 2) / (1 + m ** 2))

    # Make sure we have the correct sign
    if ux < 0:
        x1 = -x1

    # Calculate y using the slope
    y1 = m * x1

    # Pass it through the circle centre
    # to get the second point
    x2 = -x1
    y2 = -y1

    # Translate to desired centre
    return [ox + x1, oy + y1], [ox + x2, oy + y2]

def check_needle(sharp, blunt, d):
    # Check if a needle has crossed a line
    #
    # sharp - coordinate of 'sharp' end
    # blunt - coordinate of 'blunt' end
    #

    # Get coordinates
    x1, y1 = sharp[0], sharp[1]
    x2, y2 = blunt[0], blunt[1]

    # Re assign our ends so that the needles
    # logically lie left to right to make analysis
    # easier (this won't change the portability that
    # the needle crosses a line)
    if x2 < x1:
        x1, x2 = x2, x1

    cross = False

    # check if we're crossing the line
    # the line is located at y=d, so if one
    # point is < d and the other one > d
    # then we cross it...
    if x1 <= d and x2 >= d:
        cross = True

    return cross


def throw_needles(l, d, number_throws, fig, want_graphics):
    # randomly throw multiple needles on length l onto
    # the board and see how many cross the line
    throws = 0.0
    hits = 0.0

    for i in range(1, number_throws):
        if throws % 500 == 0:
            print("Throw %d " % throws)

        throws += 1

        # Now we 'throw' the needle, we model this as a randomly picked
        # diameter of a circle of radius l / 2 whose centre is also readonly
        # picked.  It is easy to pick a diameter with uniform distribution,
        # we can just pick an angle between 0 and 2Pi and use cos and sin to
        # calculate the corresponding cartesian coordinates of the end points,
        # however this seems like a huge cheat when you are trying to estimate
        # the value of Pi in the first place.  So we use a different method to
        # pick a random point on a unit circle that doesn't employ the value of
        # pi or functions like acos() or asin()

        # Centre of needle, the line is located at y=d and
        # so we let x range from [d / 2, 1.5 * d]
        ox = np.random.uniform(low=d / 2.0, high=d * 1.5 + sys.float_info.epsilon)

        # Y's value doesn't really matter for the
        # estimation of Pi, but we pick a random value
        # anyway so that we can draw the needle...
        oy = uniform(50, 350)

        radius = l / 2.0

        # We imagine that the needle has a 'sharp'
        # and a 'blunt' end.
        sharp_end, blunt_end = pick_point_on_circle(ox, oy, radius)

        xs = [sharp_end[0], blunt_end[0]]
        ys = [sharp_end[1], blunt_end[1]]

        # Draw needles that don't cross as green
        c = 'green'

        # Check if this needle crosses the line
        if check_needle(sharp_end, blunt_end, d):
            # yes it does..
            hits += 1
            c = 'red'

        # draw the needle
        if want_graphics:
            plt.plot(xs, ys, color=c)
            plt.scatter(xs[0], ys[0], color=c,s=1)
            plt.scatter(xs[1], ys[1], color=c,s=1)

    # Calculate the ration of hits to throws
    p = hits / throws

    # Now estimate Pi, see:
    # https://en.wikipedia.org/wiki/Buffon%27s_needle_problem
    #
    pie = 2 * l / (p * d)

    print "Pi is about %f" % pie


def buffon_needle():

    # Graphics width & Height
    gheight = 400
    gwidth = 300

    # Distance between the lines
    d = 100

    # The length of the needle
    l = 99

    # Set this to True if you want to
    # draw the needles on the board
    # it runs slower when we draw..
    want_graphics = True

    # How many times should we throw the
    # needle?
    number_of_throws = 5000

    fig = plt.figure()
    plt.gca().set_aspect('equal', adjustable='box')

    draw_board(fig, d, gwidth, gheight)
    throw_needles(l, d, number_of_throws, fig, want_graphics)
    fig.show()


if __name__== "__main__":
  buffon_needle()
