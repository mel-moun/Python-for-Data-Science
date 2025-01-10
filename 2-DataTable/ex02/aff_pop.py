from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def suffix(x):
    """
    Converts population values with suffixes
    ('M', 'k') into scientific notation.
    """
    try:
        x = str(x).replace('M', 'e+06').replace('k', 'e+03')
    except AttributeError:
        pass
    return x


def change_y(x, pos):
    """
    Formats y-axis tick labels to display
    population values in millions (e.g., '10M').
    """
    return str(int(round(x / 1e6, 0))) + "M"


def main():
    """
    Visualizes population projections
    for selected countries using a line plot.
    """
    try:
        data = load("../population_total.csv")

        country = data.loc[['Belgium', 'Morocco']]
        country = country.applymap(suffix) \
            .astype('float64') \
            .transpose()

        country.index = country.index.astype(np.int64)
        country = country[country.index >= 1800]
        country = country[country.index <= 2050]

        ax = sns.lineplot(data=country, dashes=False, palette=['b', 'g'])
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(np.arange(1800, 2050, 40))
        plt.yticks(np.arange(20000000, 80000000, 20000000))
        ax.yaxis.set_major_formatter(change_y)
        plt.legend(loc='lower right')
        plt.title('Population Projections')
        plt.show()

    except Exception as e:
        print(type(e).__name__, ":", e)


if __name__ == "__main__":
    main()
