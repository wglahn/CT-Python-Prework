# Wade Glahn 
# Python 102 Prework Coding Questions

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the funtion.

def hello_name(user_name):
    print(f"Hello {user_name.title()}!")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for num in range(1, 100, 2):
        print(num)

# Question 3
# Please write a Python funtion, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    return max(a_list)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not
# divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false)

def is_leap_year(a_year):
    if (a_year % 4) == 0:
        if (a_year % 100) == 0 and (a_year % 400) != 0:
            return False
        else:
            return True
    else:
        return False

# Question 5
# Write a function to check to see if all numbers in a list are consecutive numbers. For example [2,3,4,5,6,7]
# are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    boolean = True

    for item in range(1, len(a_list)):
        if a_list[item] != (a_list[item-1]+1):
            boolean = False
    
    return boolean