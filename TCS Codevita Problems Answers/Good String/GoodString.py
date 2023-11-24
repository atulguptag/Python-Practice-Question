good_string = input().strip()
name = input().strip()

total_distance = 0
previous_good_letter = good_string[0]

for letter in name:
    if letter in good_string:
        continue
    
    min_distance = float('inf')
    nearest_letter = ''
    
    for good_letter in good_string:
        distance = abs(ord(letter) - ord(good_letter))
        
        if distance < min_distance:
            min_distance = distance
            nearest_letter = good_letter
        elif distance == min_distance and abs(ord(previous_good_letter) - ord(good_letter)) < abs(ord(previous_good_letter) - ord(nearest_letter)):
            nearest_letter = good_letter
    
    previous_good_letter = nearest_letter
    total_distance += min_distance

print(total_distance)

"""
NOTE:- Getting wrong output for the second input. Do it in your own risk.
"""