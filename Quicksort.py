def swap(arr, left,right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left = left + 1
        while arr[right] > pivot:
            right = right - 1
        if left <= right:
            swap(arr, left, right)
            left = left + 1
            right = right - 1
    return left


def quickSort(arr, left, right):

    if left >= right:
        return

    pivot = arr[int((left + right) /2)]
    index = partition(arr, left, right, pivot)
    quickSort(arr, left, index - 1)
    quickSort(arr, index, right)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5, 47, 2, 5, 6,8, 90, 24, 16]
    n = len(arr)
    print(arr)
    print("After Quicksort")
    quickSort(arr, 0, n-1)
    print(arr)
