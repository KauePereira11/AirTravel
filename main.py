import os
os.system('cls')

def exibir_nome_do_programa():
  print("=================")
  print(" ✈  AIR TRAVEL ")
  print("=================")

usuarios = [ ['kaue@gmail.com', '12345', '777', '1199999'],
            ['erica@gmail.com', '1234', '666', '1197777']
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

         if encontrou == False:
            print("Email não encontrado")
         
      elif opcao == 3:
         print(listar_usuarios())
         listar_usuarios()
         usuarios[3]

      else:
         print('Obrigado por usar o Air Travel.')   
   except ValueError:
      input("\nEste número não é valido")
      return seleciona_opcao()
  

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    seleciona_opcao()




if __name__ == "__main__":
    main()  