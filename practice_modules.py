import random
a = random.choice([2,4,5,6])
print(a)
b = [2,4,5,7]
random.shuffle(b)
print(b)
c = random.randrange(2,3,2)
print(c)
d = random.uniform(2,4)
print(d)
e = random.seed(2)
print(random.random())

