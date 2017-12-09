# potential = x**2

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
import copy

def potential(x) :
    return x**4 / 4 - 2 * x**2 + 4


def calc_action(x, n, S, mass) :
    action = 0
    for i in range(n) :
        ip1 = (i+1)%n
        S.append(mass * (x[ip1] - x[i])**2 / 2 + potential(x[i]))
        action += mass * (x[ip1] - x[i])**2 / 2 + potential(x[i])
        
    return action


def change_action(x, n, x_new, j, S, SV_old, mass) :
    jp1 = (j+1) % n
    jm1 = j-1

    if j == 0 :
        jm1 = n-1
        
    Slm1 = mass * (x_new - x[jm1])**2 / 2 + potential(x[jm1])
    Sl = mass * (x[jp1] - x_new)**2 / 2 + potential(x_new)

    SV_new = SV_old + (Slm1+Sl) - (S[jm1] + S[j])
    S[jm1] = Slm1
    S[j] = Sl

    return SV_new
             

def main() :
    x = []
    S_old = []
    S_new = []
    n_dim = 100
    n_sweep = 10000
    hstep = 1.0
    h_bar = 1
    mass = 1

    # for i in range(n_dim) :  # random start
        # x.append(0.5 * (2 * rand() - 1))
    for i in range(n_dim) :  # fixed start
        x.append(2)

    SV_old = calc_action(x, n_dim, S_old, mass)
    SV_new = SV_old
    S_new = copy.deepcopy(S_old)

    for i in range(1, n_sweep+1) :
        for j in range(n_dim) :
            chk = False
            while not chk :
                x_new = x[j] + (hstep * (2 * rand() - 1))
                SV_new = change_action(x, n_dim, x_new, j, S_new, SV_old, mass)
                if SV_new < SV_old :
                    x[j] = x_new
                    S_old = copy.deepcopy(S_new)
                    SV_old = SV_new
                    chk = True
                else :
                    gamma = rand()
                    if np.exp((SV_old - SV_new) / h_bar) > gamma :
                        x[j] = x_new
                    S_old = copy.deepcopy(S_new)
                    SV_old = SV_new
                    chk = True
                    
            if i%500 == 0 or i == 1:
                x_array = np.linspace(-5, 5, 100)
                potent = potential(x_array) * 10
                plt.figure()
                plt.plot(x, np.arange(0, 100))
                plt.plot(x_array, potent)
                plt.xlim([-5, 5])
                plt.ylim([0, 100])
                plt.title('Double well potential')
                plt.xlabel('x')
                plt.ylabel('n_dim')
                plt.savefig('qm_double_{}.png'.format(i))
                plt.close()
                # plt.show()
            

if __name__ == '__main__' :
    main()
