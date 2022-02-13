def verificaExpressoes(lista):
    x = json.loads(lista)
    y = x['x']
    cont = 0
    for i in y:
        a = i['texto']


        if '.' in a:
            b = a.split('.')
            cont += 1
            print(b)



        elif '?' in a:
            if cont == 1:
                c = a.split('?')
                for i in c:
                    if i not in b:
                        cont += 2
                        b.append('///')
                        b.append(i)
                        print(b)
            else:
                c = a.split('?')
                cont += 2
                print(c)



        elif '!' in a:
            if cont == 0:    #não possui . ou ?
                cont += 7
                d = a.split('!')
                print(d)
            if cont == 1:              #possuía . e foi criada a lista sem
                e = a.split('!')
                for i in e:
                    if i not in b:
                        cont += 3
                        b.append('///')
                        b.append(i)
                        print(b)
            if cont == 2:              #possuía ? e foi criada a lista sem
                f = a.split('!')
                for i in f:
                    if i not in c:
                        cont += 3
                        c.append('///')
                        c.append(i)
                        print(c)
            if cont == 3:                 #possuía . e ? e foi criada a lista sem
                g = a.split('!')
                for i in g:
                    if i not in b and not in c:
                        cont += 3
                        b.append('///')
                        b.append(i)
                        print(b)
