__author__ = 'HongWang'

import numpy as np
from scipy import exp, sqrt, log
from scipy.stats import norm

# Least-squares monte carlo to price an american option and an european option

# Black-Scholes Parameters
S0 = 20
K = 15
r = 0.05
T = 1
Vol = 0.1

# Black-Scholes Stock Price Simulation
N = 100 # number of simulation steps
m = 500 # number of simulation paths
dt = T/N
S = np.zeros([m,N+1])
S[:,0] = S0

# simulation
ran = np.random.standard_normal((m,N))
S[:,1:N+1] = S0*exp(np.cumsum((r-Vol**2/2)*dt+Vol*sqrt(dt)*ran,axis=1))


# Monte-Carlo Black-Scholes European Option
terminalPayoff_call = np.maximum(S[:,-1]-K,0)
terminalPayoff_put = np.maximum(K-S[:,-1],0)
european_call = exp(-r*T)*np.sum(terminalPayoff_call)/m
european_put = exp(-r*T)*np.sum(terminalPayoff_put)/m

# Analytical Black-Scholes European Option
d1 = (log(S0/K)+(r+Vol**2/2)*T)/(Vol*sqrt(T))
d2 = d1 - Vol*sqrt(T)
BS_call = S0*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
BS_put = K*exp(-r*T)*norm.cdf(-d2)-S0*norm.cdf(-d1)

# LSM Black-Scholes American Option
reg = 10 # highest order of basis function
df = exp(-r*dt) # discount factor of each time step
V = np.zeros((m,N+1))
V[:,-1] = terminalPayoff_call
IE = np.maximum(S-K,0) # immediate exercise

for i in range(N-1,0,-1):
    rg = np.polyfit(S[:,i],V[:,i+1]*df,reg)
    C = np.polyval(rg,S[:,i])
    V[:,i] = np.where(C>IE[:,i],V[:,i+1]*df,IE[:,i])

american_call = df*np.sum(V[:,1])/m



print('Least-Squares Monte-Carlo American Call Price =', american_call)
print('Black-Scholes European Call Price =', BS_call)
print('Monte-Carlo Simulation European Call Price =', european_call)

















