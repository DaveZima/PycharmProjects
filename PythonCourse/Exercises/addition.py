##!/usr/bin/env python
"""
Script/Module:  addition.py

Parameters:     N/A

Description:    Importing modules exercise. Library module containst Addtion class.

Revision History:

Version  Date       Author              Description
-------- ---------- ------------------- -------------------------------------------------------------
1.0.0    2021-04-03 Dave Zima           It lives
"""
__version__ = "1.0.0"
__author__ = "Dave Zima"

###########
# Imports #
###########

# Standard library imports

# Third-party library imports

# Application library imports

####################
# Global Variables #
####################

###########
# Classes #
###########

#--------------------------------------------------------------------------------#
class Addition:

    @classmethod
    def add(cls,num1,num2):
        return num1 + num2

#--------------------------------------------------------------------------------#
class Calculator:

    @classmethod
    def add(cls,num1,num2):
        return num1 + num2

    @classmethod
    def subtract(cls,num1,num2):
        x = cls.add(num1,num2 * -1)
        return x

    @classmethod
    def multiply(cls,num1,num2):
        if num2 == 1:
            t = num1
        else:
            t = num1
            for i in range(num2 - 1):
                t = cls.add(t,num1)

        return t

    @classmethod
    def divide(cls,dividend,divisor):
        quotient = divisor
        i = 0
        while quotient <= dividend:
            quotient = cls.add(quotient,divisor)
            i += 1

        return i

#############
# Functions #
#############

