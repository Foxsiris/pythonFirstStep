#Работа с переменными
mynane = ' daniil '
mysurname = 'FOX'
fullname = f"{mynane} {mysurname} "
numOne = 14_000_765_10

fir,sec,three = 12,13,14

def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Maria')

print('Hello MR  -'+fullname.rstrip())
print(numOne)
print(fir,sec,three)

#Списки

nums = [1, 2, 3, 4, 5]
print(nums)
nums.append(12)
print(nums)
nums.insert(2,33)
print(nums)
del nums[2]
print(nums)
nums.pop(1)
print(nums)
nums.remove(12)
print(nums)
nums.sort(reverse=True)
print(nums)
print(len(nums))

#### Работа со списками
numss = [1, 2, 3, 4, 5]
for n in nums:
    print(n)

for z in range(1,12):
    print(z)

numsWithList = list(range(1,1_000))


print(numsWithList)

exampleList = []
for item in range(1,10):
    exampleList.append(item**3)
print(exampleList)
print(min(exampleList))
print(max(exampleList))
print(numsWithList[399:])

copyList = exampleList[:]
print(copyList)
exampleList.append(33)
copyList.append(22)
print(copyList)
print(exampleList)


def even_or_odd(number):
    if number%2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(even_or_odd(3))

#inputNum = input('Enter number : ')
#print(inputNum)

#### Классы

class Animal():
    def mayy(self):
        print('Maaaayy')
class Cat(Animal): # так выглядит наследование выглядит очень круто
    def __init__(self,name,age):
        self.name = name
        self.age = age





    def showInfo(self):
        print(f'Your cat name : {self.name} {self.age}')

mycat =  Cat('Max',12)
myCatTw = Cat('Two',13)
mycat.showInfo()
myCatTw.showInfo()
mycat.mayy()

with open('test.rtf') as file_object:
    content = file_object.read()
print(content)

with open('test.rtf','a') as file_object:
    file_object.write('I love Python laguge it is good')

with open('test.rtf') as file_object:
    content = file_object.read()
print(content)

import json

n = [1,2,3,4,5,6,7]
filename='fisrst.json'
with open(filename,'w') as f:
    json.dump(n,f)

filename = 'fisrst.json'
with open(filename) as f:
    nz = json.load(f)
    print(nz)