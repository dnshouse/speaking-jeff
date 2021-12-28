import random
import speech_recognition as sr
import subprocess

running = True
previous = False

r = sr.Recognizer()


def say(text):
    subprocess.call('say "' + text + '"', shell=True)


def speech():
    print("Listening")
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        say("I don't understand")

    return command


while running:

    if not previous:
        print("Say something")
        textInput = speech().lower()
        previous = True
    else:
        textInput = speech().lower()

    if textInput.find("bye") > -1:
        say("Good bye Human")
        running = False
    elif textInput.find("how are you") > -1:
        say('I am well today. How about you?')
    elif textInput.find("time") > -1:
        say('It looks like is time for bed.')
    elif textInput.find("weather") > -1:
        say('It should be sunny today but it is night already.')
    elif textInput.find("name") > -1:
        say("My name is Jeff, what's yours?")
    elif textInput.find("old") > -1:
        say("I was created less than an hour ago by Kosse.")
    elif textInput.find("age") > -1:
        say("I was created less than an hour ago by Kosse.")
    else:
        answers = ["Hmm...", "Strange", "Nice", "That's fine", "That's crazy!", "I'm not sure about that"]
        say(answers[random.randrange(0, 6)])
