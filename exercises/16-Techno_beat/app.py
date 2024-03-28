def lyrics_generator(beats):
    tres=0
    for i in range(len(beats)):
        if beats[i]==1:
            print('Drop the bass')
            tres+=1
            if tres==3:
                print('!!!Break the bass!!!')
        elif beats[i]==0:
            print('Boom')
            tres=0
                   

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
