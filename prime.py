#function returns if number is prime
def is_prime(x):
    prime = True
    n = 1
    while n in range(1, x): #loop through each number to see if it's divisible
        if x % n == 0 and n > 1 and n < x: #do not check 1 and the original number 
            prime = False
        n += 1
    
    print(prime)


        