
"""
Customer Class
To Do:
- Initialize customer
- Add balance
- Spend balance
- Get balance
- Get customer


"""
from heapq import heappush, heappop
from datetime import datetime
class Customer:
    """
    Customer class 
    Initialize customer with user_name, user_id, and balance
    
    balance should be in format of 
    [
        { "payer": "DANNON", "points":-100 },
        { "payer": "UNILEVER", "points":-200 },
        { "payer": "MILLER COORS", "points":-4,700 }

    ]
    
    """
    def __init__(self, user_id, user_name=""):
        self.user_name = user_name
        self.user_id = user_id
        self.timestamps = []
        self.balance = {} #should be a dictionary for fast access
        
    def add_balance(self, payer, points, timestamp):
        if payer in self.balance: # if payer already exists
            self.balance[payer] += points
        else:   # if payer does not exist
            self.balance[payer] = points
        dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")# convert timestamp to datetime object
        heappush(self.timestamps, [dt, payer, points])# push timestamp, payer, and points to heapq and sort by time
        return 200
    
    def spend_balance(self, amount):
        
        return 200
    
    def get_balance(self):
        return 200
    
    def get_customer(self, user_id):
        return 200
        
        