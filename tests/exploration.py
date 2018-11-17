#!/usr/bin/env python3

# NATIVE IMPORTS

# THIRD PARTY IMPORTS
import numpy as np

def break_point_range(p1, p2, resolution):
    if p1 <= p2:
        i = p1 + resolution/2
        while i < p2:
            yield i
            i += resolution
    else:
        i = p1 - resolution/2
        while i > p2:
            yield i
            i -= resolution

def measurement_to_coordinate(
        robot_coordinate, distance, robot_angle,
        sensor_relative_angle):
    alpha = robot_angle + sensor_relative_angle
    theta = np.array([
        [np.cos(alpha)],
        [np.sin(alpha)]
    ])
    return robot_coordinate + distance * theta


class Grid:
    def __init__(self, resolution=1, change_rate=0.7):
        self.resolution = resolution
        self._grid = {}
        self._change_rate = change_rate

    @property
    def resolution(self):
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        if not isinstance(value, int):
            raise ValueError("Grid resolution must be positive integer!")
        self._resolution = value

    @property
    def change_rate(self):
        return self._change_rate

    @property
    def negative_change_rate(self):
        return 1 - self.change_rate

    @change_rate.setter
    def change_rate(self, value):
        self._change_rate = value

    def get_probability_at_coordinate(self, coordinate):
        if coordinate not in self._grid:
            return 0.5
        else:
            return self._grid[coordinate]

    @property
    def grid(self):
        return self._grid.items()

    def get_squares_affected(self, measuring_coordinate, measured_coordinate):
        x1, y1 = measuring_coordinate.T[0]
        x2, y2 = measured_coordinate.T[0]
        if x1 == x2:
            # vertical line!
            x = lambda y: x1
        else:
            a = (y2-y1) / (x2-x1)
            b = y2 - a*x2
            x = lambda y: (y-b)/a

        x_start = i = round(x1/self.resolution)*self.resolution
        x_end = i_end = round(x2/self.resolution)*self.resolution
        y_start = j = round(y1/self.resolution)*self.resolution
        y_end = j_end = round(y2/self.resolution)*self.resolution
        i = int(i)
        j = int(j)
        i_end = int(i_end)
        j_end = int(j_end)
        i_dir = self.resolution if i_end >= i else -self.resolution
        j_dir = self.resolution if j_end >= j else -self.resolution
        left_to_right = i_end >= i
        x_breaks = list(break_point_range(x_start, x_end, self.resolution))
        y_breaks = list(break_point_range(y_start, y_end, self.resolution))
        y_breaks_xes = list((x(y) for y in y_breaks))

        x_pointer = 0
        y_pointer = 0
        xb_len = len(x_breaks)
        yb_len = len(y_breaks)

        while x_pointer < xb_len and y_pointer < yb_len:
            yield [(i, j), False]
            x_break_smaller = x_breaks[x_pointer] < y_breaks_xes[y_pointer]
            if      (left_to_right and x_break_smaller) or \
                    (not left_to_right and not x_break_smaller):
                i += i_dir
                x_pointer += 1
            elif    (left_to_right and not x_break_smaller) or \
                    (not left_to_right and x_break_smaller):
                j += j_dir
                y_pointer += 1
            else:
                i += i_dir
                j += j_dir
                x_pointer += 1
                y_pointer += 1

        while x_pointer < xb_len:
            yield [(i, j), False]
            i += i_dir
            x_pointer += 1

        while y_pointer < yb_len:
            yield [(i, j), False]
            j += j_dir
            y_pointer += 1

        yield [(i, j), True]

    def add_measurement(self, measuring_coordinate, measured_coordinate):
        squares_affected = self.get_squares_affected(measuring_coordinate, measured_coordinate)
        for square in squares_affected:
            p = self.get_probability_at_coordinate(square[0])
            if square[1]:
                p = self.change_rate + p*self.negative_change_rate
            else:
                p = p*self.negative_change_rate
            self._grid[square[0]] = p

    def _get_distance_to_wall(self, coordinate, angle):
        x, y = coordinate.flatten()
        angle = angle % (np.pi*2)
        i_start = i = round(x/self.resolution)*self.resolution
        j_start = j = round(y/self.resolution)*self.resolution
        if angle in [np.pi/2, np.pi*3/2]:
            while True:
                if (i, j) in self._grid:
                    if self._grid[(i, j)] > 0.5:
                        return abs(i - i_start)
                else:
                    return None
                i += self.resolution
        elif angle in [0.0, np.pi]:
            while True:
                if (i, j) in self._grid:
                    if self._grid[(i, j)] > 0.5:
                        return abs(j - j_start)
                else:
                    return None
                j += self.resolution
        else:
            going_left = np.pi/2 <= angle < np.pi*3/2
            #going_down = angle > np.pi
            a = np.tan(angle)
            b = y - a*x
            x_at_y = lambda y: (y-b)/a
            next_x_cross = i_start + self.resolution/2
            next_y_cross = j_start + self.resolution/2
            next_y_cross_x = x_at_y(next_y_cross)
            while True:
                if (i, j) in self._grid:
                    if self._grid[(i, j)] > 0.5:
                        return np.sqrt((i-i_start)**2 + (j-j_start)**2)
                else:
                    return None
                x_cross_is_next = (next_x_cross > next_y_cross_x) \
                    if going_left else (next_x_cross < next_y_cross_x)
                if next_x_cross == next_y_cross_x:
                    next_x_cross += self.resolution
                    next_y_cross += self.resolution
                    next_y_cross_x = x_at_y(next_y_cross)
                    i += self.resolution
                    j += self.resolution
                elif x_cross_is_next:
                    next_x_cross += self.resolution
                    i += self.resolution
                else:
                    next_y_cross += self.resolution
                    next_y_cross_x = x_at_y(next_y_cross)
                    j += self.resolution


    def _calculate_particle_prob(self, particle, measurements, expected_distances):
        # measurement is [robot_angle, sensor_relative_angle, distance]
        p = 1
        for measurement, expected_distance in zip(measurements, expected_distances):
            if expected_distance is not None:
                distance_diff = expected_distance - measurement[2]
                percentual_diff = distance_diff / expected_distance
                p = p * percentual_diff
        return p

    def estimate_position(self, last_known_coordinate, measurements, nr_particles = 10, spread=1):
        # calculate expected distances
        expected_distances = []
        for measurement in measurements:
            total_angle = measurement[0] + measurement[1]
            expected_distance = self._get_distance_to_wall(last_known_coordinate, total_angle)
            expected_distances.append(expected_distance)
        # generate particles
        # calc probability for each particle based on measurements
        particles = []
        for i in range(nr_particles):
            coord = last_known_coordinate + np.random.normal(loc=last_known_coordinate, scale=spread)
            prob = self._calculate_particle_prob(coord, measurements, expected_distances)
            particles.append([prob, coord])
        prob = self._calculate_particle_prob(last_known_coordinate, measurements, expected_distances)
        particles.append([prob, last_known_coordinate])
        # return coordinate with highest probability
        return sorted(particles, key=lambda p: p[0])[-1][1]


