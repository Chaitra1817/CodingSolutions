'''
860. Lemonade Change
Solved
Easy
Topics
Companies

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

Example 1:

Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Count of $5 and $10 bills in hand
        five_dollar_bills = 0
        ten_dollar_bills = 0

        # Iterate through each customer's bill
        for customer_bill in bills:
            if customer_bill == 5:
                # Just add it to our count
                five_dollar_bills += 1
            elif customer_bill == 10:
                # We need to give $5 change
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    # Can't provide change, return false
                    return False
            else:  # customer_bill == 20
                # We need to give $15 change
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    # Give change as one $10 and one $5
                    five_dollar_bills -= 1
                    ten_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    # Give change as three $5
                    five_dollar_bills -= 3
                else:
                    # Can't provide change, return false
                    return False
        # If we've made it through all customers, return true
        return True
