class Category:
    def __init__(self, name, keywords):
        self.name = name
        self.balance = 0
        self.keywords = keywords

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

def categorizedBalance(categories, movements):
    values = {}
    for category in categories:
        if(category[0] != "Deposit"):
            values[category[0]] = 0.0

    for move in movements:
        category = move[3]
        if (category != "Deposit"):
            amount = move[2]
            values[category] -= amount

    return values