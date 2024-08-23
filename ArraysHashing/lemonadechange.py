def lemonadeChange(bills):
    account = {"5": 0, "10": 0, "20": 0}
    for bill in bills:
        if bill == 5:
            account["5"] += 1
        elif bill == 10:
            if account["5"] < 0:
                return False
            else:
                account["5"] -= 1
                account["10"] += 1
        elif bill == 20:
            if account["10"] >= 1 and account["5"] >= 1:
                account["10"] -= 1
                account["5"] -= 1
                account["20"] += 1
            elif account["5"] >= 3:
                account["5"] -= 3
                account["20"] += 1
            else:
                return False
    return True

bills_t = [5,5,10,10,20]
print(lemonadeChange(bills_t))