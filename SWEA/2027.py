# 대각선 출력

# #++++
# +#+++
# ++#++
# +++#+
# ++++#

# 문자열 초기값
str_origin = ''

for i in range(5):
  str_change = str_origin + '+'*i + '#' + '+'*(4-i)
  print(str_change)