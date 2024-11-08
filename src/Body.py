class Body:
    def __init__(self, mass, x, y, z):
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z

    def update_mass(self, m):
        self.mass = m

    def update_location(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
