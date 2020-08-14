def bonAppetit(bill, k, b):
    brianBill = sum(bill)
    bill.pop(k)
    shareBill = sum(bill)

    overCharge = b - (shareBill/2)

    if overCharge == 0:
        return "Bon Appetit"
    return overCharge
