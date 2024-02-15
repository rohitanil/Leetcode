"""
Program to print all subsequences of a list
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


if __name__ == '__main__':
    result = []
    inp = [3,2,1]
    subsequences(0, [], inp)
    print(result)
