from random import *

def rel_freq(n):
    m = 0
    for _ in range(n - 1):
        a = randint(1, 6)
        b = randint(1, 6)
        if a == 6 or b == 6:
            m += 1
    return m / n


prob = 11.0 / 36
eps = 0.001
num_tests = 25 * prob * (1 - prob) / eps ** 2
print('Аналитическая вероятность = %g \n Необходимое кол-во испытаний = %g, \n'
      'Относительная частота = %g' % (prob, int(num_tests), rel_freq(int(num_tests))))


