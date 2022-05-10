n = int(input(""))  # 입력


def fectorial(x):
    sum = 1
    for i in range(1, x + 1):
        sum *= i

    return sum


for i in range(n):  # sub number 입력 받는 곳
    sub_n = int(input(""))
    cnt = 0

    for j in range(sub_n, -1, -1):  # 1이 n개일 때 부터 시작.
        one = j

        two = (sub_n - j) // 2  # 2는 n - 1의 수 //2

        for t in range(two - 1, -1, -1):  # 2가 2개 이상일 경우 ex 2가 3개인 경우는 3x2를 만들수도 있으므로
            th = (sub_n - j - t * 2)  # 3은 1과 2 더한거 모두 빼고 남은거
            if th % 3 == 0:  # 2가 2개 이상일 때 3이 될 조건
                nnn = fectorial(one + t + (th // 3)) // (fectorial(one) * fectorial(t) * fectorial(th // 3))
                # 중복 순열 aaabb가 있을 때 총 5개 이므로 5! // a 3개 이므로 3!, b가 2개 이므로 2! -> 5!/2!x3! 과같으므로
                cnt += nnn

        three = ((sub_n - j - (two * 2)) // 3)

        if (one + two * 2 + three * 3) != sub_n:
            continue

        nnn = fectorial(one + two + three) // (fectorial(one) * fectorial(two) * fectorial(three))
        cnt += nnn

    print(cnt)

n = int(input(""))  # 입력


def fectorial(x):
    sum = 1
    for i in range(1, x + 1):
        sum *= i

    return sum


for i in range(n):  # sub number 입력 받는 곳
    sub_n = int(input(""))
    cnt = 0

    for j in range(sub_n, -1, -1):  # 1이 n개일 때 부터 시작.
        one = j

        two = (sub_n - j) // 2  # 2는 n - 1의 수 //2

        for t in range(two - 1, -1, -1):  # 2가 2개 이상일 경우 ex 2가 3개인 경우는 3x2를 만들수도 있으므로
            th = (sub_n - j - t * 2)  # 3은 1과 2 더한거 모두 빼고 남은거
            if th % 3 == 0:  # 2가 2개 이상일 때 3이 될 조건
                nnn = fectorial(one + t + (th // 3)) // (fectorial(one) * fectorial(t) * fectorial(th // 3))
                # 중복 순열 aaabb가 있을 때 총 5개 이므로 5! // a 3개 이므로 3!, b가 2개 이므로 2! -> 5!/2!x3! 과같으므로
                cnt += nnn

        three = ((sub_n - j - (two * 2)) // 3)

        if (one + two * 2 + three * 3) != sub_n:
            continue

        nnn = fectorial(one + two + three) // (fectorial(one) * fectorial(two) * fectorial(three))
        cnt += nnn

    print(cnt)

