import classes_for_main_exe.class_PaymentMethod as p


class Paypal(p.PaymentMethod):


    def pay(self,amount):
        return "Redirecting to PayPal " + str(amount)
