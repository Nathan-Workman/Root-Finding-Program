# -------------------------------------------------------------------------------
# Name: Nathan Workman
# Date:   10/17/19
# Assignment:  Numerical Analysis Root Methods (Project 1)
# Description:   Calculate root finding methods
# -------------------------------------------------------------------------------
# NOTE: e(Stopping condition/convergence tolerance) typically changes e, make sure it is correct before testing. Max iterations is at the constant of 35
#All constants/variables that could be changed are at the start of each function. To run a specific method go to the bottom and uncomment the function call
import numpy as np                                  #Importing numpy to use
import math                                         #Importing the math module to use
####################################################################################################################################
#FUNCTIONS USED FOR METHODS
######################################################################################################
#BISECTION METHOD
#USE (.4,.48) as interval
def evalfunbi(x):  # Function for evaluating function "F" 
     return (math.tan((math.pi * x)) - x - 6)  # Function F, Do not ask for input, just change when need too


######################################################################################################
######################################################################################################
#FALSE POSITION FUCTION
#USE (.4,.48) as interval
def evalfunfalse(x):  # Function for evaluating function "F"
        return (math.tan((math.pi * x)) - x - 6)  # Function F, Do not ask for input, just change when need too

######################################################################################################
######################################################################################################
#FIXED POINT FUNCTION
#USE any dec. greater than  .1
def evalfunfixed(x):  # Genteration Function for evaluating
        return ((2 * x * (1 - x)))  # Genteration Function G, Do not ask for input, just change when needed

#######################################################################################################
######################################################################################################
#NEWTON METHOD FUCTIONS
#USE 1 as the starting value
def evalfunnewton(x):  # Genteration Function for evaluating
        return (math.pow(x, 7) - 3)  # Genteration Function G, Do not ask for input, just change when needed

    ######################################################################################################
    ######################################################################################################
    # Derivative
def evalderi(x):  # Genteration Function for evaluating, Derivative
        return (7 * math.pow(x, 6))  # Genteration Function G, Do not ask for input, just change when needed

    ######################################################################################################
######################################################################################################
#ACCELERATION USING FALSE POSITION FUCTION
#USE any dec. greater than  .1
def evalfunfalseacc(x):  # Function for evaluating function "F"
        return (math.tan((math.pi * x)) - x - 6)  # Function F, Do not ask for input, just change when need too

######################################################################################################

####################################################################################################################################

def Bisection():
    Nmax = 35  # Max iterations wanted, can be chnaged to get input.
    sfa = 0  # Initializing variable sfa, indicates the sign of "F" at "a"
    sfp = 0  # Initializing variable sfp, indicates the sign of "F" at "p"
    p = 0  # Initializing variable p
    i = 0  # Iteration counter, mainly used for debug
    e = (5 * (10 ** (-5)))  # Convergence Tolerance
    realzero = (.45104726)  # Real root as a variable, used to find error, can be changed if changing function
    error = 0  # Initializing variable error

    while True:  # Loops to check user-input, making sure the interval is a number
        try:
            a = float(input("Left Interval:"))  # Getting input for left interval
            b = float(input("Right Interval:"))  # Getting input for right interval
        except ValueError:  # If the type is not a integer it will print an error text
            print("That is not a vaild, please try again.")
         # better try again... Return to the start of the loop
            continue
        else:
            break  # If type is right, the loop breaks
    ######################################################################################################

    f = evalfunbi(a)  # Calling the function and evaluating it at "a"
    f = np.sign(f)  # Using numpy we just take the sign of what "F(a)" is. Note negative = 1 and positive = 1
    print("Iteration      Enclosing Interval           Aproximation                    Error")  # Formats print to show the enclosing interval/guess and error

    for i in range(1, Nmax):  # Loop created to find our root
        p = (((a) + (b)) / 2)  # We evaluate what "p" is by this formula
        error = (abs(p - realzero))  # We find the error of our guess by taking the absolute value of our guess-realzero
        print("    %d      (%.10f,%.10f)      %.10f                %.10f" % (i, a, b, p, error))  # Formats print to show the enclosing interval/guess and error
        i = (i + 1)
        if ((b - a) < (2 * e)):  # Compare to convergence tolerance to see when we are close to getting our root(zero)
            print("The Root is: ", p)  # If true we print what "p" is as the given iteration
            print("It took", i, "iterations to find the root.")  # Print number of iterations it took to find the root
            break  # Break out of the loop, we found our answer
        f = evalfunbi(p)  # If we havent meet our convergence tolerance we reevaluate "f" with "p"
        if f < 0:  # Another if statement we use this to check which interval to cut
            sfp = -1  # Resetting varaibles to reloop
        else:
            sfp = 1  # Resetting variables to reloop
        if (sfp * sfa) < 0:  # Resetting variables to reloop
            b = p
        else:
            a = p  # Resetting variables to reloop
            sfa = sfp  # Resetting variables to reloop
        if (i == Nmax):  # If Nmax is hit we stop and tell the user max iterations exceeded
            print("Max number of iterations exceeded")

