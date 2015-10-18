import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from pandas.io.data import DataReader
from datetime import datetime


x = np.random.uniform(0,1,20)

def f(x): return x * 2

noise_variance = 0.2

noise = np.random.randn(x.shape[0]) * noise_variance

t = f(x) + noise

#plt.plot(t,x, 'ro')
#plt.plot(f(x),x)

# Plot cost

def nn(x, w): return x*w

def cost(y,t): return ((t-y)**2).sum()

ws = np.linspace(0,4,num=100)

cost_ws = np.vectorize(lambda w: cost(nn(x, w), t))(ws)



plt.plot(ws, cost_ws)


# Gradient Descent

def gradient(w,x,t):
    return 2*x*(nn(x,w)-t)

def delta_w(w_k, x, t, learning_rate):
    return learning_rate * gradient(w_k, x, t).sum()

# Init Weight
w = 0.1

learning_rate = 0.1

nb_of_iterations = 4

w_cost = [(w, cost(nn(x, w), t))]
for i in range(nb_of_iterations):
    dw = delta_w(w,x,t,learning_rate)
    w = w-dw
    w_cost.append((w, cost(nn(x,w),t)))

plt.plot(ws, cost_ws, 'r-')

for i in range(1, len(w_cost)-2):
    w1, c1 = w_cost[i-1]
    w2, c2 = w_cost[i]
    plt.plot(w1,c1,'bo')
    plt.plot([w1, w2], [c1, c2], 'b-')
    plt.text(w1, c1+0.5, '$w({})$'.format(i))


w1, c1 = w_cost[len(w_cost)-3]
plt.plot(w1, c1, 'bo')


plt.show()
