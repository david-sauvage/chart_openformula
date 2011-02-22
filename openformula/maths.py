"""
Module that gives mathematicals functions of open formula
except for convert, euroconvert and subtotal
"""

#Import from Open Formula
from objects import Number, CellReference, RangeReference, LogicalExpression
from utils import is_num_range_list
from syntax import of_parameter_list

#
#Private API
#

def __simple_function(function, number):
   """
   Generic implementation the syntax for simple function like
   FUNCTION(number)
   
   Arguments :
       function -- str
       number -- Number or CellReference
   """
   if type(function) is str and isinstance(number, (Number, CellReference)):
      return function.upper()+"("+number.str+")"
   else:
      raise TypeError, "Argument must be a Number or a CellReference"


def __simple_function2(function, number1, number2):
   """
   Generic implementation the syntax for simple function with two arguments 
   like FUNCTION(number1, number2)
   
   Arguments :
       function -- str
       number -- Number or CellReference
   """
   if (type(function) is str and type(number1) in (Number, CellReference) and 
                                      type(number2) in (Number, CellReference)):
      return function.upper()+"("+of_parameter_list(number1.str,
                                                                number2.str)+")"

   else:
      raise TypeError, "Arguments must be Numbers or CellReferences"

def __num_list_function(function, *number_list):
   """
   Generic implementation the syntax for simple function with many arguments 
   like FUNCTION(num1, num2, num3, etc...)

   Arguments :
       function -- str
       number -- Number or CellReference or RangeReference
   """
   if type(function) is str and is_num_range_list(number_list):
      parameter = ""
      for i in number_list:
         parameter = parameter+i.str+" ; "
      return function.upper()+"("+parameter[0:-3]+")"
   else:
      raise TypeError, "Arguments must be Numbers or CellReferences"

def __round(function, number, count):
   """
   Generic function used by all the round function in open formula

   Arguments :
       function -- str
       number -- Number or CellReference
       count -- None or Number or CellReference
   """
   if count is None:
      if type(function) is str and type(number) in (Number, CellReference):
         return function.upper()+"("+of_parameter_list(number.str)+")"
      else:
         raise TypeError, "Argument must be a Number or a CellReference"
   else:
      if (type(function) is str and type(number) in (Number, CellReference) and 
                                        type(count) in (Number, CellReference)):

	 return function.upper()+"("+of_parameter_list(number.str,
                                                                 count.str)+")"

      else:
         raise TypeError, "Arguments must be Numbers or CellReferences"

def __floor_ceil(function, number, significance, mode):
   """
   Generic function used by ceil & floor function included in open formula

   Arguments
       function -- str 
       number -- Number or CellReference
       significance -- Number or CellRefenrece
       mode -- None or Number or CellReference
   """
   if mode is None:
      if (type(function) is str and type(number) in (Number, CellReference) and 
                                type(significance) in (Number, CellReference)):

	 return function.upper()+"("+of_parameter_list(number.str,
                                                           significance.str)+")"

      else:
         raise TypeError, "Arguments must be Numbers or CellReferences"
   else:
      if (type(function) is str and type(number) in (Number, CellReference) and 
			     type(significance) in (Number, CellReference) and 
                                        type(mode) in (Number, CellReference)):

	 return function.upper()+"("+of_parameter_list(number.str,
                                                 significance.str, mode.str)+")"

      else:
         raise TypeError, "Arguments must be Numbers or CellReferences"

#
#Public API
#

def ABS(number):
    """Return the syntax for an absolute value """
    return __simple_function("ABS", number)

def ACOS(number):
    """Return the syntax for arccosine """
    return __simple_function("ACOS", number)

def ACOSH(number):
    """Return the syntax for an inverse hyperbolic cosine """
    return __simple_function("ACOSH", number)

def ACOT(number):
    """Return the syntax for an inverse cotangent """
    return __simple_function("ACOT", number)

def ACOTH(number):
    """Return the syntax for an inverse hyperbolic cotangent """
    return __simple_function("ACOTH", number)

def ASIN(number):
    """Return the syntax for an arcsine """
    return __simple_function("ASIN", number)

def ASINH(number):
    """Return the syntax for an inverse hyperbolic sine """
    return __simple_function("ASINH", number)

def ATAN(number):
    """Return the syntax for a tangent """
    return __simple_function("ATAN", number)

