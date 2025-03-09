import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)
    
def sing_song():
    lyrics = [
        ('Cerita kita tak jauh berbeda', 0.1),
        ('Got beat down by the world, sometimes I wanna fold', 0.1),
        ('Namun suratmu kan kuceritakan ke anak-anakku nanti', 0.1),
        ('Bahwa aku pernah dicintai with everything you are', 0.1),
        ('Fully as I am with everything you are', 0.1)
    ]
    delays = [0.3, 5.0, 10.0, 15.0, 20.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        
sing_song()