import cdsw

worker_code = '''
              import os 
              engine_id = os.environ.get('CDSW_ENGINE_ID')
              print('executing a whole bunch of code inside a worker from engine : {}'.format(engine_id))
              '''

workers = cdsw.launch_workers(n=3, 
                              cpu=1, 
                              memory=1, 
                              code=worker_code) 

#Get workers ID
for worker in workers : 
  print(worker['id'])


# get workers information
import time 
# wait 10 secs for workers to come up
time.sleep(10)

for worker in workers : 
  import json
  print(json.dumps(worker, indent=4))