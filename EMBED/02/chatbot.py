import random

random_replies = ["Oh really?", "Are you sure about that?", "Perhaps…", "I don't think so",
"Come on do someething!", "I like that idead"]
chat_dict = {"happy": "I'am happy today too", "sad": "Be happy, life is good", "computer": "Computers will take over the world!",
"help": "Maybe you should take a nap", "light": "Turn on dark mode, the light attracts bugs"}

def dictionary_check(message):
    message = message.lower()
    user_words = message.split()
    smart_replies = []
    for word in user_words:
        if word in chat_dict:
            answer = chat_dict[word]
            smart_replies.append(answer)
    if smart_replies:
        reply_chosen = random.randint(1, len(smart_replies)) - 1
        return smart_replies[reply_chosen]
    else:
        return ""

def main():
    print("What would you like to talk about?")
    user_says = ""
    while user_says != "bye":
        user_says = ""
        while user_says == "":
            user_says = input("Talk to me: ")
        smart_response = dictionary_check(user_says)
        if smart_response:
            print(smart_response)
        else:
            reply_chosen = random.randint(1, len(random_replies)) - 1
            print(random_replies[reply_chosen])
            random_replies[reply_chosen] = user_says
    print("Goodbye. Thanks for chatting today!")


if __name__ == "__main__":
    main()