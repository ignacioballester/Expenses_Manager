class Category:

    def __init__(self, name, keywords):
        self.name = name
        self.balance = 0
        self.keywords = keywords

    @staticmethod
    def categorize(categories, movement, db):
        categorized = False
        for category in categories:
            splits = str(category[2]).split(", ")
            for string in splits:
                if (movement.description.find(string) != -1):
                    movement.category = category
                    db.updateRow("movements", "category", category[0], movement.id)
                    db.updateRow("categories", "balance", category[1] + movement.amount, category[0])
                    categorized = True
                    break

            if (categorized):
                break

        if (categorized == False):
            movement.category = categories[1]
            balance = db.fetchBalance("Others")[0][0]
            db.updateRow("movements", "category", "Others", movement.id)
            db.updateRow("categories", "balance",  balance+ movement.amount, "Others")

        db.commit()
        # movement.category.balance = round(movement.category.balance, 2)

