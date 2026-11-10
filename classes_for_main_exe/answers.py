from classes_for_main_exe.class_PaymentMethod import *
import classes_for_main_exe.class_CreditCard as c
import classes_for_main_exe.class_Paypal as pa
import classes_for_main_exe.class_ApplePay as a
import classes_for_main_exe.class_Character as ch
import classes_for_main_exe.class_Mage as m
import classes_for_main_exe.class_Warrior as w




for i in range(6):
    if i == 0:
        print("welcome")

    if i == 1:
        print("answer 1")
        for method in [c.CreditCard(), pa.Paypal()]:
            print(PaymentMethod.checkout(method, 100))
    if i == 2:
        print("answer 2")
        for method in [c.CreditCard(), pa.Paypal(), a.ApplePay()]:
            print(PaymentMethod.checkout(method, 100))
    if i == 3:
        print("answer 3")
        conan = w.Warrior("Conan", 100)
        merlin = m.Mage("Merlin", 60)
        ch.attack(conan, merlin)
        ch.attack(merlin, conan)
        print(merlin.name, merlin.health)
        print(conan.name, conan.health)
    if i == 4:
        print("answer 4")
        print("הפןנקציה תעבוד על שניהם מהסיבה שלשניהם יש פןנקציה speak")
        print("duck הוא אובייקט של המחלקה duck")
    if i == 5:
        print("answer 5")
        



