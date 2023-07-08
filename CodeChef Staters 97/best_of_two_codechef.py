#Cook your dish here

t = int(input())

for i in range(t):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    
    a_score = sum(sorted([a1, a2, a3])[1:])
    b_score = sum(sorted([b1, b2, b3])[1:])
    
    if a_score > b_score:
        print("Alice")
        
    elif b_score > a_score:
        print("Bob")
        
    else:
        print("Tie")