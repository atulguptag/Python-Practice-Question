#Cook your dish here

q = int(input())

for i in range(q):
    n = int(input())
    s = input().strip()
    t = input().strip()
    u = input().strip()
    
    k = (ord(t[0]) - ord(s[0])) % 26
    
    shifted_u = ""
    
    for c in u:
        shifted_ascii = (ord(c) - ord('a') + k) % 26 + ord('a')
        shifted_char = chr(shifted_ascii)
        shifted_u += shifted_char
    
    print(shifted_u)