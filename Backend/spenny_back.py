from variance import variance
from calculate_budget import calculate_budget
from piechart import piechart
from savings_function import savings_function

def spenny_back(region, salary, spendingPattern, drinks, smokes, rent, numAdults, 
                    numChildren, yearsToSave, initialAssets, amountToSave):
    
    # calculate income decile from salary
    weeklySalary = salary/52

    if weeklySalary<216:
        decile = 1
    if weeklySalary<322:
        decile = 2
    if weeklySalary<432:
        decile = 3
    if weeklySalary<548:
        decile = 4
    if weeklySalary<681:
        decile = 5
    if weeklySalary<812:
        decile = 6
    if weeklySalary<986:
        decile = 7
    if weeklySalary<1252:
        decile = 8
    if weeklySalary<1713:
        decile = 9
    else: 
        return 10
    
    # maps region or decile to the corresponding file line number
    regionKeys = {"United Kingdom":0, "England":1, "North East":2, "North West":3,
    "Yorkshire and The Humber":4, "East Midlands":5, "West Midlands":6, "East":7, "London":8, "South East":9,
    "South West":10, "Wales":11, "Scotland":12, "Northern Ireland":13}

    decileKeys = {"All":0, "Lowest":1, "Second":2, "Third":3, "Fourth":4,
    "Fifth":5, "Sixth":6, "Seventh":7, "Eighth":8, "Ninth":9, "Highest":10}

    # fetch file line numbers
    regionKey = regionKeys.get(region)
    decileKey = decileKeys.get(decile)

    # adjust to a different decile depending on spending pattern
    # assumption that lowest and highest deciles can't go lower or higher
    # moderate doesn't change the decile
    if spendingPattern == "Frugal" and decileKey != 1 and decileKey != 0:
        decileKey -= 1
    elif spendingPattern == "Spenny" and decileKey != 10:
        decileKey += 1

    # calculate a budget estimate for each parameter
    budgetRegion = calculate_budget(region, regionKey, "regions.txt")
    budgetDecile = calculate_budget(decile, decileKey, "deciles.txt")

    # find the variances of the income and region data to
    # deduce how much each factor influences expenditure
    decileVar = variance("deciles.txt")
    regionVar = variance("regions.txt")

    # normalise to find a weight for each factor
    # weights sum to one so they don't shift the data
    decileWeight = decileVar / (decileVar + regionVar)
    regionWeight = regionVar / (decileVar + regionVar)

    # find average budget by weighting parameter budgets
    budgetAverage = dict()
    budgetAverage["food"] = regionWeight*budgetRegion["food"] + decileWeight*budgetDecile["food"]
    budgetAverage["alcohol"] = regionWeight*budgetRegion["alcohol"] + decileWeight*budgetDecile["alcohol"]
    budgetAverage["clothing"] = regionWeight*budgetRegion["clothing"] + decileWeight*budgetDecile["clothing"]
    # rent, gas, electricity bills
    budgetAverage["utilities"] = regionWeight*budgetRegion["utilities"] + decileWeight*budgetDecile["utilities"]
    budgetAverage["health"] = regionWeight*budgetRegion["health"] + decileWeight*budgetDecile["health"]
    budgetAverage["transport"] = regionWeight*budgetRegion["transport"] + decileWeight*budgetDecile["transport"]
    # phone, wifi bills
    budgetAverage["communication"] = regionWeight*budgetRegion["communication"] + decileWeight*budgetDecile["communication"]
    budgetAverage["recreation"] = regionWeight*budgetRegion["recreation"] + decileWeight*budgetDecile["recreation"]
    budgetAverage["education"] = regionWeight*budgetRegion["education"] + decileWeight*budgetDecile["education"]
    # eating out
    budgetAverage["catering"] = regionWeight*budgetRegion["catering"] + decileWeight*budgetDecile["catering"]
    budgetAverage["toiletries"] = regionWeight*budgetRegion["toiletries"] + decileWeight*budgetDecile["toiletries"]

    # this is all probably not very statistically accurate
    for key in budgetAverage:
        # currently for a household of 2.4 so normalise to one person
        budgetAverage[key] = budgetAverage[key] / 2.4

        # scale up to the number of dependents
        budgetAverage[key] = numAdults * budgetAverage[key] + numChildren * 0.7 * budgetAverage[key]

        # round to the nearest 5
        budgetAverage[key] = 5 * round(budgetAverage[key] / 5)

    # calculate savings, if any
    budgetAverage["savings"] = savings_function(yearsToSave, amountToSave, initialAssets)

    # drop alcohol budget if they don't drink or smoke
    if not (drinks) and not (smokes):
        budgetAverage["alcohol"] = 0

    # who looks at the price ? it's 2018
    # calculate total weekly budget from all subcategories
    totalWeeklyBudget = 0
    for value in budgetAverage.values():
        totalWeeklyBudget += value

    return budgetAverage