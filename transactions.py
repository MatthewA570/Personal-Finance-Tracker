class Transaction:
    def __init__(self, category, cost, date):
        self.category = category
        self.cost = cost
        self.date = date

    def get_category(self):
        return self.category
    
    def get_cost(self):
        return self.cost
    
    def get_date(self):
        return self.date
    
    def set_date(self, new_date):
        self.date = new_date

    def set_cost(self, new_cost):
        self.cost = new_cost

    def set_category(self, new_category):
        self.category = new_category
