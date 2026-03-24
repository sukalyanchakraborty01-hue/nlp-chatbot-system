import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine, thank you!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break
        found = False
        for key in responses:
            if key in user_input:
                print("Chatbot:", random.choice(responses[key]))
                found = True
                break
        if not found:
            print("Chatbot: Sorry, I don't understand.")

if __name__ == "__main__":
    chatbot()
