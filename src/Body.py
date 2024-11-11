from vpython import *
import numpy as np

class Body:
    def __init__(self, mass, location, velocity, vcolor):
        self.mass = mass
        self.location = np.array(location)
        self.velocity = np.array(velocity)
        
        # Create a VPython sphere for visualization
        self.vp_sphere = sphere(pos=vec(*self.location), 
                                color=vcolor, 
                                radius=self.mass)
        
    def update_location(self, new_location):
        self.location = np.array(new_location)
        self.vp_sphere.pos = vec(*self.location)
