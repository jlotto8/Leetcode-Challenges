"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104

Idea 1. 

find the lowest number in the list as early (lowest index) in the list as possible //because I have to buy before I can sell, so buying earlier gives more options for when to sell at the best time
then find the highest number in the list, after(not before) the lowest number aka higher index
find the difference of highest number - lowest number
if the difference is < 1 (no profit) return 0
return the difference

Problems:
After finding the lowest number in the list, have to make sure to start at beyond that index to find the highest number - could make a copy of the list, and remove the lowest number once it is found?
If the lowest number is the last number in the list, do I choose the second-most low number? 
Will there be numbers that the differences equate to ties? 

sliding window plan

create a result variable to hold the max profit
create 2 pointers, left for buy and right for sell
loop through the list of numbers
    calculate the difference between the right - left, save as max profit
    # when do I incremement the left pointer? what condition? i think when prices[right] is <prices[left]
    # what do I do at the beginning of the code when r and l are both at index 0, pointing to the same element in the list? I could start the right pointer at index 1 instead of 0- but what if the len(prices) <=1?
    if current profit is < 0 do I need to do anything different?
    Do i ever stop incrementing the right pointer? - at the end of the list

create 2 pointers, left and right (buy, sell); start at 0
create a results max profit variable to hold the result

loop through the list of prices with a for loop to start at the beginning of the prices list, and go through each item in the list once; right/sell
    use a while loop to say if sell is less than buy ?
        move the left pointer by 1
    if the right pointer value - left pointer value is bigger than the max profit(starts at 0)
        reset the variable max profit sell - buy / right-left
"""
# input example - [7,1,5,3,6,4]
def maxProfit(prices):

    left_buy = 0
    max_profit = 0

    for right_sell in range(len(prices)):
        while prices[right_sell] < prices[left_buy]:
            left_buy += 1
            # print(f'sell price {prices[right_sell]}')
            # print(f'buy price {prices[left_buy]}')
            # print(f' max profit is {max_profit}')

        if prices[right_sell] - prices[left_buy] > max_profit:
            max_profit = prices[right_sell] - prices[left_buy] 
            
    return max_profit

print(maxProfit([7,6,4,3,1]))



            




#     l = 0     
#     current_profit = 0

#     for r in range(len(prices)):
#         while prices[r] <= len(prices):
#             if prices[r] - prices[l] >= current_profit:
#                 current_profit = prices[r] - prices[l]
#                 l += 1


#     if current_profit >= 0:
#         return current_profit
# print(maxProfit([7,1,5,3,6,4]))

