people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    #Your code here
    people_new=list(people)
    if person_name in people_new:
        people_new.remove(person_name)   
    return(people_new)




#Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
