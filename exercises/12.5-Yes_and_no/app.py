the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def wikiwoko(bool):
    if bool==1:
        resultado='Wiki'
    else: resultado='Woko'
    return resultado

final=list(map(wikiwoko,the_bools))

print(final)
