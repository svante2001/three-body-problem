from Body import Body
from vpython import *

# Initialize bodies.
a = Body(1, 1, 0, 0)
b = Body(1, 0, 1, 0)
c = Body(1, 0, 0, 1)

# Visualizing.
bodyA = sphere(pos = vec(a.x, a.y, a.z), color = color.blue, radius = a.mass)

# Creating the slider to change the masses.
aslider = slider(bind=lambda s: a.update_mass(s.value), min=0.5, max=5, step=0.1, value=a.mass)
labelA = wtext(text=f"Mass: {a.mass:.1f}")

# Running the simulation.
while True:
    rate(500)

    # Updating masses.
    bodyA.radius = a.mass
    labelA.text = f"Mass: {a.mass:.1f}"

    # Updating positions.
    bodyA.pos = vec(a.x, a.y, a.z)