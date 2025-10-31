# Simple Rule-Based Chatbot (CodSoft Task 1)

print("Hello! I'm Vaani, your chatbot assistant.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello there! How can I help you?")
    elif "how are you" in user_input:
        print("Bot: I'm just a bunch of code, but I’m doing great 😄")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: I'm not sure I understand that yet.")
