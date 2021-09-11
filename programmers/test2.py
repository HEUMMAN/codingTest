def solution(n, k):
    prime = []
    answer = []
    num = make_n_binary(k, n)
    make_numbers(num, prime)

    print(prime)
    for p in prime:
        if p == '':
            pass
        elif p == '2':
            answer.append(p)
        else:
            if is_prime_number(int(p)):
                answer.append(p)
    return len(answer)


def make_numbers(num, prime):
    for i in range(len(num)):
        if num[i] == '0':
            if len(prime) < 1:
                prime.append(num[:i])
                num = num[i:]
                break

    for i in range(len(num)):
        if num[i] == '0':
            for j in range(i + 1, len(num)):
                if j == len(num) - 1:
                    prime.append(num[i+1:])
                    break

                elif num[j] == '0':
                    prime.append(num[i + 1:j])
                    break


def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


def make_n_binary(k, n):
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    base = base[::-1]
    return base


solution(437674, 3)
solution(110011, 10)