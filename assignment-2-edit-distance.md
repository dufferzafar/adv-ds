
---

## Consider?

* Print the solution and not just the cost?

---


Note carefully the following instructions for the submission of programming assignment 2.

1. Your code should accept as input (on the command line) the name of a file. This file will contain 3 lines - line 1: string x, line 2: string y, line 3: cost list. The cost list is in the format <copy>,<insert>,<replace>,<delete>.

2. The strings will be alphanumeric ([a-zA-Z0-9]*) and your code must be case-sensitive. ('a' is a different character from 'A').

3. Your code should output the total cost of transforming string x into string y.

4. Zip your file(s) and submit on Moodle (link will be made available shortly). You may name your zip file "<your_entry_number>.zip".

5. Important: Ensure that your code runs on GCL machines. We will not be able to evaluate your code on your laptops/ personal machines.

6. 3. If there are any other assumptions you make in your code then specify them clearly in a separate text file called README. Do NOT email us asking for clarifications regarding corner cases.

-- 
Neha

---

There is a minor change in input format of programming assignment.

Input will consist of (3T+1) lines.

The first line will be 'T', the number of test cases.

Next 3T lines follow:

A single test case consists of 3 lines:

line 1: string x.
line 2: string y.
line 3: cost function, an array of 4 values, the cost of operations: 
(Copy, Insert, Replace, Delete)

Output:
A single integer, the cost of transforming string x to string y.

Final Output:
A list of T integers, where ith value is output of ith test case.

Constraints:

Let the length of string x is: m.
Let the length of string y is: n.
Then,
      0<=m*n<=10^9
      Cost of any operation 'C'  is 0<=C<=9*(10^10).
