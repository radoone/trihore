import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{}, {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.puttedcards = []

    def build(self):
        for s in ["Zelen", "Cerven", "Gula", "Srdce"]:
            for v in ["VII", "VII", "IX", "X", "Dolnik", "Hornik", "Kral", "Eso"]:
                self.cards.append(Card(v, s))

    def shuffle(self):
        for i in range(1, len(self.cards)):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

    def drawtablecard(self):
        self.puttedcards.append(self.drawCard())

    def put(self, Card):
        self.puttedcards.append(Card)


class Player:
    def __init__(self, name, game):
        self.name = name
        self.hand = []
        self.game = game

    def draw(self):
        self.hand.append(self.game.deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def play(self, action):
        return self.game.play(self, action)


class Game():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.drawtablecard()
        self.players = []

    def addPlayer(self, name):
        player = Player(name, self)
        self.players.append(player)
        return player

    def validmoves(self, player):
        tablecard = self.deck.puttedcards[-1]
        actions = ['Draw']
        for card in player.hand:
            if(tablecard.suit == card.suit) or (tablecard.value == card.value):
                actions.append(card)
        return actions

    def play(self, player, action):
        if action == "Draw":
            player.draw()
        print(f"{player.name} action: {action}")


game = Game()
karol = game.addPlayer("Karolinka")

karol.draw()
karol.draw()
karol.draw()
karol.draw()
karol.draw()
karol.draw()
karol.draw()
karol.draw()
karol.draw()
karol.draw()


karol.play("Draw")
print(game.validmoves(karol))
