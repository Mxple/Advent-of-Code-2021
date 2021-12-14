import sys, os
#part 1
class submarine:
    def __init__(self):
        self.x = 0
        self.y = 0
    def forward(self, num):
        self.x += num
    def up(self, num):
        self.y -= num
    def down(self, num):
        self.y += num

#part 2
class submarineWithAim:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0
    def forward(self, num):
        self.x += num
        self.y += num*self.aim
    def up(self, num):
        self.aim -= num
    def down(self, num):
        self.aim += num

#file name is input1
file = open(os.path.join(sys.path[0], "input.txt"), "r")
commands = file.read().split("\n")
file.close()

sub = submarine()
subAim = submarineWithAim()

#changing positions
for c in commands:
    if "up" in c:
        sub.up(int(c[-1]))
        subAim.up(int(c[-1]))
    elif "down" in c:
        sub.down(int(c[-1]))
        subAim.down(int(c[-1]))
    else:
        sub.forward(int(c[-1]))
        subAim.forward(int(c[-1]))

#prints horizontal * vertical positions
print(sub.x*sub.y)
print(subAim.x * subAim.y)



