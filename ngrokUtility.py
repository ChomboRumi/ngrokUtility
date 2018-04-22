import threading
import os
import requests
import json
import httplib2
import time

def worker(port):
	os.system('./ngrok http ' + str(port))

class ngrokUtility:

	def __init__( self, port ):
		t = threading.Thread(target=worker(port))
		t.start()

		#t1 = threading.Thread(target=worker1)
		#t1.start()

	def publicAddr (self,tempo):
		http = httplib2.Http()
		time.sleep(tempo)
		resp, content = http.request("http://localhost:4040/api/tunnels")
		return json.loads(content)['tunnels'][0]['public_url']



