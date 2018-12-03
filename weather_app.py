#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:24:24 2018

@author: ellenmacpherson
"""

def weather_app(temperature):
    temperature = int(input('What\'s the temperature today? '))
    if temperature <= 0: 
        print ('It\'s {} degrees. There\'s no need to get out of bed.'.format(temperature))
    if temperature > 0 and temperature <= 10:
        print ('It\'s {} degrees. Get the gloves out!'.format(temperature))
    if temperature > 10 and temperature <= 20:
        print ('It\'s {} degrees. That\'s positively balmy!'.format(temperature))
    if temperature > 20 and temperature <= 30:
        print ('It\'s {} degrees. Perfect.'.format(temperature))
    if temperature > 30: 
        print ('It\'s {} degrees. Make sure you\'ve got some sunscreen on!'.format(temperature))

weather_app(25)
