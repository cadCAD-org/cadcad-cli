from model.updates import *

psubs = [
    { 
        'policies': {
        },
        'states': {
            'box_A': update_A,
            'box_B': update_B
        }
    }
]
