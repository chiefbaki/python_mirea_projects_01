def wiki():
    with open("text.txt") as f:
        text = ''.join(filter(lambda s: s.isalpha() or s.isspace(), ' '.join([line.strip() for line in f])))
 
    di = {}
    for word in text.split():
        di[word] = di.get(word, 0) + 1
 
    common = []
    d_list = sorted(list(di.items()), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print("{} place --- {d[0]} --- {d[1]} times".format(i + 1, d=d_list[i]))
        common.append(d_list[i][0])
 
    f_text = []
    s = ''
 
    for word in text.split():
        if word in common:
            word = 'PYTHON'
        if len(s + word) < 100:
            s = s + word + " "
        else:
            f_text.append(s)
            s = word + " "
 
    with open('out.txt', 'w') as f:
        for line in f_text:
            f.write(line + '\n')
