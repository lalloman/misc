d = {}
with open('MonsterDict1.txt') as file:
    for line in file:
        (key,val) = line.strip("\n").split(",")
        d[key] = val
key = input("what monster do you wanna know about :3")
print(d[key])