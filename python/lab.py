##1. Write a Python program to print the following string in a specific format (see the output). 
##print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are')

##. Write a Python program to get the Python version you are using.
##import sys
##print(sys.version)

##3. Write a Python program to display the current date and time
##import time
##print(time.asctime())

##4. Write a Python program which accepts the radius of a circle from the user and compute the area.
##Sample Output : 
##r = 1.1
##Area = 3.8013271108436504
##import math
##radius = float(input('Radius: '))
##area = math.pi*(radius**2)
##print(area)

##5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
##fn = input('First Name: ')
##sn= input('Second Name: ')
##print(sn,fn)

##6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.
##text = '''United States Declaration of Independence
##From Wikipedia, the free encyclopedia
##The United States Declaration of Independence is the statement
##adopted by the Second Continental Congress meeting at the Pennsylvania State
##House (Independence Hall) in Philadelphia on July 4, 1776, which announced
##that the thirteen American colonies, then at war with the Kingdom of Great
##Britain, regarded themselves as thirteen independent sovereign states, no longer
##under British rule. These states would found a new nation – the United States of
##America. John Adams was a leader in pushing for independence, which was passed
##on July 2 with no opposing vote cast. A committee of five had already drafted the
##formal declaration, to be ready when Congress voted on independence.
##
##John Adams persuaded the committee to select Thomas Jefferson to compose the original
##draft of the document, which Congress would edit to produce the final version.
##The Declaration was ultimately a formal explanation of why Congress had voted on July
##2 to declare independence from Great Britain, more than a year after the outbreak of
##the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
##Second Day of July 1776, will be the most memorable Epocha, in the History of America."
##But Independence Day is actually celebrated on July 4, the date that the Declaration of
##Independence was approved.
##
##After ratifying the text on July 4, Congress issued the Declaration of Independence in
##several forms. It was initially published as the printed Dunlap broadside that was widely
##distributed and read to the public. The source copy used for this printing has been lost,
##and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
##with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
##by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
##is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
##popularly regarded as the official document. This engrossed copy was ordered by Congress on
##July 19 and signed primarily on August 2.
##
##The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
##The Declaration justified the independence of the United States by listing colonial grievances against
##King George III, and by asserting certain natural and legal rights, including a right of revolution.
##Having served its original purpose in announcing independence, references to the text of the
##Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
##(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
##on human rights, particularly its second sentence:
##
##We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
##Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.
##
##This has been called "one of the best-known sentences in the English language", containing "the most potent
##and consequential words in American history". The passage came to represent a moral standard to which
##the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
##Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
##through which the United States Constitution should be interpreted.
##
##The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
##being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
##(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
##Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
##19th century.'''
##txt_list = [x for x in text.split()]
##txt_count = [txt_list.count(x) for x in txt_list]
##print(text)
##print('List: ',txt_list)
##print('Word count:', list(zip(txt_list,txt_count)))

##6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
##lst = [x for x in input('Your input here: ').split(',')]
##print(f'List: {lst}')
##print(f'Tuple: {tuple(lst)}')

##7. Write a Python program to accept a filename from the user and print the extension of that.
##ext = input('Enter File name: ').split('.')
##print(f'Entension: {ext[-1]}')

##8. Write a Python program to display the first and last colors from the following list. Go to the editor
##color_list = ["Red","Green","White" ,"Black"]
##color_list = ["Red","Green","White" ,"Black"]
##print(color_list[0],color_list[-1])

##9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
##ex_date = (28,1,2019)
##date = '/'.join([str(x) for x in ex_date])
##print(date)

##10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
##num = int(input('Enter number: '))
##print(num+(num**2)+(num**3))

##11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

##12. Write a Python program to print the calendar of a given month and year.
##import calendar
##yr = int(input('Year: '))
##month = int(input('Month: '))
##print(calendar.monthcalendar(yr,month))

##13. Write a Python program to print the following here document.

##14. Write a Python program to calculate number of days between two dates.
import calendar


##15. Write a Python program to get the volume of a sphere with radius 6.
##import math
##radius = float(input('Radius: '))
##vol = (4/3)*(math.pi)*(radius**3)
##print(f'Volume: {vol}')

##16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
##num = float(input('Enter number: '))
##if num > 17:
##    print(2*(num-17))
##elif num <17:
##    print(17-num)

##17. Write a Python program to test whether a number is within 100 or 1000 or 2000.
##n = int(input('Enter Number: '))
##if n in range(100):
##    print('Number withing 100')
##elif n in range(1000):
##    print('Number within 1000')
##elif n in range(2000):
##    print('Number within 2000')
##else:
##    print('Out of Range')

##18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
##n1 = float(input('First Number: '))
##n2 = float(input('Second Number: '))
##n3 = float(input('Third Number: '))
##if n1 == n2 == n3:
##    print(3*(n1+n2+n3))
##else:
##    print(n1+n2+n3)

