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


def Check_Winner(just_check: bool) -> bool:
    player_score: int = CalculateScore(playerCards)
    dealer_score: int = CalculateScore(dealerCards)
    if dealer_score > 21:
        if not just_check:
            print("Dealer lost")
            print("Dealer cards: ")
            Print_Out_Hand(dealerCards)
            print("Your cards:")
            Print_Out_Hand(playerCards)
            return True
    elif dealer_score < player_score and player_score <= 21:
        if not just_check:
            print("User won")
            Print_Out_Player_And_Dealer_Hand()
            return True
    elif player_score < dealer_score:
        if not just_check:
            print("Dealer won")
            Print_Out_Player_And_Dealer_Hand()
            return True
    return False


def Print_out_current_score() -> None:
    print("--------------------------")
    print("Dealer cards: " + str(CalculateScore(dealerCards)))
    print("Your cards: " + str(CalculateScore(playerCards)))


def main_game() -> None:
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
        Check_Winner(just_check=False)
    else:
        user_want_to_continue: bool = True
        while user_want_to_continue == True and CalculateScore(playerCards) < 21:
            DrawACard("player", True)
            if CalculateScore(playerCards) > 21:
                print("Bust, Dealer won")
            else:
                print("Hit or Stand (h/s)")
                user_want_to_continue = True if input() == "h" else False
        Print_out_current_score()
        Check_Winner(just_check=False)


def main():
    continue_game: bool = True
    while continue_game:
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
        print("Menu\n1. Enter The Table\n2. Whithdraw Funds\n3. Deposite Funds")
        user_choice: str = input().lower()
        if user_choice == "1":
            main_game()


if __name__ == "__main__":
    main()
