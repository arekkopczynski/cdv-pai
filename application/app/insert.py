from app import base

example_data = [
    ['samochod', 1230],
    ['mieszkanie', 1990],
    ['jedzenie', 600]
]

for x in range(0,3):
    example_transaction = base.Expenses(example_data[x][0], example_data[x][1])
    base.db.session.add(example_transaction)

base.db.session.commit()
