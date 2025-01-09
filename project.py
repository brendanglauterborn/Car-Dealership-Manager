# project.py
# Brendan Lauterborn, David Trink and Braxton Macias
# 05/04/2020
# brendangl@tamu.edu, davidtrink55@tamu.edu and braxtonmacias00@tamu.edu
# The Dealership Manager
# This program will organize car information and sales around the country in 2019 for a car dealership. The program summarizes key information and presents multiple data figures to the user.

import matplotlib.pyplot as graph


def question_two(states):
    '''This function will plot the total amount of sales in each state'''
    keys = states.keys()
    values = states.values()
    graph.figure(1)
    graph.bar(keys, values)
    graph.title("Amount of Sale in Different States", fontsize=16)
    graph.xlabel("State", fontsize=14)
    graph.ylabel("Amount of Sale", fontsize=14)
    graph.show()


def question_three(months):
    ''' This function takes a dictionary where the keys are months and the values are sales for that month and plots month vs the sales for that month '''
    x = ['January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    y = []
    for month in x:
        sales = months[month]
        y.append(sales)
    graph.figure(2)
    graph.xlabel("Months", fontsize=14)
    graph.ylabel("Amount of Sale", fontsize=14)
    graph.title("Amount of Sale in Different Months in 2019", fontsize=16)
    graph.plot(x, y)


def question_four(percentage):
    ''' This function plots a pie chart of the percentage of sales by car brand '''
    brands = []
    totals = []
    graph.figure(3)
    for key, value in percentage.items():
        brands.append(key)
        totals.append(value)
    graph.pie(totals, labels=brands, autopct='%.1f%%', radius=1.125)
    graph.title("Percentage of Sale by Different Car Brands")
    graph.show()


def question_five(texas, california, florida, ohio, nevada):
    '''This function will plot the total sales per month for each state'''
    graph.figure(4)
    x_units = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    graph.plot(x_units, texas, color='b', label='Texas')
    graph.plot(x_units, california, color='orange', label='California')
    graph.plot(x_units, florida, color='g', label='Florida')
    graph.plot(x_units, ohio, color='r', label='Ohio')
    graph.plot(x_units, nevada, color='purple', label='Nevada')
    graph.title("Amount of Sale in Different Months in each State", fontsize=16)
    graph.xlabel("Month", fontsize=14)
    graph.ylabel("Amount of sale", fontsize=14)
    graph.legend(loc='upper right')


def main():
    ''' This is the main driver for the program '''
    print("============Data Set Details============\n")

    # grab each line
    grandTotal = 0
    carline = []
    deals = -1
    with open('2019_car_sale.csv', 'r') as doc:
        for line in doc:
            newline = line.strip('\n')
            carline.append(newline.split(','))
            deals += 1
    carline.pop(0)

    # break each word in line into list
    individual = []
    for i in range(len(carline)):
        for j in range(len(carline[i])):
            word = carline[i][j]
            individual.append(word.capitalize())

    # make price into a list and next to each other
    for i in range(5, len(individual), 8):
        first = individual[i].strip('\"')
        second = individual[i + 1].strip('\"')
        individual[i] = int(first + second)
        grandTotal += individual[i]

    texas_monthly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    california_monthly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    florida_monthly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ohio_monthly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nevada_monthly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # putting month sales for each state into list
    for i in range(3, len(individual), 8):
        if individual[i] == 'Texas':
            if individual[i - 2][0] == '1' and individual[i - 2][1] == '/':
                texas_monthly_sales[0] += individual[i + 2]
            elif individual[i - 2][0] == '2':
                texas_monthly_sales[1] += individual[i + 2]
            elif individual[i - 2][0] == '3':
                texas_monthly_sales[2] += individual[i + 2]
            elif individual[i - 2][0] == '4':
                texas_monthly_sales[3] += individual[i + 2]
            elif individual[i - 2][0] == '5':
                texas_monthly_sales[4] += individual[i + 2]
            elif individual[i - 2][0] == '6':
                texas_monthly_sales[5] += individual[i + 2]
            elif individual[i - 2][0] == '7':
                texas_monthly_sales[6] += individual[i + 2]
            elif individual[i - 2][0] == '8':
                texas_monthly_sales[7] += individual[i + 2]
            elif individual[i - 2][0] == '9':
                texas_monthly_sales[8] += individual[i + 2]
            elif individual[i - 2][1] == '0':
                texas_monthly_sales[9] += individual[i + 2]
            elif individual[i - 2][1] == '1':
                texas_monthly_sales[10] += individual[i + 2]
            elif individual[i - 2][1] == '2':
                texas_monthly_sales[11] += individual[i + 2]

        elif individual[i] == 'California':
            if individual[i - 2][0] == '1' and individual[i - 2][1] == '/':
                california_monthly_sales[0] += individual[i + 2]
            elif individual[i - 2][0] == '2':
                california_monthly_sales[1] += individual[i + 2]
            elif individual[i - 2][0] == '3':
                california_monthly_sales[2] += individual[i + 2]
            elif individual[i - 2][0] == '4':
                california_monthly_sales[3] += individual[i + 2]
            elif individual[i - 2][0] == '5':
                california_monthly_sales[4] += individual[i + 2]
            elif individual[i - 2][0] == '6':
                california_monthly_sales[5] += individual[i + 2]
            elif individual[i - 2][0] == '7':
                california_monthly_sales[6] += individual[i + 2]
            elif individual[i - 2][0] == '8':
                california_monthly_sales[7] += individual[i + 2]
            elif individual[i - 2][0] == '9':
                california_monthly_sales[8] += individual[i + 2]
            elif individual[i - 2][1] == '0':
                california_monthly_sales[9] += individual[i + 2]
            elif individual[i - 2][1] == '1':
                california_monthly_sales[10] += individual[i + 2]
            elif individual[i - 2][1] == '2':
                california_monthly_sales[11] += individual[i + 2]

        elif individual[i] == 'Florida':
            if individual[i - 2][0] == '1' and individual[i - 2][1] == '/':
                florida_monthly_sales[0] += individual[i + 2]
            elif individual[i - 2][0] == '2':
                florida_monthly_sales[1] += individual[i + 2]
            elif individual[i - 2][0] == '3':
                florida_monthly_sales[2] += individual[i + 2]
            elif individual[i - 2][0] == '4':
                florida_monthly_sales[3] += individual[i + 2]
            elif individual[i - 2][0] == '5':
                florida_monthly_sales[4] += individual[i + 2]
            elif individual[i - 2][0] == '6':
                florida_monthly_sales[5] += individual[i + 2]
            elif individual[i - 2][0] == '7':
                florida_monthly_sales[6] += individual[i + 2]
            elif individual[i - 2][0] == '8':
                florida_monthly_sales[7] += individual[i + 2]
            elif individual[i - 2][0] == '9':
                florida_monthly_sales[8] += individual[i + 2]
            elif individual[i - 2][1] == '0':
                florida_monthly_sales[9] += individual[i + 2]
            elif individual[i - 2][1] == '1':
                florida_monthly_sales[10] += individual[i + 2]
            elif individual[i - 2][1] == '2':
                florida_monthly_sales[11] += individual[i + 2]

        elif individual[i] == 'Ohio':
            if individual[i - 2][0] == '1' and individual[i - 2][1] == '/':
                ohio_monthly_sales[0] += individual[i + 2]
            elif individual[i - 2][0] == '2':
                ohio_monthly_sales[1] += individual[i + 2]
            elif individual[i - 2][0] == '3':
                ohio_monthly_sales[2] += individual[i + 2]
            elif individual[i - 2][0] == '4':
                ohio_monthly_sales[3] += individual[i + 2]
            elif individual[i - 2][0] == '5':
                ohio_monthly_sales[4] += individual[i + 2]
            elif individual[i - 2][0] == '6':
                ohio_monthly_sales[5] += individual[i + 2]
            elif individual[i - 2][0] == '7':
                ohio_monthly_sales[6] += individual[i + 2]
            elif individual[i - 2][0] == '8':
                ohio_monthly_sales[7] += individual[i + 2]
            elif individual[i - 2][0] == '9':
                ohio_monthly_sales[8] += individual[i + 2]
            elif individual[i - 2][1] == '0':
                ohio_monthly_sales[9] += individual[i + 2]
            elif individual[i - 2][1] == '1':
                ohio_monthly_sales[10] += individual[i + 2]
            elif individual[i - 2][1] == '2':
                ohio_monthly_sales[11] += individual[i + 2]

        elif individual[i] == 'Nevada':
            if individual[i - 2][0] == '1' and individual[i - 2][1] == '/':
                nevada_monthly_sales[0] += individual[i + 2]
            elif individual[i - 2][0] == '2':
                nevada_monthly_sales[1] += individual[i + 2]
            elif individual[i - 2][0] == '3':
                nevada_monthly_sales[2] += individual[i + 2]
            elif individual[i - 2][0] == '4':
                nevada_monthly_sales[3] += individual[i + 2]
            elif individual[i - 2][0] == '5':
                nevada_monthly_sales[4] += individual[i + 2]
            elif individual[i - 2][0] == '6':
                nevada_monthly_sales[5] += individual[i + 2]
            elif individual[i - 2][0] == '7':
                nevada_monthly_sales[6] += individual[i + 2]
            elif individual[i - 2][0] == '8':
                nevada_monthly_sales[7] += individual[i + 2]
            elif individual[i - 2][0] == '9':
                nevada_monthly_sales[8] += individual[i + 2]
            elif individual[i - 2][1] == '0':
                nevada_monthly_sales[9] += individual[i + 2]
            elif individual[i - 2][1] == '1':
                nevada_monthly_sales[10] += individual[i + 2]
            elif individual[i - 2][1] == '2':
                nevada_monthly_sales[11] += individual[i + 2]

    # remove extra number that is located after the now combined number
    cnt = 0
    for i in range(6, len(individual), 8):
        individual.pop(i - cnt)
        cnt += 1

    # first part of question 1
    model_set = set()
    for i in range(0, len(individual), 7):
        model_set.add(individual[i])

    brand_set = set()
    for i in range(2, len(individual), 7):
        brand_set.add(individual[i])

    safety_set = set()
    for i in range(4, len(individual), 7):
        safety_set.add(individual[i])

    color_set = set()
    for i in range(6, len(individual), 7):
        color_set.add(individual[i])

    total = 0
    for i in range(5, len(individual), 7):
        total += individual[i]

    print(f"Total number of deals: {deals}")
    print(f"Number of car models: {len(model_set)}")
    print(f"Number of car brands: {len(brand_set)}")
    print(f"Number of safety ratings: {len(safety_set)}")
    print(f"Number of colors: {len(color_set)}")
    print(f"Total amount of sale: {total}\n")

    print("========================================\n")

    # Questions 2 and 3
    worker = individual
    highest_total = 0
    highest_state = ""
    states = {}

    # sorts states into dictoinary and gives their totals
    for i in range(3, len(worker), 7):
        state_total = worker[i + 2]
        if worker[i] == False:
            continue
        else:
            for j in range(i + 7, len(worker), 7):
                if worker[i] == worker[j]:
                    state_total += worker[j + 2]
                    worker[j] = False
        states.update({worker[i]: state_total})

    first = 0
    for key, value in states.items():
        if first == 0:
            highest_state = key
            highest_total = value
            first = 1
        else:
            if value > highest_total:
                highest_total = value
                highest_state = key

    # sorts months into dictionary with their totals

    month_total = 0
    highest_month = ''
    months = {}

    for i in range(1, len(worker), 7):
        date = worker[i]
        if date[0] != '1':
            if date[0] == '2':
                worker[i] = 'February'
            if date[0] == '3':
                worker[i] = 'March'
            if date[0] == '4':
                worker[i] = 'April'
            if date[0] == '5':
                worker[i] = 'May'
            if date[0] == '6':
                worker[i] = 'June'
            if date[0] == '7':
                worker[i] = 'July'
            if date[0] == '8':
                worker[i] = 'August'
            if date[0] == '9':
                worker[i] = 'September'
        else:
            if date[1] == '/':
                worker[i] = 'January'
            if date[1] == '0':
                worker[i] = 'October'
            if date[1] == '1':
                worker[i] = 'November'
            if date[1] == '2':
                worker[i] = 'December'

    for i in range(1, len(worker), 7):
        month_total = worker[i + 4]
        if worker[i] == False:
            continue
        else:
            for j in range(i + 7, len(worker), 7):
                if worker[i] == worker[j]:
                    month_total += worker[j + 4]
                    worker[j] = False
        months.update({worker[i]: month_total})

    first = 0
    for key, value in months.items():
        if first == 0:
            highest_month = key
            month_total = value
            first = 1
        else:
            if value > month_total:
                month_total = value
                highest_month = key

    print(f"Most number of cars sold {highest_total} in {highest_state}.")
    print(f"Maximum amount of sale {month_total} was in {highest_month}.\n")
    print("========================================\n")
    print("===Amount of Sale Based on Car Brands===\n")
    # Question 4

    # sort brand with their total sales

    brand = {}
    sort_totals = []
    for i in range(2, len(worker), 7):
        brand_total = worker[i + 3]
        if worker[i] == False:
            continue
        else:
            for j in range(i + 7, len(worker), 7):
                if worker[i] == worker[j]:
                    brand_total += worker[j + 3]
                    worker[j] = False
        sort_totals.append(brand_total)
        brand.update({worker[i]: brand_total})

    # find top ten brands and other totals
    sort_totals.sort(reverse=True)
    other_total = 0
    sorted_brands = {}

    for money in sort_totals:
        for key, value in brand.items():
            if value == money:
                sorted_brands.update({key: value})
                break

    other = "Other"
    percentage = {other: 0}
    other_percent = 0
    for key, value in sorted_brands.items():
        percent = round((value / grandTotal) * 100, 2)
        if percent > 4.0:
            percentage.update({key: percent})
        else:
            other_percent += percent
            other_percent = round(other_percent, 2)
            percentage.update({other: other_percent})

    for key, value in percentage.items():
        print(f"{key} : {value}%")

    print()
    print("========================================")

    # Make the graphs
    question_two(states)
    question_three(months)
    question_four(percentage)
    question_five(texas_monthly_sales, california_monthly_sales, florida_monthly_sales, ohio_monthly_sales, nevada_monthly_sales)


if __name__ == '__main__':
    main()