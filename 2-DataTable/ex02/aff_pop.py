import matplotlib.pyplot as plt
from load_csv import load

def main():
    data = load('../life_expectancy_years.csv')

    countries = ['Belgium', 'France']
    start_year = 1800
    end_year = 2050

    plt.figure()

    for country_name in countries:
        country = data.loc[country_name]
        country = country.loc[str(start_year):str(end_year)]
        years = country.index.astype(int)
        life_expectancy = country.values

        plt.plot(years, life_expectancy, label=country_name)

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(range(start_year, end_year + 1, 40))
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
