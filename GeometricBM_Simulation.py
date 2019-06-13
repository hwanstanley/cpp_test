__author__ = 'HongWang'

import numpy as np
from scipy import exp, sqrt
import csv

#######################################################################################################################
########################### 4-dimensional geometric brownian motion simulation ######################################

N = 12 # number of time steps
m = 5000 # number of simulation paths
T = 1 # maturity
dt = T/N
t = np.linspace(T/N,T,N+1) # the time grid

#parameters
mu = np.array((-0.06,0.05,0.15,0.28))
Vol = np.array((0.36,0.38,0.44,0.54))
X0 = np.array((50,45,40,35))

# correlation parameters
rho12 = 0.1
rho13 = -0.2
rho23 = 0.3
rho14 = 0.2
rho24 = -0.15
rho34 = 0.2

# correlation matrix
C = [[1,rho12,rho13,rho14],[rho12,1,rho23,rho24],[rho13,rho23,1,rho34],[rho14,rho24,rho23,1]]

#initialise
X = np.zeros([m,N+1,4])
X[:,0,:] = X0

for ii in range(0,m,1):

    W1,W2,W3,W4 = np.random.multivariate_normal([0,0,0,0],C,N).T
    X[ii,1:,0] = X[ii,0,0]*exp(mu[0]*t[1:]+np.cumsum(W1,axis=0)*sqrt(dt)*Vol[0])
    X[ii,1:,1] = X[ii,0,1]*exp(mu[1]*t[1:]+np.cumsum(W2,axis=0)*sqrt(dt)*Vol[1])
    X[ii,1:,2] = X[ii,0,2]*exp(mu[2]*t[1:]+np.cumsum(W3,axis=0)*sqrt(dt)*Vol[2])
    X[ii,1:,3] = X[ii,0,3]*exp(mu[3]*t[1:]+np.cumsum(W4,axis=0)*sqrt(dt)*Vol[3])


# we can only print to see the variable in Pycharm
print(X)


# save the simulated asset prices of the first asset
out = open("X0.csv" , "w")
output = csv.writer(out)
for row in X[:,:,0]:
    output.writerow(row)
out.close()


out = open("X0.csv","rU")
read_data = csv.reader(out)
data = []
for row in read_data:
   row = [ float(cell) for cell in row]  # all elements are saved as string type. we have to convert them to float/int
   data.append(row)
data = np.array(data) # line 57 assumes the array#  is saved as a list. we have to convert to the array format
out.close()