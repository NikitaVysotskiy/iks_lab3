import os 

CURRENT_VERSION = os.popen('git describe --tags').read().strip()

with open('version.txt', 'w') as f:
	f.write(CURRENT_VERSION)

print(CURRENT_VERSION)

