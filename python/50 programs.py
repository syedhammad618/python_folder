##Question 1: Write a program which find all such numbers which are divisible by 7 but are not a multiple of 5.
##def program1(start, end):
##    result = []
##    for x in range(start,end+1):
##        if x%7==0:
##            if x%5==0:
##                continue
##            else:
##                result.append(x)
##    return result
##
##print(program1(0,100))

##Question 2: Write a program which can compute the factorial of a given number.
##def factorial(n):
##    count =1
##    value =1
##    while count<=n:
##        value = count*value
##        count+=1
##    return value
##print(factorial(8))

##Question 3:
##def dict_mul(n):
##    d={}
##    for x in range(1,n+1):
##        d[x] = x*x
##    return d
##print(dict_mul(8))

##Question 4:
##def program4(s):
##    l= s.split(',')
##    t = tuple(l)
##    print(l)
##    print(t)
##print(program4('1,2,3,33,4,4123,2'))

##Question 5:
##class string:
##    def __init__(self):
##        global x
##        x=input('Enter string here: ')
##    def printstring(self):
##        print(x.upper())
##program5= string()
##program5.printstring()

##Question 6:
##def cal(d):
##    c,h = 50,30
##    d = d.split(',')
##    ans = []
##    for x in d:
##        x= int(x)
##        q= int(((2*c*x)/h)**0.5)
##        ans.append(q)
##    return ans
##
##print(cal('100,150,180'))

##Question 7:
##def twodarray(x,y):
##    l=[]
##    for i in range(x):
##        li=[]
##        for j in range(y):
##            li.append(i*j)
##        l.append(li)
##    return l
##print(twodarray(3,5))

##Question 8:
##def alphorder(x):
##    x= x.split(',')
##    x.sort()
##    return x
##
##print(alphorder('bag,hello,without,world'))

##Question 9:
##def lineUp():
##    l=[]
##    while True:
##        line = input('Enter line: ')
##        if not line:
##            break
##        else:
##            l.append(line.upper())
##    for x in l:
##        print(x)
##lineUp()

##Question 10:
##def repeatsequence(line):
##    l= list(set(line.split(' ')))
##    l.sort()
##    return ' '.join(l)
##print(repeatsequence('hello world and practice makes perfect and hello world again'))

##Question 11:
##def binarydiv():
##    l = [x for x in input().split(',')]
##    lout= []
##    for i in l:
##        i_dec= int(i,2)
##        if i_dec%5==0:
##            lout.append(i)
##    return ','.join(lout)
##print(binarydiv())

##Question 12:
##def evendigits(start,end):
##    l=[]
##    for i in range(start,end+1):
##        i_str= str(i)
##        xi= [x for x in i_str]
##        xo= []
##        for j in xi:
##            if  not int(j)%2:
##                xo.append(j)
##        if len(xo)==len(xi):
##            l.append(i_str)
##    return ','.join(l)
##print(evendigits(1000,3000))

##Question 13:
##def digitsletters():
##    l = [x for x in input().split(' ')]
##    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
##    nu = [0,1,2,3,4,5,6,7,8,9]
##    num =[str(x) for x in nu]
##    letters = 0
##    digits= 0
##    for i in l:
##        for j in i:
##            if j in abc:
##                letters+=1
##            elif j in num:
##                digits+=1
##    print(f'Digits= {digits}\nLetter= {letters}')
##digitsletters()

##Question 14:
##def uporlow():
##    sen = input()
##    count_lower = 0
##    count_upper = 0
##    for x in sen:
##        if x.isupper():
##            count_upper +=1
##        elif x.islower():
##            count_lower+=1
##    result = f'Upper case {count_upper}\nLower case {count_lower}'
##    return result
##
##print(uporlow())

##Question 15:
##def problem15(a):
##    a= int(a)
##    a2= a**2
##    a3 = a**3
##    a4 = a**4
##    result = a+a2+a3+a4
##    print(a2,a3,a4)
##    return result
##print(problem15(9))

##Question 16:
##def oddsqr():
##    l = [str(int(x)**2) for x in input().split(',') if int(x)%2!=0]
##    return ','.join(l)
##
##print(oddsqr())