##19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

##20. Write a Python program to get a string which is n (non-negative integer) copies of a given string

##21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
##n = int(input('Number: '))
##if not n%2:
##    print('Even Number')
##else:
##    print('Odd Number')

##22. Write a Python program to count the number 4 in a given list
##l = [1,2,3,4,5,4,4,1,2,6,2,4,5,4]
##print(l.count(4))

##23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
##s= input('Enter the string: ')
##l = [x for x in s.split()]
##n= int(input('Number of Copies: '))
##
##if l[-1] == l[0]:
##    for x in range(n):
##        print(s)

##else:
##    for x in range(n):
##        print(l[0], l[1])

##24. Write a Python program to test whether a passed letter is a vowel or not.
##v= ['a','e','i','o','u']
##alph = input('Enter an Alphabet: ').lower()
##if alph in v:
##    print('It is a vowel')
##else:
##    print('It is a consunent')

##25. Write a Python program to check whether a specified value is contained in a group of values. 
##l1 = [1,2,3,5,7,8]
##i = int(input())
##if i in l1:
##    print(True)
##else:
##    print(False)

##26. Write a Python program to create a histogram from a given list of integers.

##27. Write a Python program to concatenate all elements in a list into a string and return it.
##l= ['a','b','c','d']
##print(''.join(l))

##28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
##Sample numbers list :
##
##numbers = [    
##    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
##    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
##    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
##    958,743, 527
##    ]
##for x in numbers:
##    if x==237:
##        break
##    elif not x%2:
##        print(x)

##29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
##Test Data : 
##color_list_1 = set(["White", "Black", "Red"]) 
##color_list_2 = set(["Red", "Green"])
##lout= [x for x in color_list_1 if x not in color_list_2]
##print(set(lout))

##30. Write a Python program that will accept the base and height of a triangle and compute the area
##base = float(input('Base: '))
##height = float(input('Height: '))
##print(f'Area = {base*height*0.5}')

##31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
##n1 = int(input('Number 1: '))
##n2 = int(input('Number 2: '))
##if n1>n2:
##    d=n1
##else:
##    d=n2
##divisor = [x for x in range(2,d) if not n1%x and not n2%x]
##print(max(divisor))

##32. Write a Python program to get the least common multiple (LCM) of two positive integers.
##n1 = int(input('Number 1: '))
##n2 = int(input('Number 2: '))
##if n1>n2:
##    d=n1
##else:
##    d=n2
##divisor = [x for x in range(2,d) if not n1%x and not n2%x]
##if not divisor:
##    print(n1*n2)
##else:
##    print(min(divisor))

##33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
##n1 = int(input('N1: '))
##n2 = int(input('N2: '))
##n3 = int(input('N3: '))
##if n1==n2 or n2==n3 or n3==n1:
##    sm = 0
##else:
##    sm = n1+n2+n3
##print(sm)

##34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
##n1 = int(input('N1: '))
##n2 = int(input('N2: '))
##sm = n1+n2
##if sm in range(15,20):
##    sm = 20
##print(sm)

##35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
##n1 = int(input('N1: '))
##n2 = int(input('N2: '))
##if n1+n2== 5 or n1==n2 or n1-n2==5 or n1-n2==-5:
##    print(True)
##else:
##    print(False)

##36. Write a Python program to add two objects if both objects are an integer type.
##o1 = input('Input 1: ')
##o2 = input('Input 2: ')
##
##if o1.isnumeric() and o2.isnumeric():
##    print(int(o1)+int(o2))

##37. Write a Python program to display your details like name, age, address in three different lines
##name = 'Python'
##age = 20
##adress = 'https://www.Python.org'
##print(f'Name: {name}\nAge: {age}\nAdress: {adress}')

##38. Write a Python program to solve (x + y) * (x + y)
##Test Data : x = 4, y = 3
##Expected Output : (4 + 3) ^ 2) = 49
##x= int(input('Enter First number: '))
##y = int(input('Enter second number: '))
##print(f'({x}+{y})^2 = {(x+y)**2}')

##39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
##amount = int(input('Amount: '))
##interest = float(input('Int: '))
##yrs = int(input('Years: '))
##
##for x in range(yrs):
##    amount+=interest*amount*0.01
##print(amount)

##40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
##import math
##p1 = (23,50)
##p2 = (44,15)
##print('Distance: ', math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))

##41. Write a Python program to check whether a file exists
##import os
##fn = input('File name: ' )
##print(os.path.isfile(fn))

##42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS
##import sys
##print(sys.version)

##43. Write a Python program to get OS name, platform and release information
##import os
##import platform
##print(os.name)
##print(platform.system())
##print(platform.release())

##44. Write a Python program to locate Python site-packages. 
##import site
##print(site.getsitepackages())

