from collections import OrderedDict

from time import sleep
while True:
     try:
         print("Polling.")
         # Poll some resource
         sleep(1)
     except KeyboardInterrupt:
         break