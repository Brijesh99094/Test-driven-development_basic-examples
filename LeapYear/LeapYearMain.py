
from operator import truediv


class CheackYear :
    
        def isLeapYear(self,year):
            if year % 400 == 0 : 
                return True
            elif year % 100 == 0 :
                return False
            elif year % 4 == 0 : 
                return True
            else : 
                return False
                
        
    

chk_year = CheackYear()
print(chk_year.isLeapYear(2000))
print(chk_year.isLeapYear(1700))
print(chk_year.isLeapYear(1800))
print(chk_year.isLeapYear(2012))
print(chk_year.isLeapYear(2008))
        