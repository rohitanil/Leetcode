def subsequenceWithSumK(idx, curr_sum,target, arr, lst):
    if idx == len(arr):
        if curr_sum == target:
            result.append(lst[:])
        return
    if curr_sum <= target:
        curr_sum += arr[idx]
        lst.append(arr[idx])
        subsequenceWithSumK(idx, curr_sum,target, arr, lst)
        curr_sum -= arr[idx]
        lst.remove(arr[idx])
    subsequenceWithSumK(idx + 1, curr_sum,target, arr, lst)


def combinationSum(arr, tar):
    subsequenceWithSumK(0, 0, tar, arr, [])
    return result


if __name__ == '__main__':
    result = []
    candidates = [2, 3, 5]
    aim = 8
    print(combinationSum(candidates, aim))
