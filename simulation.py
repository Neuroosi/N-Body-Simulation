import math
import numpy as np
import matplotlib.pyplot as plt
N = 100
softening = 0.1
np.random.seed(17)
G = 6.674*10**(-11) # Gravitational constant
dt = 0.01
masses = 20.0*np.ones((N,1))/N
positions_X = np.random.rand(N,1)
positions_Y = np.random.rand(N,1)
positions_Z = np.random.rand(N,1)
Velocity_X = np.random.rand(N,1)
Velocity_Y = np.random.rand(N,1)
Velocity_Z = np.random.rand(N,1)
Velocity_X -= np.mean(masses*Velocity_X,0)/np.mean(masses)
Velocity_Y -= np.mean(masses*Velocity_Y,0)/np.mean(masses)
Velocity_Z -= np.mean(masses*Velocity_Z,0)/np.mean(masses)

def distance(i,j):
    return math.sqrt(softening**2+(positions_Y[i]-positions_Y[j])**2 + (positions_X[i]-positions_X[j])**2 + (positions_Z[i]-positions_Z[j])**2)

def F(i,j):
    F_x = G*masses[i]*masses[j]*(positions_X[j]- positions_X[i])/distance(i,j)**3
    F_y = G*masses[i]*masses[j]*(positions_Y[j]- positions_Y[i])/distance(i,j)**3
    F_z = G*masses[i]*masses[j]*(positions_Z[j]- positions_Z[i])/distance(i,j)**3
    return F_x, F_y, F_z

def calculateVelocities():
    ##First calculate acceleration and then velocity.
    for i in range(len(masses)):
        a_x = 0
        a_y = 0
        a_z = 0
        for j in range(len(masses)):
            if i != j:
                Forces = F(i,j)
                a_x += Forces[0]
                a_y += Forces[1]
                a_z += Forces[2]
        Velocity_X[i] += dt*a_x
        Velocity_Y[i] += dt*a_y
        Velocity_Z[i] += dt*a_z

def updatePositions():
    for i in range(len(masses)):
        positions_X[i] += Velocity_X[i]*dt
        positions_Y[i] += Velocity_Y[i]*dt
        positions_Z[i] += Velocity_Z[i]*dt
        

def simulate():
    t = 0
    fig = plt.figure(figsize=(4,5), dpi=80)
    grid = plt.GridSpec(3, 1, wspace=0.0, hspace=0.3)
    ax1 = plt.subplot(grid[0:2,0])
    for i in range(1000):
        calculateVelocities()
        updatePositions()
        t += dt
        plt.sca(ax1)
        plt.cla()
        #xx = pos_save[:,0,max(i-50,0):i+1]
        #yy = pos_save[:,1,max(i-50,0):i+1]
        #plt.scatter(xx,yy,s=1,color=[.7,.7,1])
        plt.scatter(positions_X,positions_Y,s=10,color='blue')
        ax1.set(xlim=(-2, 2), ylim=(-2, 2))
        ax1.set_aspect('equal', 'box')
        ax1.set_xticks([-2,-1,0,1,2])
        ax1.set_yticks([-2,-1,0,1,2])
			
			
        plt.pause(0.001)

simulate()