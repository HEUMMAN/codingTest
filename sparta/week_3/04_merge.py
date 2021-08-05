array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array3 = []
    while len(array1) != 0 and len(array2) != 0:
        if array1[0] > array2[0]:
            array3.append(array2[0])
            array2.pop(0)
        elif array1[0] < array2[0]:
            array3.append(array1[0])
            array1.pop(0)
        else:
            array3.append(array1[0])
            array1.pop()
            array2.pop()

        if len(array1) == 0:
            for i in range(len(array2)):
                array3.append(array2[i])

        elif len(array2) == 0:
            for i in range(len(array1)):
                array3.append(array1[i])


    return array3


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!