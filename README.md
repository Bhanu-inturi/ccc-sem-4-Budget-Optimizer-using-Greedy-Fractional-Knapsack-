# ccc-sem-4-Budget-Optimizer-using-Greedy-Fractional-Knapsack-

-- Budget Optimizer using Greedy Algorithm (Fractional Knapsack)
-- 1. Introduction

Efficient resource allocation is a common problem in computing and real life. This project implements a Budget Optimization System using the Greedy Algorithm (Fractional Knapsack) to maximize value within a limited budget.

-- 2. Problem Statement

Given:

A set of items, each having:
Cost (price)
Value (benefit)
A fixed budget

-- Objective:
Select items such that the total value is maximized without exceeding the budget.

Unlike the 0/1 knapsack problem, this approach allows fractional selection of items, enabling better optimization.

-- 3. Algorithm Used: Fractional Knapsack
🔹 Key Idea
Compute value-to-cost ratio for each item
Sort items in descending order of ratio
Pick items greedily
 Steps

Calculate ratio:

ratio = value / cost
Sort items based on ratio (high → low)
Iterate through items:
Take full item if budget allows
Otherwise take a fraction
-- 4. Features
Menu-driven program
Input validation (positive values only)
Displays:
Selected items
Full or fractional selection
Percentage of item taken
Total value obtained
Efficient greedy implementation
 5. Project Structure
Budget-Optimizer/
│── budget.cpp
│── README.md

-- 6. Implementation Overview
 Data Structure
struct Item {
    string name;
    double cost, value;
};
 Core Logic

Items are sorted using:

value / cost
Greedy selection ensures optimal result
-- 7. Sample Execution
-- Input
Number of items: 3

Item 1: A, cost=10, value=60  
Item 2: B, cost=20, value=100  
Item 3: C, cost=30, value=120  

Budget = 50
-- Output
Selected Items:
✔ A (Full)
✔ B (Full)
✔ C (66.67%)

Total Value Obtained: 240
-- 8. Complexity Analysis
Component	Complexity
Sorting	O(n log n)
Selection Loop	O(n)
Overall	O(n log n)
Space	O(n)
-- 9. Test Cases
 Case 1: Full Selection

Budget is sufficient → all items selected fully

 Case 2: Fractional Selection

Budget is limited → last item partially selected

-- Case 3: Invalid Input

Negative or zero values → rejected

-- 10. Applications
Budget planning
Investment decision making
Resource allocation
Logistics optimization
E-commerce recommendations
-- 11. Limitations
Assumes items can be divided
Not suitable for indivisible goods
-- 12. Future Enhancements
Add graphical interface
Store items using database
Web-based implementation
Multi-budget comparison system
-- 13. Conclusion

This project demonstrates how the Greedy Algorithm efficiently solves optimization problems. The Fractional Knapsack approach ensures maximum utilization of available resources while maintaining simplicity and performance.
