#Question 1
print("Question 1")
#taking input from user
string_ = input("Enter a string: ")
string_=string_.lower().strip()
i=0
# Using an empty dictionary
dict={}

#checking if the string input is a word or a sentence
if " " not in string_:
     #Finding common elements
     while i<len(string_):
          counter=0
          k=0
          while k<len(string_):
               if string_[i]==string_[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          dict[f"{string_[i]}"]=counter
          i=i+1

else:
     list = str.split(string_)
     #Finding common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}")

#Question-2
print("Question-2")
#Taking input from user for the date
day=int(input('Please enter Day- '))
month=int(input('Please enter Month- '))
year=int(input('Please enter Year- '))

#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True
if month>12:
    condition=False
# Using if else conditions 
if condition:
    #checking and changing for new year
    if day==31 and month==12:
        year_new=year+1
    else:
        year_new=year
    if month==12 and day==31:
        month_new=1
    else:
        month_new=month

    #checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            day_new=1
            if month!=12:
                month_new=month+1
            else:
                month_new=1
        else:
            day_new=day+1
    #checking for the month of february and leap year
    elif month==2:
        if year%4==0:
            if day==29:
                day_new=1
                month_new=3
            else:
                day_new=day+1
        else:
            if day==28:
                day_new=1
                month_new=3
            else:
                day_new=day+1

    #covering all the remaining cases
    else:
        if day==30:
            day_new=1
            month_new=month+1
        else:
            day_new=day+1
    #printing the calculations
    print(f"Next Date is: {day_new}/{month_new}/{year_new}")

else:
    print("Error, type a valid date")

# Question 3
print("Question-3")
# defining an empty list to take input from user
list1 = []

# taking input from user
while input("Please enter Y to enter data- ").lower().strip() == 'y':
    list_elem = int(input("Plz give an integer input- "))
    list1.append(list_elem)
print(list1)

# defining an empty list to store tuple pairs later
list2 = []
for x in list1:
    tuple_c = (x, x ** 2)
    list2.append(tuple_c)
print(list2)


#Question-4
#For printing the letter grade and performance
print("Question-4")
Grade_point=int(input('Enter a grade point: ',))
if Grade_point==10:
    print('Your Grade is A+ and outstanding Performance')
elif Grade_point==9:
    print('Your Grade is A and excellent Performance')
elif Grade_point==8:
    print('Your Grade is B+ and very good Performance')
elif Grade_point==7:
    print('Your Grade is B and good Performance')
elif Grade_point==6:
    print('Your Grade is C+ and average Performance')
elif Grade_point==5:
    print('Your Grade is C and below averagePerformance')
elif Grade_point==4:
    print('Your Grade is D and poor Performance')
else:
    print('Error,the grade is out of range ') 


#Question-5
print('Question-5')

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
    print("")
 
#Question 6
print("Question 6")
condition=True

#Defining dictionary to store the values
Dictionary={}
detail="y"
while condition:
    if detail.lower()=="y":
        SID=int(input("Please enter your SID: "))
        name=input("Please enter your name: ")
        Dictionary[SID]=name
        detail= input("If you want to enter more details press Y/N: ")
        condition = True

    else:
        condition = False
#Part-a
#Printing students details stored in the dictionary.
print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

#Part-b
# Sorting dictionary using student names.
print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

#Part-c
#Sorting dictionary using SID
print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

#Part-D
# Searching a student details with SID and printing name of that student
print("Part D")
SID_new=int(input("Please enter the student's SID whose detail you need- "))
if SID_new in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_new]}")
else:
    print("This SID is not present in the given Data")
print("")


#Question 7
#Program to print Fibonacci sequence
print("Question 7")
number=int(input("Total elements of Fibonacci sequence that you want: "))

#using the formula of Fibonacci series that the sum of previous two terms is equal to the present term.
Number_1=1
Number_2=0
n=0
#initializing sum with first two terms
sum=Number_1+Number_2

#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {number} terms")
print(Number_2)
print(Number_1)

#Printing the remaining fibonnaci terms
while n<number-2:
    next_term=Number_2+Number_1
    Number_2=Number_1
    Number_1=next_term
    print(next_term)
    n=n+1
    sum+=next_term
average=sum/number
#printing the program end detail
print(f"Average of total {number} terms of sequence is {average}")
print("END")

#Question 8

print("Question 8")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#Finding symmetric difference of both the sets
print("Part-a")
set_notboth=Set1^Set2
print(f"set with elements not common in both is {set_notboth}")

#Finding symmetric difference of all sets
print("Part-b")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")

#Finding elements that is common in any two sets
print("Part-c")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")

#Finding elements common in set1 and range 1 to 10
print("Part-d")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

#Finding elements common in sets 1,2,3 and range 1 to 10
print("Part e")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")
