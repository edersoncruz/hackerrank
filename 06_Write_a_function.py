#Question Link https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
    
        if year % 100 == 0:
            leap = False
        
            if year % 400 == 0:
                leap = True
    else:
        leap = False
        
    return leap