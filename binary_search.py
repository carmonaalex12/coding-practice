def binarySearch(arr, l, r, x):

    #base case
    if r >= l:
        mid = int(l + (r-l)/2)
        

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:

            '''
            if element is smaller than element at mid
            it can only be present in the left subarray
            '''
            return binarySearch(arr,l, mid - 1, x)

        else:
            #if element is bigger look in the right subarray
            return binarySearch(arr, mid + 1, r, x)

    else:
        #element not present in the array
        return -1



if __name__ == "__main__":
    arr = [ 2, 3, 4, 10, 40 ]
    x = 2

    print(binarySearch(arr, 0, len(arr) -1, x))
