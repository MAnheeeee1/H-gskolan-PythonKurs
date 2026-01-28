import random

suits: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks: list[str] = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
]
dealerCards: list[tuple] = []
playerCards: list[tuple] = []


def DrawACard(who_is_drawing: str, should_print_out_drawn_card: bool) -> None:
    if who_is_drawing == "player":
        playerCards.append((suits[random.randint(0, 3)], ranks[random.randint(0, 12)]))
        if should_print_out_drawn_card:
            print("You have got: " + str(playerCards[-1]))
    elif who_is_drawing == "dealer":
        dealerCards.append((suits[random.randint(0, 3)], ranks[random.randint(0, 12)]))
        if should_print_out_drawn_card:
            print("Dealer got: " + str(dealerCards[-1]))
    return


def CalculateScore(list_of_cards: list[tuple]) -> int:
    score: int = 0
    amount_of_aces: int = 0
    for card in list_of_cards:
        if card[1] == "Ace":
            amount_of_aces += 1
        elif card[1] == "Jack" or card[1] == "Queen" or card[1] == "King":
            score += 10
        else:
            score += int(card[1])
    for i in range(amount_of_aces):
        potentialScore = score + 11
        if potentialScore < 21:
            score += 11
        else:
            score += 1
    return score


def Print_Out_Hand(cards: list[tuple]) -> None:
    for card in cards:
        print(card)


def Print_Out_Player_And_Dealer_Hand() -> None:
    print("Dealer cards: ")
    Print_Out_Hand(dealerCards)
    print("Your cards:")
    Print_Out_Hand(playerCards)


def Check_Winner() -> None:
    if CalculateScore(dealerCards) > 21:
        print("Dealer lost")
        print("Dealer cards: ")
        Print_Out_Hand(dealerCards)
        print("Your cards:")
        Print_Out_Hand(playerCards)
    elif CalculateScore(dealerCards) < CalculateScore(playerCards):
        print("User won")
        Print_Out_Player_And_Dealer_Hand()
    elif CalculateScore(playerCards) < CalculateScore(dealerCards):
        print("Dealer won")
        Print_Out_Player_And_Dealer_Hand()


def Print_out_current_score() -> None:
    print("--------------------------")
    print("Dealer cards: " + str(CalculateScore(dealerCards)))
    print("Your cards: " + str(CalculateScore(playerCards)))


def main():
    while True:
        print("""
            /$$$$$$$  /$$                     /$$                               /$$
           | $$__  $$| $$                    | $$                              | $$
           | $$  \\ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$
           | $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/
           | $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/
           | $$  \\ $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$
           | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \\  $$| $$|  $$$$$$$|  $$$$$$$| $$ \\  $$
           |_______/ |__/ \\_______/ \\_______/|__/  \\__/| $$ \\_______/ \\_______/|__/  \\__/
                                                  /$$  | $$
                                                 |  $$$$$$/
                                                  \\______/                               """)
        DrawACard("player", True)
        DrawACard("dealer", True)
        DrawACard("player", True)
        DrawACard("dealer", False)
        print("Dealer has drawn his second card")
        print("Hit or Stand (h/s)")
        user_choice: str = input()
        if user_choice == "s":
            print("Dealer second card was: " + str(dealerCards[-1]))
            while CalculateScore(dealerCards) < 16:
                DrawACard("dealer", True)

            Print_out_current_score()
            Check_Winner()

        break


if __name__ == "__main__":
    main()
