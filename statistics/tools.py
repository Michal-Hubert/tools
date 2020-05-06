import scipy.stats as stats


# Sort distributions according to how close they are to input_data.
# The closest one to input_data is at the beginning.
def sort_distributions(input_data):
    # See https://docs.scipy.org/doc/scipy/reference/stats.html
    distributions = ["exponweib", "norm", "pareto", "uniform", "logistic"]
    distribution_scoring = []
    distribution_parameters = {}
    for distribution_name in distributions:
        distribution = getattr(stats, distribution_name)

        # See https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.fit.html
        # See https://www.spcforexcel.com/knowledge/basic-statistics/distribution-fitting
        shape_param = distribution.fit(input_data)
        
        distribution_parameters[distribution_name] = shape_param
        _, pvalue = stats.kstest(input_data, distribution_name, args=shape_param)
        distribution_scoring.append((distribution_name, pvalue))

    distribution_scoring.sort(key=lambda element: element[1], reverse=True)
    for elem in distribution_scoring:
        print("distribution:", elem[0], " p-value:", elem[1], "parameters:", distribution_parameters[elem[0]])


data = []
for i in range(1000):
    data.append(i)

sort_distributions(data)