########################################################################################################################################################


def FalsePosition():
    Nmax = 35  # Max iterations wanted, can be chnaged to get input.
    sfa = 0  # Initializing variable sfa, indicates the sign of "F" at "a"
    sfp = 0  # Initializing variable sfp, indicates the sign of "F" at "p"
    p = 0  # Initializing variable p
    i = 0  # Iteration counter, mainly used for debug
    e = (5 * (10 ** (-5)))  # Convergence Tolerance
    Y = 0  # Initializing variable Y, used when calculating guess
    realzero = (.45104726)  # Real root as a variable, used to find error, can be changed if changing function
    error = 0  # Initializing variable error
    pold = 0  # Initializing variable pold, we store the value of pn-1 here
    polder = 0  # Initializing  variable polder, we store the value of pn-2 here
    lamval = 0         # Initializing  variable lamval, the value of lambda will be stored here

    while True:  # Loops to check user-input, making sure the interval is a number
        try:
            a = float(input("Left Interval:"))  # Getting input for left interval
            b = float(input("Right Interval:"))  # Getting input for right interval
        except ValueError:
            print("That is not a vaild, please try again.")  # If the type is not a integer it will print an error text
            # better try again... Return to the start of the loop
            continue
        else:
            break  # If type is right, the loop breaks
    ######################################################################################################

    fa = evalfunfalse(a)  # Calling the function and evaluating it at "a"
    fb = evalfunfalse(b)  # Calling the function and evaluating it at "b"
    fas = np.sign(fa)  # Using numpy we just take the sign of what "F(a)" is. Note negative = 1 and positive = 1
    fbs = np.sign(fb)  # Using numpy we just take the sign of what "F(b)" is. Note negative = 1 and positive = 1
    print("Iteration      Enclosing Interval           Aproximation               Error               Lambda")  # Formats print to show the enclosing interval/guess and error

    for i in range(1, Nmax):  # Loop created, loop until we hit Nmax
        p = ((b - (fb * ((b - a) / (fb - fa)))))  # We evaluate what "p" is by this formula
        error = (abs(p - realzero))  # We find the error of our guess by taking the absolute value of our guess-realzero
        print("    %d      (%.10f,%.10f)      %.10f            %.10f        %.10f" % (i, a, b, p, error, lamval))  # Formats print to show the enclosing interval/guess and error

        if i > 2:  # After two iterations we will then have enough stored to approx. the root
            Y = ((p - pold) / (pold - polder))  # We find Y which is just the Lamda formula
            errest = (abs((Y * (p - pold)) / (Y - 1)))  # This is the rest of the formula needed for Falsepos. Using Y we can complete finding the root.
            lamval = abs(((p - pold) / (pold - polder)))  # This is how we calculate lamda we use this to compare convergence

            if ((errest < e)):  # If errest is less than our convergence we will do:
                print("The root is: ", p)  # We print our guess
                print("It took", i,"iterations to find the root.")  # We also print how long it took to find the root
                break  # Break oout of the loop, we found our root
        fp = evalfunfalse(p)  # we evaluate the function at p and store it in fp
        sfp = np.sign(fp)  # We take the sign of fp and store it in sfp

        if (sfp * sfa) < 0:  # If the sign of 'p' and the sign of 'a' multiplied is less than 0 then
            b = p  # Resetting variables to reloop
            fb = fp  # Resetting variables to reloop
        else:
            a = p  # Resetting variables to reloop
            fa = fp  # Resetting variables to reloop
        polder = pold  # Resetting variables to reloop
        pold = p  # Resetting variables to reloop

        if (i == Nmax):
            print("Max number of iterations exceeded")  # If Nmax is reached and no root is found then the loop stops and says max iterations exceeded

##########################################################################################################################################################



