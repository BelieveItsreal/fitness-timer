from datetime import datetime
from pygame import mixer
from time import time
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}")
if __name__ == '__main__':
   #musiconloop("D:\\coding\\Area_51\\python cod\\alarm.mp3", "stop")
   init_water = time()
   init_eyes = time()
   init_exercise = time()
   watersecs = 15
   exsecs = 30
   eyesecs = 45
   while True:
        if time() - init_water > watersecs:
            print("water drinking time.Enter 'drank' to stop the alarm.")
            musiconloop("D:\\coding\\Area_51\\python cod\\alarm.mp3", "drank")
            init_water = time()
            log_now("drank water at")
        if time() - init_eyes >eyesecs:
            print("eye exercise time.Enter 'doneeyes' to stop the alarm.")
            musiconloop("D:\\coding\\Area_51\\python cod\\eyes.mp3", "doneeyes")
            init_eyes = time()
            log_now("eyes relaxed at") 
        if time() - init_exercise > exsecs:
            print("physical activity time.Enter 'donephy' to stop the alarm.")
            musiconloop("D:\\coding\\Area_51\\python cod\\exer.mp3", "donephy")
            init_exercise = time()
            log_now("exercise done at")