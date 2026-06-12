import pandas as pd


class RecommendationEngine:

    def recommend(self, customer_data):

        income = customer_data["income"]

        if income > 100000:
            return [
                "Premium Membership",
                "Luxury Products",
                "VIP Offers"
            ]

        elif income > 60000:
            return [
                "Gold Membership",
                "Seasonal Discounts"
            ]

        else:
            return [
                "Discount Coupons",
                "Budget Products"
            ]