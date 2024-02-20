# PROJECT-113776
"""Ok...instead of generating the betting list with the betting bot function...let me provide an optimized betting list...
original_bet_list = [10,10,10,10,10,20,20,40,40,60,60,80,100,120,160,200,280,320,400,520,640,800,1000,1300,1600,2000,3000,4000,6000,6000\
,10000,10000,16000,24000,30000,30000,40000,48000,60000,80000]
I didn't want to change it cause you had to see it for yourself"""


1. **Martingale Function:**
   ```python
   def martingale(target_multiplier, bet_list):
       winning_bet = bet_list[-1]
       total_bets = sum(bet_list)
       total_profit = winning_bet * target_multiplier - total_bets
       return total_profit, total_bets
   ```

   - This function calculates the total profit and total bets based on the Martingale strategy.

2. **Betting Bot Function:**
   ```python
   def betting_bot(target_multiplier, num_bets, initial_bet=10):
       bet_list = [initial_bet]

       for i in range(1, num_bets + 1):
           next_bet = bet_list[-1] * 2
           bet_list.append(next_bet)

       return bet_list
   ```

   - Simulates the betting bot's behavior by implementing the Martingale strategy.

3. **Main Function:**
   ```python
   def main():
       target_multiplier = float(input("Enter the desired target multiplier: "))
       num_bets = int(input("Enter the number of bets you would like to simulate: "))

       simulated_bets = betting_bot(target_multiplier, num_bets)

       total_profit, total_bets = martingale(target_multiplier, simulated_bets)

       print(f"Total profit: {total_profit}\nTotal bets: {total_bets}\nBets placed: {simulated_bets}\
       \nNumber of bets: {len(simulated_bets)}")

   if __name__ == "__main__":
       main()
   ```

   - The `main` function prompts the user for input, simulates the betting bot, calculates total profit and total bets, and displays the results.

