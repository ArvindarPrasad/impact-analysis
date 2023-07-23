def Helper(n, absents_made, absents_allowed, dp):
    if absents_made == 0:
        # When this condition is true, then it means that the string formed so far is containing contiguous
        # 4 A's i.e. AAAA. Therefore, the entire string formed will be invalid, and it won't add up to our solution
        # space. So we return 0.
        return 0

    if n == 0:
        # When this condition is true, one valid string is formed. So we return 1.
        return 1

    if dp[n][absents_made] != -1:
        return dp[n][absents_made]

    # part1 is getting appended with P, not physically. Rather it denotes addition of P at end of the current string
    part1 = Helper(n - 1, absents_allowed, absents_allowed, dp)
    # part2 is getting appended with A
    part2 = Helper(n - 1, absents_made - 1, absents_allowed, dp)
    ans = part1 + part2
    dp[n][absents_made] = ans
    return ans


def Solve(N):
    """
    Solution Intuition:
          For N days, we have lets say N empty spaces to fill with either A = Absent or P = Present.
          For eg, if N = 5, valid patterns = AAPPP, APPPP, PPPPP,...  Invalid patterns = PAAAA, AAAAA, AAAAP,...
          Therefore for every cell, we have two choice either fill with P or with A, but while filling we always need to
          make sure that we never get contiguous 4 A's i.e. AAAA
    """

    absents_made = absents_allowed = 4
    dp = [[-1] * (absents_allowed + 1) for i in range(N + 1)]
    ways_to_attend_classes = Helper(N, absents_made, absents_allowed, dp)

    dp = [[-1] * (absents_allowed + 1) for i in range(N + 1)]
    # For next line, we are calling the func as such that the last character is already A of the current string
    miss_graduation_ceremony = Helper(N - 1, absents_made - 1, absents_allowed, dp)

    return str(miss_graduation_ceremony) + '/' + str(ways_to_attend_classes)


n = 5
n = 10
n = 100
print('ans:', Solve(n))
