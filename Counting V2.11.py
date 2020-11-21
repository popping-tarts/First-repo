#!python3
import time 
import os
import sys
while True:
     try:
         print("What number would you like to count up to?")
         max_count = int(input())
     except ValueError:
         print ("Must be a number.\n Try again.")
         time.sleep(1)
         continue
     if isinstance(max_count,int):
        break
count =int(0)
print ("Let's go!")
while (max_count > count):
    count+=1
    time.sleep(1)
    print(count)
print("Done!")

def restart():
     while True:
         re =(input("Restart? y for 'Yes', and n for 'No\' "))
         re = re.lower()
         if re == "y": 
          os.execv(sys.executable, [sys.executable, '"' + sys.argv[0] + '"'] + sys.argv[1:])
         elif (re == "n"):
             print("Okay then. \n That's the end,folks!")
             time.sleep(3)
             exit()
         else:
             print("Invalid response.")
             continue
restart()
           





        

