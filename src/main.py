from Body import Body
from vpython import *
import numpy as np
from scipy.integrate import solve_ivp

tf = 1000.0
body1 = Body(1.0, [10.0, 0.0, 0.0], [-0.1, 0.0, 0.1], color.red)
body2 = Body(1.0, [0.0, 10.0, 0.0], [0.0, 0.1, -0.1], color.green)
body3 = Body(1.0, [0.0, 0.0, 10.0], [0.2, -0.1, 0.0], color.blue)
y0 = np.concatenate((body1.location, body2.location, body3.location,
                     body1.velocity, body2.velocity, body3.velocity))

canvas(width=600, height=600, background=color.white)

# Force function for ODE.
def f(t, y):
    # Positions
    p1, p2, p3 = y[0:3], y[3:6], y[6:9]
    
    # Distances
    d1 = np.linalg.norm(p1 - p2)
    d2 = np.linalg.norm(p2 - p3)
    d3 = np.linalg.norm(p3 - p1)
    
    # Calculate derivatives.
    dydt = np.concatenate((
        # Velocities
        y[9:18], 
        
        # Accelerations.
        body2.mass * (p2 - p1) / d1**3 + body3.mass * (p3 - p1) / d3**3,
        body1.mass * (p1 - p2) / d1**3 + body3.mass * (p3 - p2) / d2**3,
        body1.mass * (p1 - p3) / d3**3 + body2.mass * (p2 - p3) / d2**3
    ))
    return dydt

# Solve the ODEs.
solution = solve_ivp(
    f, [0.0, tf], y0, method='RK45', t_eval=np.arange(0.0, tf, 0.025) # t0, tf, and step.
)

# Visualization update loop.
for i in range(len(solution.t)):
    rate(500)
    y = solution.y[:, i]
    body1.update_location(y[0:3])
    body2.update_location(y[3:6])
    body3.update_location(y[6:9])
