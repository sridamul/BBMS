# from quote import quote
import random

quotes = {
    1: "So many books, so little time.",
    2: "A room without books is like a body without a soul.",
    3: "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.",
    4: "Good friends, good books, and a sleepy conscience: this is the ideal life.",
    5: "Outside of a dog, a book is man's best friend. Inside of a dog it's too dark to read.",
    6: "A reader lives a thousand lives before he dies, said Jojen. The man who never reads lives only one.",
    7: "If you only read the books that everyone else is reading, you can only think what everyone else is thinking.",
    8: "I have always imagined that Paradise will be a kind of library.",
    9: "Never trust anyone who has not brought a book with them.",
    10: "You can never get a cup of tea large enough or a book long enough to suit me.",
    11: "If one cannot enjoy reading a book over and over again, there is no use in reading it at all.",
    12: "There is no friend as loyal as a book.",
    13: "I find television very educating. Every time somebody turns on the set, I go into the other room and read a book.",
    14: "It is what you read when you don't have to that determines what you will be when you can't help it.",
    15: "One must always be careful of books,\" said Tessa, \"and what is inside them, for words have the power to change us."
}


def quote_of_the_day():
    i = random.randint(1, 15)
    return quotes[i]
