
def totalsum(n):
    sum=0
    for i in range(n):
        sum += i
    return sum


def list_sum(a_list):
    result = 0
    for val in a_list:
        result += val
    return result

def list_sum_recursive(a_list):
    if len(a_list) == 0:
         return 0
    
    return a_list[0] + list_sum_recursive(a_list[1:])

# print(totalsum(4))
# print(list_sum([1,3,5]))
print(list_sum_recursive([5,6,7,9,10]))