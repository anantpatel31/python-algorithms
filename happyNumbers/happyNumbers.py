# determining whether a number is happy or not    
#  a happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit
def isHappyNumber(num):    
    rem = sum = 0;    
        
    # calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;  

# collect the user input
num = int(input("Enter a number: "))
result = num;    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result);    
     
# happy number always ends with 1    
if(result == 1):    
    print(str(num) + " is a happy number");    
# unhappy number ends in a cycle of repeating numbers which contain 4    
elif(result == 4):    
    print(str(num) + " is not a happy number");