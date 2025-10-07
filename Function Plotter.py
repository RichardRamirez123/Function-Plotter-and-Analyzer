# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 21:58:18 2025

@author: richard ramirez

This program is going to plot a linear function (y = m*x + b), 
its derivative and integral. 

The program uses the function, f(x) = 4*x + 2, over the interval of [-10,10],
with 20 points. However these are easily adjustable meaning the user can define
the slope, y-intercept, number of points, and the min and max of the interval

"""
from matplotlib import pyplot as plt

def main():
    
    print("This program assumes the linear equation form y = mx + b\n")
    
    # defining variables, adjustable
    m = float(input("Enter the value m for the slope of your linear function: \n")) #ex (4) # slope of linear function, only int/float
    
    b = float(input("Enter the value b for the y-intercept of your linear function: \n")) #ex (2) # y-intercept of linear function, only int/float
    
    n = int(input("Enter the value of points to plot? \n")) #ex (20) # number of points to plot, only integer, only positive
    
    low = -10     # beginning of interval, only int/float
    
    high = 10     # end of interval, only int/float
    
    
    
    # check if number of points is a valid number, negative numbers break program
    if n <= 1:
        
        print("Error: Number of points must be greater than 1.")
        
        return
    
    
    
    # defining variables, non-adjustable
    x = linspace(low,high,n)     # generate independent variable
    
    y = [0.0]*n     # initialize y-list of original linear function
    
    dY = [0.0]*n     # initialize y-list of the derivatice of linear function
    
    iY = [0.0]*n     # initialize y-list of the integral of linear function
    
    
    
    # calculates y-values from original linear function inside range of interval
    y = originalPoints(fun, x, y, m, b, n)
    
    # calculates y-values from the derivative of linear function in interval
    dY = calcDerivative(m, n, dY)
    
    # calculates y-values from the integral of linear function in interval
    iY = calcIntegral(x,m,b,n,iY)
    
    # plots original linear function, its derivative, and its integral
    graph(x,y,dY,iY)
    

def fun(m,x,b):
    """
    This function defines the formula for a linear function.

    Parameters
    ----------
    m : int/float
        slope of the linear function.
    x : list
        values of x.
    b : int/float
        y-intercept of linear function.

    Returns
    -------
    y : int/float
        dependent value of x, result of linear function at x.

    """
    
    # linear function formula
    y = m*x + b
    
    return y


def linspace(low,high,n_pts):
    """
    This function correctly generates and spaces out the values of x

    Parameters
    ----------
    low : int/float
        beginning of interval of points.
    high : int/flaot
        end of interval of points.
    n_pts : int
        number of points.

    Returns
    -------
    x : list
        values of x throughout the interval.

    """
    # create empty list
    x = [0.0]*n_pts
    
    # calculate increment
    incr = (high-low)/(n_pts-1)
    
    # assign low value to first element
    x[0] = low
    
    # loop through index values
    for idx in range(n_pts - 1):
        
        x[idx+1]=x[idx] + incr
        
    return x
    

def originalPoints(fun, x, y, m, b, n):
    """
    This function finds the y-values of the linear function at each value of x

    Parameters
    ----------
    fun : function
        linear function x-values are put into to find output/y-values.
    x : list
        values of x.
    y : list
        empty list of values of y.
    m : int/float
        slope of linear function
    b : int/float
        y-intercept of linear function.
    n : int
        number of points.

    Returns
    -------
    y : list
        list of y-values from the original function to plot.

    """
    
    # loop through each value of x through original linear function
    # get dependent y-value at x
    for i in range(n):
        y[i] = fun(m, x[i], b)
        
    # y-values of f(x)    
    return y


def calcDerivative(m, n, dY):
    """
    This function uses the derivative of a linear function, the slope which is m,
    and assigns it to each value of dY, the y-values of the derivative 

    Parameters
    ----------
    m : int/float
        slope of linear function.
    n : int
        number of points.
    dY : list
        empty list of y-values based on the derivative of linear function.

    Returns
    -------
    dY : list
        list of y-values from the derivatice of original function to plot.

    """
    
    # assign slope to the y-values, this is the derivative of a linear function
    for i in range(n):
        dY[i] = m
    
    # y-values of derivative of f(x)
    return dY

    
def calcIntegral(x,m,b,n,iY):
    """
    This function finds the y-values of the integral of a linear function at
    each values of x. It calculates the integral by using the power rule of
    integration

    Parameters
    ----------
    x : list
        list of x-values.
    m : int/float
        slope of linear function.
    b : int/float
        y-intercept of linear function.
    n : int
        number of points.
    iY : list
        empyt list of y-values based on integral.

    Returns
    -------
    iY : list
        list of y-values from output of integral.

    """
    
    # loop through each value of x through integral of linear function
    # get dependent y-value at x
    for i in range(n):
        
        iY[i] = ((m*x[i]*x[i]) / 2.0) + (b*x[i])
    
    # y-values of integral of f(x)    
    return iY


def graph(x,y,dY,iY):
    """
    This function graphs the lists collected throughout the functions.

    Parameters
    ----------
    x : list
        values of x throughout the interval.
    y : list
        values of y based on the original linear function at x.
    dY : list
        values of y based on the derivative of linear function at x.
    iY : list
        values of y based on the integral of linear function at x.

    Returns
    -------
    None.

    """
    
    # plot points of original linear function
    plt.plot(x,y,"o",color='green')
    plt.plot(x,y,"-",color='green')
    
    # plot points of derivative of linear function
    plt.plot(x,dY,"o",color='red')
    plt.plot(x,dY,"-",color='red')

    # plot points of integral of linear function
    plt.plot(x,iY,"o",color='blue')
    plt.plot(x,iY,"-",color='blue')
        
    plt.xlabel("Independent Variable")
    plt.ylabel("Dependent Variable")
    plt.title("Linear Function as Original, Derivative and Integral")
    plt.legend(["Original f(x)","", "Derivative f(x)","", "Integral of f(x)", ""])
    plt.show()
    
    
# call main
main()