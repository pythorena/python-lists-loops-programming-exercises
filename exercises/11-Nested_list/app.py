coordinates_list = [[33.747252, -112.633853], [-33.867886, -63.987], [41.303921, -81.901693], [-33.350534, -71.653268]]

# Your code here
latitud1=coordinates_list[0][0]
longitud1=coordinates_list[0][1]
latitud2=coordinates_list[1][0]
longitud2=coordinates_list[1][1]
latitud3=coordinates_list[2][0]
longitud3=coordinates_list[2][1]
longitud4=coordinates_list[3][1]
#print(coordinates_list[0])
#print(latitud1)
print(longitud1)
#print(latitud2)
print(longitud2)
#print(latitud3)
print(longitud3)
print(longitud4)

for i in range(0, len(coordinates_list)):
    longitud=coordinates_list[i][1]
    print(longitud)
