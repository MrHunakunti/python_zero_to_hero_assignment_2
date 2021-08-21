text = "psudopodia"
temp = []

for i in text:
  if i not in temp:
    print(f"{i}:{text.count(i)}")
    temp.append(i)

