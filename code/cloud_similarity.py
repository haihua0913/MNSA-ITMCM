#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/9/14 21:27
# @Author : Haoxuan Zhang
import csv
import math


def calculate_D(Ci, Cj):
    Exi, Eni, Hei = Ci
    Exj, Enj, Hej = Cj

    sigma_i_squared = Eni ** 2 + Hei ** 2
    sigma_j_squared = Enj ** 2 + Hej ** 2

    D = 0.5 * ((Exi - Exj) ** 2 + (sigma_i_squared + sigma_j_squared)) * (1 / sigma_i_squared + 1 / sigma_j_squared)-2
    return D


def calculate_Sim(Ci, Cj):
    D = calculate_D(Ci, Cj)
    similarity = math.exp(-D)
    return similarity


# 读取CSV文件
with open('review_topic_result.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)[1:]


"""
result = []
target0 = [0.283735369,0.036472969,0.052366439]
target1 = [0.393132505,0.022540295,0.03236246]
target2 = [0.460753389,0.013929902,0.02]
target3 = [0.528374273,0.022540295,0.03236246]
target4 = [0.63777141,0.036472969,0.052366439]"""


result = []
target0 = [0.000126137,0.123085684,0.043775703]
target1 = [0.39335528,0.123085684,0.043775703]
target2 = [0.639536262,0.123085684,0.043775703]
#target3 = [0.441958533,0.040709111,0.070834471]
#target4 = [0.639536262,0.065872348,0.114618884]

output_data = [['Data', 'Selected Target', 'Similarity to Target 0', 'Similarity to Target 1', 'Similarity to Target 2']]

for row in data:
    Ci = [float(value) for value in row[0:3]]
    similarities = []
    for target in [target0, target1, target2]:
        similarity = calculate_Sim(Ci, target)
        similarities.append(similarity)
    max_similarity = max(similarities)
    label = similarities.index(max_similarity)
    output_data.append([row[0], 'Target ' + str(label), *similarities])


with open('review_target_output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(output_data)

print("Output file 'output.csv' generated successfully.")