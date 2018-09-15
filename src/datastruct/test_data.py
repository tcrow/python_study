f = open("d:/ccc.txt", "w")
try:
    for i in range(0, 10 ** 5):
        s = str(i).zfill(5) + ' ' + str(i) + ' ' + str(i + 1).zfill(5) + '\n'
        f.write(s)
finally:
    f.close()
