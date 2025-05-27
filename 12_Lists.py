# Question Link https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    
    lista = []
    
    while (N > 0):                         
        
        comando = input().strip().split()   
        
        if (comando[0] == "insert"):        
            posicao = int(comando[1])       
            valor = int(comando[2])       
            
            lista.insert(posicao, valor)    
            
        elif (comando[0] == "print"):          
            print(lista)                    
        
        elif (comando[0] == "remove"):        
            valor = int(comando[1])        
            lista.remove(valor)             
        
        elif (comando[0] == "append"):
            valor = int(comando[1])
            lista.append(valor)
            
        elif (comando[0] == "sort"):
            lista.sort()
            
        elif (comando[0] == "pop"):
            lista.pop()
            
        elif (comando[0] == "reverse"):
            lista.reverse()
            
        else:
            print ("Comando nao encontrado")   
        
        N -= 1                              #diminuindo o N para fazer as vezes exatas