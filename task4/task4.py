from io import StringIO
import csv
import math

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

    vertices = []
    for x in input:
        for y in x:
            if y not in vertices:
                vertices.append(y)
    vertices.sort()
    results = [[] for _ in vertices]
    for v in vertices:
        results[int(v)-1] = [r1.count(v), r2.count(v), r3.count(v), r4.count(v), r5.count(v)]

    enthropy = 0
    for j in range(len(vertices)):
        for i in range(5):
            if results[j][i] != 0:
                enthropy += (results[j][i] / (len(vertices) - 1)) * math.log(results[j][i] / (len(vertices) - 1), 2)

    return -enthropy