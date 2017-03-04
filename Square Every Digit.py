def square_digits(num):
    return int("".join(str(int(shuzi)**2) for shuzi in str(num)))
    
print square_digits(159456)
