from __future__ import annotations

class Point:

    base_x = .0
    base_y = .0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def move(self, x: float, y: float):
        self.x += x
        self.y += y

    def move_to(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def move_to_point(self, point: Point):
        self.x = point.x
        self.y = point.y

    def reset(self):
        self.y = Point.base_x
        self.y = Point.base_y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

p1 = Point(0, 0)
p2 = Point(1, 1)

print(Point.base_x)

p1.base_x = 1.0

Point.base_x = 2.0

print(Point.base_x)
print(p1.base_x)