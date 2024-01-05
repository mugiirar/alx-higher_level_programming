#!/usr/bin/env python
"""finding largest number"""


def find_peak(list_of_integers):
    num = len(list_of_integers)
    
    if (num == 0):
        return None

    else:

        count = 0
        ans = list_of_integers[0]

        while (count < num):
            track = list_of_integers[count]
            for seg in list_of_integers:
                if seg > track:
                    ans = seg

            count = count + 1
        
        return ans
