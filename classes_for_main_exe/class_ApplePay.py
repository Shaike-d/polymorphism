import classes_for_main_exe.class_PaymentMethod as p
class ApplePay(p.PaymentMethod):

    def pay(self, amount):
        return "Paid with Apple Pay " + str(amount)
