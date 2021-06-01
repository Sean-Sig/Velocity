def solution(a=list):
    count = 0
    if len(a) < 3:
        return 0

    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            if a[j + 1] - a[j] == a[i + 1] - a[i]:
                count += 1
            else:
                break
    return count if count < 1000000000 else -1


if __name__ == '__main__':
    print(solution(a=[1, 3, 5, 7, 9]))
    print(solution(a=[7, 7, 7, 7]))
    print(solution(a=[3, -1, -5, -9]))
    print(solution(a=[0, 1]))
    print(solution(a=[1, 1, 2, 5, 7]))
    print(solution(a=[-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))
