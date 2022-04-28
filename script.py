import requests
from datetime import datetime
amount_p = input()
r = requests.get(f'https://baconipsum.com/api/?type=meat-and-filler&paras={amount_p}')
array_p = r.json()
array_p.reverse()
count = 0
for p in array_p:
    if 'Pancetta' in p:
        count += 1

f = open("result.txt", "w")
f.write('Yurii Shevchuk \n')
f.write(f'Date run: {datetime.now()} \n')
f.write(f'Amount substring \'Pancetta\' in text: {str(count)} \n')
f.write(f'Data from requests: \n')
f.write(''.join(map(lambda p: f'{p} \n', array_p)))
f.close()
