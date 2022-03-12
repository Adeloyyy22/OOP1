class Balance:

    amount =0


balance_1 = Balance()
balance_1.amount=5000

class Person(Balance):
    first_name = None
    last_name= None
    number = None

jack = Person()
jack.first_name ='jack'
jack.last_name ='Moroko'
jack.number ='+454326421'
jack.amount = 23123


jack.amount= jack.amount + 213
print(jack.amount)