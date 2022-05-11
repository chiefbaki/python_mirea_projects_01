from re import findall

a = '{"en":"Male", "es":"Macho"}, {"en":"Female", "es":"Hembra"}, {"en":"Population", "es":"Poblacion"}'
print(';'.join(findall("[A-Z]+[a-z]*", a)))

