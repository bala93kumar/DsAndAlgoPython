

def printData(arr,top , bottom, left , right):



    if not arr or not len(arr) or left > right :
        return

    # while True:


    for i in range(top,right+1):
        print(arr[top][i],end=' ')

    top +=1

    for j in range(top, bottom+1):
        print(arr[j][right],end=' ')

    right -= 1

    for k in range(right , left - 1,-1):
        print(arr[bottom][k],end=' ')

    bottom -= 1

    for l in range(bottom,top -1 , -1):
        print(arr[l][left],end=' ')

    left += 1

    printData(arr,top , bottom , left, right)


if __name__ == '__main__':
    a = [[1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18]]


    top  = 0
    bottom = len(a) - 1
    left = 0
    right = len(a[0]) - 1

    printData(a,top , bottom,left , right)