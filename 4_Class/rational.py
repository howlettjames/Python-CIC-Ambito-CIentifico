'''
@author: Jaime Bastida
@description: Class that represents a rational number with arithmetic and logic operations
'''

class Rational:
    def __init__(self, num=0, denom=1):
        if(denom == 0):
            raise ValueError("Denominator can't be equal to 0")
            
        gcdVal = gcd(num, denom)
        if((num >= 0 and denom < 0) or (num < 0 and denom < 0)): # i.e. 3/-2 or -3/-2 is converted to 3/2
            self.num = -(num // gcdVal)
            self.denom = -(denom // gcdVal)
        else:
            self.num = num // gcdVal
            self.denom = denom // gcdVal
    
    # GETTERS AND SETTERS
    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self, num):
        if not isinstance(num, int):
            raise TypeError("Expected an integer") 
        else:
            self.__num = num

    @property
    def denom(self):
        return self.__denom

    @denom.setter
    def denom(self, denom):
        if not isinstance(denom, int):
            raise TypeError("Expected an Integer")
        else:
            self.__denom = denom

    #################################### UTILITY FUNCTIONS 
    def __str__(self):
        return f"{self.num}/{self.denom}" 

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")
        else:
            return Rational(self.num * other.denom + self.denom * other.num, self.denom * other.denom)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")
        else:
            return Rational(self.num * other.denom - self.denom * other.num, self.denom * other.denom)
    
    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")
        else:
            return Rational(self.num * other.num, self.denom * other.denom)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")
        else:
            return Rational(self.num * other.denom, self.denom * other.num)

    def __pow__(self, exp):
        if not isinstance(exp, int):
            raise TypeError("Expected an integer")    
        else:
            return Rational(self.num ** exp, self.denom ** exp)

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")    
        else:
            self_num = self.num * other.denom
            other_num = other.num * self.denom
            return True if self_num < other_num else False

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")    
        else:
            self_num = self.num * other.denom
            other_num = other.num * self.denom
            return True if self_num <= other_num else False
    
    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")    
        else:
            self_num = self.num * other.denom
            other_num = other.num * self.denom
            return True if self_num == other_num else False
    
    def __ne__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")    
        else:
            self_num = self.num * other.denom
            other_num = other.num * self.denom
            return True if self_num != other_num else False
    
    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")    
        else:
            self_num = self.num * other.denom
            other_num = other.num * self.denom
            return True if self_num > other_num else False
    
    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Expected a Rational")    
        else:
            self_num = self.num * other.denom
            other_num = other.num * self.denom
            return True if self_num >= other_num else False
    
    # GETTERS AND SETTERS COMPATIBILITY
    def getNum(self):
        return self.__num

    def setNum(self, num):
        self.__num = num           

    def getDenom(self):
        return self.__denom

    def setDenom(self, denom):
        self.__denom = denom           


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    r = 1
    while True:
        q = a // b
        r = a % b
        
        #print(f"q = {q} and r = {r} and gcd = {b}")
        if(r == 0):
            break
        else:
            a = b
            b = r

    return b

def simplify(a, b):
    gcdVal = gcd(a, b)
    a = a // gcdVal
    b = b // gcdVal

    return a, b

if __name__ == '__main__':
    print(gcd(2322, 654))