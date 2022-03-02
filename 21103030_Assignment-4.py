# Question-1
# Problem for Tower of Hanoi
# In this we are shifting 1 disc at num1 time
print('Question-1')

def Tower_Hanoi(n, source, destination, auxillary):
    if n==1:
        print("Move disc 1 from", source, "to", destination)
    else:
        Tower_Hanoi(n-1, source, auxillary, destination) # First we have to move the discs from source peg to auxillary peg
        print("Move disc", n, "from", source, "to", destination) # moves the largest peg from source peg to destination peg
        Tower_Hanoi(n-1, auxillary, destination, source) # Now we have to move discs in auxillary peg to destination peg

n=int(input("Enter the number of discs: "))
Tower_Hanoi(n, 'A', 'B', 'C') 
#Considering A as source peg and B as destination peg and C is auxilliary peg



# Question-2
# Problem for Pascal'i Triangle
print('Question-2')

num=int(input("Enter the number of rows: "))
def factorial(n): # Calculating factorial of num1 number
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

# Using iterative procedure
for i in range(0, num): # Applying loops for calculating nCr
    for j in range(0, num-i):
        print(" ", end="")
    for j in range (0, i+1):
        print(int(factorial(i)/(factorial(j)*factorial(i-j))), end=" ") # Now will put formula of nCr in the pascal's triangle
    print()

# Using Recursive Method
def pascal(n, p):
    if(n<0):
        return
    else:
        pascal(n-1, p) # recursion gives previous lines of Pascal's triangle
        for i in range(0, p-n):
            print(" ", end="")
        for i in range(0, n):
            print(int(factorial(n-1)/(factorial(i)*factorial(n-1-i))), end=" ") # Now will give current line of Pascal's Triangle
        print()
pascal(num, num)



# Question-3
# Using built-in functions
print('Question-3')
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
quot=num1//num2
rem=num1%num2
print("The quotient is", quot, "and the remainder is", rem)

# PART-(a)
# Checking whether function is callable or not
print(callable(quot))
print(callable(rem))

# PART-(b)
# checking whether values are non-zero or not
print(quot!=0)
print(rem!=0)

# PART-(c)
my_list=[quot, rem]+[4, 5, 6] # adding elements in list
print(my_list)
my_list=(list(filter(lambda i: i<=4, my_list))) # filtering out values  greater than 4
print(my_list)

# PART-(d)
my_set=set(my_list) # making set from list
print(my_set)

# PART-(e)
my_set=frozenset(my_set) # making set immutable
print(my_set)

# PART-(f)
max_num=max(my_set) # finding max value
print(max_num)
print(hash(max_num)) # finding hash value



# Question-4
# Creating a class 
print('Question-4')

class Student: # class named student
    def __init__(self, name, roll_no):
        self.name=name # assigning name
        self.roll_no=roll_no # assigning roll number

s1=Student("Abhinav",21103030) # object s1 is created
print("Student's name is", s1.name)
print("Student's SID is", s1.roll_no)

del s1 # object s1 is deleted



# Question-5
# Details of Employee
print('Question-5')

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

e1=Employee("Mehak", 40000)
e2=Employee("Ashok", 50000)
e3=Employee("Viren", 60000)

# PART-(num1)
e1.salary=70000 # updating salary of employee-1(Mehak)
print(e1.salary)

# PART-(num2)
del e3 # deleting the record of  employee-3 (Viren)



# Question-6
# Anagram Test
print('Question-6')
george_word=input("Enter George's word: ")
barbie_word=input("Enter Barbie's word: ")

def anagrams(i): # function to find list of anagrams
    if i=="":
        return [i]
    else:
        ans=[] # list of anagrams
        for w in anagrams(i[1:]): # iterates over anagrams of tail of the string
            for pos in range(len(w)+1): # putting first letter in different positions in the anagrams of the remaining letters
                ans.append(w[:pos]+i[0]+w[pos:])
        return ans

correct_words=anagrams(george_word)
if barbie_word in correct_words: # checking if Barbie's word is an anagram of George's word
    print("Friendship is True")
else:
    print("Friendship is Fake")
