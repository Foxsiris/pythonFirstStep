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
print('My git is work')