names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here
names.insert(1,'Steven')
names.append('Pepe')
names[0]=names[2] + names[4]

for i in range (len(names)-1,-1,-1):
    print(names[i])