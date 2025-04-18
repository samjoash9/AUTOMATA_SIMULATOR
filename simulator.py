from utils import *

# starting state
q0 = State('q0', {'<': 'q1'}, {'initial'})
q1 = State('q1', {'p':'q2', 's':'q17', 'q':'q18', 'i':'q24', 'b':'q31', 'u':'q38', 'h':'q50'}, 'normal')

# p tags
q2 = State('q2', {'>':'q3'}, 'normal')
q3 = State('q3', {'h': 'q3','P': 'q3','W': 'q3','N': 'q3','U': 'q3','L': 'q3','S': 'q3','>': 'q3','/': 'q3','<': 'q8','?': 'q3', '!': 'q3'}, 'normal')
q8 = State('q8', {'h': 'q8','P': 'q3','W': 'q3','N': 'q3','U': 'q3','S': 'q3','>': 'q3','/':'q5', '<':'q8'}, 'normal')
q5 = State('q5', {'p':'q6'}, 'normal')
q6 = State('q6', {'>':'q7'}, 'normal')

# s tags
q17 = State('q17', {'>':'q10'}, 'normal')
q10 = State('q10', {'h': 'q10','P': 'q10','W': 'q10','N': 'q10','U': 'q10','L': 'q10','S': 'q10','>': 'q10','/': 'q10','<': 'q12','?': 'q10', '!': 'q10'}, 'normal')
q12 = State('q12', {'h': 'q12','P': 'q10','W': 'q10','N': 'q10','U': 'q10','S': 'q10','>': 'q10','/':'q13', '<': 'q12'}, 'normal')
q13 = State('q13', {'s':'q15'}, 'normal')
q15 = State('q15', {'>':'q7'}, 'normal')

# q tags
q18 = State('q18', {'>': 'q19'}, 'normal')
q19 = State('q19', {'h': 'q19','P': 'q19','W': 'q19','N': 'q19','U': 'q19','L': 'q19','S': 'q19','>': 'q19','/': 'q19','<': 'q21', '?': 'q19', '!': 'q19'}, 'normal')
q21 = State('q21', {'h': 'q21','P': 'q19','W': 'q19','N': 'q19','U': 'q19','S': 'q19','>': 'q19','/': 'q22', '<': 'q21'}, 'normal')
q22 = State('q22', {'q': 'q23'}, 'normal')
q23 = State('q23', {'>': 'q7'}, 'normal')

# i tags
q24 = State('q24', {'>': 'q25'}, 'normal')
q25 = State('q25', {'h': 'q25','P': 'q25','W': 'q25','N': 'q25','U': 'q25','L': 'q25','S': 'q25','>': 'q25','/': 'q25','<': 'q27', '?': 'q25', '!': 'q25'}, 'normal')
q27 = State('q27', {'h': 'q27','P': 'q25','W': 'q25','N': 'q25','U': 'q25','S': 'q25','>': 'q25','/': 'q28', '<': 'q27'}, 'normal')
q28 = State('q28', {'i': 'q30'}, 'normal')
q30 = State('q30', {'>': 'q7'}, 'normal')

# b tags
q31 = State('q31', {'>': 'q32'}, 'normal')
q32 = State('q32', {'h': 'q32','P': 'q32','W': 'q32','N': 'q32','U': 'q32','L': 'q32','S': 'q32','>': 'q32','/': 'q32','<': 'q34', '?': 'q32', '!': 'q32'}, 'normal')
q34 = State('q34', {'h': 'q34','P': 'q32','W': 'q32','N': 'q32','U': 'q32','S': 'q32','>': 'q32','/': 'q35', '<': 'q34'}, 'normal')
q35 = State('q35', {'b': 'q37'}, 'normal')
q37 = State('q37', {'>': 'q7'}, 'normal')

# u tags
q38 = State('q38', {'>': 'q39'}, 'normal')
q39 = State('q39', {'h': 'q39','P': 'q39','W': 'q39','N': 'q39','U': 'q39','L': 'q39','S': 'q39','>': 'q39','/': 'q39','<': 'q40', '?': 'q39', '!': 'q39'}, 'normal')
q40 = State('q40', {'h': 'q40','P': 'q39','W': 'q39','N': 'q39','U': 'q39','S': 'q39','>': 'q39','/': 'q41', '<': 'q40'}, 'normal')
q41 = State('q41', {'u': 'q42'}, 'normal')
q42 = State('q42', {'>': 'q7'}, 'normal')

# h1 tags
q50 = State('q50', {'>': 'q46'}, 'normal')
q46 = State('q46', {'h': 'q46','P': 'q46','W': 'q46','N': 'q46','U': 'q46','L': 'q46','S': 'q46','>': 'q46','/': 'q46','<': 'q47', '?': 'q46', '!': 'q46'}, 'normal')
q47 = State('q47', {'h': 'q47','P': 'q46','W': 'q46','N': 'q46','U': 'q46','S': 'q46','>': 'q46','/': 'q48', '<': 'q47'}, 'normal')
q48 = State('q48', {'h': 'q49'}, 'normal')
q49 = State('q49', {'>': 'q7'}, 'normal')

# the final state
q7 = State('q7', {}, 'final')

states = {
    # Entry & universal flow
    'q0': q0,
    'q1': q1,
    'q7': q7,

    # p tags
    'q2': q2,
    'q3': q3,
    'q5': q5,
    'q6': q6,
    'q8': q8,

    # s tags
    'q17': q17,
    'q10': q10,
    'q12': q12,
    'q13': q13,
    'q15': q15,

    # q tags
    'q18': q18,
    'q19': q19,
    'q21': q21,
    'q22': q22,
    'q23': q23,

    # i tags
    'q24': q24,
    'q25': q25,
    'q27': q27,
    'q28': q28,
    'q30': q30,

    # b tags
    'q31': q31,
    'q32': q32,
    'q34': q34,
    'q35': q35,
    'q37': q37,

    # u tags
    'q38': q38,
    'q39': q39,
    'q40': q40,
    'q41': q41,
    'q42': q42,

    # h tags
    'q50': q50,
    'q46': q46,
    'q47': q47,
    'q48': q48,
    'q49': q49,
}

# recursive approach
def simulate_states(state, input_string, i):
    # print current state
    print("(" + str(state.name) + ")->", end="")

    # BASE CASE: check if it is the final state
    if state.type == 'final':
        return True
    
    # check outgoing states
    if len(state.outgoing) == 0:
        return False

    if input_string[i] in state.outgoing.keys():        
        # go to that state
        return simulate_states(states[state.outgoing[input_string[i]]], input_string, i+1)

    return False

def main():
    input_string = input('Please input an HTML tag (p, q, i, s, b, u, h1): ')
    input_string = process_input_string(input_string)

    if input_string == False:
        print('Invalid input')
    else:
        print('->',end="")
        res = simulate_states(q0, input_string, 0)

        if res == True:
            print('Accepted')
        else:
            print('Rejected')