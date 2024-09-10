import os
from dotenv import load_dotenv
import telebot
from question_bank import quiz


load_dotenv()

token = os.environ.get('TOKEN2')
bot = telebot.TeleBot(token)

count = 0

@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    bot.send_message(message.chat.id, 'Welcome to the appclick"s quiz!, choose 1 to continue')

def filter(message):
    text_in_small_letters = message.text.lower()
    return text_in_small_letters  == "1"

@bot.message_handler(func=filter)
def handle_message(message):
    bot.send_message(message.chat.id, f"{quiz[count]['question']}\n a. {quiz[count]['options']['a']}\n b. {quiz[count]['options']['b']}\n c. {quiz[count]['options']['c']}\n d. {quiz[count]['options']['d']}")


def answer(message):
    text_in_small_letters = message.text.lower()
    return text_in_small_letters == "c"

@bot.message_handler(func=answer)
def handle_message(message):
    global count
    count += 1
    bot.send_message(message.chat.id, "Correct answer!")
    bot.send_message(message.chat.id, f"{quiz[count]['question']}\n a. {quiz[count]['options']['a']}\n b. {quiz[count]['options']['b']}\n c. {quiz[count]['options']['c']}\n d. {quiz[count]['options']['d']}")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, 'Wrong input, please select a valid option')

bot.infinity_polling()


# class User:
#     def __init__(self, id):
#         self.id = id

#     def username(self, name):
#         print(self.id)
#         print(name + str(self.id))

# print(token)

# user = User(2)

# user.username("ola")

# user2 = User(3)
# user2.username("paul")

# def sum(num1, *args, **kwargs):
#     print(num1)
#     print(args[0])
#     print(kwargs["name"])
#     print(kwargs["age"])

# # sum(1,23,4)
# sum(1,2,name="paul", age=23)

# lambda num:num + 1
