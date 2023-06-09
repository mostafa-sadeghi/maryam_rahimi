numbers = [1,2,0,4,5,6]

def is_asc(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(i+1, len(numbers_list)):
            if numbers_list[j] < numbers_list[i]:
                return False
    return True

print(is_asc(numbers))