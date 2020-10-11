"""백준 1000번 문제"""

import sys

def invalid_range(_n):
    """주어진 int의 범위가 틀린지 확인."""
    return not 0 < _n < 10

A, B = map(int, input().split())
if invalid_range(A) or invalid_range(B):
    sys.exit('입력값이 올바르지 않습니다.')
print(A+B)
