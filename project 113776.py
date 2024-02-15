import random
import tkinter as tk
from tkinter import messagebox

def martingale(target_multiplier, bet_list):
    winning_bet = bet_list[-1]
    total_bets = sum(bet_list)
    total_profit = winning_bet * target_multiplier - total_bets
    return total_profit, total_bets, bet_list

def betting_bot(target_multiplier, num_bets, initial_bet=10):
    bet_list = [initial_bet]

    for i in range(1, num_bets + 1):
        # Implement the Martingale strategy (doubling the previous bet)
        next_bet = bet_list[-1] * 2
        bet_list.append(next_bet)

    return bet_list

def calculate_and_display_results(target_multiplier, num_bets, initial_bet):
    simulated_bets = betting_bot(target_multiplier, num_bets, initial_bet)
    total_profit, total_bets, bet_list = martingale(target_multiplier, simulated_bets)

    result_message = f"Total profit: {total_profit}\nTotal bets: {total_bets}\nBets placed:\n"
    for i, bet in enumerate(bet_list):
        result_message += f"Bet {i+1}: {bet} (Winning bet: {bet_list[-1]})"
        if bet_list[i] * target_multiplier > bet_list[-1]:
            result_message += f" - WON! ({bet_list[i] * target_multiplier - bet_list[i]} profit)\n"
        else:
            result_message += f" - LOST! (-{bet_list[i]} loss)\n"

    result_message += f"\nNumber of bets: {len(bet_list)}"
    messagebox.showinfo("Results", result_message)

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Martingale Betting Bot")

    # Create the input fields and buttons
    target_multiplier_label = tk.Label(root, text="Target multiplier:")
    target_multiplier_entry = tk.Entry(root)

    num_bets_label = tk.Label(root, text="Number of bets:")
    num_bets_entry = tk.Entry(root)

    initial_bet_label = tk.Label(root, text="Initial bet:")
    initial_bet_entry = tk.Entry(root)

    calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate_and_display_results(
        float(target_multiplier_entry.get()),
        int(num_bets_entry.get()),
        int(initial_bet_entry.get())
    ))

    # Place the input fields and buttons on the window
    target_multiplier_label.grid(row=0, column=0)
    target_multiplier_entry.grid(row=0, column=1)

    num_bets_label.grid(row=1, column=0)
    num_bets_entry.grid(row=1, column=1)

    initial_bet_label.grid(row=2, column=0)
    initial_bet_entry.grid(row=2, column=1)

    calculate_button.grid(row=3, column=0, columnspan=2)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
    