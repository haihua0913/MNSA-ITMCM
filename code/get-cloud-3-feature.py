#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/9/14 20:19
# @Author : Haoxuan Zhang



import numpy as np
import pandas as pd


def Cloud_compute(xl):

    xl = np.array(xl)
    # S2 = np.var(xl)
    S2 = np.std(xl)
    Ex = np.mean(xl)
    En = np.sqrt(np.pi / 2) * np.mean(np.abs(xl - Ex))
    He = np.sqrt(np.abs(S2 * S2 - En * En))
    return Ex, En, He


"""C1 = [0.109796243, 0.114879403, 0.116161243, 0.198906238, 0.226134292]
C2 = [0.342041588, 0.345842051, 0.371860599, 0.384723701, 0.466579808]
C3 = [0.353957614, 0.355032878, 0.379666217, 0.436850753, 0.499509364]

C4 = [0.387681827, 0.388561589, 0.439294536, 0.479177084, 0.570770093]"""

if __name__ == '__main__':

    data = pd.read_csv('review_topic.csv', sep=',', header=None)
    data_array = np.array(data)
    data_list = data_array.tolist()
    doc = open('review_topic_result.csv', 'a', encoding='utf-8')
    for i in data_list:
        print(Cloud_compute(i), file=doc)