import random

def martingale(target_multiplier, bet_list):
    winning_bet = bet_list[-1]
    total_bets = sum(bet_list)
    total_profit = winning_bet * target_multiplier - total_bets
    return total_profit, total_bets

def betting_bot(target_multiplier, num_bets, initial_bet=10):
    bet_list = [initial_bet]

    for i in range(1, num_bets + 1):
        # Implement the Martingale strategy (doubling the previous bet)
        next_bet = bet_list[-1] * 2
        bet_list.append(next_bet)

    return bet_list

def main():
    target_multiplier = float(input("Enter the desired target multiplier: "))
    num_bets = int(input("Enter the number of bets you would like to simulate: "))

    # Simulate the betting bot
    simulated_bets = betting_bot(target_multiplier, num_bets)

    # Calculate the total profit or loss
    total_profit, total_bets = martingale(target_multiplier, simulated_bets)

    # Display results
    print(f"Total profit: {total_profit}\nTotal bets: {total_bets}\nBets placed: {simulated_bets}\
    \nNumber of bets: {len(simulated_bets)}")

if __name__ == "__main__":
    main()