# Imports 
import pyttsx
import aiml
import os


# Initiate speech engine
engine = pyttsx.init()

# Initiate AIML kernel
kernel = aiml.Kernel()

#Learn AIML files
kernel.learn("std-startup.xml")
kernel.respond("load aiml")



while True:
    response = kernel.respond(input(">> "))
    engine.say(response)
    print(response)
    engine.runAndWait()