##Question 17:
##def bank():
##    balance = 0
##    while True:
##        log = [x for x in input().split(' ')]
##        if log[0].lower() == 'd':
##            balance+=int(log[1])
##        elif log[0].lower() == 'w':
##            balance+=-int(log[1])
##        elif not log[0]:
##            break
##    return balance
##print(bank())

##Question 18:
##def pwd():
##    pw = [x for x in input().split(',') if len(x) in range(6,13)]
##    az = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
##    AZ = [x.upper() for x in az]
##    num = [str(x) for x in range(10)]
##    sym = ['$','@','#']
##    correctpw = []
##    for i in pw:
##        count_alphalow = 0
##        count_alphaup= 0
##        count_num=0
##        count_sym=0
##        for j in i:
##            if j in az:
##                count_alphalow+=1
##            elif j in AZ:
##                count_alphaup+=1
##            elif j in num:
##                count_num+=1
##            elif j in sym:
##                count_sym+=1
##        if count_alphalow >0 and count_alphaup>0 and count_num>0 and count_sym >0:
##            correctpw.append(i)
##    return ','.join(correctpw)
##
##print(pwd())

##Question 19:
##def sorttuple():
##    l = []
##    while True:
##        inpl = [x for x in input().split(',')]
##        if not inpl[0]:
##            break
##        else:
##            inpt = tuple(inpl)
##            l.append(inpt)
##    l.sort()
##    return l
##
##print(sorttuple())

##Question 20:
##class gen:
##    def __init__(self):
##        print('Hello from inside the Class!')
##        
##    def genr(self,n):
##        for x in range(n):
##            if not x%7:
##                yield x
##                
##clsf = gen().genr(100)
##
##for t in clsf:
##    print(t)

##Question 21:
##def botmoves():
##    up = 0
##    down = 0
##    right = 0
##    left = 0
##    while True:
##        move = [x for x in input().split(' ')]
##        if move[0].lower() == 'up':
##            up+=int(move[1])
##        elif move[0].lower() == 'down':
##            down+=int(move[1])
##        elif move[0].lower() == 'right':
##            right+=int(move[1])
##        elif move[0].lower() == 'left':
##            left+=int(move[1])
##        elif not move[0]:
##            break
##    x= left-right
##    y= up-down
##    if left>right and down>up:
##        direction= 'Down and  Left'
##    elif left>right and down<up:
##        direction = 'Up and Left'
##    elif right>left and down<up:
##        direction = 'Up and Right'
##    elif right>left and up<down:
##        direction = 'Down and Right'
##    distance = ((x*x)+(y*y))**0.5
##    return f'distance is: {distance} and the direction is {direction}'
##
##print(botmoves())

##Question 22:
##def frequency():
##    l = [x for x in input().split(' ')]
##    lcount =[]
##    ldict = {}
##    for i in l:
##        i = i.lower()
##        if i in lcount:
##            ldict[i]+=1 
##        elif i not in lcount:
##            ldict[i] = 1
##            lcount.append(i)
##            
##    for x,y in ldict.items():
##        print(f'{x}: {y}')
##        
##frequency()

##Question 23: Write a method which can calculate square value of number
##class cal:
##    def __init__(self):
##        print('Getting Started... Please wait!')
##        n= int(input())
##        self.sqr(n)
##    def sqr(self,n):
##        print(n*n)
##cl = cal()

##Question 24: Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
##And add document for your own function



##Question 25: Define a class, which have a class parameter and have a same instance parameter.
##class py():
##    modulename= 'numpy'
##    def __init__(self,modulename = None):
##        self.modulename = modulename
##mod = py('Tkinter')
##print(py.modulename, mod.modulename)
##an = py()
##an.modulename = 'Tensorflow'
##print(an.modulename, py.modulename)

##Question 26: Define a function which can compute the sum of two numbers.
##def sumtwo(n1,n2):
##    return n1+n2
##print(sumtwo(12,22))

##Question 27:Define a function that can convert a integer into a string and print it in console.
##def inttostr(x):
##    return str(x)
##print(inttostr(123))

##Question 28:Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
##def added(m, n):
##    return str(int(m)+int(n))
##print(added('12','23'))

