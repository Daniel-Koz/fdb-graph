#coding: utf-8

import random

random.seed(1)

def gb(tam):
    return [[random.randint(0,100) for i in range(tam)] for j in range(tam)]
