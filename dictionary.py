kind = int(input('''알파벳이 몇번째 인지 : 1
몇번째가 무슨 알파벳인지 : 2
번호를 입력해주세요:'''))
def factoriar(a):
    if a == 0:
        return 1
    else:
        result = 1
        for i in range(a):
            result *= (i+1)
        return result
def front_number(arrangement):
    NB = len(arrangement)
    for i in range(NB):
        arrangement[i] -=1
        for j in range(i):
            if arrangement[j] < arrangement[i]:
                arrangement[i] -= 1
if kind == 1:
    ranking = 1
    result = 0
    arrangement = list(input('''========================
알파벳을 입력해 주세요
:'''))
    number_arrangement = []
    for i in range(len(arrangement)):
        number_arrangement.append(0)

    for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        for j in range(len(arrangement)):
            if arrangement[j] == i:
                number_arrangement[j] += ranking
                ranking += 1
    front_number(number_arrangement)
    for i in range(len(number_arrangement)):
        result += number_arrangement[i]*(factoriar(len(number_arrangement) - i -1))
    print('========================')
    print(result+1,'번째 입니다.')
elif kind == 2:
    alphabet_kind = list(input('''사용하는 알파벳을 입력해 주세요.
:'''))
    alphabet_kind.sort()
    NB = int(input('''몇번째 배열을 구할지 입력해 주세요.
:'''))-1
    number = len(alphabet_kind)
    result = []
    for i in range(number):
        a = NB // factoriar(number - i-1)
        result.append(a)
        NB -= a* factoriar(number - i-1)
    true_result = []
    k = len(alphabet_kind)
    for i in range(k):
        true_result.append(alphabet_kind[result[i]])
        alphabet_kind.pop(result[i])
    print('====================')
    print(str(true_result))