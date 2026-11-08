import os
from html import escape
from datetime import date
os.system('cls')
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.database import (
    criar_tabela_usuarios,
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario
)
app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
templates = Jinja2Templates(directory="frontend")
@app.post("/login")
def login(email: str = Form(...), senha: str = Form(...)):
    usuario = buscar_usuario(email, senha)
    if usuario:
        return RedirectResponse(url="/frontend/destinos.html", status_code=303)
    return {"mensagem": "E-mail ou senha inválidos."}
@app.post("/cadastro")
def cadastro(
    email: str = Form(...),
    senha: str = Form(...),
    cpf: str = Form(...),
    telefone: str = Form(...)
):
    cadastrar_usuario(email, senha, cpf, telefone)
    return RedirectResponse(
    url="/destinos.html",
    status_code=303
)
@app.on_event("startup")
def iniciar_banco():
    criar_tabela_usuarios()
@app.get("/buscar-passagens", response_class=HTMLResponse)
def buscar_passagens(request: Request):
    origem_original = request.query_params.get("origem", "").strip()
    destino_original = request.query_params.get("destino", "").strip()
    tipo_viagem = request.query_params.get("tipo-viagem", "ida")
    data_ida = request.query_params.get("data-ida", "")
    data_volta = request.query_params.get("data-volta", "")
    classe = request.query_params.get("classe", "economica")
    passageiros = request.query_params.get("passageiros", "1")

    if not origem_original or not destino_original:
        return HTMLResponse("<h2>Preencha a origem e o destino.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    if origem_original.casefold() == destino_original.casefold():
        return HTMLResponse("<h2>A origem e o destino não podem ser iguais.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    if not data_ida:
        return HTMLResponse("<h2>Informe a data de ida.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    try:
        ida = date.fromisoformat(data_ida)
        volta = date.fromisoformat(data_volta) if data_volta else None
    except ValueError:
        return HTMLResponse("<h2>Informe datas válidas.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    if ida < date.today():
        return HTMLResponse("<h2>A data de ida não pode estar no passado.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    if tipo_viagem == "ida-volta":
        if not volta:
            return HTMLResponse("<h2>Informe a data de volta.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)
        if volta <= ida:
            return HTMLResponse("<h2>A volta deve ser depois da ida.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)
    elif tipo_viagem == "ida":
        data_volta = ""
        volta = None
    else:
        return HTMLResponse("<h2>Tipo de viagem inválido.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    if classe not in ["economica", "executiva"]:
        return HTMLResponse("<h2>Classe inválida.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    try:
        quantidade_passageiros = int(passageiros)
        if quantidade_passageiros < 1 or quantidade_passageiros > 9:
            raise ValueError
    except ValueError:
        return HTMLResponse("<h2>Quantidade de passageiros inválida.</h2><a href='/frontend/compra.html'>Voltar</a>", status_code=400)

    origem = escape(origem_original)
    destino = escape(destino_original)
    data_ida_formatada = ida.strftime("%d/%m/%Y")
    data_volta_formatada = volta.strftime("%d/%m/%Y") if volta else "Não se aplica"
    classe_formatada = "Econômica" if classe == "economica" else "Executiva"

    voos = [
        ("AirTravel Express", "08:00", "12:30", "R$ 850,00"),
        ("Voo Nacional", "13:30", "18:00", "R$ 1.120,00"),
        ("Conexão Aérea", "19:15", "23:45", "R$ 980,00")
    ]

    cards_voos = ""
    for companhia, horario_ida, horario_chegada, preco in voos:
        cards_voos += f"""
        <div class="voo-card">
            <div>
                <h3>{companhia}</h3>
                <p>{horario_ida} → {horario_chegada}</p>
                <p>{origem} → {destino}</p>
            </div>
            <div>
                <h3>{preco}</h3>
                <p>{classe_formatada}</p>
                <p>{quantidade_passageiros} passageiro(s)</p>
            </div>
            <a href="/frontend/compra.html">Selecionar voo</a>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/frontend/style.css">
        <title>Voos encontrados - AirTravel</title>
    </head>
    <body>
        <header>
            <h1>✈ AIR TRAVEL | Sua viagem começa aqui!</h1>
            <nav>
                <a href="/frontend/index.html">Início</a>
                <a href="/frontend/destinos.html">Destinos</a>
                <a href="/frontend/compra.html">Passagens</a>
            </nav>
        </header>
        <main>
            <section class="compra-passagem">
                <h2>Voos encontrados</h2>
                <div class="resumo-busca">
                    <p><strong>Origem:</strong> {origem}</p>
                    <p><strong>Destino:</strong> {destino}</p>
                    <p><strong>Ida:</strong> {data_ida_formatada}</p>
                    <p><strong>Volta:</strong> {data_volta_formatada}</p>
                    <p><strong>Classe:</strong> {classe_formatada}</p>
                    <p><strong>Passageiros:</strong> {quantidade_passageiros}</p>
                </div>
                <div class="lista-voos">
                    {cards_voos}
                </div>
                <a href="/frontend/compra.html">Voltar à busca</a>
            </section>
        </main>
    </body>
    </html>
    """


def exibir_nome_do_programa():
    print("=========================================")
    print(" ✈  AIR TRAVEL | Sua viagem começa aqui!")
    print("=========================================")
destinos_pacotes = [
    "Miami - EUA",
    "Nova York - EUA",
    "Washington, D.C. - EUA",
    "Madrid - Espanha",
    "Barcelona - Espanha",
    "Paris - França",
    "Nice - França"
]
info_pacotes = [
    ["Miami - The Betsy - South Beach", 7500],
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
    ["Berlim - Hilton Berlin", 7500]
]
def cadastrar_novo_usuario():
    os.system('cls')
    print('Novo Cadastro.')
    while True:
        email = input("Email: ")
        if "@" in email and email.endswith(".com"):
            break
        print("Email inválido. Digite um email válido.")
    while True:
        senha = input("Senha: ")
        if any(not caractere.isalnum() for caractere in senha):
            break
        print("Senha inválida. Digite pelo menos um caractere especial.")
    while True:
        cpf = input("CPF: ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        print("CPF inválido. Digite exatamente 11 números.")
    while True:
        telefone = input("Telefone: ")
        if telefone.isdigit() and len(telefone) == 11:
            break
        print("Telefone inválido. Digite 11 números.")
    cadastrar_usuario(email, senha, cpf, telefone)
    print("Cadastro realizado!")
    input('Digite uma tecla para voltar ao inicio.')
def listar_usuarios_cadastrados():
    usuarios = listar_usuarios()
    for usuario in usuarios:
        print(f'ID: {usuario[0]}')
        print(f'Email: {usuario[1]}')
        print(f'CPF: {usuario[3]}')
        print(f'Telefone: {usuario[4]}')
        print('-' * 30)
    input("\nPressione Enter para voltar.")
def exibir_opcoes():
    print()
    print("1 - Criar Conta: ")
    print("2 - Fazer Login: ")
    print("3 - Usuarios cadastrado: ")
    print("4 - Sair :")
def seleciona_opcao():
    while True:
        exibir_opcoes()
        try:
            opcao = int(input("Escolha uma opção: "))
            os.system('cls')
            if opcao == 1:
                cadastrar_novo_usuario()
            elif opcao == 2:
                email = input("Email: ")
                senha = input("Senha: ")
                usuario_logado = buscar_usuario(email, senha)
                if usuario_logado:
                    menu_usuario(usuario_logado)
                else:
                    print("Email ou senha incorretos.")
                    input("\nPressione Enter para voltar.")
            elif opcao == 3:
                listar_usuarios_cadastrados()
            elif opcao == 4:
                print("Obrigado por usar o Air Travel")
                break
            else:
                print("Opção inválida")
                input("\nPressione Enter para voltar.")
        except ValueError:
            print("Você precisa digitar um número.")
            input("\nPressione Enter para voltar.")
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
        print()
        try:
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
                print(f"Classe: {classe}")
                confirma_compra = input(
                    "Confirmar compra? (sim/não): "
                ).strip().lower()
                print()
                if confirma_compra == "sim":
                    print("Compra confirmada")
                    print(
                        "Que legal! Sua passagem foi comprada, "
                        "acompanhe todo o passo a passo por email "
                        "e tenha uma excelente viagem!"
                    )
                    input("\nPressione Enter para voltar ao menu.")
                else:
                    print("Compra cancelada")
                    input("\nPressione Enter para voltar ao menu.")
            elif opcao == 2:
                print("======= RESUMO DO PACOTE =======")
                pacote_viagens()
                confirmar_pacote = input(
                    "Confirmar compra do pacote? (sim/não): "
                ).strip().lower()
                print()
                if confirmar_pacote == "sim":
                    print("========= PAGAMENTO =========")
                    print()
                    print("1 - PIX")
                    print("2 - Cartão de crédito")
                    print("3 - Cartão de débito")
                    pagamento_valido = 0
                    try:
                        forma_pagamento = int(
                            input("Escolha a forma de pagamento: ")
                        )
                        if forma_pagamento == 1:
                            print("Pagamento via PIX")
                            pagamento_valido = 1
                        elif forma_pagamento == 2:
                            print("Pagamento via cartão de crédito")
                            pagamento_valido = 1
                        elif forma_pagamento == 3:
                            print("Pagamento via cartão de débito")
                            pagamento_valido = 1
                        if pagamento_valido == 1:
                            print("Que legal! Seu pacote foi confirmado!")
                            input(
                                "\nPressione Enter para voltar ao menu."
                            )
                        else:
                            print("Forma de pagamento inválida")
                            input(
                                "\nPressione Enter para voltar ao menu."
                            )
                    except ValueError:
                        print("Número inválido")
                else:
                    print("Compra cancelada")
                print()
            elif opcao == 3:
                email = usuario_logado[1]
                cpf = usuario_logado[3]
                telefone = usuario_logado[4]
                print(f"Email: {email}")
                print(f"CPF: {cpf}")
                print(f"Telefone: {telefone}")
                input("\nPressione Enter para voltar ao menu.")
            elif opcao == 4:
                destinos()
            elif opcao == 5:
                print("Obrigado por usar o Air Travel")
                break
            else:
                print("Opção inválida")
        except ValueError:
            input("\nEsse número é inválido.")
def destinos():
    print("\n======= DESTINOS DISPONÍVEIS =======")
    for numero, destino in enumerate(destinos_pacotes, start=1):
        print(f"{numero} - {destino}")
    input("\nPressione ENTER para voltar ao menu.")
def pacote_viagens():
    try:
        print("\n")
        for numero, pacotes in enumerate(destinos_pacotes, start=1):
            print(f"{numero} - {pacotes}")
        print("\n")
        opcao = int(input("Digite o Destino: "))
        if opcao < 1 or opcao > len(destinos_pacotes):
            print("Opção inválida")
            input("\nPressione ENTER para tentar novamente.")
            return pacote_viagens()
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
        if opcao_hotel < 1 or opcao_hotel > len(hoteis):
            print("Opção inválida")
            input("\nPressione ENTER para tentar novamente.")
            return pacote_viagens()
        hotel_escolhido = hoteis[opcao_hotel - 1]
        print(f"Hotel: {hotel_escolhido[0]}")
        print(f"Preço: R$ {hotel_escolhido[1]}")
        data_ida = input("Digite a data de ida: ")
        data_ida = data_ida.split("/")
        data_volta = input("Digite a data de volta: ")
        while len(data_ida) != 3:
            print("Data inválida")
            data_ida = input("Digite a data de ida novamente: ")
            data_ida = data_ida.split("/")
        data_volta = data_volta.split("/")
        while len(data_volta) != 3:
            print("Data inválida")
            data_volta = input("Digite a data de volta novamente: ")
            data_volta = data_volta.split("/")
        print("\n")
        print("======= RESUMO DA COMPRA =======")
        print(f"Destino: {destino_pacote}")
        print(f"Hotel: {hotel_escolhido[0]}")
        print(f"Preço: R$ {hotel_escolhido[1]}")
        print(f"Data de ida: {'/'.join(data_ida)}")
        print(f"Data de volta: {'/'.join(data_volta)}")
        print()
    except ValueError:
        print("Você precisa digitar um NÚMERO")
informacoes_destinos = {
    "miami": {
        "nome": "Miami - Estados Unidos",
        "imagem": "miami.jpg",
        "descricao": "Miami encanta seus visitantes com praias, clima tropical, vida noturna e diversidade cultural.",
        "atracoes": [
            "South Beach",
            "Ocean Drive",
            "Wynwood Walls",
            "Bayside Marketplace"
        ],
        "curiosidades": "Miami possui forte influência latino-americana e é conhecida por sua diversidade cultural."
    },
    "paris": {
        "nome": "Paris - França",
        "imagem": "paris.jfif",
        "descricao": "Paris é conhecida como a Cidade Luz, famosa por sua arquitetura, gastronomia, arte e romantismo.",
        "atracoes": [
            "Torre Eiffel",
            "Museu do Louvre",
            "Arco do Triunfo",
            "Catedral de Notre-Dame"
        ],
        "curiosidades": "A Torre Eiffel foi construída para a Exposição Universal de 1889."
    },
    "newyork": {
        "nome": "Nova York - Estados Unidos",
        "imagem": "Times Square.jpg",
        "descricao": "Nova York é conhecida por sua energia, diversidade, arranha-céus e atrações culturais.",
        "atracoes": [
            "Times Square",
            "Central Park",
            "Estátua da Liberdade",
            "Empire State Building"
        ],
        "curiosidades": "Nova York é conhecida mundialmente pelo apelido Big Apple."
    },
    "madrid": {
        "nome": "Madrid - Espanha",
        "imagem": "madrid.jpg",
        "descricao": "Madrid combina história, cultura, gastronomia e uma vida urbana bastante movimentada.",
        "atracoes": [
            "Palácio Real",
            "Museu do Prado",
            "Parque do Retiro",
            "Plaza Mayor"
        ],
        "curiosidades": "Madrid é uma das capitais europeias localizadas em maior altitude."
    },
    "roma": {
        "nome": "Roma - Itália",
        "imagem": "coliseu-roma-italia-1.jpg",
        "descricao": "Roma é conhecida como a Cidade Eterna e reúne monumentos históricos, arte e gastronomia.",
        "atracoes": [
            "Coliseu",
            "Fontana di Trevi",
            "Panteão",
            "Vaticano"
        ],
        "curiosidades": "Roma abriga o Vaticano, o menor país do mundo em território."
    },
    "londres": {
        "nome": "Londres - Inglaterra",
        "imagem": "londres.jfif",
        "descricao": "Londres mistura tradição e modernidade, com monumentos históricos, museus e parques.",
        "atracoes": [
            "Big Ben",
            "London Eye",
            "Tower Bridge",
            "Palácio de Buckingham"
        ],
        "curiosidades": "O metrô de Londres foi inaugurado em 1863."
    }
}

@app.get("/destino.html", response_class=HTMLResponse)
def pagina_destino(request: Request, destino: str):
    informacoes = informacoes_destinos.get(destino)

    if informacoes is None:
        return HTMLResponse(
            "<h2>Destino não encontrado.</h2>"
            '<a href="/destinos.html">Voltar</a>',
            status_code=404
        )

    return templates.TemplateResponse(
        request=request,
        name="destino.html",
        context={"destino": informacoes}
    )

@app.get("/destinos.html", response_class=HTMLResponse)
def pagina_destinos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="destinos.html",
        context={"destinos": informacoes_destinos}
    )
def main():
    criar_tabela_usuarios()
    exibir_nome_do_programa()
    seleciona_opcao()
if __name__ == "__main__":
    main()
