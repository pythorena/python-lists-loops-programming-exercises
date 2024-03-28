all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def nombres_r(lista):
    return lista[0].lower() == "r"

resulting_names=list(filter(nombres_r,all_names))
print(resulting_names)