def Fixedpoint():
    Nmax = 35  # Max iterations wanted, can be chnaged to get input.
    i = 0  # Iteration counter
    e = (5 * (10 ** (-5)))  # Convergence Tolerance
    sc = 0  # Stopping Condition, Linear or Superlinear
    x0 = 0                        # Initializing  variable xo, this is the starting value
    realzero = (.5)                 #Real root as a variable, used to find error, can be changed if changing function
    error = 0                     #Initializing variable error
    lamval = 0                    # Initializing  variable lamval, the value of lambda will be stored here

    while True:  # Loops to check user-input, making sure the starting value is a number
        try:
            x1 = float(input("Starting Value:"))  # Getting input for starting value\
            conveg = int(input(
                "Is this Linear or Superlinear Convergence? (Type '1' for Linear and '2' for Superlinear): "))  # Convergence Type 1=Linear, 2=Superlinear
        except ValueError:  # If the type is not a integer it will print an error text
            print("That is not a vaild, please try again.")
            # better try again... Return to the start of the loop
            continue
        else:
            break  # If type is right, the loop breaks
    ######################################################################################################
    print("Iteration              Aproximation             Error              Lambda")  # Formats print to show the guess/error and lamda

    for i in range(1, Nmax + 1):  # Loop created, loop until we hit Nmax
        x2 = evalfunfixed(x1)  # We evaluate what "x2" is by evaluating our function at x1(Starting)
        error = (abs(realzero - x2))  # We find the error of our guess by taking the absolute value of our guess-realzero
        print("   p%d    =   g(%d)  =   %.10f          %.10f        %.10f" % (i, i - 1, x2, error, lamval))  # Formats print to show the #of iteration we are on/guess and error

        if i > 2:  # After two iterations we will then have enough stored to approx. the root
            lamval = abs((x2 - realzero) / (math.pow(x1 - realzero, 2)))  # This is how we calculate lamda we use this to compare convergence

            if conveg == 1:  # Formula used if function is linear, is conveg is 1
                sc = (abs((x2 - x1) / (x1 - x0)))
            else:
                sc = (abs(x1 - x2))  # Formula used if function is Superlinear, if conveg isnt 1 so 2. Could work with any number
            if abs(sc) < e:  # This is our stopping condition, we check if abs(sc) our formula based on convergence is less than our tolerance
                print("The root is: ", x2)  # If this is true we print our x2
                print("It took", i, "iterations to find the root.")
                break  # Break out of loop
        x0 = x1  # If not we are resetting variables to reloop
        x1 = x2  # If not we are resetting variables to reloop
        if (i == Nmax):  # If Nmax is reached and no root is found then the loop stops and says max iterations exceeded
            print("Max number of iterations exceeded")

##########################################################################################################################################################


def Newton():
    Nmax = 35  # Max iterations wanted, can be chnaged to get input.
    i = 0  # Iteration counter
    e = (5 * (10 ** (-5)))  # Convergence Tolerance
    sc = 0  # Stopping Condition, Linear or Superlinear
    x0 = 0              #Initializing variable xo
    realzero = (math.pow(3, (1 / 7)))          #Real root as a variable, used to find error, can be changed if changing function
    error = 0                                   #Initializing variable error
    lamval = 0                                      # Initializing  variable lamval, the value of lambda will be stored here 

    while True:  # Loops to check user-input, making sure the starting value is a number
        try:
            x1 = float(input("Starting Value:"))  # Getting input for starting value\
            # conveg= int(input("Is this Linear or Superlinear Convergence? (Type '1' for Linear and '2' for Superlinear): "))            #Convergence Type 1=Linear, 2=Superlinear
        except ValueError:  # If the type is not a integer it will print an error text
            print("That is not a vaild, please try again.")
            # better try again... Return to the start of the loop
            continue
        else:
            break  # If type is right, the loop breaks
    ######################################################################################################
    print("Iteration         Aproximation                Error                Lambda")  # Formats print to show the guess/error and lamda

    for i in range(1, Nmax + 1):  # Loop created, loop until we hit Nmax

        x2 = (x1 - ((evalfunnewton(x1)) / (evalderi(x1))))  # We evaluate what "x2" is by evaluating our function at x1(Starting)

        error = (abs(realzero - x2))  # We find the error of our guess by taking the absolute value of our guess-realzero
        print("   p%d      =      %.10f             %.10f         %.10f" % (i, x2, error, lamval))  # Formats print to show the guess/error and lamda

        if i > 2:  # After two iterations we then, do as follows
            lamval = abs((x2 - realzero) / (math.pow(x1 - realzero, 2)))  # This is how we calculate lamda we use this to compare convergence
        if abs(x2 - x1) < e:  # Stopping condition, as long as x2-realzero is less then our e
            print("The root is: ", x2)  # We print the root
            print("It took", i, "iterations to find the root.")  # How many iterations it took to get to the zero
            break  # Breaks out of loop since answer is found

        x1 = x2  # If not we are resetting variables to reloop

        if (i == Nmax):  # If Nmax is reached and no root is found then the loop stops and says max iterations exceeded
            print("Max number of iterations exceeded")
