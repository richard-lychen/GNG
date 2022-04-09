from math import sin,cos,asin,acos,atan,sqrt,degrees,radians, pi

def coordinate_to_degrees(x, y): # function to convert coordinates to angles from the x-axis (0~360)
    x += 0.00001 # this is to avoid zero division error in case x == 0
 
    if x >= 0 and y >= 0:   # first quadrant
        angle = degrees(atan(y/x))
    elif x < 0 and y >= 0:  # second quadrant
        angle = 180 + degrees(atan(y/x))
    elif x < 0 and y < 0:   # third quadrant
        angle = 180 + degrees(atan(y/x))
    elif x >= 0 and y < 0:  # forth quadrant
        angle = 360 + degrees(atan(y/x))
    return round(angle,1)


# try the following code to see how it works
'''test_coordinates = [[0,0], [1,1], [0,1], [-1,1], [-1, 0], [-1,-1], [0, -1], [1,-1]]
for XY in test_coordinates: 
    print(f'[{XY[0]}, {XY[1]}] in degrees is {coordinate_to_degrees(XY[0], XY[1])}')'''



def IK(pos): # pos = [x, y, z]
 
    x, y, z = pos[0], pos[1], pos[2]
    x += 0.0000001 # this is to avoid zero-division math error

    # specify the length of the leg components
    coxa    = 10      # coxa length
    femur   = 10      # femur length
    tibia   = 10      # tibia length

    theta1 = coordinate_to_degrees(x, y)    # this is the angle from x-axis in anticlockwise rotation


    # remove the offset due to the length of coxa    
    x -= coxa*cos(radians(theta1))
    y -= coxa*sin(radians(theta1))
    
    if theta1 > 180: 
        theta1 -= 360

    P = sqrt(x**2 + y**2)
        
    if sqrt(x**2 + y**2 + z**2) > femur + tibia: 
        print("MATH ERROR: coordinate too far")
        return [theta1, 0, 0]
    
    alpha = atan(z/P)

    c = sqrt(P**2 + z**2)
    
    beta = acos((femur**2+c**2-tibia**2)/(2*femur*c))
    theta2 = beta + alpha
    theta3 = acos((tibia**2+femur**2-c**2)/(2*tibia*femur)) - pi
    
    return round(theta1,1), round(degrees(theta2),1), round(degrees(theta3),1)

'''# Example of usage
angles = IK([-7.07, 7.07, 10])
print(angles)
angles = IK([7.07, 7.07, 10])
print(angles)'''


def IK_leg(pos, LegID=1): # modified version of IK(), and will take the offset angles of each leg into account
    x, y, z = pos[0], pos[1], pos[2]
    x += 0.00000001 # this is to avoid zero-division math error

    # specify the length of the leg components <- put your original values
    coxa    = 10      # coxa length
    femur   = 10      # femur length
    tibia   = 10      # tibia length

    # offset angle of each leg from x axis (+ve counterclockwise)
    offset_angles = [0, 45, 135, 180, 225, 315] #  <- put your original values; there is not limit on numbers of leg, but they should all be between 0 ~ 360 degrees

    theta1 = coordinate_to_degrees(x, y)    # angle from x-axis in anticlockwise rotation

    # remove the offset due to the length of coxa    
    x -= coxa*cos(radians(theta1))
    y -= coxa*sin(radians(theta1))

     # subtract the offset angle from the x axis
    theta1 -= offset_angles[LegID-1] # theta1 = theta1 - offset_angles[LegID-1]
    
    if theta1 > 180: # keep the theta1 between -180 <= theta1 <= 180
        theta1 -= 360

    P = sqrt(x**2 + y**2) # calculate length P
        
    if sqrt(x**2 + y**2 + z**2) > femur + tibia: # detect math error
        print("MATH ERROR: coordinate too far")
        return [theta1, 0, 0]
    
    alpha = atan(z/P) # calculate angle alpha
    c = sqrt(P**2 + z**2) # calculate length c
    
    beta = acos((femur**2+c**2-tibia**2)/(2*femur*c)) # calculate angle beta
    theta2 = beta + alpha # find theta2
    theta3 = acos((tibia**2+femur**2-c**2)/(2*tibia*femur)) - pi # find theta3
    
    return round(theta1,1), round(degrees(theta2),1), round(degrees(theta3),1)



import math
def base_rotation(x,y,z):
    x1=1
    y1=0
    tanA=(x-x1)/(y-y1)
    tana=math.degrees(math.tan(tanA))
    return tana
