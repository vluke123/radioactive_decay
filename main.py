import numpy as np
import matplotlib.pyplot as plt

# dx = (r - bX) * dt     =     Equation for radioactive leak

X0 = 1  # intial amount of radioactivty at t=0

X = r / beta  # Steady state by setting that dX/dt = 0

# Exact solution is X(t) = (r / beta) + (X0 - (r / beta))*np.exp(-beta*t)

# Set in the inital conditions below

r = 1
beta = 0.5
t_max = 10 # Max Time
dt = 1  # Timestep

# Create an empty to list to store X(t) values

y_list = []
 
# Create a for loop with the max range being t_max (thus it iterates in increments of 1 from 0 to 10 for this instance)

for i in range(t_max): # loops i up until t_max has been reached
  Xi = (r / beta) + (X0 - (r / beta)) * np.exp(-1 * beta * i)  # i = t in this formula; loops over the equation for i=0 to i=10
  print(Xi) # Just for debugging purposes to see values
  y_list.append(Xi) # Adds the latest value onto the end of y_list
  
 # Create an array for the y_list and create an array for the time (or x_plot)
 
 y_plot = np.arange(y_list)
 x_plot = np.arange(0,dt,t_max)
 

 
