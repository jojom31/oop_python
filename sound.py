#import playsound
#from AppKit import NSSound
#playsound.playsound('Hello world')


#from pygame import mixer

MAGIC_NUMBER = 6
user_input = int(input("Please type a number: "))

if user_input == MAGIC_NUMBER:
    print("Whoa!!! Are you a mind reader?!?!")

else:
    print("Sorry, try again next time!")

MAGIC_NUMBER = 4

user_input = int(input("Please type a number 0-6"))


day_of_week = int(input("What Day of The Week"))
sleep = True 

if day_of_week == 0 or day_of_week == 6:
    sleep = True

if sleep:
    print("Sleep in!!")
else:
    print("Go to work.")




##mixer.init()
#mixer.music.load("elevator.wav")
#mixer.music.play(-1)

#pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
#pygame.init() #turn all of pygame on.


#elevator_sound = mixer.music("audio/elevator.wav")
#elevator_sound.play(-1)
#mixer.init()

#mixer.sound.load("audio/footsteps.wav")
#mixer.sound. play(-1)