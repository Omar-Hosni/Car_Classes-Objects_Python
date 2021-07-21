class Car:

    def __init__(self, model, price, name, isclosed):
        self.model = model
        self.price = price
        self.name = name
        self.isclosed = isclosed

    def insurance_price(self):
         if(self.model>2010 and self.model<2020) and (self.price>6000 and self.price<17000):
            total_cost = self.price + (self.price*0.05)
            insurance_cost = self.price*0.05
            print('the insurance cost is 5% of car price which equals %s' % insurance_cost)
            print('the price after insurance is %s ' % total_cost)
            return insurance_cost
         else:
            insurance_cost2 = self.price*0.07
            print('the insurance price is worth 7% of the car which equals %s' % insurance_cost2)
            return insurance_cost2


     def doors_status(self):
        if(self.isclosed == True):
         return True
        else:
         return False


    def car_details(self):
            print('the model is %s , and it costs %s ' % self.model % self.price)



Tesla = Car('Model X' , 67000 , 'Tesla', True)
Tesla.car_details()
