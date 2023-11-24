#python program for creation of string
String1='Hello, this is a single quoted string '
print("String with the use of single quotes:")
print(String1)
String2="Python is my favorite programming language"
print("\n String with the use of double quotes:")
print(String2)
print(type(String2))
#Creating a
#  string with 
# #triple quotes
String3='''this is a triple quoted string that spans across multiple lines'''
print("string with the use of triple quotes ")
print(String3)
print(type(String3))
#creating string with triple quotes allows multiple lines
String4='''\nStrings
can 
be
multiline'''
print("\ncreating a multiline string")
print(String4)
'''concatinating two strings'''
String5=String4+" and "+String2
print("\n Concatenated String:")
print(String5)


#Program to demonstrate built in functions abs(),len(),min(),round(),isalnum(),type()
print(abs(-10))
print(len("WelcomeTo,Miet"))
print(min([10,20,30]))
print(round(3.527534,2))
print("CSE ,3RD SEM!".isalnum())
#symbols are not alphanumeric
print("123abc".isalnum())
print(type(10))
print(type("AI and  ML!"))

