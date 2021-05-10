import re

def RESearch(string, pattern):
  out = re.search(pattern, string)
  
  if out is None:
    out = -1

  return out