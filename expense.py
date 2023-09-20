from PyInquirer import prompt
import json
from state import load_state,save_state

def new_expense(*args):
    state = load_state()
    if 'users' not in state:
        state['users'] = []
    
    if len(state['users']) == 0:
        print("No users registered.")
        return False

    expense_questions = [
        {
            "type":"input",
            "name":"amount",
            "message":"New Expense - Amount: ",
        },
        {
            "type":"input",
            "name":"label",
            "message":"New Expense - Label: ",
        },
        {
            "type":"list",
            "name":"spender",
            "message":"New Expense - Spender: ",
            "choices": state['users']
        },
    ]
    infos = prompt(expense_questions)

    # ask for people involved

    people_questions = [
        {
            "type":"checkbox",
            "name":"people",
            "message":"New Expense - People: ",
            "choices": state['users'],
            "multiselect":True,
        }
    ]

    infos['people'] = prompt(people_questions)['people']

    if 'expenses' not in state:
        state['expenses'] = []
    
    state['expenses'].append(infos)
    save_state(state)
    return True


