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