import json
import random
import sys

filename = sys.argv[1]
data = json.loads(open(filename).read())
instruments = data['instruments']

band = random.sample(instruments, 10)

output = "The Randoms: \n"

for instrument in band:
    output += instrument + "\n"

print(output)

with open('theband.txt', 'w') as file:
    file.write(output)
