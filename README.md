# The code and output explanation.

```python
def f_name(s):
    return s
```

The above function takes single string parameter (s) and fruitfully returns the string back to the calling function.

```python 
def n_name(s,n):
    return s[0:n]
```

The above function: n_name(s,n) takes two parameter (s,n) where s is a string (i.e name) and n is the number of characters to display from the s string. The function fruitfully returns the slice of the string from the zeroth index to but not including the nth index (s[0:n])back to the calling function.

```python 
```python    
def reverse_name(s):
    return s[::-1]
```

Python doesn't come with a function that can reverse a String. Utilizing a slice that advances -1 steps backwards is the quickest and simplest method.In this instance,the above function returned the slice of string s with the expression s[::-1]. It reads start at the end of the string s, and end at position 0 with a step-backward movement of one place using the step -1, negative one value.

```python   
def n_vowels(s):
    count = 0
    vowels = ['a','e','o','u','i']
    for c in s.lower():
        if(c in vowels):
            count = count + 1
    return count
```

The function n_vowels(s) was able to return the number of vowels in its string parameter s by first having a count parameter initialized to zero and another local variable called vowels, which is a list of the vowel characters. Then there is a for-loop statement that first converts the string s to lowercase, and for each character, it checks if the character is in the list of vowels. If the character is truly in the list of vowels, then it increments the count by one (1). After completing the loop, it returned the updated value of the count.

```python
while True:   
    print("Type x or X to exit")
    s= input('What is your name: ')
    if(s.lower() == 'x'): break
    n = int(input('Enter the number of character you want display from left of your name: '))
    print(f'Welcome {f_name(s)}! \n Your name has {n_vowel(s)} vowels. \n In reverse it is {reverse_name(s)},\n {n} characters from your name are {n_name(s,n)} ')
```

I want to make the program more interactive, so I wrapped it in a while loop that repeats as long as the user wants. With the first print statement, the user is informed of how to terminate the loop by typing x. Then the user is asked to enter his or her name, which is collected as input, and save it in a variable. If the input is x, the program terminates; otherwise, the rest of the code runs. The second prompt for the number of characters to display runs; the input is then converted to an integer before being saved to the variable n. Finally, the print statement: Using the f-string format syntax, Python code (in curly braces and will be executed) can be written within a string in a format one wants it to appear within the string. Below is an example of the output:

```sh
Type x or X to exit
What is your name: 
Umaru Gloria
Enter the number of character you want display from left of your name: 
4
Welcome Umaru Gloria! 
 Your name has 6 vowels. 
 In reverse it is airolG uramU,
 4 characters from your name are Umar 
Type x or X to exit
What is your name: 
x

```

# Referrece

1. Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. https://greenteapress.com/thinkpython2/thinkpython2.pdf
2. How to reverse a String in Python. (n.d.). https://www.w3schools.com/python/python_howto_reverse_string.asp
