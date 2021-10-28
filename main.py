#find_missing_nums(nums)
def is_prime(num):
return len([i for i in range(1, num+1) if num % i == 0]) == 2
def get_next_prime(num):
while not is_prime(num):
num += 1
return num

print(get_next_prime(int(input()) + 1))