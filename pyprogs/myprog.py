# first python program

import myfunc

a = 1

if a == 1 :
	print (a)
	print ("the world is not enough")


# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

print (spam, " ", text)


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

'Shashank' 'Shanker'

text = ('Put several strings within parentheses'
            'to have them joined together.')
path = 'C:/Users/Admin/Desktop/myprog.py'

print (path)


word = 'python'

word[-1]
word[0]
word[3]


a, b = 0, 1
while b < 1000:
    print (b)
    print (" \n ")
    a, b = b, a+b


def printhello():
         y = myfunc.myfunc()
         print ("The number entered is" + " " + y)
         
         
printhello()
# print x


## def printbye(b):
#         print printhello()

         
# print printbye(20)
         

