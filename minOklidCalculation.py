import math
points=[(1,2),(3,3),(6,6),(7,8)] #uzaydaki noktaları temsil eden tuples

def euclideanDistance(point1,point2):
    #d = √(x₂-x₁)²+(y₂-y₁)²
    calculate=math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2)) 
    return calculate

distances=[] #mesafeleri tutan liste
for i in range(len(points)):
    for j in range(i+1,len(points)):
        dist=euclideanDistance(points[i],points[j])
        distances.append(dist)
minDis=min(distances)
print("points",points)
print("distances",distances)
print("min diss",minDis)