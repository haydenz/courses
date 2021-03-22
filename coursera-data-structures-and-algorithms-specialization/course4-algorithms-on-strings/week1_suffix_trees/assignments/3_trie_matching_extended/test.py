import numpy as np
import datetime as dat
from trie_matching_extended import solve

def random_string(chars,n):
  return ''.join(np.random.choice(chars) for _ in range(n))      
      
def gen(chars,textn,pattn):
    text = random_string(chars,textn)
    patterns = []
    for i in range(pattn):
        patterns.append(random_string(chars,np.random.randint(1,textn)))
    return (text, patterns)
  
def BruteForce(text,patterns,silent=True):
  ids = []
  n = len(text)
  for p in patterns:
    plen = len(p)
    for i in range(n-plen+1):
      if (text[i:(i+plen)] == p):
        if not(silent):
          print('Found %s at %d'%(p,i))
        ids.append(i)
  return ids

def testme(text,patterns,silent):
  print('---Brute Force')
  stt = dat.datetime.now()
  BFids = BruteForce(text,patterns,silent)
  print('--Execution time: %s'%(dat.datetime.now()-stt))
  BFids = np.unique(BFids).tolist()
  print('---Trie Ext')
  # YOUR CODE TO CALL THE EXTENDED TRIE MATCHING GOES HERE
  # IT SHOULD RETURN A LIST OF INDICES
  TEids = solve(text, len(patterns), patterns)
  TEids = np.unique(TEids).tolist()  
  print('--Execution time: %s'%(dat.datetime.now()-stt))
  print('BF: %r\nTE: %r'%(BFids,TEids))
  if (BFids != TEids):
    print('Difference Found!')
  else:
    print('NO Difference(s) Found!')

if __name__ == '__main__':
    text, patterns = gen(list('acgt'), 7, 5)
    testme(text,patterns,True)