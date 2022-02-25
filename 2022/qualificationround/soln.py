
class Contributor:
  def __init__(self, name, levels, no_of_skills, raw_skills):
    self.name = name
    self.levels = levels
    self.raw_skills = raw_skills
    self.no_of_skills = no_of_skills
    self.working = False

  def __str__(self):
    return f"""
    {self.name} ({str(self.no_of_skills)} skills)
    """

class Project:
  total_days = 0
  def __init__(self, name, no_of_days, score, best_before, no_of_roles, roles, raw_roles):
    self.name = name
    self.no_of_days = no_of_days
    self.score = score
    self.best_before = best_before
    self.no_of_roles = no_of_roles
    self.roles = roles
    self.raw_roles = raw_roles
    self.days_worked = 0

    Project.total_days += no_of_days


  def __str__(self):
    return f"""
    {self.name} ({self.no_of_days} days)
    {str(self.score)} points
    {str(self.best_before)}
    {str(self.no_of_roles)} roles
    
    """

[no_of_contributors, no_of_projects] =  list(map(int, input().split(" ")))

contributors: list = list()
projects: list  = list()

output = {}


for i in range(no_of_contributors):
  [name, no_of_skills] = input().split(" ")
  no_of_skills = int(no_of_skills)
  l: dict = {}
  raw_skills = []
  for i in range(no_of_skills):
    [skill, level] = input().split(" ")
    level = int(level)
    if l.get(level):
      l[level].append(skill)
    else:
      l[level] = [skill]

    raw_skills.append([skill, level])

  c = Contributor(name, l, no_of_skills,raw_skills)
  # print(l)
  contributors.append(c)


for i in range(no_of_projects):
  [name, no_of_days, score, best_before, no_of_roles] = input().split(" ")
  no_of_days = int(no_of_days)
  score = int(score)
  best_before = int(best_before)
  no_of_roles = int(no_of_roles)
  roles = {}
  raw_roles = []
  for i in range(no_of_roles):
    [r_name, level] = input().split(" ")
    level = int(level)
    if roles.get(level):
      roles[level].append(r_name)
    else:
      roles[level] = [r_name]

    raw_roles.append([r_name, level])

  p = Project(name, no_of_days, score, best_before, no_of_roles, roles, raw_roles)
  projects.append(p)

projects.sort(key=lambda x: x.score, reverse=True)

day = 0
currProj = 0

def get_contributor(r_name, level):
  for c in contributors:
    for r in c.raw_skills:
      if r[0] == r_name and r[1] >= level and not c.working:
        c.working = True
        return c
  return None


while day * 5 < Project.total_days:

  for p in projects:
    finish = False
    assigned_roles = []
    for r in p.raw_roles:
      c = get_contributor(r[0], r[1])
      if c:
        # print(f"{c.name} assigned to {p.name} as {r[0]}")

        assigned_roles.append(c)
      else:
        break


    if len(assigned_roles) != p.no_of_roles:
      for a in assigned_roles:
        a.working = False
      finish = True

    if finish:
      continue

    output[p.name] = assigned_roles

    p.days_worked += 1
    # print(output[p.name])
    if p.days_worked >= p.no_of_days:
      for a in output[p.name]:
        print(a, a.working)
        a.working = False

  day += 1

new_output = [v for k, v in output.items() if len(v) > 0]
print(len(new_output))
for k,v in output.items():
  if len(v) < 1:
    continue
  print(k)
  print(" ".join(x.name for x in v))