name = input("Enter your name: ")
age = int(input("Enter your age: "))
employment = input("Enter your employment yes/no: ")  
salary = int(input("Enter your salary: "))
cibilscore = int(input("Enter your cibil score: "))

print("\nLOAN APPLICATION")
print("Name:", name)
print("Age:", age)
print("Employment:", employment)  
print("Salary:", salary)
print("Cibil Score:", cibilscore)

if employment.lower() == "yes" and age >= 21 and salary >= 30000 and cibilscore >= 780:
    print("\nStatus: Loan APPROVED ")

elif employment.lower() == "yes" and age>= 31 and salary>= 30000 and cibilscore >= 600:
    print("\nStatus:Contradiction Application Documents Verification")

else:
    print("status: Not approved")



