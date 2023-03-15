def currency(Inr,curr):
    if curr=="Euro":
        print(Inr*0.01417)
    elif(curr=="British pound"):
        print(Inr*0.0100)
    elif(curr=="Australian Dollar"):
        print(Inr*0.02140)
    elif(curr=="canadian Dollar"):
        print(Inr*0.02027)
    else:
        print("-1")
currency(300,"Euro")
currency(300,"British pound")
currency(300,"Australian Dollar")
currency(300,"canadian Dollar")
