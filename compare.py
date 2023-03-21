import sys

with open('test.txt', 'r') as f:
    for line in f:
        fields = line.split()
        if fields[0] != fields[1]:
            sys.stdout.write(line)
