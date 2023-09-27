a = int(input())
b = int(input())
n = b - a + 1
used = [False] * n

def perm(n, used, numbers=[]):
  if len(numbers) == n:
    print(''.join(numbers))
    return
  for i in range(n):
    if not used[i]:
      used[i] = True
      numbers.append(str(i+a))
      perm(n, used, numbers)
      used[i] = False
      numbers.pop()

perm(n, used)
