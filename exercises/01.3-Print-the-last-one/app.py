# import the random package here "import random"
import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list

my_stupid_list = generate_random_list()

# Write your code below this comment, good luck!
def the_last_one():
    longitud=len(my_stupid_list)
    print("La liste tiene:",longitud," posiciones")
    print(my_stupid_list[-1])

the_last_one()