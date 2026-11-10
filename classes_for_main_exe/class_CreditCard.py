import classes_for_main_exe.class_PaymentMethod as p


class CreditCard(p.PaymentMethod):


    def pay(self, amount):
        return "Charging card " + str(amount)

def fee(self,amount):
    return amount*0.02


    