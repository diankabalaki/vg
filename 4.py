#A
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
#B
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        x = abs(self.x - point.x)
        y = abs(self.y - point.y)
        z = (x ** 2 + y ** 2) ** 0.5
        return round(z, 2)
#C
class RedButton():
    def __init__(self):
        self.x = 0

    def click(self):
        print("alarm!")
        self.x += 1

    def count(self):
        return self.x
#D
class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hours_worked = 0
        self.salary_per_hour = {'Junior': 10, 'Middle': 15, 'Senior': 20}
        self.total_salary = 0

    def work(self, time):
        self.hours_worked += time
        self.total_salary += time * self.salary_per_hour[self.position]

    def rise(self):
        if self.position == 'Senior':
            self.salary_per_hour[self.position] += 1

    def info(self):
        return f"{self.name} {self.hours_worked}h {self.total_salary}yrg"
#E
class Rectangle:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        

    def perimeter(self):
        AB, BA = self.stor()
        perimeter = AB * 2 + BA * 2 
        return perimeter
    
    def area(self):
        AB, BA = self.stor()
        area = AB * BA
        return area
        
    def stor(self):
        AB = self.pointB[0] - self.pointA[0]
        BA = self.pointB[1] - self.pointA[1]
        return AB, BA
#F
class Rectangle:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def perimeter(self):
        AB, BA = self.stor()
        perimeter = AB * 2 + BA * 2
        return round(perimeter, 2)

    def area(self):
        AB, BA = self.stor()
        area = AB * BA
        return round(area, 2)

    def stor(self):
        AB = abs(self.pointB[0] - self.pointA[0])
        BA = abs(self.pointB[1] - self.pointA[1])
        return AB, BA

    def get_pos(self):
        return (min(self.pointA[0], self.pointB[0]), max(self.pointA[1], self.pointB[1]))

    def get_size(self):
        AB, BA = self.stor()
        return (AB, BA)

    def move(self, dx, dy):
        self.pointA = (self.pointA[0] + dx, self.pointA[1] + dy)
        self.pointB = (self.pointB[0] + dx, self.pointB[1] + dy)

    def resize(self, width, height):
        if width >= 0 and height >= 0:
            pos = self.get_pos()
            self.pointB = (pos[0] + width, pos[1] - height)
        else:
            raise ValueError("Width and height must be non-negative.")
#G
import math

class Rectangle:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def perimeter(self):
        AB, BA = self.stor()
        perimeter = AB * 2 + BA * 2
        return round(perimeter, 2)

    def area(self):
        AB, BA = self.stor()
        area = AB * BA
        return round(area, 2)

    def stor(self):
        AB = abs(self.pointB[0] - self.pointA[0])
        BA = abs(self.pointB[1] - self.pointA[1])
        return AB, BA

    def get_pos(self):
        return (min(self.pointA[0], self.pointB[0]), max(self.pointA[1], self.pointB[1]))

    def get_size(self):
        AB, BA = self.stor()
        return (AB, BA)

    def move(self, dx, dy):
        self.pointA = (self.pointA[0] + dx, self.pointA[1] + dy)
        self.pointB = (self.pointB[0] + dx, self.pointB[1] + dy)

    def resize(self, width, height):
        if width >= 0 and height >= 0:
            pos = self.get_pos()
            self.pointB = (pos[0] + width, pos[1] - height)
        else:
            raise ValueError("Width and height must be non-negative.")

    def turn(self):
        center = ((self.pointA[0] + self.pointB[0]) / 2, (self.pointA[1] + self.pointB[1]) / 2)
        self.pointA = ((self.pointA[0] - center[0]) * 0 - (self.pointA[1] - center[1]) * -1 + center[0], (self.pointA[0] - center[0]) * 1 + (self.pointA[1] - center[1]) * 0 + center[1])
        self.pointB = ((self.pointB[0] - center[0]) * 0 - (self.pointB[1] - center[1]) * -1 + center[0], (self.pointB[0] - center[0]) * 1 + (self.pointB[1] - center[1]) * 0 + center[1])

    def scale(self, factor):
        if factor >= 0:
            center = ((self.pointA[0] + self.pointB[0]) / 2, (self.pointA[1] + self.pointB[1]) / 2)
            self.pointA = ((self.pointA[0] - center[0]) * factor + center[0], (self.pointA[1] - center[1]) * factor + center[1])
            self.pointB = ((self.pointB[0] - center[0]) * factor + center[0], (self.pointB[1] - center[1]) * factor + center[1])
        else:
            raise ValueError("Factor must be non-negative.")
#H
class Cell:
    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers:
    def __init__(self):
        self.board = {}
        for row in '12345678':
            for col in 'ABCDEFGH':
                if (int(row) + ord(col)) % 2 == 0:
                    self.board[col + row] = Cell('X')
                elif int(row) <= 3:
                    self.board[col + row] = Cell('B')
                elif int(row) >= 6:
                    self.board[col + row] = Cell('W')
                else:
                    self.board[col + row] = Cell('X')

    def move(self, f, t):
        self.board[t] = self.board[f]
        self.board[f] = Cell('X')

    def get_cell(self, p):
        return self.board[p]
#I
class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self, items):
        self.queue.append(items)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return 'is empty'    
    
    def is_empty(self):
        return len(self.items) == 0
#J
class Queue:
    def __init__(self):
        self.queue = []
        
    def push(self, items):
        self.queue.append(items)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return 'is empty'    
    
    def is_empty(self):
        return len(self.items) == 0