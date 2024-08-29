def coletar_informacoes_pet():
    nome = input("Nome do pet: ")

   idade = int(input("Idade do pet (em anos): "))
   while idade < 0:
        print("A idade não pode ser negativa. Tente novamente.")
        idade = int(input("idade do pet( em anos): "))
                
   peso = float(input("Peso do pet(em kg): "))
   while peso < 0:
        print("O peso não pode ser negativo. Tente novamente.")
        peso = float(input("Peso do pet(em kg): "))
            
        # Print da Michelle
        print(f"\nInformações do pet:\nNome: {nome}\nIdade: {idade} anos\nPeso: {peso} kg")
    # Print da Thayse
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

coletar_informacoes_pet()
