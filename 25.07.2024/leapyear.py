def is_leap(year):
    leap = False
    
    if((year % 100 ==0) and (year % 400 ==0) or (year % 4==0)):
        return True
    

    
    return leap

year = int(input())
print(is_leap(year))
