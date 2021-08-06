s = "(())()"


def is_correct_parenthesis(string):
    arr = []
    for i in range(len(string)):
        if string[i] == '(':
            arr.append(string[i])
        else:
            if len(arr) == 0:
                return False
            else:
                arr.pop()

    if len(arr) != 0:
        return False
    else:
        return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
