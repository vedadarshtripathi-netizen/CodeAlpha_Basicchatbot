def get_bot_response(user_message):
    """Returns a predefined reply based on user input."""
    # Normalize input: trim whitespace and convert to lowercase
    msg = user_message.strip().lower()

    if msg in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif msg in ["how are you", "how's it going", "how are you doing"]:
        return "I'm doing well, thank you! How are you?"
    elif msg in ["what is your name", "who are you"]:
        return "I'm a simple rule-based Python chatbot."
    elif msg in ["help", "what can you do"]:
        return "You can say 'hello', ask 'how are you', or type 'bye' to exit."
    elif msg in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I know."


def run_chatbot():
    """Main loop to handle console input/output."""
    print("=== Simple Python Chatbot ===")
    print("Type 'bye' or 'exit' whenever you want to leave.\n")

    while True:
        user_input = input("You: ")

        # Skip empty inputs
        if not user_input.strip():
            continue

        response = get_bot_response(user_input)
        print(f"Bot: {response}\n")

        # Terminate loop when user says goodbye
        if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break


# Run the chatbot
if __name__ == "__main__":
    run_chatbot()