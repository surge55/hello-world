#########################################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Problem Set 2: finances and credit
''''
Each month, a credit card statement will come with the option for you to pay a minimum amount of your 
charge, usually 2% of the balance due. However, the credit card company earns money by charging interest 
on the balance that you don't pay. So even if you pay credit card payments on time, interest is still 
accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum 
monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining 
balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will 
call  (b for balance; subscript 0 to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in 
month 0, . Thus, your unpaid balance for month 0, , is equal to .

ub0 = b0 - p0

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So 
if your annual interest rate is , then at the beginning of month 1, your new balance is your previous 
unpaid balance , plus the interest on this unpaid balance for the month. In algebra, this new balance 
would be

b1 = ub0 + (r/12.0)*ub0

In month 1, we will make another payment, . That payment has to cover some of the interest costs, so it 
does not completely go towards paying off the original charge. The balance at the beginning of month 2, , 
can be calculated by first calculating the unpaid balance after paying , then by adding the interest accrued:

ub1 = b1 - p1
b2 = ub1 + (r/12.0)*ub1

If you choose just to pay off the minimum monthly payment each month, you will see that the compound 
interest will dramatically reduce your ability to lower your debt.

Let's look at an example. If you've got a $5,000 balance on a credit card with 18% annual interest rate, 
and the minimum monthly payment is 2% of the current balance, we would have the following repayment 
schedule if you only pay the minimum payment each month:

Month	Balance	Minimum Payment	Unpaid Balance	Interest
0	5000.00	100 (= 5000 * 0.02)	4900 (= 5000 - 100)	73.50 (= 0.18/12.0 * 4900)
1	4973.50 (= 4900 + 73.50)	99.47 (= 4973.50 * 0.02)	4874.03 (= 4973.50 - 99.47)	73.11 (= 0.18/12.0 * 4874.03)
2	4947.14 (= 4874.03 + 73.11)	98.94 (= 4947.14 * 0.02)	4848.20 (= 4947.14 - 98.94)	72.72 (= 0.18/12.0 * 4848.20)

You can see that a lot of your payment is going to cover interest, and if you work this through month 12, 
you will see that after a year, you will have paid $1165.63 and yet you will still owe $4691.11 on what 
was originally a $5000.00 debt. Pretty depressing!
'''
#########################################################################################################

## PROBLEM 1 - Paying Debt off in a Year
## Write a progra to calculate the credit card balance after one year if a person only pays the minimum
## monthly payment required by the credit card company each month.
##
## The following variables contain values as described below:
## 1. balance - the outstanding balance on the credit card
## 2. annualInterestRate - annual interest rate as a decimal
## 3. monthlyPaymentRate - minimum monthly payment rate as a decimal
##
## For each monthly, calculate statements on the monthly payment and remaining balance. At the end of 12 
## months, print out the remaining balance. Be sure to print our not more than two decimal
## digits of accuracy - so print.
##
## Example: 
## (Remaining balance: 813.41)
## 
## Provided variables -->
## balance: the outstanding balance on the credit card
## annualInterestRate: annual interest rate as a decimal
## monthlyPaymentRate: minimum monthly payment rate as a decimal

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    minPay = balance*monthlyPaymentRate
    reBalance = (balance - (minPay))
    balance = reBalance + (annualInterestRate/12)*reBalance
    #print("Remaining balance: ", round(balance, 2))

print("Remaining balance: ", round(balance, 2))

#########################################################################################################
## PROBLEM 2 - Paying Debt Off in a Year
## Now write a program that calculates the minimum fixed monthyl payment needed in order pay off a credit
## card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change
## each month, but instead is a constant amount that will be paid each month.
##
## In this problem, we will not be dealing with a minimum monthly payment rate.
##
## The following variables contain values as described below:
## 1. balance - the outstanding balance on the credit card
## 2. annualInterestRate - annual interest rate as a decimal
##
## The program should print out one line: the lowest monthly payment that will pay off all debt in under
## 1 year, for example:
## (Lowest Payment: 180)
##
## Assume that the interest is compounded monthly according to the balance at the end of the month (after
## the payment for that month is made). The monthly payment must be a muliple of $10 and is the same for 
## all months. Notice that it is possible for the balance to become negative using this payment scheme, 
## which is ok.

balance = 3926
annualInterestRate = 0.2
monthInterestRate = annualInterestRate/12

minPay = 0
startBalance = balance

while balance > 0:
    minPay += 10
    balance = startBalance
    for i in range(12):
        reBalance = (balance - (minPay))
        balance = reBalance + (annualInterestRate/12)*reBalance

print("Lowest Payment: ", minPay)

#########################################################################################################
## PROBLEM 3 - Using Bisection Search to Make the Program Faster
## You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it 
## that way? You can try running your code locally so that the payment can be any dollar and cent amount 
## (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but
## you may notice that your code runs more slowly, especially in cases with very large balances and interest 
## rates. (Note: when your code is running on our servers, there are limits on the amount of computing time 
## each submission is allowed, so your observations from running this experiment on the grading system might 
## be limited to an error message complaining about too much time taken.)
##
## Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without 
## running into the problem of slow code? We can make this program run faster using a technique introduced 
## in lecture - bisection search!
##
## The following variables contain values as described below:
## balance - the outstanding balance on the credit card
## annualInterestRate - annual interest rate as a decimal
##
## To recap the problem: we are searching for the smallest monthly payment such that we can pay off the 
## entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious 
## answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly 
## payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth
## of the original balance is a good lower bound.
##
## What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the 
## end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, 
## because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for 
## the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for 
## an entire year.
##
## In short:
## Monthly interest rate = (Annual interest rate) / 12.0
## Monthly payment lower bound = Balance / 12
## Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
##
## Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on 
## bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can 
## pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large 
## inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.
##
## Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run 
## on our servers.

balance = 999999
annualInterestRate = 0.18
monthInterestRate = annualInterestRate/12

startBalance = balance
low = balance/12
high = (balance*(1+monthInterestRate)**12)/12

minPay = (high + low)/2

while abs(balance) >= 0.01:

    balance = startBalance
    for i in range(12):
        reBalance = (balance - (minPay))
        balance = reBalance + (annualInterestRate/12)*reBalance
        #print(' month: ' + str(i) + ' low: ' + str(low) + ' high: ' + str(high) + ' minPay: ' + str(minPay))

    if balance < 0:
        high = minPay
    else:
        low = minPay
    minPay = (high + low)/2

print("Lowest Payment: ", round(minPay,2))

