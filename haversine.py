from math import *
def haversine(coord1 , coord2):
    
    lat1 , lon1 = radians(coord1[0]) , radians(coord1[1])
    lat2 , lon2 = radians(coord2[0]) , radians(coord2[1])

    delta_phi = lat2 - lat1
    delta_lambda = lon2 - lon1

    def hav(x):

        h = pow(sin(x/2) , 2)
        return h
    
    H = hav(delta_phi) + cos(lat1)*cos(lat2)*hav(delta_lambda)
    R = 6378

    d = 2*R*asin(sqrt(H))
    
    print(d," km")
