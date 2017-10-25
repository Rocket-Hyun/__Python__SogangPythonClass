import random
num = list(random.sample(range(2500000, 6000000), 4825))

#generate randomly shuffled numbers
with open("apply.dat", "w") as f:
    for i in num:
        f.write("%d\n"%(i))

#generate sorted random number
num.sort()
with open("master.dat", "w") as f:
    for i in num:
        f.write("%d\n"%(i))