if __name__ == "__main__":
    if False:
        g = Grid(resolution=1, change_rate=0.7)
        c1 = np.array([
            [0.],
            [0.]
        ])
        c2 = np.array([
            [9.],
            [4.]
        ])
        g.add_measurement(c1, c2)
        for thing in g.grid:
            print(thing)

        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.set_aspect(1.0)
        for sq in g.grid:
            plt.scatter(sq[0][0], sq[0][1], s=10, color="BLACK", alpha=sq[1], marker="s")
        plt.show()

    if True:
        MEASUREMENTS = 1000
        angle_step = 2*np.pi / MEASUREMENTS
        robot_coordinates = np.array([
            [6.],
            [8.5]
        ])
        robot_coordinates = [robot_coordinates]*MEASUREMENTS
        distances = list(map(lambda x: 20.0+np.random.normal(0,1), range(MEASUREMENTS)))
        robot_angles = [0.0]*MEASUREMENTS
        sensor_relative_angles = list(map(lambda x: angle_step*x, range(MEASUREMENTS)))

        list_trace = []
        trace = []
        for r, d, a, b in zip(robot_coordinates, distances, robot_angles, sensor_relative_angles):
            list_trace.append([a, b, d])
            m_coords = measurement_to_coordinate(r, d, a, b)
            trace.append(m_coords)

        trace = np.array(trace)

        import matplotlib.pyplot as plt

        fig, axs = plt.subplots(1,2, sharex=True, sharey=True)
        axs[0].set_aspect(1.0)
        axs[0].set_title("{} measurements\nfrom sensor".format(len(trace)))

        axs[0].scatter(*robot_coordinates[0])
        axs[0].scatter(*trace.T[0], s=1, color="black")

        resolution = 3
        g = Grid(resolution=resolution, change_rate=0.7)
        from time import time
        t = time()
        for rc, m in zip(robot_coordinates, trace):
            g.add_measurement(rc, m)
        print("Time needed to update {} measurements: {:.5f}".format(len(trace), time()-t))
        axs[1].set_aspect(1.0)
        axs[1].set_title("Bayesian filter\napplied on\ndiscretization of world")
        axs[1].set_facecolor('xkcd:salmon')
        for sq in g.grid:
            axs[1].scatter(sq[0][0], sq[0][1], s=10*resolution, color="WHITE", marker="s")
        for sq in g.grid:
            axs[1].scatter(sq[0][0], sq[0][1], s=10*resolution, color="BLACK", alpha=sq[1], marker="s")
        axs[1].scatter(*robot_coordinates[0])
        plt.show()

        import random
        SUBSETSIZE = 10
        PARTICLES = 10
        measurements_subset = random.sample(list_trace, SUBSETSIZE)
        t = time()
        print(g.estimate_position(robot_coordinates[0], measurements_subset, nr_particles = PARTICLES, spread=1))
        print("Time needed to estimate position using {} measurements and {} particles: {:.5f}".format(SUBSETSIZE, PARTICLES, time()-t))
