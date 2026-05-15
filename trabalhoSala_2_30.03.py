def eh_potencia_de_dois(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

def F(n: int) -> int:
    
    if n == 1:  
        return 5
    
    metade = n // 2
    return F(metade) + 3 * F(metade)

def main():
    try:
        n = int(input("Digite um valor n |potência de 2| "))
        
        if not eh_potencia_de_dois(n):
            print("Erro: Nao é  potência de 2.")
            return
        
        resultado = F(n)
        print(f"F({n}) = {resultado}")
    
    except ValueError:
        print("Precisa ser inteiro")


if __name__ == "__main__":
    main()