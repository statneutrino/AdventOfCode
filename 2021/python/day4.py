#!/usr/bin/env python
# coding: utf-8

import numpy as np
# Read file as list
with open("../data/input_4.txt") as file:
   bingo = file.read().split('\n\n')


numbers_called = bingo.pop(0).split(',')
numbers_called = list(map(int, numbers_called))

bingo_array = np.zeros((len(bingo),5,5), dtype=int)

bingo_array
for i in range(len(bingo)):
    board = np.fromstring(bingo[i], dtype=int, count=- 1, sep=' ').reshape((5, 5))
    bingo_array[i,:,:] = board


def tick_number(bingo_array, number):
    bingo_array[bingo_array == number] = 0
    return(bingo_array)


def play_bingo(bingo_array, numbers_called):
    for n in numbers_called:
        bingo_array = tick_number(bingo_array, n)
        for i in range(bingo_array.shape[0]):
            column_sum = bingo_array[i,:,:].sum(axis=0)
            row_sum = bingo_array[i,:,:].sum(axis=1)
            if 0 in row_sum or 0 in column_sum:
                return bingo_array[i,:,:], n


winner, final_number = play_bingo(bingo_array, numbers_called)

print("Answer to part 1 is: {}".format(winner.sum() * final_number))

# Part 2
def play_bingo_to_lose(bingo_array, numbers_called):
    for n in numbers_called:
        bingo_array = tick_number(bingo_array, n)
        winning_boards = []
        for i in range(bingo_array.shape[0]):
            column_sum = bingo_array[i,:,:].sum(axis=0)
            row_sum = bingo_array[i,:,:].sum(axis=1)
            if 0 in row_sum or 0 in column_sum:
                if bingo_array.shape == (1, 5,5):
                    return bingo_array, n
                else:
                    winning_boards.append(i) 
        bingo_array = np.delete(bingo_array, winning_boards, axis=0)

loser, final_number = play_bingo_to_lose(bingo_array, numbers_called)

print("Answer to part 2 is: {}".format(loser.sum() * final_number))