from load_csv import load
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def suffix(x):
    """
    Converts GDP values with suffixes
    ('M', 'k') into scientific notation.
    """
    try:
        x = str(x).replace('M', 'e+06').replace('k', 'e+03')
    except AttributeError:
        pass
    return x


def change_x(x, pos):
    """
    Formats x-axis tick labels to display
    GDP values in thousands (e.g., '10k').
    """
    return str(int(round(x / 1e3, 0))) + "k"


def main():
    """
    Creates a scatter plot to visualize the
    relationship between GDP per capital
    and life expectancy for various countries in the year 1900.
    """
    try:
        gdp = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        expectancy = load("../life_expectancy_years.csv")

        gdp_1900 = gdp.loc[:, '1900'].apply(suffix).astype('float64')
        expectancy_1900 = expectancy.loc[:, '1900'].astype('float64')

        combined_data = pd.DataFrame({
            'GDP per Capita (PPP, 1900)': gdp_1900,
            'Life Expectancy (1900)': expectancy_1900
        }).dropna()

        plt.figure(figsize=(6.4, 4.8))
        ax = sns.scatterplot(
            x='GDP per Capita (PPP, 1900)',
            y='Life Expectancy (1900)',
            data=combined_data,
            alpha=0.8
        )

        plt.title('1900', fontsize=16)
        plt.xlabel('Gross domestic product', fontsize=14)
        plt.ylabel('Life Expectancy', fontsize=14)
        plt.xscale('log')
        ax.xaxis.set_major_formatter(change_x)
        plt.legend(['Country'], loc='upper left')
        plt.show()

    except Exception as e:
        print(type(e).__name__, ":", e)


if __name__ == "__main__":
    main()
