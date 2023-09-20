import json

def load_state():
    try:
        file = open("state.json","r")
    except FileNotFoundError:
        file = open("state.json","w")
        file.write("{}")
        file.close()
        file = open("state.json","r")
    state = json.load(file)
    file.close()
    return state

def save_state(state):
    # write state.json
    file = open("state.json","w")
    json.dump(state,file)
    file.close()

