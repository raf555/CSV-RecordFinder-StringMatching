import csv
from time import time
from algoritma.kmp import KMPSearch
from algoritma.bm import BMSearch
from algoritma.regex import RESearch

def start(showtime = True):
  filename = input("Masukkan nama fail dan direktori jika ada: ")

  try:
    file = open(filename, "r")
  except:
    print("Fail tidak ditemukan")
    return
  
  proceed(file)

  file.close()

def proceed(file):
  tablestring = csvTostring(file)

  algo, cs, pattern = askinput()
  
  if algo == "kmp":
    algorithm = KMPSearch
  elif algo == "bm":
    algorithm = BMSearch
  elif algo == "regex":
    algorithm = RESearch
  
  result, deltatime = findRecord(tablestring, cs, pattern, algorithm)

  print()
  print("==================HASIL==================")
  print("indeks - [field]")
  if len(result) == 0:
    print ("Tidak ditemukan kecocokan pada record manapun")
  else:
    for string in result:
      print (string)
  print("=========================================")
  
  print("\nMenghabiskan "+str(deltatime)+" detik")

def findRecord(table, cs, pattern, algorithm):
  out = []
  now = time()

  for i, data in enumerate(table):
    if cs == "y":
      string = data
      pola = pattern
    else:
      string = data.lower()
      pola = pattern.lower()
    
    if algorithm(string, pola) != -1:
      out.append(str(i) + " - " + data)
  
  return out, round(time()-now, 5)

def askinput():
  algo = input("Pilih algoritma yang akan digunakan (kmp/bm/regex): ")
  cs = input("Apakah case sensitive? (y/n): ")
  pattern = input("Masukkan pattern: ")

  return algo, cs, pattern

def csvTostring(file):
  reader = csv.DictReader(file)
  out = []
  
  for row in reader:
    string = ""
    for i, field in enumerate(row):
      if i != 0:
        string += " - "
      
      string += row[field]
    out.append(string)
  
  return out