import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    data = load('../life_expectancy_years.csv')

    france_data = data.loc['France']

    years = france_data.index.astype(int)
    life_expectancy = france_data.values

    plt.plot(years, life_expectancy)
    plt.title('France life expectancy projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.show()


if __name__ == "__main__":
    main()
