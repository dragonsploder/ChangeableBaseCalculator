BaseCommands = ["HELP", "BASELIST", "BASESET", "QUIT"]
NumbertoOddBaseDictStart = {
    "D" :".",
    "N" : "-",
    0 :"0",
    1 :"1",
    2 :"2",
    3 :"3",
    4 :"4",
    5 :"5",
    6 :"6",
    7 :"7",
    8 :"8",
    9 :"9",
    10 :"a",
    11 :"b",
    12 :"c",
    13 :"d",
    14 :"e",
    15 :"f",
    16 :"g",
    17 :"h",
    18 :"i",
    19 :"j",
    20 :"k",
    21 :"l",
    22 :"m",
    23 :"n",
    24 :"o",
    25 :"p",
    26 :"q",
    27 :"r",
    28 :"s",
    29 :"t",
    30 :"u",
    31 :"v",
    32 :"w",
    33 :"x",
    34 :"y",
    35 :"z",
    36 :"A",
    37 :"B",
    38 :"C",
    39 :"D",
    40 :"E",
    41 :"F",
    42 :"G",
    43 :"H",
    44 :"I",
    45 :"J",
    46 :"K",
    47 :"L",
    48 :"M",
    49 :"N",
    50 :"O",
    51 :"P",
    52 :"Q",
    53 :"R",
    54 :"S",
    55 :"T",
    56 :"U",
    57 :"V",
    58 :"W",
    59 :"X",
    60 :"Y",
    61 :"Z"
}
OddBasetoNumberDictStart = {
    "." :"D",
    "-" : "N",
    '0': 0, 
    '1': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    'a': 10, 
    'b': 11, 
    'c': 12, 
    'd': 13, 
    'e': 14, 
    'f': 15, 
    'g': 16, 
    'h': 17, 
    'i': 18, 
    'j': 19, 
    'k': 20, 
    'l': 21, 
    'm': 22, 
    'n': 23, 
    'o': 24, 
    'p': 25, 
    'q': 26, 
    'r': 27, 
    's': 28, 
    't': 29, 
    'u': 30, 
    'v': 31, 
    'w': 32, 
    'x': 33, 
    'y': 34, 
    'z': 35, 
    'A': 36, 
    'B': 37, 
    'C': 38, 
    'D': 39, 
    'E': 40, 
    'F': 41, 
    'G': 42, 
    'H': 43, 
    'I': 44, 
    'J': 45, 
    'K': 46, 
    'L': 47, 
    'M': 48, 
    'N': 49, 
    'O': 50, 
    'P': 51, 
    'Q': 52, 
    'R': 53, 
    'S': 54, 
    'T': 55, 
    'U': 56, 
    'V': 57, 
    'W': 58, 
    'X': 59, 
    'Y': 60, 
    'Z': 61
}

# Create two dictionaries connecting each symbol with its corresponding number
def Setbase(BaseNumber):
    global Base
    global OddBasetoNumberDict
    global NumbertoOddBaseDict
    Base = BaseNumber
    OddBasetoNumberDict = OddBasetoNumberDictStart
    NumbertoOddBaseDict = NumbertoOddBaseDictStart
    z = len(OddBasetoNumberDictStart) - 3
    if Base > z:
        y = Base - z
        for x in range(y):
            hexid = chr(x + 161)
            OddBasetoNumberDict[hexid] = x + z
            NumbertoOddBaseDict[x + z] = hexid
    elif Base < z:
        y = z - Base
        OddBasetoNumberDict = dict(OddBasetoNumberDict)
        NumbertoOddBaseDict = dict(NumbertoOddBaseDict)
        for x in range(y + 1):
            a = z - x
            del OddBasetoNumberDict[NumbertoOddBaseDict[a]]
            del NumbertoOddBaseDict[a]
        OddBasetoNumberDict = OddBasetoNumberDict
        NumbertoOddBaseDict = NumbertoOddBaseDict

# Set the base
def BASESET():
    print("What base would you like")
    base = int(input(">"))
    Setbase(base)
    print("Base set to:", base)

# Print help
def HELP():
    print("""
    BASELIST - List symbols for current base
    BASESET - Set base number
    QUIT - exit

    +-*/ accepted

    Unused symbols will be ignored

    Starting base is 10

    """)

# Exit
def QUIT():
    print("Bye")
    exit(1)

# List the symbols and their corresponding numbers
def BASELIST():
    global OddBasetoNumberDict
    for Symbols in OddBasetoNumberDict:
        if Symbols != "." and Symbols != "-":
            print(Symbols, ":", OddBasetoNumberDict[Symbols])

