#!/usr/bin/env python
# coding: utf-8

from statistics import multimode

with open("../data/input_3.txt") as file:
   report = file.read().splitlines()


def binary_to_decimal(binary_string):
    return sum([int(element) * 2**index for index, element in enumerate(binary_string[::-1])])


def most_common(lst):
    return max(set(lst), key=lst.count)


def eval_gamma(report):
    total_rows = len(report)
    gamma_string = ''
    for position in range(len(report[0])):
        total_ones = 0
        gamma_string += most_common([x[position] for x in report])
    return(gamma_string)

gamma_binary = eval_gamma(report)

def gamma_bin_to_epsilon(gamma_binary):
    return ''.join(['1' if i == '0' else '0' for i in gamma_binary])


epsilon_binary = gamma_bin_to_epsilon(gamma_binary)

gamma = binary_to_decimal(gamma_binary)
epsilon = binary_to_decimal(epsilon_binary)

print("Answer to part 1 is: {}".format(gamma * epsilon))

def eval_oxygen(report):
    total_rows = len(report)
    for position in range(len(report[0])):
        most_common_bit = multimode([x[position] for x in report])
        bit_to_keep = most_common_bit[0] if len(most_common_bit) == 1 else '1'
        report = [x for x in report if x[position] == bit_to_keep]
        if len(report) == 1:
            return(report[0])

def eval_CO2(report):
    total_rows = len(report)
    for position in range(len(report[0])):
        most_common_bit = multimode([x[position] for x in report])
        bit_not_to_keep = most_common_bit[0] if len(most_common_bit) == 1 else '1'
        report = [x for x in report if x[position] != bit_not_to_keep]
        if len(report) == 1:
            return(report[0])


oxygen_string = eval_oxygen(report)
CO2_string = eval_CO2(report)


oxygen = binary_to_decimal(oxygen_string)
CO2 = binary_to_decimal(CO2_string)

print("Answer to part 2 is: {}".format(oxygen * CO2))
