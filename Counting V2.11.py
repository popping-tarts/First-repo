#!python3
import time 
import os
import sys
while True:
     try:
         print("What number would you like to count up to?")
         max_count = int(input())
         max_count = (max_count + 1)
     except ValueError:
         print ("Must be a number.\n Try again.")
         time.sleep(1)
         continue
     if isinstance(max_count,int):
        break
print ("Let's go!")
count = 0
for count in range(count,max_count):
    print(count)
    time.sleep(1)
if count == max_count:
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
           





        

