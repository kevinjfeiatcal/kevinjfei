# File: homework1.py
# following: # --- Variables and Data Types ---

a = 10
b = 1.5
c = 3j
d = "hello"
e = [1, 2, 3]
f = {"name": "Ellen", "favorite fruit": "strawberry"} 
g = (1, 2) 
h = ["apple", "banana", "strawberry"] 
i = True 
j = None 
k = [True, "blue", 12] 
l = str(14) 
m = 1e4 

print(a)
print(type(a)) # int

print(b)
print(type(b)) # float

print(c)
print(type(c)) # google: apparently j is imaginary number, so its a complex number.

print(d)
print(type(d)) # string

print(e)
print(type(e)) # list

print(f)
print(type(f)) # google: where each key has a corresponding value. hence, dict for dictionary

print(g)
print(type(g)) # is this not a list too? what is difference of parenthasis around list and of brackets
# google: nvm, this is a tuple, meaning that the elements inside cannot be changed. 

print(h)
print(type(h)) # now a list of strings!

print(i)
print(type(i)) # boolean (true/false)

print(j)
print(type(j)) # holds a none, different than 0 or false for sure, probably different 
# than an empty response as well. 
# probably good for checking if a value has been provided (if none, then do this instead)

print(k)
print(type(k)) # list of different variables inside.    

print(l)
print(type(l)) # string since str(..) turns anything inside to string. str(14) not the same as 14, can't 
# do numerical operations on it. 

print(m) 
print(type(m)) # scientific notation w! float apparently tho becaues it comes with a decimal (all e has decimal ig)

"""
1. diff types of var: int, float, complex, str, list, dict, typle, bool, NoneType. js googled and are no arrays in python
2. welp js did that... 9 types total tho!
3. lists of h and k, strings l and d, floats b and m. 
4. explained in comments
5. set: a list without order and therefore unindexed, and without repeated instances inside. is mutable, 
but the variables inside must be immutable. 
can be created with curly brackets {} or with set([a list inside :D])

"""

# --- 3.2 booleans --- 

10 > 9 # true
10 == 9 # false
10 <= 9 # false 
print(bool("abc")) # true (nonempty string)
print(bool(123)) # true same as above
print(bool(["apple", "cherry", "banana"])) # true, same
print(bool(True))# true by def
print(bool(False)) # false by def
print(bool(0)) # false, 0 is false
print(bool("")) # false, empty
print(bool(" ")) # true, not empty
print(bool(())) # false, empty tuple
print(bool([])) # false, empty list
print(bool({})) # false, empty set
print(bool(True and False)) # false, isn't both
print(bool(True and True)) # true, same
print(bool(False and False)) # true, both are false 
print(bool(True or False)) # true, true is true
print(bool(True or True)) # true is true
print(bool(False or False)) # false, neither is true
print(bool(not(False))) # true
print(bool(not(True))) # false

"""
1) idk patterns, just logic
2) i didn't know about the empty = false thing
3) 1 != 2, 1 not equal to 2
4) not(True) or False
"""

# --- 3.3 Operators ---

