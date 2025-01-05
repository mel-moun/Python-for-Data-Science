import matplotlib.pyplot as plt
from load_csv import load


def main():
    data = load('../life_expectancy_years.csv')

    country = 'Belgium'
    country = data.loc[country]

    years = country.index.astype(int)
    life_expectancy = country.values

    country_two = 'France'
    country_two = data.loc[country_two]

    years_two = country_two.index.astype(int)
    life_expectancy_two = country_two.values

    plt.plot(years, life_expectancy, label=country.name, color='blue')
    plt.plot(years_two, life_expectancy_two, label=country_two.name, color='red')
    plt.title('Life Expectancy Comparison')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
