ings = input().split(" ")
ings.pop(0)
f = open("inputs/d_difficult.in", "r")

ans = 0

def has_all_likes(likes, ings):
  for i in likes:
    if i not in ings:
      return False
  return True

def has_none_dislikes(dislikes, ings):
  for i in dislikes:
    if i in ings:
      return False
  return True

t = int(f.readline())
for it in range(t):
  l = f.readline()[:-1].split(" ")
  d = f.readline()[:-1].split(" ")
  l.pop(0)
  d.pop(0)
  # print(l, d)
  if has_all_likes(l, ings) and has_none_dislikes(d, ings):
    ans += 1

print(ans)