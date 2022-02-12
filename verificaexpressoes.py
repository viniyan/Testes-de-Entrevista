import json

lista = ''' {"x": [{"id": 1, "texto": "Em primeiro lugar, a forma atual de ensino, em que o aluno é obrigado a sentar-se em intervalos determinados pelos superiores, forma os adultos que levam essa forma de produção para o ofício. Logo, baseado no que foi dito, vale citar o filósofo Pitágoras, que explica que é melhor educar bem as crianças do que ter que reeducá-las como adultos. Assim, os maus hábitos adquiridos na infância podem gerar, nos adultos, muitas complicações, já que dentro da sala de aula, a movimentação dos alunos pelo ambiente é repudiada e muitas vezes com consequências. Como consequência, a doutrinação do modelo educacional não atende aos paradigmas de formação de um adulto atento à saúde ocupacional."},
{ "id": 4, "texto": "Perante os argumentos citados, é alarmante o número de indivíduos que crescem traumatizados, muitas vezes sem tratamento adequado, durante ou após a infância, desenvolvendo uma realidade de mundo inquietante. Por conseguinte, é relevante adicionar que, sendo a cultura - associada às relações e experiências de vida do cidadão - um meio pelo qual se cria a construção da realidade na consciência dos jovens, a realidade que está sendo criada pelas vítimas pode refletir na decadência da sociedade brasileira, em termos de segurança, educação e até cultural."}]}'''

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
            else:
                c = a.split('?')
                cont += 2
                print(c)



        elif '!' in a:
            if cont == 0:              #não possui . ou ?
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
            if cont == 2:              #possuía ? e foi criada a lista sem
                f = a.split('!')
                for i in f:
                    if i not in c:
                        cont += 3
                        c.append('///')
                        c.append(i)
            if cont == 3:                 #possuía . e ? e foi criada a lista sem
                g = a.split('!')
                for i in g:
                    if i not in b:
                        cont += 3
                        b.append('///')
                        b.append(i)
