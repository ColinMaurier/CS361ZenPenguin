#imports
import pyttsx3
import time
import random
import sys

def speak_text(text):
    engine = pyttsx3.init("nsss")
    voices = engine.getProperty('voices')

    #set properties for voice
    #engine.setProperty('voice','english_rp+f3')
    engine.setProperty('rate', 160)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.75)  # Volume 0-1
    
    #speak the text
    engine.say(text)
    
    #block input the speech is done
    engine.runAndWait()
    
    #ask user how they are feeling
def feelings():
        user_feeling = input("Please enter how you are feeling: 'sad', 'anxious', or 'happy', (or 'Q' to quit): ")
        if user_feeling in ['sad', 'anxious', 'happy']:
            return user_feeling
        if user_feeling in ['Q']:
            sys.exit(0)
        else:
            print("Please enter: 'sad', 'anxious', or 'happy': ")
  
#load responses for sadness   
def SadResponses():
    lines = open('Sad.txt').read().splitlines()
    myline =random.choice(lines)
    print(myline)
    speak_text(myline)
    
#load responses for anxious   
def AnxiousResponses():
    lines = open('Anxious.txt').read().splitlines()
    myline =random.choice(lines)
    print(myline)
    speak_text(myline)
    
#load responses for happy   
def HappyResponses():
    lines = open('Happy.txt').read().splitlines()
    myline =random.choice(lines)
    print(myline)
    speak_text(myline)
    
#about function
def about():
    user_input = input("Please enter 'about' to read software information, (or anything else to just continue): ")
    if user_input.lower() == 'about':
        print("Software Name: ZenPenguin")
        print("Version: 1.0")
        print("Developer: Colin Maurier")
        print("This program introduces users to Penny the Penguin, the fun, loving, and supportive emotional compananion.")
    else:
        print("Continuing with ZenPenguin...")
 
#setting up header
def print_header():
    header = """
    ____________________________________________________
    < Welcome to ZenPenguin - Your Stress Reliever App 😊 >
    ----------------------------------------------------
         \\
          \\
              .--.
             |o_o |
             |:_/ |
            //   \\ \\
           (|     | )
          /'\\_   _/`\\
          \\___)=(___/
    """
    print(header)

def main():
    print("")
    time.sleep(2)
    print("Initailizing ZenPenguin...")
    print("")
    time.sleep(2)
    print("Warning: This application automatically plays sound.")
    print("")
    time.sleep(2)
    print("Please mute your system now if you do not want to hear sound.")
    print("")
    time.sleep(5)
    print_header()
    Prompt1 =("Welcome to ZenPenguin, Your Stress Reliever Application!")
    print(Prompt1)
    speak_text(Prompt1)
    Prompt5 =("With your friend, Penny the Penguin.")
    print(Prompt5)
    speak_text(Prompt5)
    print("")
    about()
    print("")
    Prompt2 = "Please enter your name to get started: "
    print(Prompt2)
    speak_text(Prompt2)
    name = input("")
    Prompt3 = ("Hello " +name+"!")
    print(Prompt3)
    speak_text(Prompt3)
    Prompt4 = ("How can Penny help you today, "+name+"?")
    print(Prompt4)
    speak_text(Prompt4)
    
    #begin loop for questioning user
    while True:
        user_feeling = feelings()
        if user_feeling == 'sad':
            SadResponses()
            print("Do not worry, "+name+".")
            speak_text("Do not worry, "+name+".")
            print("(Reminder, please wait for prompts to finish before hitting enter)")
        elif user_feeling == 'anxious':
            AnxiousResponses()
            print("You are very loved, "+name+".")
            speak_text("You are very loved, "+name+".")
            print("(Reminder, please wait for prompts to finish before hitting enter)")
        elif user_feeling == 'happy':
            HappyResponses()
            print("You are awesome, "+name+"!")
            speak_text("You are awesome, "+name+"!")
            print("(Reminder, please wait for prompts to finish before hitting enter)")
            
             # Ask the user if they want to continue
        user_input = input("Do you want to enter another feeling? (yes/no): ").lower()
        if user_input != 'yes':
            print("Goodbye!")
            speak_text("Goodbye!")
            break

if __name__ == "__main__":
    main()



