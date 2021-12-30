import itertools as it

s_in = input()
unordered_permutation_without_repetition = set(it.permutations(s_in))
ordered_pwr = sorted(unordered_permutation_without_repetition)
result = list(map("".join, ordered_pwr))
print(len(result))
print(*result, sep='\n')
