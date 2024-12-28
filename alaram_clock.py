# python alaram clock
import time
import pygame
import datetime

def set_alaram(str_alarm_time):
    print(f"Alarm set for {str_alarm_time}")
    str_sound_path = "alarm.mp3"
    bln_running = True
    
    while bln_running:
        currenct_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(currenct_time)
        
        if currenct_time == str_alarm_time:
            print("WAKE UP............!")
            pygame.mixer.init()
            pygame.mixer.music.load(str_sound_path)
            pygame.mixer.music.play()
            # to play music continously
            while pygame.mixer.music.getbusy():
                time.sleep(1)
            
            bln_running = False
            
        time.sleep(1)
        



















if __name__ == "__main__":
    str_alarm_time = input("Enter the alarm tim (HH:MM:SS) : ")
    set_alaram(str_alarm_time)
    