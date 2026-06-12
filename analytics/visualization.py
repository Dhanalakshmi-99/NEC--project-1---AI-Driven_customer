import plotly.express as px


class Visualizations:

    @staticmethod
    def income_distribution(df):

        fig = px.histogram(
            df,
            x="income",
            title="Income Distribution"
        )

        return fig

    @staticmethod
    def city_distribution(df):

        fig = px.pie(
            df,
            names="city",
            title="Customer City Distribution"
        )

        return fig

    @staticmethod
    def age_vs_income(df):

        fig = px.scatter(
            df,
            x="age",
            y="income",
            color="gender",
            title="Age vs Income"
        )

        return fig