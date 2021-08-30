def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    print(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False

    return True


solution(["123","45612","78129", "13354", "12574", "1373", "16358"])