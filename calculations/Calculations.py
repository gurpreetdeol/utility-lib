import math


class Calculations():
    """A class that contains various mathematical calculations"""

    def __init__(self):
        """A class that contains various mathematical calculations"""
        pass

    # Calculate the sum of two numbers
    def add(a, b):
        """Calculate the sum of two numbers"""
        return a + b

    # Calculate the difference of two numbers
    def subtract(a, b):
        """Calculate the difference of two numbers"""
        return a - b

    # Calculate the product of two numbers
    def multiply(a, b):
        """Calculate the product of two numbers"""
        return a * b

    # Calculate the division of two numbers
    def divide(a, b):
        """Calculate the division of two numbers"""
        return a / b

    # Calculate the square of a number
    def square(num):
        """Calculate the square of a number"""
        return num ** 2

    # Calculate the square root of a number
    def square_root(num):
        """Calculate the square root of a number"""
        return math.sqrt(num)

    # Calculate the cube of a number
    def cube(num):
        """Calculate the cube of a number"""
        return num ** 3

    # Calculate the cube root of a number
    def cube_root(num):
        """Calculate the cube root of a number"""
        return num ** (1/3)

    # Calculate the power of a number
    def power(num, p):
        """Calculate the power of a number"""
        return num ** p

    # Calculate the factorial of a number
    def factorial(num):
        """Calculate the factorial of a number"""
        return math.factorial(num)

    # Calculate the natural logarithm of a number
    def natural_log(num):
        """Calculate the natural logarithm of a number"""
        return math.log(num)

    # Calculate the base 10 logarithm of a number
    def log10(num):
        """Calculate the base 10 logarithm of a number"""
        return math.log10(num)

    # Calculate the base 2 logarithm of a number
    def log2(num):
        """Calculate the base 2 logarithm of a number"""
        return math.log2(num)

    # Calculate the sine of an angle
    def sin(angle):
        """Calculate the sine of an angle"""
        return math.sin(math.radians(angle))

    # Calculate the cosine of an angle
    def cos(angle):
        """Calculate the cosine of an angle"""
        return math.cos(math.radians(angle))

    # Calculate the tangent of an angle
    def tan(angle):
        """Calculate the tangent of an angle"""
        return math.tan(math.radians(angle))

    # Calculate the inverse sine of a number
    def asin(num):
        """Calculate the inverse sine of a number"""
        return math.degrees(math.asin(num))

    # Calculate the inverse cosine of a number
    def acos(num):
        """Calculate the inverse cosine of a number"""
        return math.degrees(math.acos(num))

    # Calculate the inverse tangent of a number
    def atan(num):
        """Calculate the inverse tangent of a number"""
        return math.degrees(math.atan(num))

    # Calculate the hyperbolic sine of a number
    def sinh(num):
        """Calculate the hyperbolic sine of a number"""
        return math.sinh(num)

    # Calculate the hyperbolic cosine of a number
    def cosh(num):
        """Calculate the hyperbolic cosine of a number"""
        return math.cosh(num)

    # Calculate the hyperbolic tangent of a number
    def tanh(num):
        """Calculate the hyperbolic tangent of a number"""
        return math.tanh(num)

    # Calculate the inverse hyperbolic sine of a number
    def asinh(num):
        """Calculate the inverse hyperbolic sine of a number"""
        return math.asinh(num)

    # Calculate the inverse hyperbolic cosine of a number
    def acosh(num):
        """Calculate the inverse hyperbolic cosine of a number"""
        return math.acosh(num)

    # Calculate the inverse hyperbolic tangent of a number
    def atanh(num):
        """Calculate the inverse hyperbolic tangent of a number"""
        return math.atanh(num)

    # Calculate the greatest common divisor of two numbers
    def gcd(a, b):
        """Calculate the greatest common divisor of two numbers"""
        return math.gcd(a, b)

    # Calculate the least common multiple of two numbers
    def lcm(a, b):
        """Calculate the least common multiple of two numbers"""
        return a * b // math.gcd(a, b)

    # Calculate the absolute value of a number
    def abs(num):
        """Calculate the absolute value of a number"""
        return math.fabs(num)

    # Calculate the remainder of a division
    def remainder(a, b):
        """Calculate the remainder of a division"""
        return a % b

    # Calculate the quotient of a division
    def quotient(a, b):
        """Calculate the quotient of a division"""
        return a // b

    # Calculate the exponential of a number
    def exp(num):
        """Calculate the exponential of a number"""
        return math.exp(num)

    # Calculate the power of 10 of a number
    def pow10(num):
        """Calculate the power of 10 of a number"""
        return 10 ** num

    # Calculate the power of 2 of a number
    def pow2(num):
        """Calculate the power of 2 of a number"""
        return 2 ** num

    # Calculate the power of e of a number
    def powe(num):
        """Calculate the power of e of a number"""
        return math.e ** num

    # Calculate the power of pi of a number
    def powpi(num):
        """Calculate the power of pi of a number"""
        return math.pi ** num

    # Calculate the power of phi of a number
    def powphi(num):
        """Calculate the power of phi of a number"""
        return math.phi ** num

    # Calculate the power of the golden ratio of a number
    def powgolden(num):
        """Calculate the power of the golden ratio of a number"""
        return math.golden ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powem(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.em ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powcatalan(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.catalan ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powkhinchin(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.khinchin ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powapery(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.apery ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powglaisher(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.glaisher ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powmertens(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.mertens ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powtwinprime(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.twinprime ** num

    # Calculate the power of the Euler-Mascheroni constant of a number
    def powj(num):
        """Calculate the power of the Euler-Mascheroni constant of a number"""
        return math.j ** num