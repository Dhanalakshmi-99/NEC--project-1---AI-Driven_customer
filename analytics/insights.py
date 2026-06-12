class CustomerInsights:

    @staticmethod
    def generate(customer):

        income = customer['income']
        tenure = customer['tenure']

        if income > 100000:
            segment = "Premium Customer"

        elif income > 60000:
            segment = "Gold Customer"

        else:
            segment = "Regular Customer"

        if tenure > 36:
            loyalty = "Highly Loyal"

        elif tenure > 12:
            loyalty = "Moderately Loyal"

        else:
            loyalty = "New Customer"

        return {
            "segment": segment,
            "loyalty": loyalty,
            "recommendation":
                f"Offer personalized promotions for {segment}"
        }