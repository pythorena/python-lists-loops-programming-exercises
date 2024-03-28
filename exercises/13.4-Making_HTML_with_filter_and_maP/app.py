all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here

def generate_li(lista):
    return f"<li>{lista['label']}</li>"

def filter_colors(lista):
    return lista["sexy"]==True

sexy_colors=list(filter(filter_colors,all_colors))
resultado=list(map(generate_li,sexy_colors))
print(resultado)

