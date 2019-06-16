from local_machine_info import print_machine_info
import thread
import time 
import datetime

vrijeme = datetime.date.today()
print vrijeme	
print_machine_info()

# Definicija funkcije za nit
def print_time( threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s: %s" % ( threadName, time.ctime(time.time()))
		

# Kreiramo dvije niti
try:
	thread.start_new_thread( print_time, ("Thread-1", 2, ))
	thread.start_new_thread( print_time, ("Thread-2", 4, ))

except:
	print "Greška: ne mogu pokrenuti nit!!"
		
#Cekaj dok se sve niti ne izvrše
while 1:
	pass

