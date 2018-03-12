# Create the lists of word-equivalents from 1-19, then one for the tens group.
# Finally, a list of the (for lack of a better word) "zero-groups".

ByOne = [
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"
]

ByTen = [
"zero",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"
]

zGroup = [
"",
"thousand",
"million",
"billion",
"trillion",
"quadrillion",
"quintillion",
"sextillion",
"septillion",
"octillion",
"nonillion",
"decillion",
"undecillion",
"duodecillion",
"tredecillion",
"quattuordecillion",
"sexdecillion",
"septendecillion",
"octodecillion",
"novemdecillion",
"vigintillion"
]

#strNum = raw_input("Please enter an integer:\n>> ")

# A recursive function to get the word equivalent for numbers under 1000.

def subThousand(inputNum):
    num = int(inputNum)
    if 0 <= num <= 19:
        return ByOne[num]
    elif 20 <= num <= 99:
        if inputNum[-1] == "0":
            return ByTen[int(inputNum[0])]
        else:
            return ByTen[int(inputNum[0])] + "-" + ByOne[int(inputNum[1])]
    elif 100 <= num <= 999:
        rem = num % 100
        dig = num / 100
        if rem == 0:
            return ByOne[dig] + " hundred"
        else:
            return ByOne[dig] + " hundred and " + subThousand(str(rem))

# A looping function to get the word equivalent for numbers above 1000
# by splitting a number by the thousands, storing them in a list, and
# calling subThousand on each of them, while appending the correct
# "zero-group".

def thousandUp(inputNum):
    num = int(inputNum)
    arrZero = splitByThousands(num)
    lenArr = len(arrZero) - 1
    resArr = []
    for z in arrZero[::-1]:
        wrd = subThousand(str(z)) + " "
        zap = zGroup[lenArr] + ", "
        if wrd == " ":
            break
        elif wrd == "zero ":
            wrd, zap = "", ""
        resArr.append(wrd + zap)
        lenArr -= 1
    res = "".join(resArr).strip()
    if res[-1] == ",": res = res[:-1]
    return res

# Function to return a list created from splitting a number above 1000.

def splitByThousands(inputNum):
    num = int(inputNum)
    arrThousands = []
    while num != 0:
        arrThousands.append(num % 1000)
        num /= 1000
    return arrThousands

### Last part is pretty much just the output.

sum = 0
for i in range(1,1001):
    strNum = str(i)

    intNum = int(strNum)

    if intNum < 0:
        print "Minus",
        intNum *= -1
        strNum = strNum[1:]


    if intNum < 1000:
        sum += len((subThousand(strNum)).replace('-','').replace(' ',''))
    else:
        sum += len((thousandUp(strNum)).replace('-', '').replace(' ', ''))
        #print thousandUp(strNum)

print sum