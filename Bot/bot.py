import aiml
import os
import pyttsx

kernel = aiml.Kernel()

engine = pyttsx.init()


if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load")
    kernel.saveBrain("bot_brain.brn")

# Kernel now ready for use
while True:
    response = (kernel.respond(input(">> ")))
    engine.say(response)
    print(response)
    engine.runAndWait()
