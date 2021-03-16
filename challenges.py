## Acronym
## Given a string, return an acronym containing the first letter of every word in the string
## "Will you answer the door?" --> return "Wyatd"

## declare a function, accept a string as a function
    ## store the first letter
    ## loop through the string
        ## if current value is a space
        ## add next string value to acronym
    ## return acronym

# def generate_acronym(long_string):
#     acronym = long_string[0]
#     for i in range(len(long_string)):
#         if long_string[i] == " ":
#             acronym += long_string[i+1]
#     return acronym

# print(generate_acronym("Welcome To Python"))
# print(generate_acronym("Object Oriented Programming"))
# print(generate_acronym("Application Programming Interface"))

## Parentheses Valid
## Given a string, test whether parentheses inside of the string are valid. 
# "he(llo)()" --> returns True, opening parentheses have corresponding closing parentheses
# "goodb(ye)(" --> returns False, opening parenthese is missing closing parenthese
# "hell)(ogood(bye)" --> returns False, closing parenthese comes before opening

# declare my function, given a string
    ## declare a close count
    ## declare an open count
    ## Loop through the string
        ## if open paren
            ## count open
        ## if close paren
            ## count close
        ## if close > open
            ## return False
    ## if count open == count close
        ## return True
    ## return False

# def parens_valid(par_string):
#     open_count=0
#     close_count=0
#     for letter in par_string:
#         if letter == "(":
#             open_count+= 1
#         elif letter == ")":
#             close_count+=1
#         if close_count > open_count:
#             return False
#     if open_count == close_count:
#         return True
#     return False
# print(parens_valid("goodb(ye)()()()"))

# Given a list of numbers, sort the numbers with the smaller number on the left and the largest number on the right
# def list_of_nums(some_list):
#     for num in range(len(some_list)): 
#         minnum = min(some_list[num:])
#         min_index = some_list[num:].index(minnum)
#         some_list[num + min_index] = some_list[num]
#         some_list[num] = minnum
#         print(minnum)
# loop through list
# find smallest number and swap with the number at the zero index
# find second smallest number and swap with the number at the 1st index

# list_of_nums([8, 5, 2, 6, 9, 3, 1, 4, 0, 7])

 def print_greeting():
#     print("Hello, Welcome to python")
# print_greeting():

# def print_greeting(name):
#     print(f"Hello {name}, welcome to python!")
# print_greeting("liam")

# def print_greeting(name):
    # print(f"Hello {name}, welcome to python!") #prints Hello Liam, welcome to python!
    # return name # Return will not show up unless you print what the function evaluates to on this line
# print_greeting("Liam")

# def print_greeting(name):
#     print(f"Hello {name}, welcome to python!")
#     return name 
# print(print_greeting("Liam")) #Return is shown because function was called with a print statement around it

# def print_greeting(name, num):
#     for i in range(num):
#         print(f"Hello {name}, welcome to session two python!")
#     return[num, name]
# print_greeting("Adam", 10)

# def print_greeting(name, num=1):
#     for i in range(num):
#         print(f"Hello {name}, welcome to session two python!")
#     return[num, name]
# print_greeting("Adam")

# def print_greeting(name="Vineet", num=1):
#     for i in range(num):
#         print(f"Hello {name}, welcome to session two python!")
#     return[num, name]
# print_greeting()

# def print_greeting(name="Vineet", num=1):
#     for i in range(num):
#         print(f"Hello {name}, welcome to session two python!")
#     return[num, name]
# print_greeting("Cameron") # overrides the str Vineet

# def print_greeting(name="Vineet", num=1):
#     for i in range(num):
#         print(f"Hello {name}, welcome to session two python!")
#     return[num, name]
# print_greeting(num = 10, name="Cameron") # overrides both 1 & Vineet
