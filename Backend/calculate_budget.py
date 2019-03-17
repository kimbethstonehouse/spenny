# reads part of file corresponding to parameter into dictionary
def calculate_budget(parameterKey, dir):
    budget = dict()

    with open(dir, "r") as all:
        file = all.read().split("\n")

    # grab the corresponding line
    costs = file[parameterKey]
    
    # split into 11 values
    costs = costs.split(" ")
    budget["food"] = float(costs[0])
    budget["alcohol"] = float(costs[1])
    budget["clothing"] = float(costs[2])
    # rent, gas, electricity bills
    budget["utilities"] = float(costs[3])
    budget["health"] = float(costs[4])
    budget["transport"] = float(costs[5])
    # phone, wifi bills
    budget["communication"] = float(costs[6])
    budget["recreation"] = float(costs[7])
    budget["education"] = float(costs[8])
    # eating out
    budget["catering"] = float(costs[9])
    budget["toiletries"] = float(costs[10])

    return budget