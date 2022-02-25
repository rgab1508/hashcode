
t = int(input())

likes_db: dict = {}
dislikes_db: dict = {}

ans = []

for it in range(t):
  l = input().split(" ")
  d = input().split(" ")


  l.pop(0)
  d.pop(0)
  
  for i in l:
    if likes_db.get(i):
      likes_db[i] += 1
    else:
      likes_db[i] = 1
  for j in d:
    if dislikes_db.get(j):
      dislikes_db[j] += 1
    else:
      dislikes_db[j] = 1

for i in likes_db.keys():
  if likes_db[i] > dislikes_db.get(i, 0):
    ans.append(i)

print(f"{len(ans)} {' '.join(ans)}", end="")