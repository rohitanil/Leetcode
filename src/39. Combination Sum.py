def subsequenceWithSumK(idx, target, arr, lst):
    if idx == len(arr):
        if target == 0:
            result.append(lst[:])
        return
    if arr[idx] <= target:
        lst.append(arr[idx])
        subsequenceWithSumK(idx, target - arr[idx], arr, lst)
        lst.remove(arr[idx])
    subsequenceWithSumK(idx + 1, target, arr, lst)


def combinationSum(arr, tar):
    subsequenceWithSumK(0, tar, arr, [])
    return result


if __name__ == '__main__':
    result = []
    candidates = [2, 3, 5]
    aim = 8
    print(combinationSum(candidates, aim))
