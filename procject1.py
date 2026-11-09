print("Welecom to Mithila Heritage")
print("Deiscover the Histroy and Culture of MIthila")
print("Hello MIthila ")
print("Create by : Prakhar Jha")

# Mithila Heritage AI Chatbot

# 1. List
famous_things = [
    "Madhubani Painting",
    "Maithili Language",
    "Mithila Paag",
    "Makhana",
    "Sikki Grass Craft"
]

# 2. Dictionary
knowledge = {
    "mithila": "Mithila apni sanskriti ke liye prasiddh hai.",
    "sita": "Punaura Dham, Sitamarhi Mata Sita ki janmabhoomi ki parampara se juda hai.",
    "darbhanga": "Darbhanga Mithila ka ek pramukh aitihasik kendra hai.",
    "maithili": "Maithili Mithila ki pramukh bhasha hai.",
    "painting": "Madhubani painting Mithila ki prasiddh kala hai."
}

# 3. Function
def chatbot(message):
    message = message.lower()

    for keyword, answer in knowledge.items():
        if keyword in message:
            return answer

    if "famous" in message:
        return ", ".join(famous_things)

    else:
        return "Sorry! Is topic ki jankari abhi mere paas nahi hai."


# 4. Main Chat
while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("AI: Jai Mithila!")
        break

    response = chatbot(user)
    print("AI:", response)

