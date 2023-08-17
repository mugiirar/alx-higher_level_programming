#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    b_key = None
    max_value = float('-inf')  # Initialize with negative infinity
    
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            b_key = key
    
    return b_key
