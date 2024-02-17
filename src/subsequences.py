"""
Program to
    1. print all subsequences of a list
    2. print all subsequences equal to sum k
"""


def subsequences(idx, lst, arr):
    if idx >= len(arr):
        result.append(lst[:])
        return
    # Take element
    lst.append(arr[idx])
    subsequences(idx + 1, lst, arr)
    # Not take element
    lst.remove(arr[idx])
    subsequences(idx + 1, lst[:], arr)


def subsequenceSum(idx, lst, curr_sum, target, arr):
    if idx >= len(arr):
        if curr_sum == target:
            result2.append(lst[:])
        return
    lst.append(arr[idx])
    curr_sum += arr[idx]
    subsequenceSum(idx+1, lst, curr_sum, target, arr)
    lst.remove(arr[idx])
    curr_sum -= arr[idx]
    subsequenceSum(idx + 1, lst[:], curr_sum, target, arr)



if __name__ == '__main__':
    result = []
    result2 = []
    inp = [1, 2, 1]
    target = 2

    subsequences(0, [], inp)
    print("Subsequences: ", result)
    subsequenceSum(0, [], 0, target, inp)
    print(f"Subsequences with sum {target}: {result2}")