
with open('charles.txt', 'r', encoding='utf8') as filel:
    fileLines = filel.readlines()
    print(len(fileLines))
    print(fileLines)

with open('randtext.txt', 'w', encoding='utf8') as filel:
    listl = ['cadena1', 'cadena2', 'cadena3']
    for line in listl:
        filel.write(line)
        filel.write('\n')