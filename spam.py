words = ["prize", "rewards","offer","discount","date"]

email = input("Enter your email: ")

for word in words:
    if word in email.lower():
        print("Spam mail detected")
        break
else:
        print("spam mail not detected")