######################################################################################################################################################################
def Acceleration():            #USING FALSE-POSITION
    Nmax = 35  # Max iterations wanted, can be chnaged to get input.
    sfa = 0  # Initializing variable sfa, indicates the sign of "F" at "a"
    sfp = 0  # Initializing variable sfp, indicates the sign of "F" at "p"
    p = 0  # Initializing variable p
    i = 0  # Iteration counter, mainly used for debug
    e = (5 * (10 ** (-5)))  # Convergence Tolerance
    Y = 0  # Initializing variable Y, used when calculating guess
    realzero = (.45104726)  # Real root as a variable, used to find error, can be changed if changing function
    error = 0  # Initializing variable error
    pold = 0  # Initializing variable pold, we store the value of pn-1 here
    polder = 0  # Initializing  variable polder, we store the value of pn-2 here
    lamval = 0         # Initializing  variable lamval, the value of lambda will be stored here

    while True:  # Loops to check user-input, making sure the interval is a number
        try:
            a = float(input("Left Interval:"))  # Getting input for left interval
            b = float(input("Right Interval:"))  # Getting input for right interval
        except ValueError:
            print("That is not a vaild, please try again.")  # If the type is not a integer it will print an error text
            # better try again... Return to the start of the loop
            continue
        else:
            break  # If type is right, the loop breaks
    ######################################################################################################

    fa = evalfunfalseacc(a)  # Calling the function and evaluating it at "a"
    fb = evalfunfalseacc(b)  # Calling the function and evaluating it at "b"
    fas = np.sign(fa)  # Using numpy we just take the sign of what "F(a)" is. Note negative = 1 and positive = 1
    fbs = np.sign(fb)  # Using numpy we just take the sign of what "F(b)" is. Note negative = 1 and positive = 1
    print("THIS IS USING THE METHOD OF ACCELERATION (AITKINS'S METHOD)")
    print("Iteration      Enclosing Interval           Aproximation               Error               Lambda")  # Formats print to show the enclosing interval/guess and error

    for i in range(1, Nmax):  # Loop created, loop until we hit Nmax
        p = ((b - (fb * ((b - a) / (fb - fa)))))  # We evaluate what "p" is by this formula
        error = (abs(p - realzero))  # We find the error of our guess by taking the absolute value of our guess-realzero
        print("    %d      (%.10f,%.10f)      %.10f            %.10f        %.10f" % (i, a, b, p, error, lamval))  # Formats print to show the enclosing interval/guess and error

        if i > 2:  # After two iterations we will then have enough stored to approx. the root
            p = (polder-(math.pow(polder-pold,2)/(polder + p - 2 *pold)))  # We evaluate what "p" is by this formula
            Y = ((p - pold) / (pold - polder))  # We find Y which is just the Lamda formula
            errest = (abs((Y * (p - pold)) / (Y - 1)))  # This is the rest of the formula needed for Falsepos. Using Y we can complete finding the root.
            lamval = abs(((p - pold) / (pold - polder)))  # This is how we calculate lamda we use this to compare convergence

            if ((errest < e)):  # If errest is less than our convergence we will do:
                print("The root is: ", p)  # We print our guess
                print("It took", i,"iterations to find the root.")  # We also print how long it took to find the root
                break  # Break oout of the loop, we found our root
        fp = evalfunfalse(p)  # we evaluate the function at p and store it in fp
        sfp = np.sign(fp)  # We take the sign of fp and store it in sfp

        if (sfp * sfa) < 0:  # If the sign of 'p' and the sign of 'a' multiplied is less than 0 then
            b = p  # Resetting variables to reloop
            fb = fp  # Resetting variables to reloop
        else:
            a = p  # Resetting variables to reloop
            fa = fp  # Resetting variables to reloop
        polder = pold  # Resetting variables to reloop
        pold = p  # Resetting variables to reloop

        if (i == Nmax):
            print("Max number of iterations exceeded")  # If Nmax is reached and no root is found then the loop stops and says max iterations exceeded

    
   
#####################################################################################################################################################################   
#Uncomment which Method you want to run, it will start the given method onced code is started 

#USE (.4,.48) as interval-BISECTION
#Bisection()
            
#FALSE POSITION FUCTION
#USE (.4,.48) as interval           
#FalsePosition()
            
#FIXED POINT FUNCTION
#USE any dec. greater than  .1         
#Fixedpoint()
            
#NEWTON METHOD FUCTIONS
#USE 1 as the starting value            
#Newton()
 
#ACCELERATION FUNCTION
#USE any dec. greater than  .1             
#Acceleration()
    
