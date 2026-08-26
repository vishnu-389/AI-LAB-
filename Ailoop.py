while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("AI: Thank you! Have a great day.")
        break

    elif question.lower() == "how much discount i can get":
        print("AI: You can get a maximum discount of 15%.")

    elif question.lower() == "when will the car get delivered":
        print("AI: The car will be delivered within 2-3 days.")

    else:
        print("AI: Sorry, I don't understand your question.")

    print("AI: Anything else I can help you with?")


   