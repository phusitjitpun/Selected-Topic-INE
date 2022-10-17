import re
import random

# Define a a dictionary 'keywords'.
keywords = {'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye',
'farewell'], 'thankyou': ['thank', 'thx']}
# Define a dictionary of patterns
patterns = {}
# Iterate over the keywords dictionary
for intent, keys in keywords.items():
# Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))
    
# Print the patterns
print(patterns)

bot_template = "BOT : {0}"
user_template = "USER : {0}"
responses = {'greet': 'Hello you!:)', 'goodbye': 'goodbye for now','thankyou': 'you are very welcome', 'default': 'default message'}
# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
    # Check if the pattern occurs in the message
        if pattern.search(message):
            matched_intent = intent
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

def send_message(message):
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

for i in range(3):
    value = input("USER: ")
    send_message(value)

# Send messages
'''send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")'''
