#!/usr/bin/env python
# coding: utf-8

# Read file as list
with open("../data/input_2.txt") as file:
   course = file.read().splitlines()

course = list(map(lambda x: (x.split(' ')[0], int(x.split(' ')[1])), course))

# Part 1
class Submarine:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        
    def execute_direction(self, direction_tuple):
        direction, distance = direction_tuple
        assert direction in {'forward', 'down', 'up'}, "Direction invalid"
        if direction == 'forward':
            self.x += distance
        elif direction == 'down':
            self.y -= distance
        elif direction == 'up':
            self.y += distance
            
    def travel_whole_course(self, course):
        for i in course:
            self.execute_direction(i)
        return(self.x, self.y)

sub = Submarine(0,0)
course[0]

final_x, final_y = sub.travel_whole_course(course)

print("Answer to part 1 is: {}".format(final_x * final_y))

# Part 2
class Submarine_2:
    def __init__(self):
        self.x = self.depth = self.aim = 0
    
    def execute_direction(self, direction_tuple):
        direction, magnitude = direction_tuple
        assert direction in {'forward', 'down', 'up'}, "Direction invalid"
        if direction == 'forward':
            self.x += magnitude
            self.depth += magnitude * self.aim
        elif direction == 'down':
            self.aim += magnitude
        elif direction == 'up':
            self.aim -= magnitude
            
    def travel_whole_course(self, course):
        for i in course:
            self.execute_direction(i)
        return(self.x, self.depth)

sub = Submarine_2()

final_x, final_y = sub.travel_whole_course(course)

print("Answer to part 1 is: {}".format(final_x * final_y))



