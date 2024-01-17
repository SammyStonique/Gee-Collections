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

coupon = coupon_generator()
print("The generated coupon code is ",coupon)


        