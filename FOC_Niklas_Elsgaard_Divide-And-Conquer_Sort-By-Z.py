# FOC - Niklas Elsgaard - Divide-And-Conquer-And-Sort algorithm thing

import rhinoscriptsyntax as rs

# defines sort function - Stops after length of 3 (cant be divided further)
def sort_points_by_z(points):
    if len(points) <= 1:
        return points
    
    # splits list into two seperate lists (whole integers)
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]
    
    # sorts the two halfs
    left_sorted = sort_points_by_z(left)
    right_sorted = sort_points_by_z(right)
    
    # merge the two sorted halves - Left and Right
    # In the loop, the lowest index is appended into Result, then move the index by +=1 and appends the remaining point

    result = []
    L = 0
    R = 0
    while L < len(left_sorted) and R < len(right_sorted):
        if left_sorted[L][2] < right_sorted[R][2]:
            result.append(left_sorted[L])
            L += 1
        else:
            result.append(right_sorted[R])
            R += 1
    
    result += left_sorted[L:]
    result += right_sorted[R:]
    
    return result

# In rhino: Select points to sort - When point appended, label enumerate number of points using Rhino Text Dots
points = rs.GetObjects("I'M MR. MEESEEKS. I NEED POINTS TO FULFILL MY PURPOSE SO I CAN GO AWAY. LOOK AT ME!")
if points:
    points = [(rs.PointCoordinates(pt)) for pt in points]
    sorted_points = sort_points_by_z(points)
    for L, pt in enumerate(sorted_points):
        rs.AddTextDot(str(L), pt)
print "GOODBYE!"
print "*poof*"