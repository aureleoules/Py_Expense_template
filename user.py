from PyInquirer import prompt
from state import load_state,save_state
user_questions = [
    {
            "type":"input",
            "name":"name",
            "message":"What is you name?",
    },
]

def add_user():
    state = load_state()
    if 'users' not in state:
        state['users'] = []

    user = prompt(user_questions)
    state['users'].append(user)
    save_state(state)
    print("User {} added.".format(user['name']))