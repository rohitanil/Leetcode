"""
Program to
    1. print all subsequences of a list
    2. print all subsequences equal to sum k
    3. check if subsequence with sum k exists
    4. count subsequences with sum k
"""


# 1
def subsequences(idx, lst, arr):
    if idx == len(arr):
        result.append(lst[:])
        return
    # Take element
    lst.append(arr[idx])
    subsequences(idx + 1, lst, arr)
    # Not take element
    lst.remove(arr[idx])
    subsequences(idx + 1, lst[:], arr)


# 2
def subsequenceSum(idx, lst, curr_sum, target, arr):
    if idx == len(arr):
        if curr_sum == target:
            result2.append(lst[:])
        return
    lst.append(arr[idx])
    curr_sum += arr[idx]
    subsequenceSum(idx + 1, lst, curr_sum, target, arr)
    lst.remove(arr[idx])
    curr_sum -= arr[idx]
    subsequenceSum(idx + 1, lst[:], curr_sum, target, arr)


# 3
def checkAnySubsequenceWithSumK(idx, curr_sum, target, arr):
    if idx == len(arr):
        if curr_sum == target:
            return True
        else:
            return False

    curr_sum += arr[idx]
    if checkAnySubsequenceWithSumK(idx + 1, curr_sum, target, arr):
        return True

    curr_sum -= arr[idx]
    if checkAnySubsequenceWithSumK(idx + 1, curr_sum, target, arr):
        return True
    return False


# 4
def countSubsequencesWithSumK(idx, curr_sum, target, arr):
    if idx == len(arr):
        if curr_sum == target:
            return 1
        else:
            return 0
    curr_sum += arr[idx]
    left = countSubsequencesWithSumK(idx + 1, curr_sum, target, arr)
    curr_sum -= arr[idx]
    right = countSubsequencesWithSumK(idx + 1, curr_sum, target, arr)
    return left + right


if __name__ == '__main__':
    result = []
    result2 = []

    inp = [1, 2, 1]
    tar = 2

    subsequences(0, [], inp)
    print("Subsequences: ", result)
    subsequenceSum(0, [], 0, tar, inp)
    print(f"Subsequences with sum {tar}: {result2}")
    print(f"Subsequences with sum {tar} present {checkAnySubsequenceWithSumK(0, 2, tar, inp)}")
    print(f"Number of subsequences with sum {tar}: {countSubsequencesWithSumK(0, 0, tar, inp)}")
