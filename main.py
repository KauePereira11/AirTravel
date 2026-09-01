import os
os.system('cls')

def exibir_nome_do_programa():
  print("=================")
  print(" ✈  AIR TRAVEL ")
  print("=================")

usuarios = [ ['kaue@gmail.com', '12345', '777', '1199999'],
            ['erica@gmail.com', '1234', '666', '1197777']
]

destinos_pacotes = ["Miami - EUA",
                    "Nova York - EUA",
                    "Washington, D.C. - EUA",
                    "Madrid - Espanha",
                    "Barcelona - Espanha",
                    "Paris - França",
                    "Nice - França"]

info_pacotes = [["Miami - The Betsy - South Beach", 7500],
                ["Miami - Loews Miami Beach Hotel", 8200],
                ["Miami - Fontainebleau Miami Beach", 9500],

                ["Nova York - New York Marriott Marquis", 8500],
                ["Nova York - The Times Square EDITION", 9200],
                ["Nova York - Hyatt Centric Times Square Nova York", 7900],

                ["Washington, D.C. - The Mayflower Hotel", 7800],
                ["Washington, D.C. - Washington Hilton", 7200],
                ["Washington, D.C. - The Westin Georgetown", 8000],

                ["Madrid - JW Marriott Hotel Madrid", 7300],
                ["Madrid - Hotel Montera Madrid", 6800],
                ["Madrid - Meliá Castilla", 6500],

                ["Barcelona - Hotel ILUNION Barcelona", 6700],
                ["Barcelona - Hotel Acevi Villarroel", 6300],
                ["Barcelona - AC Hotel Diagonal L'Illa", 7000],

                ["Paris - Le Bristol Paris", 12000],
                ["Paris - The Peninsula Paris", 11500],
                ["Paris - Mandarin Oriental Paris", 10800],

                ["Nice - Hôtel Negresco", 8500],
                ["Nice - Le Méridien Nice", 7500],
                ["Nice - Hôtel Aston La Scala", 6800],

                ["Londres - The Savoy", 11000],
                ["Londres - The Ritz London", 12500],
                ["Londres - Shangri-La The Shard", 11800],

                ["Lisboa - Four Seasons Hotel Ritz Lisbon", 9000],
                ["Lisboa - Corinthia Lisbon", 7500],
                ["Lisboa - Tivoli Avenida Liberdade Lisboa", 8000],

                ["Cancún - Hyatt Ziva Cancun", 9000],
                ["Cancún - JW Marriott Cancun Resort & Spa", 9500],
                ["Cancún - NIZUC Resort & Spa", 11000],

                ["Roma - Hotel de Russie", 11000],
                ["Roma - Rome Cavalieri", 9500],
                ["Roma - Hotel Eden", 12000],

                ["Amsterdã - Waldorf Astoria Amsterdam", 12000],
                ["Amsterdã - Hotel Okura Amsterdam", 9500],
                ["Amsterdã - Kimpton De Witt Amsterdam", 8000],

                ["Oslo - The Thief", 10000],
                ["Oslo - Grand Hotel Oslo", 8500],
                ["Oslo - Radisson Blu Plaza Hotel Oslo", 7500],

                ["Berlim - Hotel Adlon Kempinski Berlin", 11000],
                ["Berlim - The Ritz-Carlton Berlin", 10000],
                ["Berlim - Hilton Berlin", 7500],

]

def cadastrar_novo_usuario():
   os.system('cls')
   print('Novo Cadastro.')
   email = input("Email: ")
   senha = input("Senha: ")
   cpf = input("CPF: ")
   telefone = input("Telefone: ")

   usuarios.append([email, senha, cpf, telefone])

   print("Cadastro realizado!")
   input('Digite uma tecla para voltar ao inicio.')

def listar_usuarios():
   os.system('cls')
   print('Usuarios cadastrado:')

   for usuario in usuarios:
      print(f".{usuario}")


   input('\nDigite uma tecla para voltar ao inicio.')

def exibir_opcoes():
  print()
  print("1 - Criar Conta: ")
  print("2 - Fazer Login: ")
  print("3 - Usuarios cadastrado: ")
  print("4 - Sair :")

