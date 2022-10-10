from email import message


bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot response
    bot_message = "I can hear you! You said: " + message
    # Return the result
    return bot_message

# Test function
print(respond("hello!"))

def send_message(message):
        # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


# Define variables
name = "Bot"

weather = "cloudy"
# Define a dictionary with the predefined responses
responses = {
    "what's your name?": "my name is {0}".format(name),
    "what's today's weather?": "the weather is {0}".format(weather),
    "default": "default message"
    }
# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        #Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message

def send_message(message):
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
print(bot_template.format("Hi!"))
value = input("USER: ")
send_message(value)