# 3.3.1 - arithmetic
print (10 + 5) # 15 add
print (10 - 5) # 5 minus
print ( 2 * 4) # 8 multiply
print(6/3) # 2 divide
print(5%2) # 1 remainder (..mod?)
print(3**2) # 9 sq
print(15//2) # divide no remainder

# 3.3.2 - comparison
print(5==2) # false, unequal
print(10!=10) #false, not not equal
print(2<5) # true, less than
print(12>5) # true, grater than
print(5<=6) # true, less equal than
print (1>= 10) #false, not greater equal than

# 3.3.2 - assignment
x= 5
x += 5
print(x) # 10, is x + 5
x=5
x-=4
print(x) # 1, is x - 4
x=5
x*=3
print(x) # 15, is x * 3

# 3.3.4 - logical
"""
1. What does the operator and do?
    returns true if both are true, else false
Write an expression that results in True. 
    10 == 10 and 5 != 10
Write an expression that results in False. 
    False and 3>5
2. What does the operator or do? 
    returns True if one is True, else False
Write an expression that results in True. 
    True or False
Write an expression that results in False. 
    False or False
3. What does the operator not do? 
    returns opposite
Write an expression that results in True. 
    False
Write an expression that results in False. 
    True
"""
# more questions

"""
1. What is the difference between / and //? 
    // no remainder, / remainder
2. What is the difference between % and //? 
    % only remainder
3. What operator would you use to calculate the remainder when dividing two numbers? Give an example. 
    %
    5%2 = 1
4. How do assignment operators work? 
    they assign that variable to a new value

"""

# --- 3.4 strings ---
my_string = "hello" 

print(my_string)
print(my_string[0])
for i in range(len(my_string)):
    print(my_string[i])
# wow i do not remember how to do anything in python
# index starts at 0, counts up

print(my_string[-1]) # last char i believe
print(my_string[1:3]) # from 1 to 3, not including 3 (el)
print(my_string[0:5:2]) # from 0 to 5, 2 per step (h_l_o minus the underscores. i suppose there being index 5 is ok here
print(len(my_string)) # length, 5
print(my_string + ", goodbye.") #hello, goodbye. 
print(7 * my_string) #hellohellohellohellohellohellohello

"""
Define the term slicing. For which of the manipulations did you slice your string? 
    I believe the ones that "slice" through the string

2. Call the following, describe the result: 
"""
name = "Oski" 
print("Hello, my name is", name) 

"""
    Hello, my name is Oski
    works as expected, i suppose the comma works like +

3. Call the following, describe the result. 
"""
name = "Oski" 
print(f"Hello, my name is {name}") 

"""
    google: the f is a formatted string, meaining that python looks through the string for the curly brackets
    and looks up the variable.

4. What is the difference between the two last print statements? 
Hint: Look up f-strings. 

    welp, ^

"""

# --- 3.5 terminal commands ---
"""
For each command listed below, do the following: 
1. Define the command as a comment. 
2. Explain how to use it. 
3. Give an example of how to use it. 
4. Try out the command on your terminal. 
"""

"""
1. cd 
    change directory, goes in that directory
    cd (folder name)
    in order to move somewhere
2. ls 
    list
    just type it
    use when want to find eveyrhting inside something

3. ls -a 
    same as list everything but it shows hidden and use when want to show hidden (list all)

4. mkdir 
    make directory
    makes a new folder
    mkdir new_folder

5. cat 
    concatenate
    displays the file contents in the terminal
    cat file_name

6. pwd 
    print working directory
    prints the file path basically
    pwd

7. cd .. 
    change directory to parent directory
    moves up one folder in file path
    js use it

8. cd . 
    erm.. 
    changes directory to current? not sure why you would use this one


9. cd ∼ 
    change directory to home 

10. cp 
    copy
    ex. cp file.txt to backup.txt


11. mv 
    move 
    ooh actually or rename!
    mv file_name location/
    mv file_name new_name

12. rm (be careful with this one) 
    remove
    deletes permenantly!
    rm file_name
    no delete

13. clear 
    clears terminal screen
    js for cleaning
    clear

14. grep 
    "global regular expression print"
    searches for text patterns..
    grep "example text" file_name


    
1. Look up 3 other commands not present. Define and explain how to use them on the command line. 
echo example_text 
    prints the input in the terminal
head file_name
    shows first ten lines of it
nano file_name
    text editor within the terminal
    

2. What is the difference between ls and ls -a? 
    ls -a shows the hidden files contrary to ls
3. What is a hidden file? 
    files hidden by default to avoid clutter
    signified with .file_name (period)
    config files or whatnot
4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line. 
    ls -l shows more info
    ls -h human readable numbers, shortens 1000 to 1k for example (gb, tb, etc.)
        ls -lh 
    rm -i adds safety confirmation after remove

"""