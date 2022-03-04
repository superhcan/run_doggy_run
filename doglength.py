"""
Lng: Winning lengths or beaten lengths. 

A “length” is .07 of a second, roughly the time it takes the full length of a dog to pass a given point at speed. 

“ns”=nose, .01 of a second; 

“hd”=head, .02 of a second; 

“nk”=neck, .03 of a second; 

“½”=half a length, anywhere from .04 to .06 of a second. 

For a winner, this number is the lengths in front of the 2nd-place finisher; for all other finishers, this is the number of lengths behind the winner.
"""
import re

def frac_to_dec(input_string):

    if not input_string:
        return 0
    res = re.split(r"&frac", input_string)
    print("res ", res)
    if(res[0] == ""):
        return 0    
    w = int(res[0])
    if not res[1]:
        return w
    else:    
        b = re.split(r"", res[1])
        t = int(b[1])
        n = int(b[2])
        dec = w + t/n
        return dec
       
def to_sec(distance_beaten):
    if(distance_beaten == 'ns'):
        return 0.01
    elif(distance_beaten == 'hd'):
        return 0.02
    elif(distance_beaten == 'nk'):
        return 0.03
    else:        
        return frac_to_dec(distance_beaten) * 0.07

