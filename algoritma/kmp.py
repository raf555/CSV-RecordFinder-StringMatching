# referensi algoritma
# https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2020-2021/Pencocokan-string-2021.pdf

def computeFail(pattern):
  fail = [0 for i in range(len(pattern))]
  
  m = len(pattern)
  j = 0
  i = 1

  while i < m:
    if pattern[j] == pattern[i]:
      fail[i] = j + 1
      i += 1
      j += 1
    else:
      if j > 0:
        j = fail[j-1]
      else:
        fail[i] = 0
        i += 1
  
  return fail

def KMPSearch(string, pattern):
  n = len(string)
  m = len(pattern)

  fail = computeFail(pattern)

  i = 0
  j = 0

  while i < n:
    if pattern[j] == string[i]:
      if j == m-1:
        return i - m + 1
      j += 1
      i += 1
    
    else:
      if j > 0:
        j = fail[j-1]
      else:
        i += 1
  
  return -1
