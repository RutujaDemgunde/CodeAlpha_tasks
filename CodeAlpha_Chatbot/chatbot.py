import random
import time


# Response mappings — keyword triggers → possible replies
RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "howdy", "hiya"): [
        "Hey there! 😊 How can I help you today?",
        "Hi! Great to see you. What's on your mind?",
        "Hello! Hope you're having a good day!",
    ],

    # How are you
    ("how are you", "how r u", "how's it going", "how are things", "you good"): [
        "I'm doing great, thanks for asking! What about you?",
        "All good on my end! How can I assist you?",
        "Feeling fantastic! What can I do for you today?",
    ],

    # User feeling good
    ("i'm good", "i am good", "i'm fine", "doing well", "pretty good", "great"): [
        "That's awesome to hear! 😄",
        "Glad to know that! So, what brings you here today?",
        "Wonderful! Let me know if there's anything I can help with.",
    ],

    # Name
    ("what's your name", "what is your name", "who are you", "your name"): [
        "I'm CodeBot, your friendly assistant! 🤖",
        "You can call me CodeBot. Nice to meet you!",
    ],

    # Help
    ("help", "what can you do", "assist", "support"): [
        "I can chat with you, answer simple questions, and keep you company. Just type anything!",
        "I'm here to help! Try asking me how I'm doing, what my name is, or just say hello.",
    ],

    # Time / date
    ("time", "what time", "what's the time"): [
        f"I don't have a live clock, but your device can tell you the exact time! ⏰",
    ],

    # Joke
    ("joke", "tell me a joke", "make me laugh", "funny"): [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the developer go broke? Because he used up all his cache! 💸",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 😄",
    ],

    # Thanks
    ("thanks", "thank you", "thx", "ty"): [
        "You're welcome! Anytime 😊",
        "Happy to help! Let me know if you need anything else.",
        "No problem at all!",
    ],

    # Bye
    ("bye", "goodbye", "see you", "later", "exit", "quit"): [
        "Goodbye! Take care! 👋",
        "See you later! Have a wonderful day!",
        "Bye! It was nice chatting with you 😊",
    ],

    # Weather
    ("weather", "is it raining", "temperature outside"): [
        "I can't check live weather, but you can ask Google or check your weather app!",
    ],

    # Age
    ("how old are you", "your age", "when were you born"): [
        "I'm as young as the last line of code that made me! 😄",
        "Age is just a number — I was born the moment you started chatting!",
    ],

    # Feeling sad
    ("i'm sad", "i am sad", "feeling down", "not good", "depressed", "i'm upset"): [
        "I'm sorry to hear that. 💙 Sometimes talking helps — I'm here if you want to chat.",
        "Hang in there! Even rough days come to an end. You've got this 💪",
    ],
}

# Default replies when nothing matches
DEFAULT_REPLIES = [
    "Hmm, I'm not sure I follow. Could you rephrase that?",
    "Interesting! Tell me more?",
    "I didn't quite catch that. Try asking me something else!",
    "That's a bit beyond my knowledge right now, but I'm learning! 😅",
]


def get_response(user_input):
    """Match user input against known keywords and return an appropriate reply."""
    user_input = user_input.lower().strip()

    for keywords, replies in RESPONSES.items():
        for keyword in keywords:
            if keyword in user_input:
                return random.choice(replies)

    return random.choice(DEFAULT_REPLIES)


def typing_effect(text, delay=0.03):
    """Print text with a typewriter effect for a more natural feel."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def run_chatbot():
    print("\n" + "="*45)
    print(" 🤖 Welcome to CodeBot!")
    print("="*45)
    typing_effect("Hey! I'm CodeBot, your virtual assistant.")
    typing_effect("Type something to get started. Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nCodeBot: Goodbye! 👋\n")
            break

        if not user_input:
            print("CodeBot: Looks like you didn't type anything. Say hi! 😊")
            continue

        response = get_response(user_input)
        print(f"CodeBot: ", end="")
        typing_effect(response)
        print()

        # Exit condition
        if any(word in user_input.lower() for word in ("bye", "goodbye", "exit", "quit")):
            break


if __name__ == "__main__":
    run_chatbot()