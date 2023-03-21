with open("complete_genome_list.txt", 'r') as file1, open("list", 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

difference = []

for line in lines1:
    if line not in lines2:
        difference.append(line.strip())

for item in difference:
    print(item)

