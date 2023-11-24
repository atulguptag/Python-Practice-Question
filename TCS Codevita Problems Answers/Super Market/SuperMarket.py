def max_bags(n, m, customers, bags):
    customers.sort(key=lambda x: (-x[0], x[1]))
    bags.sort(key=lambda x: (-x[0], x[1]))
    
    sold_item = 0
    
    for i in range(n):
        for j in range(m):
            if bags[j][1] <= customers[i][1] and bags[j][0] >= customers[i][0]:
                sold_item += 1
                bags.pop(j)
                m -= 1
                break

    return sold_item

n, m = map(int, input().split())
customers = []
for _ in range(n):
    a, b = map(int, input().split())
    customers.append((a, b))
    
bags = []
for _ in range(m):
    q, p = map(int, input().split())
    bags.append((q, p))

print(max_bags(n, m, customers, bags))
