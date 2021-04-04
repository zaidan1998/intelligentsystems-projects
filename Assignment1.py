# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:32:49 2019

@author: Cita 20
"""


pi=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)

def main_function():
    pi=22/7
    height = float(input('Height of cylinder: '))
    radian = float(input('Radius of cylinder: '))

    calculate(pi, radian, height) 

def calculate(pi, radian, height):
    volume = pi * radian * radian * height
    sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)

    answer(volume, sur_area)

def answer(volume, sur_area):
    print("Volume is: ", volume)
    print("Surface Area is: ", sur_area)

main_function() 
