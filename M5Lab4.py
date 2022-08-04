p=1 #declaring variable p
while p<=50:#while loop
    #checking if p is divisible by 3 and 5
    if p%3==0 and p%5==0:#when p is divisible by 3 and 5
        print("Divisible by both")
    #checking if p is divisible by 3
    elif p%3==0:#when p is divisible by 3
        print("Divisible by three")
    #checking if p is divisible by 5
    elif p%5==0:#when p is divisible by 5
        print("Divisible by five")
    else:#when number is not divisible by 3 or 5
        print(p) #print number
    p=p+1#increment p
