class FeatureEngineering:

    @staticmethod
    def income_category(df):

        df['income_category'] = df[
            'income'
        ].apply(
            lambda x:
            "Low"
            if x < 50000
            else
            "Medium"
            if x < 100000
            else
            "High"
        )

        return df

    @staticmethod
    def loyalty_score(df):

        df['loyalty_score'] = (
            df['tenure'] * 0.5
        )

        return df