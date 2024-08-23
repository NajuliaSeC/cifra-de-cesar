while True:
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    menu = """
        ============MENU============
        (1) Cifrar
        (2) Decifrar
        (3) Sair
        """
    print (menu)
    opcao=input("Digite a opcao que deseja realizar: ")
    frase_final = ""
    try:
        if opcao == "1":
            frase = input("Digite uma frase: ").lower()
            for letra in frase:
                if letra in alfabeto: 
                    posicao = alfabeto.index(letra)
                    nova_posicao = (posicao + 3) % 26
                    frase_final += alfabeto[nova_posicao]
                else:
                    frase_final += letra  
            print("Frase cifrada:", frase_final)
        
        elif opcao == "2":
            frase = input("Digite uma frase: ").lower()
            for letra in frase:
                if letra in alfabeto:  
                    posicao = alfabeto.index(letra)  
                    nova_posicao = (posicao - 3) % 26  
                    frase_final += alfabeto[nova_posicao]  
                else:
                    frase_final += letra 
            print("Frase decifrada:", frase_final)
        elif opcao == "3":
                break
        else:
            print ("Opção inválida") 
            
                
            
    except ValueError:
        print ("Digite uma das opções acima, por favor")
