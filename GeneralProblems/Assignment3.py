## Assignment 3 ME369P
## Name: Alejandro Gleason Méndez
## EID: ag77698
##
import math as m
import matplotlib.pyplot as plt


# Helper functions to calculate RK45
def RK4(yi, h, k1, k3, k4, k6):
    # return yi + h * (0.097 * k1 + 0.40 * k3 + 0.21 * k4 + 0.29 * k6)
    return yi + h * ((37 / 378) * k1 + (250 / 621) * k3 + (125 / 594) * k4 + (512 / 1771) * k6)


def RK5(yi, h, k1, k3, k4, k5, k6):
    # return yi + h * (.102 * k1 + .383 * k3 + .244 * k4 + .193 * k5 + .25 * k6)
    return yi + h * (
            (2825 / 27648) * k1 + (18575 / 48384) * k3 + (13525 / 55295) * k4 + (277 / 14336) * k5 + (1 / 4) * k6)


def hnew(h_present, delta_desired, delta_actual):
    alpha = .2 if delta_actual <= delta_desired else .25
    return h_present * pow(abs(delta_desired / delta_actual), alpha)


'''
Kwargs can be:
    initial_step        : float
    max_step            : float
    relative_tolerance  : float
'''


# Do not modify the function input parameters
def ODE45(func, duration, initial_states, **kwargs):
    time = [0]
    states = []
    total_states = len(initial_states)
    for init_state in initial_states:
        states.append([init_state])
    # Retrieving and assigning default params if required
    initial_step = kwargs.get('initial_step', 0.01)
    max_step = kwargs.get('max_step', 0.25)
    relative_tolerance = kwargs.get('relative_tolerance', 0.001)
    h = initial_step
    i = time[0]
    while i < duration[1]:
        h_new, error = 1, 1
        y_i = [0] * total_states
        rk4i = [0] * total_states
        rk5i = [0] * total_states
        while error > relative_tolerance:
            # print("time", time[-1])
            # Calculate ks
            for j in range(total_states):
                y_i[j] = states[j][-1]
            ki1 = list(func(i, y_i))
            # print("k11", k11)
            # print("k21", k21)
            for j in range(total_states):
                y_i[j] = states[j][-1] + 0.2 * h * ki1[j]
            ki2 = list(func(i + .2 * h, y_i))
            # print("k12", k12)
            # print("k22", k22)
            for j in range(total_states):
                y_i[j] = states[j][-1] + 0.3 * h * ki2[j]
            ki3 = list(func(i + .3 * h, y_i))
            # print("k13", k13)
            # print("k23", k23)
            for j in range(total_states):
                y_i[j] = states[j][-1] + 0.6 * h * ki3[j]
            ki4 = list(func(i + .6 * h, y_i))
            # print("k14", k14)
            # print("k24", k24)
            for j in range(total_states):
                y_i[j] = states[j][-1] + 1 * h * ki4[j]
            ki5 = list(func(i + 1 * h, y_i))
            # print("k15", k15)
            # print("k25", k25)
            for j in range(total_states):
                y_i[j] = states[j][-1] + 0.875 * h * ki5[j]
            ki6 = list(func(i + .875 * h, y_i))
            # print("k16", k16)
            # print("k26", k26)
            for j in range(total_states):
                rk4i[j] = RK4(states[j][-1], h, ki1[j], ki3[j], ki4[j], ki6[j])
                rk5i[j] = RK5(states[j][-1], h, ki1[j], ki3[j], ki4[j], ki5[j], ki6[j])
            # print("rk41", rk4i, "rk51", rk5i)
            # The only error that matters is the difference in the first state from a set of 1st order ODEs
            error = abs(rk4i[0] - rk5i[0])
            h_new = hnew(h, relative_tolerance, error)
            if h_new > max_step:
                h_new = max_step
            if error > relative_tolerance:
                h = h_new
            if i + h > duration[1]:
                # Adjust to finish exactly on last time
                difference = i + h - duration[1]
                h -= difference

        for j in range(total_states):
            states[j].append(rk5i[j])
        i += h
        time.append(i)
        # update the new h as h_present = h_new
        h = h_new
    return time, states


def mySystem(t, y):
    # This is given, do not modify
    y_prime_1 = 0.5 * y[1]
    y_prime_2 = -0.3 * y[1] - 0.1 * y[0] + 4 * m.cos(t)
    y_prime = (y_prime_1, y_prime_2)
    return y_prime


def PlotStates(time, states):
    ## Bonus Function
    colors = ['b+', 'r+', 'g+', 'c+', 'm+', 'y+', 'k+']
    fig = plt.figure()
    for idx, state in enumerate(states):
        plt.plot(time, state, colors[idx % len(colors)], linestyle='-')
    # Set extra characteristics
    fig.canvas.set_window_title('Assignment 3 Plot')
    fig.suptitle('States Plot')
    plt.xlabel('time')
    plt.ylabel('states')
    plt.grid(True, linestyle='dashed')
    plt.xlim(time[0], time[-1])
    fig.savefig('plot.png')
    return


def main():
    time, states = ODE45(mySystem, [0, 30], [4, 0])
    PlotStates(time, states)


if __name__ == '__main__':
    main()
