# python3
import sys


###############################################
############ Method I: BWMatching #############
###############################################

def LastToFirst(bwt):
  """
  return a dict s.t. given a symbol at position i in LastColumn (key), it gives
  a val of its position in FirstColumn
  """
  sorted_bwt = sorted([(b, i) for i, b in enumerate(bwt)])

  res = dict()
  for i in range(len(bwt)):
    res.update({sorted_bwt[i]: i})
  
  del sorted_bwt
  return res

def BWMatching(pattern, bwt, last_to_first):
  top, bottom = 0, len(bwt) - 1
  while top <= bottom:
    if len(pattern) > 0:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      if symbol in bwt[top:bottom+1]:
        first_pos = bwt[top:bottom+1].index(symbol)
        last_pos = len(bwt[top:bottom+1]) - list(reversed(bwt[top:bottom+1])).index(symbol) - 1
        top, bottom = last_to_first[(bwt[first_pos+top], first_pos+top)], last_to_first[(bwt[last_pos+top], last_pos+top)]
      else:
        return 0
    else:
      return bottom - top + 1

###############################################
######### Method II: BetterBWMatching #########
###############################################

def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  sorted_bwt = sorted(bwt)
  bwt_len = len(bwt)
  unq_bwt = list(set(bwt))
  starts, occ_counts_before = dict(), dict()
  for unq in unq_bwt:
    starts.update({unq: sorted_bwt.index(unq)})
    occ_counts_before.update({unq: [0]})
  for i in range(0, bwt_len):
    for unq in unq_bwt:
      if bwt[i] == unq:
        occ_counts_before[unq].append(occ_counts_before[unq][i] + 1)
      else:
        occ_counts_before[unq].append(occ_counts_before[unq][i])

  del sorted_bwt, bwt
  return starts, occ_counts_before, bwt_len

def CountOccurrences(pattern, bwt_len, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  top, bottom = 0, bwt_len - 1
  while top <= bottom:
    if len(pattern) > 0:
      symbol = pattern[-1]
      pattern = pattern[:-1]

      if (symbol in occ_counts_before) and (occ_counts_before[symbol][bottom+1] - occ_counts_before[symbol][top] > 0):
        top = starts[symbol] + occ_counts_before[symbol][top] 
        bottom = starts[symbol] + occ_counts_before[symbol][bottom+1]-1
      else:
        return 0
    else:
      return bottom - top + 1


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  


  # Method I
  # last_to_first = LastToFirst(bwt)
  # Method II
  starts, occ_counts_before, bwt_len = PreprocessBWT(bwt)

  res = []
  for p in patterns:
    # Method II
    res.append(CountOccurrences(p, bwt_len, starts, occ_counts_before))
    # Method I
    # res.append(BWMatching(p, bwt, last_to_first))
  print(' '.join(map(str, res)))
