sample_array = [8, 7, 2, 5, 3, 1]
find_sum = 10


# Naive Approach ==> 0(n^2)

def find_pair_naive(sample_array, find_sum):
    indexes = list()
    for i in range(len(sample_array)):
        for j in range(i + 1, len(sample_array)):
            if sample_array[i] + sample_array[j] == find_sum:
                indexes.append([i, j])
    return indexes


def find_pair_hashing(sample_array, find_sum):
    indexes = list()
    sample_dict = dict()
    for i in range(len(sample_array)):
        if (find_sum - sample_array[i]) in sample_dict:
            indexes.append([i, sample_dict[find_sum - sample_array[i]]])
        else:
            sample_dict[sample_array[i]] = i
    return indexes


print(find_pair_naive(sample_array, find_sum))
print(find_pair_hashing(sample_array, find_sum))
