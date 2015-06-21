# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:12:57 2015

@author: altmeyer
"""

import pandas

wdir = "C:\Users\\altmeyer\Documents\GitHub\Udacity\Intro to Data Science\Lesson2"
baseball = pandas.read_csv(wdir + '\Master.csv')
print baseball.describe()