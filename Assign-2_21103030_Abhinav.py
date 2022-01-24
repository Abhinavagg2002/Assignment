# Question 1
_string= "Python is a case sensitive language"
# Part a [Finding the length of input string]
print(len(_string))

# Part b [Reversing the order]
part_b=_string[-1::-1]
print(part_b)

# Part c [Using slice function]
Part_c=_string[10:26]
print(Part_c)

# Part d [Replacing a part of string]
part_d=_string.replace("a case sensitive", "object oriented")
print(part_d)

# Part e [Finding a]
part_e=_string.find("a")
print(part_e)

# Part f [Removing white spaces]
part_f=_string.replace(" ", "")
print(part_f)


# Question 2 
letter = '''Hey,ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is Q'''
name=input("Enter your name: ",)
_SID=input("Enter your SID: ",)
department=input("Enter your department: ",)
cgpa=input("Enter your CGPA: ",)
letter=letter.replace("ABC", name)
letter=letter.replace("2110XXXX", _SID)
letter=letter.replace("XYZ", department)
letter=letter.replace("Q", cgpa)
print(letter)


# Question-3
a=56
b=10

# part-a
_part_a=a&b
print("Part a: ", _part_a)

# part-b 
_part_b=a|b
print("Part b: ",  _part_b)

# part-c
_part_c=a^b
print("Part c: ", _part_c)

# part-d
_part_d_1=a<<2
print("First part of Part d:", _part_d_1)
_part_d_2=b<<2
print("Second part of Part d:", _part_d_2)

# part-e
_part_e_1=a>>2
print("First part of Part e: ", _part_e_1)
_part_e_2=b>>4
print("Second part of Part e ", _part_e_2)


# Question-4
Num_1=float(input("Enter the first number: "))
Num_2=float(input("Enter the second number: "))
Num_3=float(input("Enter the third number: "))
if Num_1>=Num_2 and Num_1>=Num_3 :
 print(" The first number is greatest")
elif Num_2>=Num_1 and Num_2>=Num_3 :
 print("The second number is greatest")
else :
 print("The third number is greatest") 


# Question-5
statement=input("Enter a statement: ",)
namecount=statement.count("name")
if namecount>= 1 :
 print("Yes")
else:
 print("No")


# Question 6
# The principle is that the sum of any two sides a triangle should be greater than the remaining side then only it will form a triangle
Side_1=int(input("Enter the length of first side of triangle: "))
Side_2=int(input("Enter the length of second side of triangle: "))
Side_3=int(input("Enter the length of third side of triangle: "))
if Side_3>=Side_1+Side_2 :
 print("NO")
elif Side_2>=Side_1+Side_3 :
 print("NO")
elif Side_1>=Side_2+Side_3 :
 print("NO")
else :
 print("YES")
 
