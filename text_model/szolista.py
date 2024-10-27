f = open('training.txt','r', encoding='utf-8')
szolista = {}
kifejezesek = []

for line in f:
    for word in line.split():
        word = word.lower().strip('.;,-“’”:?—‘!()_')
        kifejezesek.append(word)
        if len(kifejezesek) == 3:
            kifejezes = (kifejezesek[0],kifejezesek[1])
            folytatas = kifejezesek[2]
            if kifejezes in szolista:
                szolista[kifejezes].append(folytatas)
            else:
                szolista[kifejezes]=[folytatas]
            kifejezesek.pop(0)
