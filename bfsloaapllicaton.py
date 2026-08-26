from collections import deque

name = input("Enter your name: ")
age = int(input("Enter your age: "))
employment = input("Enter your employment yes/no: ")
salary = int(input("Enter your salary: "))
cibilscore = int(input("Enter your cibil score: "))

queue = deque()

queue.append(("Employment", employment.lower() == "yes"))

while queue:
    condition, result = queue.popleft()

    if condition == "Employment":
        if result:
            queue.append(("Age", age >= 21))
        else:
            print("Status: Loan NOT APPROVED")
            break

    elif condition == "Age":
        if result:
            queue.append(("Salary", salary >= 30000))
        else:
            print("Status: Loan NOT APPROVED")
            break

    elif condition == "Salary":
        if result:
            queue.append(("CIBIL", cibilscore >= 780))
        else:
            print("Status: Loan NOT APPROVED")
            break

    elif condition == "CIBIL":
        if result:
            print("Status: Loan APPROVED")
        elif cibilscore >= 600:
            print("Status: Document Verification...")
        else:
            print("Status: Loan NOT APPROVED")

        '''




        Employment
            |
           Age
            |
          Salary
            |
          Cibil
           / \
        600+  <600
         |      |
      verify   Reject

      780+  -->  approved
          
           
            
              '''