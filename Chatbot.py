import datetime
import time
import pywhatkit

print("Example: Tell me the time, Play Sun Goes Down, Send a mail, Send a Whatsapp message, Search Lorem Ipsum, Info about Python")

def run_chatbot():
    user_request = input("Enter a commmand: ")

    if "time" in user_request:

          now = datetime.datetime.now()
          dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
          print(dt_string)
          time.sleep(30)

    if "play" in user_request:

        song = user_request.replace("play", "")
        pywhatkit.playonyt(song)

    if "info about" in user_request:

        about = user_request.replace("info about", "")
        pywhatkit.info(about)

    if "search" in user_request:

        search = user_request.replace("search", "")
        pywhatkit.search(search)

    if "mail" in user_request:

        sender = input("From: ")
        password = input("Password: ")
        title = input("Title: ")
        body = input("Body: ")
        to = input("To: ")
        pywhatkit.send_mail(sender, password, title, body, to)

    else:

        print("Try Tell me the time, Play Sun Goes Down, Send a mail, Send a Whatsapp message, Search Lorem Ipsum, Info about Python")


while True:
    run_chatbot()
