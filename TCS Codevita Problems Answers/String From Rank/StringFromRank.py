def find_string(rank, length):
    import math
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    while length > 0:
        q, r = divmod(rank - 1, math.factorial(length-1))
        result += alphabets[q % len(alphabets)] 
        alphabets = alphabets[:q] + alphabets[q+1:]
        rank = r + 1
        length -= 1
    return result

rank_input = int(input())
length_input = int(input())

result_output = find_string(rank_input, length_input)
print(result_output)