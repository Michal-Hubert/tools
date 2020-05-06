import scipy.stats as stats


# Sort distributions according to how close they are to input data.
# The closest one to data is the first.
def sort_distributions(data):
    # See https://docs.scipy.org/doc/scipy/reference/stats.html
    distributions = ["exponweib", "norm", "pareto", "uniform", "logistic"]
    distribution_scoring = []
    distribution_parameters = {}
    for distribution_name in distributions:
        dist = getattr(stats, distribution_name)
        param = dist.fit(data)
        distribution_parameters[distribution_name] = param
        _, p = stats.kstest(data, distribution_name, args=param)
        distribution_scoring.append((distribution_name, p))

    distribution_scoring.sort(key=lambda elem: elem[1], reverse=True)
    for elem in distribution_scoring:
        print("distribution:", elem[0], " p-value:", elem[1], "parameters:", distribution_parameters[elem[0]])


data = []
for i in range(1000):
    data.append(i)

sort_distributions(data)