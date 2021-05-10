# referensi algoritma
# https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2020-2021/Pencocokan-string-2021.pdf

def lastOccurence(pattern):
  last = {} #dictionary

  for idx, huruf in enumerate(pattern):
    last[huruf] = idx
  
  return last

def BMSearch(string, pattern):
  last = lastOccurence(pattern)
  n = len(string)
  m = len(pattern)
  i = m-1

  if i > n-1:
    return -1

  j = m-1

  while i <= n-1:
    if pattern[j] == string[i]:
      if j == 0:
        return i
      else:
        # looking glass
        i -= 1
        j -= 1
    else:
      try:
        lo = last[string[i]]
      except:
        lo = -1
      
      i += m - min(j, 1+lo)
      j = m - 1

  return -1