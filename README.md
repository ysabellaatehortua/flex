# Flex
# To run validation script
run `python3 main.py` in terminal
# Approach to the problem
Looking at the ERD immediately reminded me of binary trees. I used the same logic as a binary search algorithm to traverse the nodes and calculate each value. I've used similar algoritms to say, find the greatest number in a binary tree.
# Assumptions made
The biggest was that I ignored small floating-point errors and assumed that past the second decimal point, any descrepancies where neglegible which may not be the case in practice. 
# Any issues or inconsistencies you found in the data
Discrepancy found in 'Liabilities': Computed=948018.89, Reported=1025016.99

Discrepancy found in 'Current Liabilities': Computed=937527.65, Reported=1014525.75

Bonus tiny discrepancy in 'ASSETS': Computed=13318970.870000001, Reported=13318970.87 (this was ignored for the purpose of this excerise)
# If I had more time
I would build some unit tests to ensure the script is working as intended on other test files. Add other data validation checkpoints, for example, making sure there are no unexpected positive or negative values or that there are no duplicate accounts.

I also would've spent more time on the ERD. I would've been able to think about establishing foreign key relationships, perhaps implementing a star schema, or really think about the best way to model the data.