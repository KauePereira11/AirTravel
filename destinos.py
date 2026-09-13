continentes = {
    'Ásia': ['Japão', 'China', 'Coreia do Sul', 'Tailândia', 'Indonésia', 'Singapura'],
    'América do Norte': ['EUA', 'Canadá', 'México', 'Costa Rica'],
    'América do Sul': ['Brasil', 'Argentina', 'Peru', 'Bolívia', 'Uruguai', 'Chile', 'Colômbia'],
    'Europa': ['França', 'Espanha', 'Portugal', 'Inglaterra', 'Itália', 'Grécia', 'Suiça', 'Holanda', 'Alemanha', 'Noruega']
}


lugares = {
    'Japão': {
        'Pontos Turisticos': ['Monte Fuji', 'Tóquio', 'Quioto'],
        'Curiosidade': 'O Japão é conhecido pela tecnologia, cultura tradicional e pelos templos históricos.'
    },

    'China': {
        'Pontos Turisticos': ['Muralha da China', 'Cidade Proibida', 'Xangai'],
        'Curiosidade': 'A China possui uma das civilizações mais antigas do mundo.'
    },

    'Coreia do Sul': {
        'Pontos Turisticos': ['Seul', 'Palácio Gyeongbokgung', 'Busan'],
        'Curiosidade': 'A Coreia do Sul é conhecida mundialmente pelo K-pop e pela tecnologia.'
    },

    'Tailândia': {
        'Pontos Turisticos': ['Bangkok', 'Phuket', 'Ilhas Phi Phi'],
        'Curiosidade': 'A Tailândia é conhecida por suas praias paradisíacas e templos.'
    },

    'Indonésia': {
        'Pontos Turisticos': ['Bali', 'Jacarta', 'Ilhas Gili'],
        'Curiosidade': 'A Indonésia possui milhares de ilhas.'
    },

    'Singapura': {
        'Pontos Turisticos': ['Marina Bay Sands', 'Gardens by the Bay', 'Sentosa'],
        'Curiosidade': 'Singapura é uma das cidades mais modernas e organizadas da Ásia.'
    },

    'EUA': {
        'Pontos Turisticos': ['Miami Beach', 'Times Square', 'Estátua da Liberdade'],
        'Curiosidade': 'Os Estados Unidos possuem uma grande diversidade cultural e turística.'
    },

    'Canadá': {
        'Pontos Turisticos': ['Toronto', 'Vancouver', 'Cataratas do Niágara'],
        'Curiosidade': 'O Canadá é o segundo maior país do mundo em território.'
    },

    'México': {
        'Pontos Turisticos': ['Cancún', 'Cidade do México', 'Chichén Itzá'],
        'Curiosidade': 'O México possui uma rica cultura e antigas civilizações.'
    },

    'Costa Rica': {
        'Pontos Turisticos': ['San José', 'Vulcão Arenal', 'Parque Nacional Manuel Antonio'],
        'Curiosidade': 'A Costa Rica é conhecida por suas florestas e praias.'
    },

    'Chile': {
        'Pontos Turisticos': ['Deserto do Atacama', 'Santiago', 'Patagônia'],
        'Curiosidade': 'O Chile é um dos países mais longos do mundo.'
    },

    'Brasil': {
        'Pontos Turisticos': ['Rio de Janeiro', 'Fernando de Noronha', 'Foz do Iguaçu'],
        'Curiosidade': 'O Brasil é o maior país da América do Sul.'
    },

    'Peru': {
        'Pontos Turisticos': ['Machu Picchu', 'Lima', 'Cusco'],
        'Curiosidade': 'Machu Picchu é um dos destinos turísticos mais famosos do mundo.'
    },

    'Colômbia': {
        'Pontos Turisticos': ['Cartagena', 'Bogotá', 'Medellín'],
        'Curiosidade': 'A Colômbia é conhecida pelo café e pelas paisagens naturais.'
    },

    'Uruguai': {
        'Pontos Turisticos': ['Montevidéu', 'Punta del Este', 'Colônia do Sacramento'],
        'Curiosidade': 'O Uruguai é conhecido por suas praias e cidades históricas.'
    },

    'Argentina': {
        'Pontos Turisticos': ['Buenos Aires', 'Bariloche', 'Cataratas do Iguaçu'],
        'Curiosidade': 'A Argentina é famosa pelo tango, futebol e gastronomia.'
    },

    'Bolívia': {
        'Pontos Turisticos': ['Salar de Uyuni', 'La Paz', 'Lago Titicaca'],
        'Curiosidade': 'O Salar de Uyuni é o maior deserto de sal do mundo.'
    },

    'França': {
        'Pontos Turisticos': ['Torre Eiffel', 'Museu do Louvre', 'Nice'],
        'Curiosidade': 'A França é um dos países mais visitados do mundo.'
    },

    'Espanha': {
        'Pontos Turisticos': ['Madrid', 'Barcelona', 'Sevilha'],
        'Curiosidade': 'A Espanha possui uma cultura muito rica e diversa.'
    },

    'Portugal': {
        'Pontos Turisticos': ['Lisboa', 'Porto', 'Algarve'],
        'Curiosidade': 'Portugal possui forte ligação histórica e cultural com o Brasil.'
    },

    'Inglaterra': {
        'Pontos Turisticos': ['Londres', 'Big Ben', 'Palácio de Buckingham'],
        'Curiosidade': 'Londres é uma das cidades mais visitadas da Europa.'
    },

    'Itália': {
        'Pontos Turisticos': ['Roma', 'Veneza', 'Coliseu'],
        'Curiosidade': 'A Itália é conhecida por sua história, arte e gastronomia.'
    },

    'Grécia': {
        'Pontos Turisticos': ['Atenas', 'Santorini', 'Mykonos'],
        'Curiosidade': 'A Grécia é considerada o berço de parte da civilização ocidental.'
    },

    'Suiça': {
        'Pontos Turisticos': ['Zurique', 'Alpes Suíços', 'Genebra'],
        'Curiosidade': 'A Suíça é conhecida pelos Alpes, chocolates e relógios.'
    },

    'Holanda': {
        'Pontos Turisticos': ['Amsterdã', 'Museu Van Gogh', 'Keukenhof'],
        'Curiosidade': 'A Holanda é famosa pelos canais, bicicletas e tulipas.'
    },

    'Alemanha': {
        'Pontos Turisticos': ['Berlim', 'Munique', 'Castelo de Neuschwanstein'],
        'Curiosidade': 'A Alemanha possui uma forte história e cultura.'
    },

    'Noruega': {
        'Pontos Turisticos': ['Oslo', 'Fiordes Noruegueses', 'Tromsø'],
        'Curiosidade': 'A Noruega é conhecida pelos fiordes e pela aurora boreal.'
    }
}


