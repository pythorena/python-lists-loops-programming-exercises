parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(matriz):
    state={'total':0,'disponibles':0,'ocupados':0}
    for i in range(len(matriz)):
        for j in range(len(matriz)):
          if matriz[i][j]==1:
            state['ocupados']+=1
            state['total']+=1
          elif matriz[i][j]==2:
             state['disponibles']+=1
             state['total']+=1
    return state
   
print(get_parking_lot(parking_state))