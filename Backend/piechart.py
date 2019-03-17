import matplotlib.pyplot as plt

def piechart(budget_dict):
    labels = ["Food and Non Alcoholic Drinks", "Alcoholic Drinks, Tobacco and Narcotics", "Clothing and Footwear", "Gas, Water and Electricity", "Health", "Transport", "Phone and WiFi", "Recreation", "Education", "Restaurants", "Miscellaneous", "Savings"]
    values = []

    for key, value in budget_dict.items():
        values.append(value)

    plt.axis("equal")
    plt.pie(values, labels=labels, autopct=None)
    plt.show()