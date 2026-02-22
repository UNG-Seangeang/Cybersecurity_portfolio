# SQL Filtering and Analysis

## Objective
To extract relevant security data using SQL queries.

## Queries Used
SELECT * FROM users WHERE login_attempts > 3;

## Output
Identified users with multiple failed login attempts.

## Explanation
Filtering helps detect suspicious activities such as brute-force attacks.

## Recommendation
- Lock accounts after multiple failed attempts
- Monitor login patterns
