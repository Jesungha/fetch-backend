
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
        self.money = 0
        
    def add_balance(self, payer, points, timestamp):
        if points < 0:
            try:
                self.spend_balance(-points)
            except:
                return {"error": "insufficient balance"}
            return
        if payer in self.balance: # if payer already exists
            self.balance[payer] += points
        else:   # if payer does not exist
            self.balance[payer] = points
        dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")# convert timestamp to datetime object
        self.money += points
        heappush(self.timestamps, [dt, payer, points])# push timestamp, payer, and points to heapq and sort by time
    
    def spend_balance(self, amount):
        used_amount = 0 # used_amount is the amount of points used so far
        returnlist = []
        if amount > self.money:
            print(amount, self.money)
            return {"error": "insufficient balance"}
        while amount > used_amount:
            if len(self.timestamps) == 0:
                #need to put it back since transaction is not possible
                for i in returnlist:
                    self.balance[i["payer"]] += -i["points"]
                    self.timestamps.append([i["dt"], i["payer"], -i["points"]])
                return
            dt, payer, points = self.timestamps[0] # set dt, payer, and points to the first element in the heapq
            if amount - used_amount >= points:  # if amount is greater than points pop the first element in the heapq
                used_amount += points
                heappop(self.timestamps)# pop the first element in the heapq
                self.balance[payer] -= points
                tot_point = points
            else:   
                self.balance[payer] -= (amount - used_amount) # 10000 - 4700 = 5300
                self.timestamps[0] =  [dt, payer, points - (amount - used_amount)]# set 0 to new amount 10000 - 4700 = 5300
                tot_point = (amount - used_amount) # = 4700
                used_amount += (amount - used_amount)
            self.money -= tot_point 
            returnlist.append({"dt": dt, "payer": payer, "points": -tot_point})# return to returnlist
                
        return returnlist
    
    def get_balance(self):
        #return balance
        return self.balance
    
    def get_customer(self):
        
        return self
        
        