def ATAN2(number1, number2):
    """Return the syntax for a tangent with specified coordonates """
    return __simple_function2("ATAN2", number1, number2)

def ATANH(number):
    """Return the syntax for an inverse hyperbolic tangent """
    return __simple_function("ATANH", number)

def CEILING(number, significance, mode=None):
    """
    Return the syntax for a ceiling
    Rounds a number to the nearest multiple of significance
    """
    return __floor_ceil("CEILING", number, significance, mode)
    
def COMBIN(number1, number2):
    """
    Return the syntax for a combination (without repetitions)
    Calculates the number of combinations for elements without repetition
    """
    return __simple_function2("COMBIN", number1, number2)

def COMBINA(number1, number2):
    """
    Return the syntax for a combination (with repetitions)
    Calculates the number of combinations for elements including repetition
    """ 
    return __simple_function2("COMBINA", number1, number2)
   
def COS(number):
    """Return the syntax for a cosine """
    return __simple_function("COS", number)

def COSH(number):
    """Return the syntax for an hyperbolic cosine """
    return __simple_function("COSH", number)

def COT(number):
    """Return the syntax for a cotagent """
    return __simple_function("COT", number)

def COTH(number):
    """Return the syntax for an hyperbolic cotangent """
    return __simple_function("COTH", number)

def COUNTBLANK(cell_range):
    """Return the syntax for a countblank """
    if type(cell_range) in (CellReference, RangeReference):
            return "COUNTBLANK("+cell_range.str+")"
    else:
        raise TypeError, "Argument must be a RangeReference or a CellReference"

def COUNTIF(cells, criteria):
   """Return the syntax for a countif """
   if (type(cells) in (CellReference, RangeReference) and type(criteria) in 
               (Number, CellReference, RangeReference, LogicalExpression, str)):

      return "COUNTIF("+cells.str+";"+criteria.str+")"
   else:
      raise TypeError, """First argument has to be CellReference or  
			RangeReference, second argument must be Number,  
                        CellReference, RangeReference"""

def DEGREES(number):
    """
    Return the syntax for a degrees
    Convert Radians to Degrees
    """
    return __simple_function("DEGREES", number)

def EVEN(number):
    """
    Return the syntax for an even
    Rounds a positive number up and a negative number down
    to the nearest even integer
    """
    return __simple_function("EVEN", number)

def EXP(number):
    """
    Return the syntax for an exponential
    Calculates the exponent for basis e
    """
    return __simple_function("EXP", number)

def FACT(number):
    """Return the syntax for an factorial """
    return __simple_function("FACT", number)

def FLOOR(number, significance, mode=None):
    """
    Return the syntax for a floor
    Round number down to the nearest multiple of significance
    """
    return  __floor_ceil("FLOOR", number, significance, mode)

def GCD(*number_list):
    """Return the syntax for a Greatest Common Divisor """
    return __num_list_function("GCD", *number_list)
 

def GCD_ADD(*number_list):
    """Return the syntax for a Greatest Common Divisor """
    return __num_list_function("GCD_ADD", *number_list)

def INT(number):
    """
    Return the syntax for an integer function
    Round a number to the nearest integer
    """
    return __simple_function("INT", number)
 
def ISEVEN(number):
    """
    Return the syntax for an "iseven"
    Return true if the value is an even integer
    """
    return __simple_function("ISEVEN", number)

def ISODD(number):
    """Return the syntax for an "isodd"
    Return true if the value is an odd integer
    """
    return __simple_function("ISODD", number)

def LCM(*number_list):
    """Return the syntax for a lowest common multiple """
    return __num_list_function("LCM", *number_list)

def LCM_ADD(*number_list):
    """Return the syntax for a lowest common multiple """
    return __num_list_function("LCM_ADD", *number_list)

def LN(number):
    """
    Return the syntax for a "ln"
    Calculates the natural logarithm
    """
    return __simple_function("LN", number)

def LOG(number, base):
    """
    Return the syntax for a "log" with the base you want
    Calculates the logarithm to any specified base
    """
    return __simple_function2("LOG", number, base)

def LOG10(number):
    """
    Return the syntax for a "log" in base 10
    Calculates the base 10 logarithm of a number
    """
    return __simple_function("LOG10", number)

def MOD(dividend, divisor):
    """Return the syntax for a "modulo" """
    return __simple_function2("MOD", dividend, divisor)

