def f_name(s):
    return s
    
def n_name(s,n):
    return s[0:int(n)]
    
def reverse_name(s):
    return s[::-1]
    
def n_vowel(s):
    count = 0
    vowels = ['a','e','o','u','i']
    for c in s.lower():
        if(c in vowels):
            count = count + 1
    return count
    

while True:   
    print("Type x or X to exit")
    s= input('What is your name: ')
    if(s.lower() == 'x'): break
    n = int(input('Enter the number of character you want display from left of your name: '))
    print(f'Welcome {f_name(s)}! \n Your name has {n_vowel(s)} vowels. \n In reverse it is {reverse_name(s)},\n {n} characters from your name are {n_name(s,n)} ')