##Question 29:Define a function that can accept two strings as input and concatenate them and then print it in console.
##def strconcatenate(n,m):
##    return str(n)+str(m)
##print(strconcatenate(12,41))

##Question 30: Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
##def maxlen(x,y):
##    if len(x)>len(y):
##        return x
##    elif len(y)>len(x):
##        return y
##    else:
##        return f'{x} \n{y}'
##
##print(maxlen('hello','world'))

##Question 31:
##def evenodd(n):
##    if not n%2:
##        return 'It is an even number'
##    else:
##        return 'It is an odd number'
##
##print(evenodd(123))

##Question 32:Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
##def sqrdict():
##    d = {}
##    for i in range(1,4):
##        d[i] = i*i
##    return d
##
##print(sqrdict())

##Question 33: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
##def dictionary():
##    d= {}
##    for x in range(1,21):
##        d[x] = x*x
##    for x in d.values():
##        print(x)
##
##dictionary()

##Question 34: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
##def dictionary2():
##    d ={}
##    for x in range(1,21):
##        d[x] = x*x
##    for x in d.keys():
##        print(x)
##
##dictionary2()

##Question 35: Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
##def sqrlist():
##    l = [x*x for x in range(1,21)]
##    for x in l:
##        print(x)
##
##sqrlist()

##Question 36: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
##def sqrlistFirst5():
##    l=[x*x for x in range(1,21)]
##    for x in l[:5]:
##        print(x)
##        
##sqrlistFirst5()

##Question 37: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
##def sqrlistLast5():
##    l= [x*x for x in range(1,21)]
##    for x in l[-1:-6:-1]:
##        print(x)
##        
##sqrlistLast5()

##Question 38: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
##def sqrlist5():
##    l = [x*x for x in range(1,21)]
##    for x in l[5:]:
##        print(x)
##
##sqrlist5()

##Question 39: Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
##def sqrtuple():
##    t= (x*x for x in range(1,21))
##    for x in t:
##        print(x)
##
##sqrtuple()

##Question 40: With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
##def halftuple():
##    t= (1,2,3,4,5,6,7,8,9,10)
##    print(t[:5])
##    print(t[5:])
##
##halftuple()

##Question 41: Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
##def eventuple():
##    t= (1,2,3,4,5,6,7,8,9,10)
##    teven = (x for x in t if not x%2)
##    for x in teven:
##        print(x)
##
##eventuple()

##Question 42: Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
##def yesno():
##    yn = input()
##    if yn.lower() == 'yes':
##        print('Yes')
##    else:
##        print('No')
##
##yesno()

##Question 43: Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
##def filterlist():
##    l= [1,2,3,4,5,6,7,8,9,10]
##    for x in filter(lambda x:not x%2,l):
##        print(x)
##
##filterlist()

##Question 44: Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
##def maplist():
##    l = [1,2,3,4,5,6,7,8,9,10]
##    sqrlist = map(lambda x: x*x,l)
##    print(list(sqrlist))
##    
##maplist()

##Question 45:Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
##def evenmap():
##    l= [x for x in [1,2,3,4,5,6,7,8,9,10] if not x%2]
##    lsqr = map(lambda x: x*x,l)
##    print(list(lsqr))
##
##evenmap()

##Question 46: Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
##def filtereven():
##    l = [x for x in range(1,21)]
##    lfilter = filter(lambda x: not x%2,l)
##    print(list(lfilter))
##
##filtereven()

##Question 47: Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
##def mapsqr():
##    l= [x for x in range(1,21)]
##    lmap = map(lambda x: x*x,l)
##    print(list(lmap))
##
##mapsqr()

##Question 48: Define a class named Pakistani which has a static method called printNationality.
##class Pakistani:
##    def printNationality(self):
##        print('Pakistani')
##
##iampakistani = Pakistani()
##iampakistani.printNationality()

##Question 49: Define a class named Pakistan and its subclass Karachi. 
##class Pakistan(object):
##    pass
##class Karachi(Pakistan):
##    print('Karachi... the MINI PAKISTAN')
##    pass
##country = Pakistan()

##Question 50: Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
##class circle():
##    def area(self,radius):
##        import math
##        print(math.pi*radius**2)
##
##shape= circle()
##shape.area(4)
