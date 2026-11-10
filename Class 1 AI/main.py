#Hello chatbot
User1 = input("AI:hello I am Shaurya,whats your name:")
print(User1)
print("AI:hello",User1)
User2 = input("AI:how was your day? Good or bad?:")
if User2 == "good":
    print("AI:great")
elif User2 == "bad":
    print("AI:sad")
else:
    print("AI:idk")
User3 = input("AI:Do you want to end conversation? Yes or no?:")
if User3 == "Yes":
    print("AI:conversation ended")
elif User3 == "No":
    print("AI:...")
elif User3 == "no":
    print("AI:...")
else:
    print("AI:conversation has ended")