import numpy as np
import matplotlib.pyplot as plt
N = 100
softening = 0.1
np.random.seed(17)
G = 1.0 # Gravitational constant
dt = 0.01
masses = 20*np.ones((N,1))/N
positions_X = np.random.rand(N,1)
positions_Y = np.random.rand(N,1)
positions_Z = np.random.rand(N,1)
Velocity_X = np.random.rand(N,1)
Velocity_Y = np.random.rand(N,1)
Velocity_Z = np.random.rand(N,1)
Velocity_X -= np.mean(masses*Velocity_X)/np.mean(masses)
Velocity_Y -= np.mean(masses*Velocity_Y)/np.mean(masses)
Velocity_Z -= np.mean(masses*Velocity_Z)/np.mean(masses)

def distance(i,j):
    return np.sqrt(softening**2+(positions_Y[i]-positions_Y[j])**2 + (positions_X[i]-positions_X[j])**2 + (positions_Z[i]-positions_Z[j])**2)

def F(i,j):
    dist = distance(i, j)**3
    dx = positions_X[j]-positions_X[i]
    dy = positions_Y[j]-positions_Y[i]
    dz = positions_Z[j]-positions_Z[i]
    F_x = (G*masses[j]*dx)/dist
    F_y = (G*masses[j]*dy)/dist
    F_z = (G*masses[j]*dz)/dist
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
        Velocity_X[i] += a_x*dt/2
        Velocity_Y[i] += a_y*dt/2
        Velocity_Z[i] += a_z*dt/2

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
        calculateVelocities()
        t += dt
        plt.sca(ax1)
        plt.cla() ## uncomment if u dont want to see the trails
        plt.scatter(positions_X,positions_Y,s=10,color='blue')
        ax1.set(xlim=(-2, 2), ylim=(-2, 2))
        ax1.set_aspect('equal', 'box')
        ax1.set_xticks([-2,-1,0,1,2])
        ax1.set_yticks([-2,-1,0,1,2])
			
			
        plt.pause(0.0000001)

simulate()