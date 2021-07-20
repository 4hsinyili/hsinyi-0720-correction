def solution(N):
    # Correction 1: if N == 0, program should return 1 instead of 0
    if N == 0:
        return 1
    elif N == 1:
        return 2
    elif N == 2:
        return 2

    init_layer = [1, 2, 1]
    loop_count = 2

    while loop_count < N:
        final_layer = [1]
        for index in range(len(init_layer)):
            if index == len(init_layer) - 1:
                final_layer.append(1)
                break
            final_layer.append(init_layer[index] + init_layer[index + 1])
        init_layer = final_layer
        loop_count += 1

    def extract_first(carry, ans):
        while carry > 0:
            remainder = carry % 10
            if remainder == 1:
                ans += 1
            carry = (carry - remainder) // 10
        return False, 0, ans

    def loop(carry, arr, ans):
        right = arr.pop()
        right += carry
        if right == 1:
            ans += 1
        elif right > 9:
            remainder = right % 10
            if remainder == 1:
                ans += 1
            # Correction 2: use "//" instead of "/", to avoid unstable float.
            carry = (right - remainder) // 10

        if len(arr) == 0:
            # Correction 3: build a function to deal with first digit's carry.
            return extract_first(carry, ans)
        else:
            return True, carry, ans

    check = True
    carry = 0
    ans = 0
    while check:
        check, carry, ans = loop(carry, final_layer, ans)
    return ans


def wrong_solution(N):
    # Fault 1: return 0 when N is 0, 11**0 should be 1
    if N == 0:
        return 0
    elif N == 1:
        return 2
    elif N == 2:
        return 2

    init_layer = [1, 2, 1]
    loop_count = 2

    while loop_count < N:
        final_layer = [1]
        for index in range(len(init_layer)):
            if index == len(init_layer) - 1:
                final_layer.append(1)
                break
            final_layer.append(init_layer[index] + init_layer[index + 1])
        init_layer = final_layer
        loop_count += 1

    ans = 0

    def loop(prev, arr, ans):
        right = arr.pop()
        right += prev
        carry = 0
        if right == 1:
            ans += 1
        elif right > 9:
            remainder = right % 10
            if remainder == 1:
                ans += 1
            # Fault 2: "/" will return float, it is unstable in python
            #          like int((956367673263128722 - 2) / 10) will be 95636767326312864
            carry = (right - remainder) / 10

        if len(arr) == 0:
            # Fault 3: forgot to deal with first digit's carry
            return False, carry, ans
        else:
            return True, carry, ans

    check = True
    carry = 0
    while check:
        check, carry, ans = loop(carry, final_layer, ans)

    return ans


test = 300

print(solution(300))
print(wrong_solution(300))
