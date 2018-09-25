from datetime import datetime
from datetime import timedelta
import time

start_time = int((datetime.utcnow()-datetime.utcfromtimestamp(0)).total_seconds())

out = False
while not out:
    current_time = int((datetime.utcnow()-datetime.utcfromtimestamp(0)).total_seconds())
    if current_time - start_time < 15:
        print "Sleep for 1 second..."
        time.sleep(1)
        print 
    else:
        print "We are done"
        break
