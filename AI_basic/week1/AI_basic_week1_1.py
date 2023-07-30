num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    odd = []
    for x in num_list:
        if x % 2 == 1:
            odd.append(x)
    return odd
    
print(get_odd_num(num_list))