def exibir_continentes():
    for numero, continente in enumerate(continentes, start=1):
        print(f"{numero} - {continente}")


def seleciona_continente():
    try:
        print()
        opcao = int(input('Escolha um continente: '))

        if opcao == 1:
            continente_escolhido = 'Ásia'
        elif opcao == 2:
            continente_escolhido = 'América do Norte'
        elif opcao == 3:
            continente_escolhido = 'América do Sul'
        elif opcao == 4:
            continente_escolhido = 'Europa'
        else:
            print('Opção inválida')
            input(
                "\nVocê precisa digitar um número válido."
                "\nPressione ENTER para voltar."
            )
            return seleciona_continente()

        return continente_escolhido

    except ValueError:
        input("\nVocê precisa digitar um número válido. Pressione ENTER para voltar.")
        return seleciona_continente()


def seleciona_pais(continente):
    try:
        print()

        for numero, pais in enumerate(continentes[continente], start=1):
            print(f"{numero} - {pais}")

        print()

        escolha = int(input("Escolha um país: "))

        paises = continentes[continente]
        pais_escolhido = paises[escolha - 1]

        print()
        print(f"Legal! Você escolheu {pais_escolhido}:")
        print()

        print('Lugares turísticos deste país que quero conhecer:')
        print()

        for numero, lugar in enumerate(lugares[pais_escolhido], start=1):
            print(f"{numero} - {lugar}")

        print()

        escolha = int(input('Escolha uma opção: '))
        print()

        if escolha == 1:
            for numero, lugar in enumerate(
                lugares[pais_escolhido]['Pontos Turisticos'],
                start=1
            ):
                print(f"{numero} - {lugar}")

            input("\nPressione ENTER para continuar.")

        elif escolha == 2:
            print(lugares[pais_escolhido]['Curiosidade'])
            input("\nPressione ENTER para continuar.")

        else:
            print('Opção inválida')
            input(
                "\nVocê precisa digitar um número válido."
                "\nPressione ENTER para voltar."
            )
            return seleciona_pais(continente)

    except ValueError:
        print("Você precisa digitar um NÚMERO")
        return seleciona_pais(continente)