class RomanNumerals:
    
    # we have a dictionary of roman numerals and their corrosponding values
    # we iterate through each key of our dictionary in descending order
    # assuming that val is > 0, we divide val by the key to obtain the number of times the roman numeral repeats. 2 // 1000 = 0
    # add roman numeral * times to repeat to our output
    # we get the remainder of our division and repeat the process once again with the next key until we're done with all of them
   
 
    def to_roman(val):
        romans_dict = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL",50:"L", 90: "XC",100:"C",400:"CD",500:"D", 900:"CM",1000:"M"}
        output = ''
        for i in sorted(romans_dict, reverse =  True):
            if val > 0:
                repeat = val // i
                output += romans_dict[i] * repeat
                val = val % i
        return output


    # we have the same roman numeral dict but with keys and values reversed
    # we go through our given string from right to left
    # if the current roman numeral is greater than or equal to the previous roman numeral then add the numerical value of it to output and set last digit to the current
    # else subtract from the output


    def from_roman(roman_num):
        nums_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        output = 0
        last_numeral = 0
        for i in roman_num[::-1]:
            if nums_dict[i] >= last_numeral:
                last_numeral = nums_dict[i]
                output += nums_dict[i]
            else:
                output -= nums_dict[i]
        return output
            


