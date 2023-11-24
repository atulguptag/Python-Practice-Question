def compute_cost(seats, prices, total_collection):
    total_seats = sum(len(row) for row in seats)
    total_booked_seats = 0
    total_cost = 0

    for i, row in enumerate(seats):
        row_cost = prices[i] if prices[i] != '?' else 0
        total_cost += len(row) * row_cost
        total_booked_seats += len(row)

    missing_row_cost = (total_collection - total_cost) / (len(seats[0]) - total_booked_seats)
    return int(missing_row_cost)

def book_tickets(seating, groups, prices, total_collection):
    priority = len(groups) // 2
    priority_dict = {}

    for i in range(len(groups)):
        priority_dict[priority] = i
        if i < len(groups) // 2:
            priority -= 1
        else:
            priority += 1

    seats_left = len(seating[0])
    not_booked = []

    for p in range(1, len(groups) + 1):
        group_index = priority_dict[p]
        group_size = groups[group_index]

        for i in range(len(seating)):
            if seats_left >= group_size:
                for j in range(group_size):
                    seating[i][j] = p
                seats_left -= group_size
                break

        if seats_left < group_size:
            not_booked.append(p)

    missing_row_cost = compute_cost(seating, prices, total_collection)
    return seating, seats_left, not_booked, missing_row_cost

def print_seating(seating):
    for row in seating:
        print("".join(str(x) if x != 0 else '_' for x in row))

def main():
    n = int(input())
    seating = [list(input().strip()) for _ in range(n)]

    groups = list(map(int, input().strip().split(',')))
    prices = list(map(lambda x: int(x) if x != '?' else x, input().strip().split()))
    total_collection = int(input())

    seating, seats_left, not_booked, missing_row_cost = book_tickets(seating, groups, prices, total_collection)

    print_seating(seating)
    print(seats_left, *not_booked)
    print(missing_row_cost)

if __name__ == "__main__":
    main()
