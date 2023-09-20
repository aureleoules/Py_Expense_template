from PyInquirer import prompt
from state import load_state,save_state

def show_status():
    state = load_state()

    debts = {}


    # calcule les dettes betement pour chaque personne, les dettes sont equitables
    for expense in state['expenses']:
        amount_per_person = float(expense['amount']) / len(expense['people'])
        for person in expense['people']:
            if person == expense['spender']:
                continue
            if person not in debts:
                debts[person] = {}
            if expense['spender'] not in debts[person]:
                debts[person][expense['spender']] = 0
            debts[person][expense['spender']] += amount_per_person

    # annule les dettes entre deux personnes mutuellement
    for person in debts:
        for spender in debts[person]:
            if spender in debts and person in debts[spender]:
                if debts[spender][person] > debts[person][spender]:
                    debts[spender][person] -= debts[person][spender]
                    debts[person][spender] = 0
                else:
                    debts[person][spender] -= debts[spender][person]
                    debts[spender][person] = 0


    # affiche les dettes
    for person in debts:
        for spender in debts[person]:
            print("{} owes {} to {}".format(person, debts[person][spender], spender))