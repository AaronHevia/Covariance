import numpy as np
x = np.array([9, 15, 25, 14, 10, 18, 0, 16, 5, 19, 16, 20])
y = np.array([39, 56, 93, 61, 50, 75, 32, 85, 42, 70, 66, 80])

def Covariance(x, y):
    # Calculate averages.
    x_average = np.average(x)
    y_average = np.average(y)

    # Difference between each value and mean price.
    x_differences = []
    for value in x:
        x_differences.append(value - x_average)

    y_differences = []
    for value in y:
        y_differences.append(value - y_average)

    # Multiply Results.
    i = 0
    results = []
    for i in range(len(x_differences)):
        results.append(x_differences[i] * y_differences[i])
    
    return (sum(results)/(len(x_differences) - 1))

print (Covariance(x, y))