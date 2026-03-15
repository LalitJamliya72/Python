def convert_temperature(temp,unit):
    if unit=='c':
     return(temp*9/5)+32
    elif unit=='f':
        return(temp-32)*5/9
    else:
        return None
       
print(convert_temperature(25,'c'))
print(convert_temperature(45,'f'))
       
 