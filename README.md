# 365-Days-of-Code-23
Coding every single day in 2023 by solving problems on LEETCODE

## Day 1
### Word pattern
This is a program that compares two strings. The function takes in a pattern and a strings of words. The string is then compared to see if it follows the pattern of the first string.
#### Example: 
the program returns True for: "abba" and "cat dog dog cat". This is because "cat dog dog cat" follows the pattern "abba".


## Day 2
### Palindrome Number
This program takes in an integer value and returns a boolean value indicating whether the integer value is a palindrome.
#### Examples:
the program returns True for: 121 because it is a palindrome, i.e. when read from behind, it remains unchanged.
the program returns False for: 133 because it is not a palindrome, i.e. when read from behind, it reads 331 which is not equal to the value 133.

## Day 3
### Minimum deletion size
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

#### Example:

Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

## Day 4

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

#### Example 1:

Input: s = "egg", t = "add"
Output: true
#### Example 2:

Input: s = "foo", t = "bar"
Output: false

## Day 5

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

 

#### Example 1:

Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
#### Example 2:

Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

## Day 6

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

#### Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
#### Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
#### Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

## Day 7
Given a table of candidates and their skills, you're tasked with finding the candidates best suited for an open Data Science job. You want to find candidates who are proficient in Python, Tableau, and PostgreSQL.

Write a query to list the candidates who possess all of the required skills for the job. Sort the the output by candidate ID in ascending order.

#### Assumption:

There are no duplicates in the candidates table.
candidates Table:

| **Column Name** | **Type** |
|-----------------|----------|
| candidate_id    | integer  |
| skill           | varchar  |

#### candidates Example Input:

| **candidate_id** | **skill**    |
|------------------|--------------|
|       123	       |   Python     |
|       123	       |   Tableau    |
|       123	       |   PostgreSQL |
|       234	       |   R          |
|       234	       |   PowerBI    |
|       234	       |   SQL Server |
|       345	       |   Python     |
|       345	       |   Tableau    |

#### Example Output:
candidate_id
123
Explanation
Candidate 123 is displayed because they have Python, Tableau, and PostgreSQL skills. 345 isn't included in the output because they're missing one of the required skills: PostgreSQL.