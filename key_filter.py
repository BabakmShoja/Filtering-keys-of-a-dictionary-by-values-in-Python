#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:52:30 2019

@author: babakmalekishoja
"""

def keys_geq_cutoff(num_dict, min_cutoff):
    allKeys=[]
    for key,value in num_dict.items():
        if value>=min_cutoff:
            allKeys.append(key)
    print(allKeys)
    return allKeys
