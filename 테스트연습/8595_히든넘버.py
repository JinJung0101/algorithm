# n = int(input())
# text = list(input())
# nums = set('0123456789')
# ans = []
# for t in text:
#     if t in nums:
#         ans.append(t)
#     else:
#         ans.append(' ')

# print(sum(list(map(int, ''.join(ans).split()))))

import re

n = int(input())
text = input()
# 정규표현식을 사용하여 숫자만 찾아 리스트로 만듭니다.
nums = re.findall('\d+', text)
print(nums)
# 리스트 컴프리헨션을 사용하여 숫자들을 int로 변환하고 합합니다.
print(sum(int(num) for num in nums))

