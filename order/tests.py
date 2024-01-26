from django.test import TestCase
import random
import string

# Create your tests here.
#Function to generate random string that serves as coupon code
def coupon_generator(letter_count=2, digit_count=2):  
        str1 = ''.join((random.choice(string.ascii_uppercase) for x in range(letter_count)))  
        str2 = ''.join((random.choice(string.digits) for x in range(digit_count))) 
        str3 = ''.join((random.choice(string.ascii_uppercase) for x in range(letter_count)))  
    
        sam_list = list(str1+str2+str3) # it converts the string to list.  
        # random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
        final_string = ''.join(sam_list)  
        return final_string

# coupon = coupon_generator()
# print("The generated coupon code is ",coupon)

def convert_to_words(num):  
    if num == 0:  
        return "zero"  
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    
    words = "" 

    if num>= 10000 and num<=19999:  
        words += teens[num // 10000] + " thousand "  
        num %= 10000
    if num>= 1000 and num<=9999:  
        words += ones[num // 1000] + " thousand "  
        num %= 1000  
    if num>= 100:  
        words += ones[num // 100] + " hundred "  
        num %= 100  
    if num>= 10 and num<= 19:  
        words += teens[num - 10] + " "  
        num = 0  
    elif num>= 20:  
        words += tens[num // 10] + " "  
        num %= 10  
    if num>= 1 and num<= 9:  
        words += ones[num] + " "  
    return words.strip()

def myConverter(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] 
    
    words = ""
    if num == 0:  
        return "zero"
    
    if num>=10 and num<=19:
        words += teens[num -10]
    if num >= 100000 and num <= 999999:
        if num%100000 == 0:
           words += ones[num //100000] + " hundred thousand "
        else:
           words += ones[num //100000] + " hundred and "
        num%=100000
    if num >=20000 and num<=99999:
        if num%10000 == 0:
           words += tens[num //10000] + " thousand "
        else:
           words += tens[num //10000] + " "
        num%=10000
    if num >=10000 and num<=19999:
        words += teens[num //1000 - 10] + " thousand "
        num %= 1000
    if num >=1000 and num<=9999:
        words += ones[num //1000] + " thousand "
        num %= 1000
    if num>=100 and num<=999:
        if num%100 == 0:
           words += ones[num // 100] + " hundred "
        else:
            words += ones[num // 100] + " hundred and "
        num %= 100
    if num>=20 and num<=99:
        words += tens[num // 10] + " "
        num %= 10
    if num>=1 and num<=9:
        words += ones[num]
    return words.strip().title()

        