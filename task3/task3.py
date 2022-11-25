from io import StringIO
import csv

def task(csvString):
  f = StringIO(csvString)
  reader = csv.reader(f, delimiter=',')
  input = []
  for row in reader:
    input.append(row)
  
  r1, r2, r3, r4, r5 = [], [], [], [], []

  def direct(index, storage):
    for row in input:
      if row[index] not in storage:
        storage.append(row[index])

  direct(0, r1)
  direct(1, r2)

  def indirect(firstIndex, secondIndex, storage):
    for row in input:
      for nextRow in input:
        if row[firstIndex] not in storage and nextRow[firstIndex] == row[secondIndex]:
          storage.append(row[firstIndex])
  
  indirect(0, 1, r3)
  indirect(1, 0, r4)

  for row in input:
      for nextRow in input:
        if row[1] not in r5 and nextRow[0] == row[0] and nextRow != row:
          r5.append(row[1])

  return [r1, r2, r3, r4, r5]
