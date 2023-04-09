from datetime import datetime
test = 1
with open('/home/test/Desktop/CICD/python_script_log.txt', 'a') as f:
    f.write(f'testing - {datetime.now().isoformat()} \n')

while True:
	a=1