def MROUND(number, multiple):
    """
    Return the syntax for a "mround"
    returns the number rounded to a specified multiple
    """
    return __simple_function2("MROUND", number, multiple)

def MULTINOMIAL(*number_list):
    """
    Return the syntax for a "multinomial"
    Return the multinomial coefficient of a set of number
    """
    return __num_list_function("MULTINOMIAL", *number_list)

def ODD(number):
    """
    Return the syntax for an "odd" 
    Rounds a positive number up and a negative number down
    to the nearest odd integer
    """
    return __simple_function("ODD", number)

def PI():
    """Return the syntax in order to get Pi """
    return "PI()"

def POWER(base, exponent):
    """Return the syntax for a power (base^exponent)"""
    return __simple_function2("POWER", base, exponent)

def PRODUCT(*number_list):
    """Return the syntax for a product """
    return __num_list_function("PRODUCT", *number_list)
  
def QUOTIENT(numerator, denominator):
    """Return the syntax for a quotient """
    return __simple_function2("QUOTIENT", numerator, denominator)

def RADIANS(number):
    """
    Return the syntax for a "radians"
    Convert degrees to radians
    """
    return __simple_function("RADIANS", number)

def RAND():
    """Return the syntax in order to get a random number """
    return "RAND()"

def RANDBETWEEN(bottom, top):
    """
    Return the syntax for a randbetween
    in order to get a random number between bottom and top
    """
    return __simple_function2("RANDBETWEEN", bottom, top)

def ROUND(number, count=None):
    """
    Return the syntax for a round
    Rounds a number to a predefined accuracy
    """
    return __round("ROUND", number, count)
  
def ROUNDDOWN(number, count=None):
    """
    Return the syntax for a rounddown
    Rounds down a number to a predefined accuracy
    """
    return __round("ROUNDDOWN", number, count)

def ROUNDUP(number, count=None):
    """
    Return the syntax for a roundup
    Rounds up a number to a predefined accuracy
    """
    return __round("ROUNDUP", number, count)

def SERIESSUM(x, n, m, coeff):
    """
    Return the syntax for a seriessum
    Gives the sum of a power series
    """
    if (type(x) in (Number, CellReference) and  
            type(n) in (Number, CellReference) and 
            type(m) in (Number, CellReference) and 
            type(coeff) in (Number, CellReference, RangeReference)):
        parameters = of_parameter_list(x.str, n.str, m.str, coeff.str)
        return "SERIESSUM(" + parameters + ")"
    raise TypeError, "Wrong type of arguments"

def SIGN(number):
    """
    Return the syntax for a "sign" 
    Give the algebraic sign of the number
    """
    return __simple_function("SIGN", number)
  
def SIN(number):
    """Return the syntax for a sine"""
    return __simple_function("SIN", number)

def SINH(number):
    """Return the syntax for an hyperbolic sine"""
    return __simple_function("SINH", number)

def SQRT(number):
    """Return the syntax for a square root """
    return __simple_function("SQRT", number)

def SQRTPI(number):
    """Return the syntax for a square root * pi """
    return __simple_function("SQRTPI", number)

def SUM(*number_list):
    """Return the syntax for a sum """
    return __num_list_function("SUM", *number_list)

def SUMIF(cells, criteria, sum_range=None):
   """Return the syntax for a sumif """
   if sum_range is None:
      if (type(cells) in (CellReference, RangeReference) and 
	 type(criteria) in (Number, CellReference, RangeReference,
                                                       LogicalExpression, str)):

         return "SUMIF("+cells.str+";"+criteria.str+")"
      else:
         raise TypeError, "Wrong types of arguments"
   else:
      if (type(cells) in (CellReference, RangeReference) and 
	 type(criteria) in (Number, CellReference, RangeReference,
                                                 LogicalExpression, str) and  
         type(sum_range) in (CellReference, RangeReference)):

         return "SUMIF("+cells.str+";"+criteria.str+";"+sum_range.str+")"
      else:
         raise TypeError, "Wrong types of arguments"

def SUMSQ(*number_list):
    """Return the syntax for a sum of the squares """
    return __num_list_function("SUMSQ", *number_list)

def TAN(number):
    """Return the syntax for a tangent """
    return __simple_function("TAN", number)
 
def TANH(number):
    """Return the syntax for an hyperbolic tangent """
    return __simple_function("TANH", number)

def TRUNC(number, count):
    """Return the syntax for a truncate """
    return __simple_function2("TRUNC", number, count)
