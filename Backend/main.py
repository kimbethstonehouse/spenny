# Spenny: Fly to Financial Freedom
# Hack the Burgh 2019 
# Liana Ahmed, Kim Stonehouse, Mo Javad, Anu Chowdhury

from variance import variance
from calculate_budget import calculate_budget
from piechart import piechart
from savings_function import savings_function
from spenny_back import spenny_back

# things I have not yet managed to do
# 0. compare rent with average house prices - suggest hey you could be paying less
# 1. calculate income decile from salary - need Anu's help idk
# 2. can't find any data on occupation
# 3. currently just calculating the cost of one person and multiplying by 0.7 to account
# for each child dependent (or just 1 for adult) - maybe need a better scale factor, speak to Anu, see line 79
# 4. can't find data  on student vs part time vs full time - maybe we need to weight the data
# such as increase budget for alcohol if student, etc
 
def main():
    # parameters I am expecting from Moseph
    # set these when user input is sorted !!!!!!!
    region = "Scotland"
    salary = 16,000                 # calculate decile with this
    spendingPattern = "Frugal"
    drinks = False
    smokes = False
    rent = 500
    numAdults = 2
    numChildren = 2
    yearsToSave = 5
    initialAssets = 1000
    amountToSave = 5000                # currently needs an amount from user
                                    # perhaps can take an item (ie car) and calculate the amount needed (ie £5,000)

    budgetAverage = spenny_back(region, salary, spendingPattern, 
                    drinks, smokes, rent, numAdults, numChildren, yearsToSave, initialAssets, amountToSave)

    # who looks at the price ? it's 2018
    # calculate total weekly budget from all subcategories
    totalWeeklyBudget = 0
    for value in budgetAverage.values():
        totalWeeklyBudget += value

    piechart(budgetAverage)

if __name__ == "__main__":
    main()