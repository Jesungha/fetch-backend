
"""
Customer Class
To Do:
- Initialize customer
- Add balance
- Spend balance
- Get balance
- Get customer


"""

class Customer:
    
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.balance = []
        
    def add_balance(self, payer, points, timestamp):
        self.balance.append({"payer": payer, "points": points, "timestamp": timestamp})
        return 200
    
    def spend_balance(self, amount):
        return 200
    
    def get_balance(self):
        return 200
        
        