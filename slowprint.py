import time, sys

def slowprint(string, pause_time):
    itr = iter(string)
    for letter in itr:
        time.sleep(pause_time)
        sys.stdout.write(letter)
        sys.stdout.flush()
 
 slowprint("Sorry! I am a slow typer as you can see...", 0.2) 
       
