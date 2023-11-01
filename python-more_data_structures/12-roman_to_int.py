#!/usr/bin/python3
#def roman_to_int(roman_string):
 #   if roman_to_int is None:
  #      return (None)
   # roman_dict = {'M': 1000, 'D': 500, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    #rom = list(roman_string)
    #x = roman_dict.keys()
    
    #for i in 
    #print(x)
    #return (x)
    

roman_number = "XVV"
roman_dict = {'M': 1000, 'D': 500, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
rom = list(roman_number)

result = 0
for i in roman_dict.keys():
    print(i)
    if roman_number in roman_dict.keys():
        result += roman_dict[i]
print(result)

#print("{} = {}".format(roman_number, roman_to_int(roman_number)))