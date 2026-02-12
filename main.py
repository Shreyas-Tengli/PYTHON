#sucking is fun
#print("YOU SUCK")
#print("NO, YOU SUCK MORE!")

#Variable assignment and printing

#strings
#var1 ="NIGGESH"
#var2 = "suck"
#email= "123suck@gasmil.com"

#print(var1)
#print(f"helo {var1}")
#print(f"You {var2} ")
#print(f"YOUR email is {email}")

#integers

#print(f"you are {age} years old")

#float

#print(f"you are height is {height} feets")

'''TYPECASTING'''

# name="shreyas"
# age=20
# height = 6.2
# is_std= True

# print(type(is_std))
# print(type(height))
# print(age)
# print(type(age))
# print(type(name))

# age= float(age)
# print(age)
# print(type(age))

# is_std=str(is_std)
# print(is_std)
# print(type(is_std))

'''      TAKING I/P FRM USER '''

# name=input("Enter your name: ")
# age=int(input("Enter your age: "))

# print(f"hello {name}")
# print(f"You are {age} years old")
# print(type(age))


''' Conditional statment'''

# num=-3
# a=3
# b=7
# max_num="a"if a>b else "b"
# print(max_num)
# # print("positive"if num>0 else "Negative")

# # print("EVEN" if num%2==0 else "ODD")

'''     STRINGS     '''         
#x=input("Enter your full name: ")
# y=len(x)                                                #length of the string
#y=x.find("s")            #find the position of the thing in the string if it is not there the o/p will be -1
# y=x.rfind("s")             #if the word has two similar char then the reverse find will find from the last
#y=x.capitalize()            #capitalise first leter in the string
#y=x.upper()                #all char in string become capital letters
#y=x.lower()                 #all char in string become small letters
# y=x.isdigit()                chreck weather it is true or  false
# y=x.isalpha()

#y=x.count("s")                  count he no. of things in the string
# y=x.replace("s","x")             replace all s with x  

# print(y)

#print(help(str))                   gives evry info abt the str and other shit

'''         problem take input name then check shld not be more than 12 chars
            name shld not have space btw them
            name shld not have any digi btween them         '''

# name=input("Enter your name: ")
# x=len(name)
# space=name.count(" ")
# digi=name.isalpha()
# if x>12:
#     print("name should not exceed more than 12 words")
# elif space>0: 
#     print("dont put space btw ur name")
# elif not digi==True:
#     print(" your name shld not contain any digits")
# else:
#     print(f"Hello {name}")



'''      String indexing       '''

# var_name[start : end : step/increment]

# aadhar_number="1234-5678-9012"
# print(aadhar_number[5:9])

# print(aadhar_number[::2])

# print(f"Your aadhar no. is XXXX-XXXX-{aadhar_number[-5:]}")

# print(aadhar_number[::-1])          #this will reverse the no. inside the string    


'''          Python format specifiers         '''


# a=12341234.5
#decimal presicion
#print(f"THE A value is {a:.2f}")             # .2 reffers two points after decimal f reffers to flating point number

#padding give certain space to display the o/p like a has 10space alloted in which 6 is val of a oth is space
# print(f"THE A value is {a:10}") 
# print(f"THE A value is {a:010}")    # sapce will be added with zeros

# justify 
# print(f"THE A value is {a:<10}")        # no. will be left justified then u will have space after
# print(f"THE A value is {a:>10}")        # opp as above
# print(f"THE A value is {a:^10}")        # center alligned
# print(f"THE A value is {a:+}")          # positive no. are preseeded with the plus sign and -ve no. will be same 
# print(f"THE A value is {a: }")          # leaves space 
# print(f"THE A value is {a:,}")          # adds a comma after every thousands digit


'''        WHILE LOOP         '''

# name= input("Ente ur name: ")
# while name=="":
#     print("you cant keep ur name empty")
# print(f"heloo {name}")
    
'''         for loops          '''
# for x in range(0,11,2):        /start,stop,step
#     print(x)

# for x in reversed(range(0,11,2)):
#     print(x)
# print("HAPPY NEW YEAR ")
# cred="1234-5678-9012-3456"
# for x in cred :
#     print(x)

# for x in range(0,21):
#     if x==13:
#         break
#     else:
#         print(x)

# for x in range(0,21):
#     print(x,end=",")    # add smtg to end and can make it as a single line code


# row=int(input("Enter the number of rows: "))
# col=int(input("Enter the no. of coloumn: "))
# sym= input("enter a symbol to use")
# for x in range(row):
#     for y in range(col):
#         print(sym,end=" ")
#     print()


'''         LIST TUPLE SET          '''
# all are collection of items in single single variable used to store multiple data 
# List = [] it is ordered unchange able , Duplicates
# set={} unorderd immutable , can add and remove cannot duplicate
# tuple=() ordered and unchangeable , Duplicates (faster)

# everything is same as string indexing 
'''       LIST      '''
# friends=["abhi","prajwal","prem","prajwal"]
# for friend in friends:
#     print(friend)
# print(friends[::2])
# print(dir(friends))   this shows bunch of diff function taht can be peraformed on it
# print(help(friends))  this show the methods to use the functions  
# print("prem" in friends )
# print(len(friends))   this prints the no. of items in the list

# friends[2]="SWJ"
# friends.append("prem")
# friends.remove("SWJ")
# friends.insert(1,"yash")
# friends.sort()
# friends.reverse() 
# friends.clear()
# print(friends.index("prajwal"))
# print(friends.count("prajwal"))
# print(friends)

'''       SETS      '''

# friends={"abhi","prajwal","prem"} 
# print(friends)              #it is unorder so the print has random arrangement of the things
# print(dir(friends))   this shows bunch of diff function taht can be peraformed on it
# we cannot use indexing coz they are unorderd
# print(friends.add("SUS"))
# print(friends.remove("prem"))
# friends.pop() # removes out random element
# friends.clear()
# print(friends) 

'''         TUPLES        '''      
# ordered and unchangeable , Duplicates (faster) same as list but faster and unchangeable

'''         2D COLLECTIONS        '''
# fruits=["apple","nana","melon"]
# foods= ["pizza","burger","choco"]
# drinks=["juice", "shake", "matcha"]

# matrix=[fruits,foods,drinks]
# print(item[1]) print the whole list

# print(item[1][2])  print with the indexing like matrix

# for collection in matrix:             print all items in the matrix
#     for item in collection:
#         print(item,end=" ")
#     print()                           prints all elements in the same matrix order

'''        DICTIONARY         '''
# it is set of {key:value} pairs      its is ordred and changeable but no duplicates are allowed

students={"shreyas":123,
          "abhi":243,
          "lodu":109}
# print(students)
# print(dir(students))                        # shows all the functions it can perform
# print(help(students))                       # shos methods use the following funtions
# print(students.get("prem"))                   # gets the value of the key

# if students.get("prajwal"):
#     print("that name does  exist ")
# else:
#     print("the name does not exist")

students.update({"prajwal":234})
# students.update({"shreyas":212})

# students.pop("lodu")
# students.popitem()
# student.clear()   
# print(students)
# keys=students.keys()  all key values stored in keys var
# for key in students.keys():         to print the each key in diff line 
#     print(key)                                        same can be done with the values
# values=students.values()
# print(values)

# items=students.items()
# print(items)
# for key,value in students.items():                   prints the key and value together
#     print(f"{key}: {value}")