def seleciona_opcao():
   try:
      print()
      opcao = int(input('Escolha uma opção: '))

      if opcao == 1:
         cadastrar_novo_usuario()
         

      elif opcao == 2:
         email = input("Email: ")
         senha = input("Senha: ")

         encontrou = False

         for usuario in usuarios:
            
            if email == usuario[0] and senha == usuario[1]:
               print('Login encontrado!')
               usuario_logado = usuario
               encontrou = True
               menu_usuario(usuario_logado)
               

         if encontrou == False:
            print("Email ou senha incorretos.")
         
      elif opcao == 3:
         print(listar_usuarios())
         listar_usuarios()
         usuarios[3]

      else:
         print('Obrigado por usar o Air Travel.')   
   except ValueError:
      input("\nEste número não é valido")
      return seleciona_opcao()
  
def menu_usuario(usuario_logado):
   while True:
        os.system('cls')

        print("===========================")
        print("Bem vindo ao ✈ AIR TRAVEL!")
        print("===========================")
        print()
        print("1 - Comprar passagem")
        print("2 - Pacotes de viagem")
        print("3 - Meus dados")
        print("4 - Destinos")
        print("5 - Sair")
        print("\n")


        try:
         print()  
         opcao = int(input("Escolha uma opção: "))
         print("\n")

         os.system('cls')

         if opcao == 1:
            destino = input("Digite o destino: ")
            data = input("Digite a data da viagem (DD/MM/AAAA): ")
            passageiros = int(input("Digite a quantidade de passageiros: "))
            classe = input("Digite qual classe deseja viajar: ")
            print("\n")

            print(f"Destino: {destino}")
            print(f"Data: {data}")
            print(f"Passageiros: {passageiros}")
            print(f"Classe: {classe}" )

            confirma_compra = input("Confirmar compra? (sim/não): ").strip().lower()
            print()

            if confirma_compra == "sim":
               print("Compra confirmada")
               print("Que legal! Sua passagem foi comprada, acompanhe todo o passo a passo por email e tenha uma excelente viagem!")
               input("\nPressione Enter para voltar ao menu.")

            else:
               print("Compra cancelada")
               input("\nPressione Enter para voltar ao menu.")

         elif opcao == 2:
            
            print("======= RESUMO DO PACOTE =======")

            pacote_viagens()

            confirmar_pacote = input("Confirmar compra do pacote? (sim/não): ").strip().lower()
            print()

            if confirmar_pacote == "sim":
               print("Compra confirmada")
               print("Que legal! Seu pacote foi confirmado!")
               input("\nPressione Enter para voltar ao menu.")

            else:
               print("Compra cancelada")
               input("\nPressione Enter para voltar ao menu.")   

            print()

         elif opcao == 3:
            email = usuario_logado[0]
            cpf = usuario_logado[2]
            telefone = usuario_logado[3]

            print(f"Email: {email}")
            print(f"CPF: {cpf}")
            print(f"Telefone: {telefone}")

            input("\nPressione Enter para voltar ao menu.")

         elif opcao == 4:
            print()

         elif opcao == 5:
            break

         else:
            print("Obrigado por usar o Air Travel")
        except ValueError:
         input("\n Esse número é invalido")

def pacote_viagens():
   try:
      print("\n")
      for numero, pacotes in enumerate(destinos_pacotes, start=1):
         print(f"{numero} - {pacotes}")
         
      print("\n")
      opcao = int(input("Digite o Destino: "))
      print("\n")

      destino_pacote = destinos_pacotes[opcao - 1]

      cidade = destino_pacote.split(" - ")[0]

      numero = 1
      hoteis = []
      
      for pacotes in info_pacotes:
            if cidade in pacotes[0]:    
               print(f"{numero} - {pacotes[0]} - R$ {pacotes[1]}")
               hoteis.append(pacotes)
               numero += 1

      print("\n")
      opcao_hotel = int(input("Escolha o hotel: "))
      print("\n")
      hotel_escolhido = hoteis[opcao_hotel - 1]
      print(f"Hotel: {hotel_escolhido[0]}")
      print(f"Preço: R$ {hotel_escolhido[1]}")
      data_ida = input("Digite a data de ida: ")
      data_volta = input("Digite a data de volta: ")


      print("\n")
      print("======= RESUMO DA COMPRA =======")
      print(f"Destino: {destino_pacote}")
      print(f"Hotel: {hotel_escolhido[0]}")
      print(f"Preço: R$ {hotel_escolhido[1]}")
      print(f"Data de ida: {data_ida}")
      print(f"Data de volta: {data_volta}")
      print()
         
   except ValueError:
      print("Você precisa digitar um NÚMERO")

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    seleciona_opcao()

if __name__ == "__main__":
    main()