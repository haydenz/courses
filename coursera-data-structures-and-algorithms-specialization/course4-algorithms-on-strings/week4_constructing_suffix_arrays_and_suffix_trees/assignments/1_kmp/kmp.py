# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  res = []
  # Implement this function yourself
  if len(pattern) > len(text): return res
  st = pattern + '$' + text
  s = [0] * len(st)
  b = 0
  for i in range(1, len(st)):
    while b > 0 and st[i] != st[b]:
      b = s[b - 1]
    if st[i] == st[b]:
      b += 1
    else:
      b = 0
    s[i] = b
    if s[i] == len(pattern):
      res.append(i - 2 * len(pattern))
  return res


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

