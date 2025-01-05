import matplotlib.pyplot as plt
from load_csv import load


def main():
    data = load('../life_expectancy_years.csv')

    country = 'Morocco'
    country = data.loc[country]

    years = country.index.astype(int)
    life_expectancy = country.values

    plt.plot(years, life_expectancy)
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.legend([country.name])
    plt.show()


if __name__ == "__main__":
    main()
