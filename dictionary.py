

phone = input("enter phone number : ")

digit_mapping ={
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4"  : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero",
    
}
output =""
for ch in phone:
    output = output + digit_mapping.get(ch,"!") + " " 

print(output)    