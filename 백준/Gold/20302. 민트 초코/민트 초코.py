max_num = 100001
sp = [0] * (max_num + 1)
primes = []
for i in range(2, max_num + 1):
    if sp[i] == 0:
        sp[i] = i
        primes.append(i)
        
    j = 0
    while j < len(primes) and i * primes[j] <= max_num and primes[j] <= sp[i]:
        sp[i * primes[j]] = primes[j]
        j += 1

n = int(input())
li = input().split()

ct = [0] * 100001

is_zero = False

v = abs(int(li[0]))
if v == 0:
    is_zero = True
while v > 1:
    ct[sp[v]] += 1
    v //= sp[v]

for i in range(1, len(li), 2):
    v = abs(int(li[i + 1]))
    is_div = li[i] == '/'
    
    if v == 0:
        is_zero = True
        break
        
    while v > 1:
        ct[sp[v]] += 1 - 2 * is_div
        v //= sp[v]
        
if is_zero:
    print('mint chocolate')
else:
    ip = True
    for p in primes:
        if ct[p] < 0:
            ip = False
            break
            
    if ip:
        print('mint chocolate')
    else:
        print('toothpaste')