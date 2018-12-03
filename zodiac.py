#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:17:31 2018

@author: ellenmacpherson
"""

def zodiac_app():
    
    month = input('What month were you born in? ')
    day = int(input('What day were you born on? '))
    
    
    if month == 'December':
        if day >= 22:
            return ('Capricorn')
        else: 
            return ('Sagittarius')
        
    if month == 'January':
        if day >= 20:
            return ('Aquarius')
        else: 
            return ('Capricorn')
        
    if month == 'February':
        if day >= 19:
            return ('Pieces')
        else: 
            return ('Aquarius')
    
    if month == 'March':
        if day >= 21:
            return ('Aries')
        else: 
            return ('Pieces')
    
    if month == 'April':
        if day >= 20:
            return ('Taurus')
        else: 
            return ('Aries')
        
    if month == 'May':
        if day >= 21:
            return ('Gemini')
        else: 
            return ('Taurus')
    
    if month == 'June':
        if day >=  21:
            return ('Cancer')
        else: 
            return ('Gemini')
    
    if month == 'July':
        if day >= 23:
            return ('Leo')
        else: 
            return ('Cancer')
    
    if month == 'August':
        if day >= 23:
            return ('Virgo')
        else:
            return ('Leo')
            
    if month == 'September':
        if day >= 23:
            return ('Libra')
        else:
            return ('Virgo')
    
    if month == 'October':
        if day >= 23:
            return ('Scorpio')
        else:
            return ('Libra')
            
    if month == 'November': 
        if day >=22:
            return ('Sagittarius')
        else:
            return ('Scorpio')
            
    
