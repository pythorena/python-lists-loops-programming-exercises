incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def data_transformers(lista):
    nombre = lista["name"]
    apellido = lista["last_name"]
    return f"{nombre} {apellido}"

nueva_lista=list((map(data_transformers,incoming_ajax_data)))
print(nueva_lista)