# Change any number with any base to base ten
def OddBasetoNumber(BNumber):
    global Base
    global OddBasetoNumberDict
    IsNegitive = False
    if type(BNumber) is list:
        BNumber = str(BNumber[0])
    # Remove the "-" symbol if necessary
    if BNumber[0][0] == "-":
        BNumber = str(BNumber)[1:]
        IsNegitive = True

    BNumber = BNumber[::-1] # Reverse the list
    Total = 0

    # Makes note of the decimal location
    Location = 0
    IsDecimal = False
    for Char in BNumber:
        if "." == Char:
            IsDecimal = True
            break
        Location -= 1
    if IsDecimal == False:
        Location = 0
    # For each symbol this loop finds its corresponding number, 
    # multiplies it by the base to the power of the location
    # (tens place, hundreds place, ect) (decimals have negative location)
    for Part in BNumber:
        if Part in OddBasetoNumberDict and Part != ".":
            Total += OddBasetoNumberDict[Part] * (Base ** Location)
            Location += 1
    
    # Puts the "-" symbol back if necessary
    if IsNegitive == True:
        Total = "-" + str(Total)
    else:
        Total = str(Total)
    return Total

# Split a string or list at the decimal point returning a list
def SplitAtDecimal(Float):
    IsDecimal = False
    LocationOfDecimal = 0
    Float = str(Float)
    for Char in Float:
        if "." == Char:
            IsDecimal = True
            break
        LocationOfDecimal += 1
    if IsDecimal == True:
        WholeNumberPart = Float[:LocationOfDecimal]
        DecimalPart = Float[LocationOfDecimal:]
        return [WholeNumberPart, DecimalPart]
    else:
        return None

# Change a base ten number to an any base number
def NumbertoOddBase(Number):
    global Base
    global NumbertoOddBaseDict
    IsNegitive = False
    #IsDecimal = False
    LocationOfDecimal = 0
    # Remove the "-" symbol if necessary
    if str(Number)[0] == "-":
        Number = str(Number)[1:]
        IsNegitive = True
    # Makes note of the decimal location
    SplitNumber = SplitAtDecimal(Number)
    # If the number has a decimal, split it into two parts;
    # the whole number part will be fed back through this function
    # and the decimal part will be fed into the while loop
    if SplitNumber is not None:
        WholeNumberPart = NumbertoOddBase(SplitNumber[0])
        WholeNumber = WholeNumberPart + "."
        OddBasePart = SplitNumber[1]
        i = 0
        # Multiplys the decimal part by the base
        # The part before the decimal in the new number is converted to its 
        # corresponding symbol and appended (after the decimal) to the whole number
        # The part after the decimal is fed back ino the loop
        # This process repeats until the part after the decimal is 0
        # or it has happedn 10 times
        while (OddBasePart != ".0") and (i < 10):
            SplitNumber = SplitAtDecimal(str(float(OddBasePart) * Base))
            WholeNumber += NumbertoOddBaseDict[int(SplitNumber[0])]
            OddBasePart = SplitNumber[1]
            i += 1
        return WholeNumber

    # If the number is a whole number, the number is divided by the base, 
    # the remander is used to find the corresponding symboll and appended to the NewNumber
    # The "Whole Number Part" of the division is put back into the loop
    NewNumber = []
    Number = int(Number)
    while Number != 0:
        Remander = Number % Base
        Number = int(Number/Base)
        NewNumber.append(NumbertoOddBaseDict[Remander])
    # Reverse digits in New Number
    NewNumber = NewNumber[::-1]
    # If IsDecimal == True:
    #    NewNumber.insert(LocationOfDecimal, ".")
    NewNumber = ''.join(NewNumber)
    # Put the negative back if necessary
    if IsNegitive == True:
        NewNumber = "-" + NewNumber
    return NewNumber

# Takes parsed input and returns solution
def Solve(ParsedNumber):
    Location = 0
    Equation = []
    for Part in ParsedNumber:
        if (Part != "+") and (Part != "-") and (Part != "*") and (Part != "/") and (Part != "."):
            Equation.append(OddBasetoNumber(Part))
        else:
            Equation.append(Part)
    Equation = "".join(Equation)
    Equation = eval(Equation)
    return Equation
      
# Main Loop
print("Simple Calculator With Changeable Base \n   Type HELP")
Setbase(10)
while True:
    cmd = input(">")

    if cmd in BaseCommands:
        cmd = cmd + "()"
        exec(cmd)
        continue

    Number = cmd.split(" ")

    if Number[0] == "":
        print("")
    elif len(Number) == 1:
        NormalNumber = OddBasetoNumber(Number)
        print("    ", NormalNumber)
    else:
        Answer = Solve(Number)
        print("    ", NumbertoOddBase(Answer))