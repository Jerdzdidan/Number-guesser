import random

def high_and_low(high, low):
    up_or_down = random.randint(high, low)
    n = up_or_down
    return n


def main():
    m = random.randint(1,100)
    high = 1
    low = 100
    while True:
        print("Think of a number from 1 - 100 \n")
        player_input = str(input("Have you picked a number yet? "))

        if player_input.lower() == "yes":
            player_input = str(input(f"{m} is this your number? "))

            while player_input.lower() == "no":
                input_for_high_and_low = str(input("Is your number higher or lower? "))

                if input_for_high_and_low.lower() == "higher":
                    high = m + 1
                    m = high_and_low(high, low)
                    player_input = str(input(f"\n{m} is this your number? "))
                elif input_for_high_and_low.lower() == "lower":
                    low = m - 1
                    m = high_and_low(high, low)
                    player_input = str(input(f"\n{m} is this your number? "))
                else:
                    print("Unrecognized Input")
                    continue

            if player_input == "yes":
                print(f"The computer has guessed your number {m}")
                break
            else:
                print("Unrecognized input")
                continue

        else:
            print("Unrecognized input")
            continue


main()