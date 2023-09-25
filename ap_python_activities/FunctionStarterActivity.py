# 1. In your own words, describe what a function is
A function that does something
Code that a computer can read and transform into data. 

# re-usable code. Only runs when called. 
def starterFunction(): #A function that does something Code that a computer can read and transform into data. 
    print("jaseil") # print users name
    print(2+2) # equals 4
    print("all done the program") #  finished the program

#starterFunction() # read



# 2. What is are function parameters and arguments and describe
# the difference between the 2.
A parameter is a variable in the declaration of the function. An argument is the actual value of the variable that gets passed to the function.

def addTwo(randomNumber): 1-20
    print(randomNumber + 2) # add 2 to the random number

def addtwo(randNumber): 2-21
    print(randNumber +2) # add 2 

print (addTwo) #addtwo(2)




# 3. Write a function that will print out a welcome message
# that includes a user's name. You will need to use parameters and arguments
def welcome_msg(username): jaseil
    print('welcome '+ username + ' to coding class.')
    print('have a great day')

#welcome_msg('Jaseil')


# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmetic operators (add, subtract, multiply, divide)

def calculate(randNumber, randomNumber2, randomNumber3): 
    print(randNumber +randomNumber2 + randomNumber3)

#calculate(7,12,12) # 7 100 700

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard-coded data.

def userMsg():
    nextClass = input('what is your next class.')
    print("you have " + nextClass +" after this.")
   
    
userMsg()
