class PaymentMethod:
    # def __init__(self, owner):
    #     self.owner = owner 

    def pay(self,amount):
        raise NotImplementedError("every payment method must implement pay()")
    
    def fee(self,amount):
        return 0 

    def checkout(method,amount):
        return method.pay(amount), "| fee:", method.fee(amount)

