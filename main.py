import random


class Carta():

    def __init__(self, naipe, numero) -> None:
        super().__init__()
        self.naipe = naipe
        self.numero = numero


class Deck():
    def __init__(self) -> object:
        super().__init__()
        numeros = ["0", "1", "2", "3", '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        naipes = ["♥", "♦", "♣", "♠"]
        self.cards = []
        for naipe in naipes:
            for numero in numeros:
                self.cards.append(Carta(naipe, numero))
        self.flush_deck()

    def flush_deck(self):
        random.shuffle(self.cards)

    def get_card(self, num):
        cards = []
        for c in range(num):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards


class Player():
    cartas: [Carta]

    def __init__(self, id) -> None:
        super().__init__()
        self.points = 1500
        self.cartas = []
        self.id = id
        self.betnow = 0

    def set_cards(self, cards):
        self.cartas = cards

    def bet(self, bet):
        self.points = self.points - bet
        return int(bet)


class Round():
    Players: [Player]
    cards: [Deck]
    tableCards: [Carta]

    def __init__(self, players, dealer) -> None:
        """
        :type players: [Player]
        """
        super().__init__()
        self.Players = players
        self.dealer = dealer
        self.smallBlind = self.betSBlinds()
        self.bigBlind = self.betBBlinds()
        # Deck da mesa
        self.cards = Deck()
        # Cartas da mesa
        self.tableCards = self.cards.get_card(5)
        # Montante de aposta da rodada
        self.tableBet = 0
        # Maior aposta atual
        self.betAtual = self.bigBlind
        # Rodada ativa ou nao
        self.game = True
        # Numero de cartas abertas
        self.cartasAbertas = 0

        # tipo de melhor jogada
        self.best_game = 1

    def destribui_cards(self):
        for player in self.Players:
            player.set_cards(round.cards.get_card(2))

    def betBBlinds(self):
        n = self.dealer - 2
        value = int(input(f"Valor do Big blind deve ser no minimo o dobro de {self.smallBlind}: "))
        self.Players[n].betnow = value
        return self.Players[n].bet(value)

    def betSBlinds(self):
        n = self.dealer - 1
        value = int(input("Valor do small blind: "))
        self.Players[n].betnow = value
        return self.Players[n].bet(value)

    def fold(self, player):
        """
        :type player: Player
        """
        Players.remove(player)

    def call(self, player):
        """
        :type player: Player
        """
        player.betnow = self.betAtual
        self.tableBet += player.bet(self.betAtual - player.betnow)

    def bets(self, player, bet):
        self.betAtual = self.betAtual + bet
        player.betnow = self.betAtual
        self.tableBet += player.bet(bet)

    def jogada(self, player):
        x = input(f""""
        Jogador {player.id}
        Money $ {player.points}

        Aposta da mesa {self.betAtual}
        Sua aposta atual {player.betnow}
        
        O que voce deseja fazer ? 
        
        [0] - sair
        [1] - {"Passar" if player.betnow == self.betAtual else "Pagar"} {"" if player.betnow == self.betAtual else "[" + str(self.betAtual - player.betnow) + "]"}
        [2] - apostar
       """)

        if x == "0":
            self.fold(player)
        elif x == "1":
            if player.betnow != self.betAtual:
                self.call(player)
        else:
            self.bets(player, int(input("Digite o valor da aposta: ")))

    def turn_cards(self):
        if self.cartasAbertas == 0:
            self.cartasAbertas = 3
            return 3
        elif self.cartasAbertas == 3:
            self.cartasAbertas = 4
            return 4
        else:
            self.cartasAbertas = 5
            return 5

    def verifica_vitoria(self) -> []:
        # verifica ROYAL STRAIGHT FLUSH
        jogador = self.verifica_royal_straight()
        if id != -1:
            return [self.tableBet, jogador]
        # verifica STRAIGHT FLUSH
        jogador = self.verifica_royal_straight()
        if id != -1:
            return [self.tableBet, jogador]
        # verifica Quadra
        jogador = self.verifica_quadra()
        if id != -1:
            return [self.tableBet, jogador]
        jogador = self.verifica_full_house()
        if id != -1:
            return [self.tableBet, jogador]
        jogador = self.verifica_flush()
        if id != -1:
            return [self.tableBet, jogador]
        jogador = self.verifica_sequencia()
        if id != -1:
            return [self.tableBet, jogador]
        jogador = self.verifica_trinca()
        if id != -1:
            return [self.tableBet, jogador]
        jogador = self.verifica_pares(2)
        if id != -1:
            return [self.tableBet, jogador]
        jogador = self.verifica_pares(1)
        if id != -1:
            return [self.tableBet, jogador]

        return [self.tableBet, self.verifica_maior_carta()]

    def verifica_quadra():

        possiveisCartas = []
        numeros = []
        numerosp = []
        v = False
        for carta in round.tableCards:
            numeros.append(carta.numero)

        for num in numeros:
            if numeros.count(num) >= 2:
                numerosp.append(num)
                v = True
        for carta in round.tableCards:
            if carta.numero in numerosp:
                possiveisCartas.append(carta.numero)

        if v:
            v = False
            jogadorganhando = 0
            maiorcarta = 0
            for player in round.Players:
                cartasPossiveisJogador = []
                for carta in player.cartas:
                    if carta.numero in numerosp:
                        cartasPossiveisJogador.append(carta.numero)

                for carta in cartasPossiveisJogador:
                    if cartasPossiveisJogador.count(carta) + possiveisCartas.count(carta) == 4:
                        if int(carta) > int(maiorcarta):
                            v = True
                            jogadorganhando = player
                            maiorcarta = carta
            if v:
                return player
        return -1

    def identifica_sequencia(numCartas):
        seq = 1
        for c in range(len(numCartas)):
            seq = seq + 1
            if c == len(numCartas) - 1:
                break
            if numCartas[c] + 1 != numCartas[c + 1]:
                seq = 1
            if seq == 5:
                return True
        return False

    def identifica_trinca(numCartas):
        maiorcarta = 0
        for carta in numCartas:
            if numCartas.count(carta) == 3:
                if carta > maiorcarta:
                    maiorcarta = carta
        return maiorcarta

    def identifica_numero_par(numCartas, carta):
        if numCartas.count(carta) == 2:
            return True
        return False

    def identifica_par(numCartas):
        maiorcarta = 0
        num_par = 0
        for carta in numCartas:
            if self.identifica_numero_par(numCartas, carta):
                num_par = num_par + 1
                if carta > maiorcarta:
                    maiorcarta = carta
        return (num_par / 2, maiorcarta)

    def verifica_royal_straight(self):
        v = False
        possiveisCartas = []
        for carta in self.tableCards:
            if int(carta.numero) in (10, 11, 12, 13, 0):
                possiveisCartas.append(carta)

        if len(possiveisCartas) >= 3:
            naipes = []
            for carta in possiveisCartas:
                naipes.append(carta.naipe)

            for naipe in naipes:
                if naipes.count(naipe) >= 3:
                    naipeJogada = naipe
                    v = True
            for carta in possiveisCartas:
                if carta.naipe != naipeJogada:
                    possiveisCartas.remove(carta)

        if v:
            v = False
            for player in self.Players:
                cartasPossiveisJogador = []
                for carta in player.cartas:
                    if int(carta.numero) in (10, 11, 12, 13, 0):
                        cartasPossiveisJogador.append(carta)
                for carta in cartasPossiveisJogador:
                    print(carta.numero)
                    if carta.naipe != naipeJogada:
                        cartasPossiveisJogador.remove(carta)
                if len(possiveisCartas) + len(cartasPossiveisJogador) >= 5:
                    cartasjogada = []
                    for carta in possiveisCartas:
                        cartasjogada.append(int(carta.numero))
                    for carta in cartasPossiveisJogador:
                        cartasjogada.append(int(carta.numero))
                    cartasjogada.sort()

                    if cartasjogada == [0, 10, 11, 12, 13]:
                        v = True
                if v:
                    return player
        else:
            return -1

    def verifica_straight_flush(self):
        possiveisCartas = []
        naipes = []
        naipeJogada = "0"
        v = False
        for carta in round.tableCards:
            naipes.append(carta.naipe)
            possiveisCartas.append(carta)
        for naipe in naipes:
            if naipes.count(naipe) >= 3:
                naipeJogada = naipe
                v = True
        for carta in round.tableCards:
            if carta.naipe != naipeJogada:
                possiveisCartas.remove(carta)

        if v:
            v = False
            jogadorganhando = 0
            maiorcarta = 0
            for player in round.Players:
                cartasPossiveisJogador = []
                for carta in player.cartas:
                    if carta.naipe == naipeJogada:
                        cartasPossiveisJogador.append(carta)
                if len(possiveisCartas) + len(cartasPossiveisJogador) >= 5:
                    cartasjogada = []
                    for carta in possiveisCartas:
                        cartasjogada.append(int(carta.numero))
                    for carta in cartasPossiveisJogador:
                        cartasjogada.append(int(carta.numero))
                    cartasjogada.sort()

                    if self.identifica_sequencia(cartasjogada):
                        v = True
                        if max(cartasjogada) > maiorcarta:
                            jogadorganhando = player
                            maiorcarta = max(cartasjogada)
            if v:
                return jogadorganhando

        return -1

    def verifica_flush(self):

        possiveisCartas = []
        naipes = []
        naipeJogada = "0"
        v = False
        for carta in round.tableCards:
            naipes.append(carta.naipe)
            possiveisCartas.append(carta)
        for naipe in naipes:
            if naipes.count(naipe) >= 3:
                naipeJogada = naipe
                v = True
        for carta in round.tableCards:
            if carta.naipe != naipeJogada:
                possiveisCartas.remove(carta)

        if v:
            v = False
            jogadorganhando = 0
            maiorcarta = 0
            for player in round.Players:
                cartasPossiveisJogador = []
                for carta in player.cartas:
                    if carta.naipe == naipeJogada:
                        cartasPossiveisJogador.append(carta)
                if len(possiveisCartas) + len(cartasPossiveisJogador) >= 5:
                    cartasjogada = []
                    for carta in cartasPossiveisJogador:
                        cartasjogada.append(int(carta.numero))
                    v = True
                    if max(cartasjogada) > maiorcarta:
                        jogadorganhando = player
                        maiorcarta = max(cartasjogada)
            if v:
                return jogadorganhando
        return -1

    def verifica_sequencia(self):
        possiveisCartas = []
        naipeJogada = "0"
        v = False
        for carta in round.tableCards:
            possiveisCartas.append(int(carta.numero))

        jogadorganhando = 0
        maiorcarta = 0
        cartasjogada = []
        for player in round.Players:
            cartasPossiveisJogador = []
            for carta in player.cartas:
                cartasPossiveisJogador.append(int(carta.numero))
            for carta in cartasPossiveisJogador:
                cartasjogada.append(int(carta))
            for carta in possiveisCartas:
                cartasjogada.append(int(carta))
            cartasjogada.sort()

            if identifica_sequencia(cartasjogada):
                v = True
                if max(cartasjogada) > maiorcarta:
                    jogadorganhando = player
                    maiorcarta = max(cartasjogada)
        if v:
            return jogadorganhando
        return -1

    def verifica_trinca(self):
        possiveisCartas = []
        naipeJogada = "0"
        v = False
        for carta in round.tableCards:
            possiveisCartas.append(int(carta.numero))

        jogadorganhando = 0
        maiorcarta = 0
        cartasjogada = []
        for player in round.Players:
            cartasPossiveisJogador = []
            for carta in player.cartas:
                cartasPossiveisJogador.append(int(carta.numero))
            for carta in cartasPossiveisJogador:
                cartasjogada.append(int(carta))
            for carta in possiveisCartas:
                cartasjogada.append(int(carta))
            cartasjogada.sort()
            trinca = self.identifica_trinca(cartasjogada)
            if trinca != 0:
                v = True
                if trinca > maiorcarta:
                    jogadorganhando = player
                    maiorcarta = trinca
        if v:
            return jogadorganhando
        return -1

    def verifica_pares(self, num):
        possiveisCartas = []
        naipeJogada = "0"
        v = False
        for carta in round.tableCards:
            possiveisCartas.append(int(carta.numero))

        jogadorganhando = 0
        maiorcarta = 0

        for player in round.Players:
            cartasjogada = []
            cartasPossiveisJogador = []
            for carta in player.cartas:
                cartasPossiveisJogador.append(int(carta.numero))
            for carta in cartasPossiveisJogador:
                cartasjogada.append(int(carta))
            for carta in possiveisCartas:
                cartasjogada.append(int(carta))
            cartasjogada.sort()
            pares = self.identifica_par(cartasjogada)
            print(pares)
            if pares[0] == num:
                v = True
                if pares[1] > maiorcarta:
                    jogadorganhando = player
                    maiorcarta = pares[1]
                elif pares[1] == maiorcarta:
                    cartasMelhor = []
                    for carta in jogadorganhando.cartas:
                        cartasMelhor.append(int(carta.numero))
                    if sum(cartasPossiveisJogador) > sum(cartasMelhor):
                        jogadorganhando = player
                        maiorcarta = pares[1]
        if v:
            return jogadorganhando
        return -1

    def verifica_full_house(self):

        possiveisCartas = []
        naipeJogada = "0"
        v = False
        for carta in round.tableCards:
            possiveisCartas.append(int(carta.numero))

        jogadorganhando = 0
        maiorcarta = 0

        for player in round.Players:
            cartasjogada = []
            cartasPossiveisJogador = []
            for carta in player.cartas:
                cartasPossiveisJogador.append(int(carta.numero))
            for carta in cartasPossiveisJogador:
                cartasjogada.append(int(carta))
            for carta in possiveisCartas:
                cartasjogada.append(int(carta))
            cartasjogada.sort()

            trinca = self.identifica_trinca(cartasjogada)
            pares = self.identifica_par(cartasjogada)
            if trinca != 0 and pares[0] > 0:
                v = True
                if trinca > maiorcarta:
                    jogadorganhando = player
                    maiorcarta = pares[1]
        if v:
            return jogadorganhando
        return -1

    def verifica_maior_carta(self):
        melhorJogador = 0
        maiorcarta = 0
        v = False
        for player in round.Players:
            for carta in player.cartas:
                if int(carta.numero) > maiorcarta:
                    jogadorganhando = player
                    maiorcarta = int(carta.numero)
                if int(carta.numero) == maiorcarta and sum(
                        [int(jogadorganhando.cartas[0].numero), int(jogadorganhando.cartas[1].numero)]) < sum(
                    [int(player.cartas[0].numero), int(player.cartas[1].numero)]):
                    jogadorganhando = player
                    maiorcarta = int(carta.numero)
        return jogadorganhando


class graphic_game():

    @staticmethod
    def print_card(cards, num=-1):
        """

        :type cards: [Carta]
        """
        if num == -1:
            for carta in cards:
                print(f"""                            --------
                            |{carta.naipe}     |
                            |      |
                            |   {carta.numero}  |
                            |      |
                            |     {carta.naipe}|
                            -------- """)


        else:
            for c in range(0, num):
                print(f"""                            --------
                                            |{cards[c].naipe}     |
                                            |      |
                                            |   {cards[c].numero}  |
                                            |      |
                                            |     {cards[c].naipe}|
                                            --------
                                            """)


Players = []

for c in range(int(input("Digite o numero de jogadores: "))):
    Players.append(Player(c))
dealer = 0
while 1:
    print("-" * 20, "COMEÇANDO NOVA RODADA", 20 * "-")
    round = Round(Players, dealer)

    round.destribui_cards()

    # INICIA UMA RODADA
    while round.game:
        apostas = True

        # INICIA NOVA RODADA DE APOSTA DO JOGO ATUAL
        while apostas:

            # Verifica se esta devendo, se nao pode pular a vez
            for player in round.Players:
                if player.points >0:
                    graphic_game.print_card(player.cartas)
                    round.jogada(player)

            apostas = False
            for player in round.Players:
                if player.betnow != round.betAtual:
                    apostas = True
        if round.cartasAbertas == 5:
            round.game = False
        graphic_game.print_card(round.tableCards, round.turn_cards())

    for c in range (len(player)):
        Players[c].points = round.Players[c]
    final = round.verifica_vitoria()
    Players[final[1].id].points+= int(final[0])
    print(f"vitoria jogador {final[1].id}")

    dealer += 1
    if dealer == len(Players):
        dealer = 0