##45. Write a python program to call an external command in Python


##46. Write a python program to get the path and name of the file that is currently executing.
##import os
##print(os.path.realpath(__file__))

##47. Write a Python program to find out the number of CPUs using.
##import multiprocessing
##print(multiprocessing.cpu_count())

##48. Write a Python program to parse a string to Float or Integer. 
##x = '233.455'
##print(float(x))
##print(int(float(x)))

##49. Write a Python program to list all files in a directory in Python.
##import os
##print(os.listdir())

##50. Write a Python program to print without newline or space.
##print('Hello... This ', end='')
##print('is ',end='')
##print('python.',end='')

##51. Write a Python program to determine profiling of Python programs.
##
##Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
##import cProfile
##def xyz():
##    print('python!')
##print(cProfile.run('xyz()'))

##54. Write a Python program to get the current username.
##import getpass
##print(getpass.getuser())

##57. Write a program to get execution time for a Python method. 
##import time
##t1 = time.time()
##for x in range(20):
##    print(x)
##t2 = time.time()
##print(t2-t1)

##58. Write a python program to sum of the first n positive integers
##n= int(input('N: '))
##print(sum([x for x in range(n)]))

##59. Write a Python program to convert height (in feet and inches) to centimeters.
##h_ft = int(input('Feet: '))
##h_inch = int(input('Inches: '))
##
##total_h_inch = h_ft*12 + h_inch
##total_h_cm = total_h_inch*0.3936
##print(total_h_cm , ' cm')

##60. Write a Python program to calculate the hypotenuse of a right angled triangle.
##import math
##b = float(input('Base: '))
##p = float(input('Perpendicular: '))
##print('Hypotenuse =  ', math.tan(p/b))

##61. Write a Python program to convert the distance (in feet) to inches and miles
##d_feet = float(input('Distance in Feet: '))
##print(f'In Inches {d_feet*12}')
##print(f'In Miles {d_feet/5248}')

##62. Write a Python program to convert all units of time into seconds.
##time_h = int(input('Hours: '))
##time_m = int(input('Min: '))
##time_s = int(input('Second: '))
##
##time_total = time_h*3600 + time_m*60 +time_s 
##print(f'Time in seconds: {time_total}')

##63. Write a Python program to get an absolute file path.
##import os
##print(os.path.abspath('1-50.py'))

##64. Write a Python program to get file creation and modification date/times
##import time, os
##print('Created ',time.ctime(os.path.getctime('1-50.py')))
##print('Last Modified',time.ctime(os.path.getmtime('1-50.py')))

##65. Write a Python program to convert seconds to day, hour, minutes and seconds. 
##total_s = int(input('Seconds: '))
##days = total_s//86400
##hours = (total_s%86400)//3600
##minutes = (total_s%3600)//60
##sec = total_s%60
##print(days, 'Days')
##print(hours,'Hours')
##print(minutes,'Minutes')
##print(sec,'Seconds')

##66. Write a Python program to calculate body mass index.

##67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

##68. Write a Python program to calculate the sum of the digits in an integer
##i = input('Integer: ')
##print(sum([int(x) for x in i]))

##69. Write a Python program to sort three integers without using conditional statements and loops. 
##l = [3,4,0]
##print(sorted(l))

##71. Write a Python program to get a directory listing, sorted by creation date.
##import os
##import time
##file_names = ['1-50.py','abc.txt']
##c_time = []
##for x in file_names:
##    c_time.append(time.ctime(os.path.getctime(x)))
##print(sorted(c_time))

##72. Write a Python program to get the details of math module.
##import math
##print(dir(math))

##73. Write a Python program to calculate midpoints of a line
##x1 = int(input('Staring point X: '))
##y1 = int(input('Starting point Y: '))
##x2 = int(input('Ending poing X: '))
##y2 = int(input('Ending poing Y: '))
##
##mid_px = (x1+x2)/2
##mid_py = (y1+y2)/2
##print(f'X mid poing: {mid_px}\nY mid poing: {mid_py}')

##74. Write a Python program to hash a word.

##75. Write a Python program to get the copyright information.
##import sys
##print(sys.copyright)

##76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
##import argparse
##parser = argparse.ArgumentParser()
##parser.add_argument('you',type = str ,help = 'Your name')
##args = parser.parse_args()
##
##print('Hello',args.you)

##78. Write a Python program to find the available built-in modules.
##import sys
##print(sys.modules.keys())

##79. Write a Python program to get the size of an object in bytes.

##81. Write a Python program to concatenate N strings.
##l = ['a','b','c','d']
##for x in l:
##    print(x, end= '')

##82. Write a Python program to calculate the sum over a container.
##l = [x for x in range(10)]
##print(sum(l))

