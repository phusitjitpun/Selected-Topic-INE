from email import message
import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"
name = "Bot"
weather = "cloudy"
# Define a dictionary containing a list of responses for each message
responses = {
    'statement': [
        'tell me more!',
        'why do you think that?',
        'how long have you felt this way',
        'I find that extremely intersting',
        'can you back that up?', 'oh wow!',
        ':)'
    ],
    'question': [
        "I don't know :(",
        'you tell me!'
    ]
}

def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


def send_message(message):
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")
