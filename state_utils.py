
class point3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return str(self.x) + ', ' + str(self.y) + ', ' + str(self.z)

    def __add__(self, other):
        new = point3D()
        new.x = self.x + other.x
        new.y = self.y + other.y
        new.z = self.z + other.z
        return new

    def __sub__(self, other):
        new = point3D()
        new.x = self.x - other.x
        new.y = self.y - other.y
        new.z = self.z - other.z
        return new

    """returns a unit vector with the direction of self"""
    def direction(self):
        return self.scale(1.0/self.magnitude())

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    #scaler multiplication of the vector
    def scale(self, factor):
        new = point3D()
        new.x = self.x * factor
        new.y = self.y * factor
        new.z = self.z * factor
        return new



if __name__ == "__main__":
    #run some tests or something
    p1 = point3D(1, 2, 3)
    print p1.scale(2)
    print p1.magnitude()
    print p1.direction().magnitude()
