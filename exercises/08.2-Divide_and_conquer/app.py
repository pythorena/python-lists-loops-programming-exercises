list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(list):
    even=[]
    sorted_list=[]
    for i in range (0, len(list_of_numbers)):
        if list_of_numbers[i]%2==0:
            even.append(list_of_numbers[i])
        else: sorted_list.append(list_of_numbers[i])
    total = sorted_list+even
    return total

print(sort_odd_even(list_of_numbers))

