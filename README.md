# ccc-sem-4-Budget-Optimizer-using-Greedy-Fractional-Knapsack-
Budget Optimizer using Greedy Algorithm
-- Problem Statement

Given a limited budget and a list of items with cost and value, select items to maximize total value.

-- Algorithm Used

Fractional Knapsack (Greedy)

Sort items by value-to-cost ratio
Select highest ratio first
Take fraction if needed
-- Features
Menu-driven program
Input validation
Displays:
Selected items
Fraction taken
Total value
-- Sample Input
A: cost=10, value=60
B: cost=20, value=100
C: cost=30, value=120
Budget = 50
-- Output
A (Full), B (Full), C (66.67%)
Total Value: 240
-- Complexity
Time: O(n log n) (sorting)
Space: O(n)

-- How to Run
g++ budget.cpp -o budget
./budget
-- Conclusion

This project demonstrates how greedy algorithms efficiently solve optimization problems like resource allocation.
