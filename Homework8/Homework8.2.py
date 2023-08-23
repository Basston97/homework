class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def subtract(self, other_circle):
        if isinstance(other_circle, Circle):
            radius_difference = abs(self.radius - other_circle.radius)

            if radius_difference == 0:
                return Point(self.center.x, self.center.y)
            else:
                return Circle(self.center, radius_difference)
        else:
            raise ValueError("The input must be another Circle object")

center1 = Point(0, 0)
center2 = Point(2, 2)

circle1 = Circle(center1, 5)
circle2 = Circle(center2, 3)

result_circle = circle1.subtract(circle2)
if isinstance(result_circle, Circle):
    print(f"Resulting Circle - Center: ({result_circle.center.x}, {result_circle.center.y}), Radius: {result_circle.radius}")
else:
    print(f"Resulting Point - Coordinates: ({result_circle.x}, {result_circle.y})")
