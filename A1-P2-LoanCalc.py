#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 
"""
Student Name: Andrew Beaver
Program Title: Loan calculator
Description:  Assignment 1 Part 2
"""

def main():
    
    #Display opening message
    print("Weekly Loan Calculator")

    #Prompt user for loan amount
    loanAmount = float(input("\nEnter the amount of loan: "))

    #Prompt user for interest rate
    interestRate = float(input("Enter the interest rate (%): "))
    
    #Prompt user for the number of years
    loanYears = float(input("Enter the number of years: "))

    #Math to calculate the weekly payments
    periodicInterestRate = interestRate / 5200

    weeklyPayment = (periodicInterestRate / (1-(1 + periodicInterestRate)**-(52 * loanYears))) * loanAmount

    #Display the weekly payments
    print("\nYour weekly payment will be: ${0:,.2f}".format(weeklyPayment))

main()