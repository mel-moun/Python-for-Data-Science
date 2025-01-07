from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def change_suffix(x):
    if isinstance(x, str):
        x = x.replace('M', 'e+06').replace('k', 'e+03')
    return x


def y_formatter(x, pos):
    return str(int(round(x / 1e6, 0))) + "M"


def main():
    try:
        data = load("../population_total.csv")

        country_data = data.loc[['Belgium', 'France']]
        country_data = country_data.applymap(change_suffix) \
            .astype('float64') \
            .transpose()

        country_data.index = country_data.index.astype(np.int64)
        country_data = country_data[country_data.index >= 1800]
        country_data = country_data[country_data.index <= 2050]

        ax = sns.lineplot(data=country_data, dashes=False, palette=['b', 'g'])
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(np.arange(1800, 2050, 40))
        plt.yticks(np.arange(20000000, 80000000, 20000000))
        ax.yaxis.set_major_formatter(y_formatter)
        plt.legend(loc='lower right')
        plt.title('Population Projections')
        plt.show()

    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        return None


if __name__ == "__main__":
    main()
