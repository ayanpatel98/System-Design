'''
As we all know that poker cards have four suites: Spades, Hearts, Clubs and Diamonds with figures from 1 to 13.
Now you are given a set of poker cards, you can pick any one card as the first card. And except for the first card, you can only pick the card that has the same suit or figure with the previous one.
Return the max number of cards you can.
For example: [(H, 3), (H, 4), (S, 4), (D, 5), (D, 1)], it returns 3 as follows: (H,3)-->(H,4)-->(S,4)
'''

# Time: O(N × N!) | Space: O(N²)

import collections
class PokerGame:

    def findMaxReturnedCards(self, cards):
        maxCards = 0

        graph = collections.defaultdict(list)

        for i in range(len(cards)):
            for j in range(len(cards)):
                if i!=j and (cards[i][0]==cards[j][0] or cards[i][1]==cards[j][1]):
                    graph[cards[i]].append(cards[j])

        for card in cards:
            maxCards = max(maxCards, self.backtrack(graph, card, set(), 0))
        return maxCards

    # In the worst case, each card is connected to all others (i.e., the graph is complete).
    # Then from each card, you can go to any of the n-1 unvisited cards → n × (n-1) × (n-2) × ... = n! paths.
    def backtrack(self, graph, startCard, visited, steps):
        if startCard in visited:
            return steps
        
        maxSteps = 0
        visited.add(startCard)

        for nei in graph[startCard]:
            maxSteps = max(maxSteps, self.backtrack(graph, nei, visited, steps+1))

        visited.remove(startCard)
        return maxSteps

pokerGame = PokerGame()

cards = [('H', 3), ('H', 4), ('S', 4), ('D', 5), ('D', 1)]
print(pokerGame.findMaxReturnedCards(cards))

cards = [ ("H", 2),("H", 3), ("H", 4), ("S", 4), ("D", 5), ("D", 1) ]
print(pokerGame.findMaxReturnedCards(cards))

cards = [ ("H",2),("H", 3), ("H", 4), ("S", 2), ("D", 3), ("C", 4), ("C", 7) ]
print(pokerGame.findMaxReturnedCards(cards))

