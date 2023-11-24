import itertools

def generate_permutations(length):
    alphabets = [chr(ord('a') + i) for i in range(26)]
    all_permutations = list(itertools.permutations(alphabets, length))
    sorted_permutations = sorted(all_permutations)
    return sorted_permutations

def find_string(rank, length):
    sorted_permutations = generate_permutations(length)
    required_permutation = sorted_permutations[rank-1]
    return ''.join(required_permutation)


rank_input = int(input())
length_input = int(input())

result_output = find_string(rank_input, length_input)
print(result_output)
