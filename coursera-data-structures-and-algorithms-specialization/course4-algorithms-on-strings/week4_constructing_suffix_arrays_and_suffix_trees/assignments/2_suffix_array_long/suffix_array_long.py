# python3
import sys

class Suffix:

  def __init__(self):
    self.index = 0
    self.rank = [0, 0]

def buildSuffixArray(text, n):
  suf = [Suffix() for _ in range(n)]

  for i in range(n):
    suf[i].index = i
    suf[i].rank[0] = (ord(text[i]) - ord("a"))
    suf[i].rank[1] = (ord(text[i + 1]) - ord("a")) if ((i + 1) < n) else -1

  suf = sorted(suf, key=lambda x: (x.rank[0], x.rank[1]))

  ind = [0] * n
  k = 4
  while (k < 2 * n):
    rank = 0
    prev_rank = suf[0].rank[0]
    suf[0].rank[0] = rank
    ind[suf[0].index] = 0

    for i in range(1, n):
      if (suf[i].rank[0] == prev_rank and
              suf[i].rank[1] == suf[i - 1].rank[1]):
        prev_rank = suf[i].rank[0]
        suf[i].rank[0] = rank
      else:
        prev_rank = suf[i].rank[0]
        rank += 1
        suf[i].rank[0] = rank
      ind[suf[i].index] = i

    for i in range(n):
      nextindex = suf[i].index + k // 2
      suf[i].rank[1] = suf[ind[nextindex]].rank[0] if (nextindex < n) else -1

    suf = sorted(suf, key=lambda x: (x.rank[0], x.rank[1]))
    k *= 2

  return [s.index for s in suf]


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, buildSuffixArray(text, len(text)))))
