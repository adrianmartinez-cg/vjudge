#Custo para transformar uma string de forma que todos os seus caracteres sejam iguais a char
def transformStr(s,l,r,char):
    count = 0
    for i in range(l,r+1):
        if s[i] != char:
            count += 1
    return count

#Funcao recursiva para calcular a quantidade minima de transformacoes
def getMinMoves(s,l,r,char):
    if l == r:
        if s[l] == char:
            return 0 
        else:
            return 1
    else:
        mid = (l + r) // 2
        nextChar = chr(ord(char)+1)

        # minimo entre transformar a metade esquerda para ser igual ao caractere, e a 
        # metade direita ser (c+1) good string OU transformar a metade direita, e a 
        # metade esquerda ser (c+1) good string
        return min(
                    transformStr(s,l,mid,char)+getMinMoves(s,mid+1,r,nextChar),
                    transformStr(s,mid+1,r,char)+getMinMoves(s,l,mid,nextChar)
                  )                                                     

#Autor: Pedro Adrian Pereira
if __name__ == "__main__":
    t = int(input())
    costs = []
    for _ in range(t):
        n = int(input())
        s = input()
        costs.append(getMinMoves(s,0,n-1,"a"))
    for cost in costs:
        print(cost)