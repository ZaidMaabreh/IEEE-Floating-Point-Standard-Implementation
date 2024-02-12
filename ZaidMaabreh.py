
def FloatToBinaryConverter(FltNum):
    
    if FltNum < 0 :
        global Sign
        Sign = 1
        FltNum = abs(FltNum) 
        
    
    if FltNum == 0 :
        return 0
    
    IntPart = int(FltNum)
    IntBin = DecimalToBinaryConverter(IntPart)
    
    FracPart = FltNum - IntPart
    FracBin = FractionToBinaryConverter(FracPart)
    
    BinaryNumber = IntBin + '.' + FracBin

    return BinaryNumber 

def DecimalToBinaryConverter(IntPart):
    
   BinaryNumber = ""

   while IntPart > 0 :
       
       BinaryNumber = str(IntPart % 2) + BinaryNumber
       
       IntPart //= 2

   return BinaryNumber
    

def FractionToBinaryConverter(FracPart) :
    
    BinaryNumber = ""
    
    if FracPart == 0 :
        return "0"

    while FracPart > 0 :
        
        FracPart = FracPart * 2
        
        BinaryNumber = BinaryNumber + str(int(FracPart))
        
        FracPart = FracPart - int(FracPart)

    return BinaryNumber

def NormalisedMantissa(BinaryNumber):

    global Biased  
    '''
        at first i used the binary number as a regular float like this:
            
            while (BinaryNumber) > 2 :
                
                BinaryNumber /=10
                Biased += 1
            Mantinssa = BinaryNumber - 1 
            
        which keeps dividing the number by 10 to move the point to the left
        until the number is less than 2 which is the last bit and count how
        many time we moved the point, which is the exponent, but i ran into
        the following problem which is that when the loop ends i get an 
        inaccurate mantissa that has '2's in it so i looked for why the number 
        is not accurateand i found out that in the IEE floating point standard
        is when the number gets big there are less bits in the mantissa to
        represent the fraction which will decrease the number of fractions that
        i can represent, so when the number cannot be represented it will be
        rounded to the nearest representable number so thats why i got 2's in 
        the number and i had to use the number as a string instead.
        
        sorry for wasting your time but i thought that i had to explain why i 
        used the number as a string
        
    '''
    BinaryNumber = str(BinaryNumber)
    for i in range(len(BinaryNumber)):
        if BinaryNumber[i] == '.':
            DotIndex = i
            Biased = Biased + i - 1
        
    
    FirstPart = BinaryNumber[0:DotIndex]
    SecondPart = BinaryNumber[DotIndex+1:len(BinaryNumber)]
    Mantissa = FirstPart[1:] + SecondPart
    
    
    return Mantissa
    

def IEEE_Double_Precision(Sign , Biased , Mantissa ):
    while len(Mantissa) < 52 :
        Mantissa += "0"
    print(str(Sign) + " " + str(Biased) + " " + str(Mantissa))
    return str(Sign) + str(Biased) + str(Mantissa)

def BinaryToHexaConverter(DoubleNumberRepresentation):
    
    Dectionary = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    HexaResult = ""
    
    for i in range (0 , len(DoubleNumberRepresentation)-3,4) :
        
        BinNipple = DoubleNumberRepresentation[i:i+4]
        HexaResult += Dectionary[str(BinNipple)]
        
        
    return HexaResult
    
""" I assumed that the number is positive , if not the sign will
 change to 0 while coverting th number to binary in the fisrt step """
Sign = 0


FltNum = float(input("Please Enter a Number : "))
BinaryNumber = (FloatToBinaryConverter(FltNum))
print()
print("The Bainary Number = " , BinaryNumber)
print()

Biased = 1023 
Mantissa = NormalisedMantissa(BinaryNumber)
print("The Normalised Mantissa = " , Mantissa)
print()
print("The Biased Exponent = " , Biased )
print()
print("The Biased Exponent In Binary = " , DecimalToBinaryConverter(Biased) )
print()
Biased = DecimalToBinaryConverter(Biased)
print("The IEEE 754 double precision is = ")
DoubleNumberRepresentation = IEEE_Double_Precision(Sign, Biased, Mantissa)

print()
print("This can be written in hexadecimal form :" , 
      BinaryToHexaConverter(DoubleNumberRepresentation))
print()

#-----------------------------------------------------------------------------

'''


"""
And here an extra code which convert the  calculate the Single precision IEEE 
Standard 754 floating point number for a decimal floating point number 
"""

def IEEE_Single_Precision(Sign, Biased, Mantissa):
    while len(Mantissa) < 23 :
        Mantissa += "0"
    print(str(Sign) + " " + str(Biased) + " " + str(Mantissa))
    return str(Sign) + str(Biased) + str(Mantissa)
    
print("------------------------------------------------------------")

Biased = 127
Mantissa = NormalisedMantissa(BinaryNumber)
print("The Normalised Mantissa = " , Mantissa)
print()
print("The Biased Exponent = " , Biased )
print()
print("The Biased Exponent In Binary = " , DecimalToBinaryConverter(Biased) )
print()
Biased = DecimalToBinaryConverter(Biased)
print("The IEEE 754 Single precision is = ")
print()
DoubleNumberRepresentation = IEEE_Single_Precision(Sign, Biased, Mantissa)
HexaNumberRepresentation =  BinaryToHexaConverter(DoubleNumberRepresentation)
print("This can be written in hexadecimal form :" , HexaNumberRepresentation)

        
'''
    
    
    
    
    
    

