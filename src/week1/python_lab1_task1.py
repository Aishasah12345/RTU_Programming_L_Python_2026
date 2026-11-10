"""
Task 1 – Simple Function with Arithmetic

Write a function circle_area(radius) that returns the area of a circle.
Use math.pi * radius ** 2 and do not round the returned value.

Examples:
>>> round(circle_area(1), 2)
3.14
>>> round(circle_area(2), 2)
12.57
>>> circle_area(0)
0.0
"""

import math


def circle_area(radius: float) -> float:
    """Return the area of a circle given its radius (unrounded)."""
    return math.pi * radius**2


if __name__ == "__main__":
    radius = float(input("Enter radius: "))
    area = circle_area(radius)
    print(f"Area of the circle: {area:.2f}")
