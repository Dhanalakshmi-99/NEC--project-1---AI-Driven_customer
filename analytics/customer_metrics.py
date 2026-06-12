import pandas as pd


class CustomerMetrics:

    @staticmethod
    def total_customers(df):
        return len(df)

    @staticmethod
    def average_income(df):
        return round(df['income'].mean(), 2)

    @staticmethod
    def total_revenue(df):
        return df['income'].sum()

    @staticmethod
    def average_tenure(df):
        return round(df['tenure'].mean(), 2)

    @staticmethod
    def gender_distribution(df):
        return df['gender'].value_counts()

    @staticmethod
    def city_distribution(df):
        return df['city'].value_counts()