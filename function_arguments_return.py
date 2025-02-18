import math

def circle_area(radius):
    """Calculate and return the area of a circle."""
    area = math.pi * radius**2
    return area

radius = 5
area = circle_area(radius)

print(f"The area of a circle with radius 5 is: {area:.2f}") 
