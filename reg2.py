import re
fh = open('regex_sum_2173657.txt')
sm = 0
for line in fh:
    res = re.findall('[0-9]+',line)
    for it  in res:
        sm += int(it)

print(sm)