##83. Write a Python program to test whether all numbers of a list is greater than a certain number. 
##l = [x for x in range(10,20)]
##n = int(input('number: '))
##if min(l)<n:
##    print(False)
##else:
##    print(True)

##84. Write a Python program to count the number occurrence of a specific character in a string.
##f= 'n'
##print(input('Integer: ').count(f))

##85. Write a Python program to check if a file path is a file or a directory
##import os
##p = input('Path: ')
##print('File path?? ',os.path.isfile(p))
##print('Dir path?? ',os.path.isdir(p))

##86. Write a Python program to get the ASCII value of a character.
##x = input('Enter the letter: ')
##print('ASCII value: ',ord(x))

##87. Write a Python program to get the size of a file.
##import os
##print(os.path.getsize('1-50.py'))

##88. Given variables x=30 and y=20, write a Python program to print t "30+20=50"
##x=30
##y=20
##print(f'"{x}+{y}={x+y}"')

##89. Write a Python program to perform an action if a condition is true. Go to the editor
##Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
##
##v= input('Enter text here: ')
##if v=='1':
##    print('First day of the Month!')

##90. Write a Python program to create a copy of its own source code. 
##f=open('copy.py','w')
##f1=open('1-50.py')
##
##f.write(f1.read())
##print('Copied')

##91. Write a Python program to swap two variables.
##a= 'a'
##b= 'b'
##temp = a
##a=b
##b=temp
##print('a: ', a)
##print('b: ',b)

##93. Write a Python program to get the identity of an object.
##print(id(object()))

##94. Write a Python program to convert a byte string to a list of integers.
##s = b'abcdef'
##print(list(s))

##95. Write a Python program to check if a string is numeric.
##x = input('Enter some text: ')
##print(x.isnumeric())

##98. Write a Python program to get the system time
##import time
##print(time.ctime())

##99. Write a Python program to clear the screen or terminal.
##import os
##import time
##os.system('help')
##time.sleep(5)
##os.system('cls')

##103. Write a Python program to extract the filename from a given path.
##import os
##x= [os.getcwd(),'python.py']
##print(os.path.basename('/'.join(x)))

##105. Write a Python program to get the users environment.
##import os
##print(os.environ)

##107. Write a Python program to retrieve file properties. 
##import os
##import time
##f= '1-50.py'
##print('File Created: ',time.ctime(os.path.getctime(f)))
##print('File Modified: ' ,time.ctime(os.path.getmtime(f)))
##print('File Accessed: ',time.ctime(os.path.getatime(f)))
##print('File Size: ',os.path.getsize(f),'Bytes')

##109. Write a Python program to check if a number is positive, negative or zero.
##n = int(input('Number: '))
##if n>0:
##    print('Greater than Zero')
##elif n== 0:
##    print('Equal to Zero')
##else:
##    print('Less than Zero')


##110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous functio
##print([x for x in range(1,100) if not x%15])

##111. Write a Python program to make file lists from current directory
##import os
##print(os.listdir(os.getcwd()))

##112. Write a Python program to remove the first item from a specified list
##l = [x for x in range(5)]
##l.pop(0)
##print(l)

##113. Write a Python program to input a number, if it is not a number generate an error message. 
##try:
##    int(input('Input: '))
##except ValueError:
##    print('Please Enter a string...')

##114. Write a Python program to filter the positive numbers from a list.
##l = [x for x in range(-20,20)]
##ls = filter(lambda x:x>0, l)
##print(list(ls))

##115. Write a Python program to compute the product of a list of integers l = [x for x in range(1,20)]
##import functools
##l = [x for x in range(1,5)]
##print(functools.reduce(lambda x,y:x*y,l))

##117. Write a Python program to prove that two string variables of same value point same memory location.
##x= 'abc'
##y= 'abc'
##if id(x) == id(y):
##    print(True)

##119. Write a Python program to display a floating number in specified numbers.
##n = float(input('number: '))
##x= int(input('Decimal Places: '))
##print(f'%.{x}f'%n)

##120. Write a Python program to format a specified string to limit the number of characters to 6.
##n = int(input('Number: '))
##print('%.6s'%n)

##121. Write a Python program to determine if variable is defined or not.
##try:
##    y= 'abc'
##    if x:
##        print('Defined')
##except NameError:
##    print('Undefined')

##128. Write a Python program to check if lowercase letters exist in a string.
##s = input('String: ')
##lower = False
##for x in list(s):
##    if x.islower():
##        lower = True
##print(lower)

##133. Write a Python program to calculate the time runs (difference between start and current time) of a program.
##import time
##t1= time.time()
##for x in range(100):
##    print(x)
##t2= time.time()
##print(f'Time taken: {t2-t1} seconds')

##134. Write a Python program to input two integers in a single line.
##x,y = map(int,input().split())
##print('x= ',x)
##print('y= ',y)
