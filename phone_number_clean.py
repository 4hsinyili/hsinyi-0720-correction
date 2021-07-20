def solution(S):
    tmp = []
    length = len(S)
    loop_count = 1

    for index in range(length):
        char = S[index]
        if char != ' ' and char != '/' and char != '-':
            tmp.append(str(char))
            if loop_count % 3 == 0:
                tmp.append('-')
            loop_count += 1

    if tmp[-2] == '-':
        tmp[-2], tmp[-3] = tmp[-3], tmp[-2]
    # Correction: leave this condition outside of for-loop, maybe ugly, but safer.
    if tmp[-1] == '-':
        tmp.pop()

    ans = ''.join(tmp)

    return ans


def wrong_solution(S):
    tmp = []
    length = len(S)
    loop_count = 1

    for index in range(length):
        char = S[index]
        if char != ' ' and char != '/' and char != '-':
            tmp.append(str(char))
            # Fault: loop_count will always less than length, so the condition won't work as I thought.
            if (loop_count % 3
                    == 0) and (loop_count < length) and (loop_count > 1):
                tmp.append('-')
            loop_count += 1

    if tmp[-2] == '-':
        tmp[-2], tmp[-3] = tmp[-3], tmp[-2]

    ans = ''.join(tmp)

    return ans


test = '12345-6'

print(solution(test))
print(wrong_solution(test))
