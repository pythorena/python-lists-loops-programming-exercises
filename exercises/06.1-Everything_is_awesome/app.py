my_list = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]

def my_function(numbers):
    new_list = []
    for i in numbers:
        # The magic happens here
        if (i==1):
            new_list.append(1)
        else: new_list.append('Yahoo')
    for x in new_list:
        print(x)  
    return new_list
    
#print(my_function(my_list))
my_function(my_list)
