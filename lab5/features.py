'''
    Returns the features in a dictionary format compatible with scikit-learn. 
    (You have a code example of feature encoding in this format in the chunking program.)
'''
def extract(stack, queue, graph, feature_names, sentence):
    features = "poop"
    return features

if __name__ == '__main__':
    features_1 = ['w_1_STACK', 'pos_1_STACK', 'w_1_QUEUE', 'pos_1_QUEUE', 
                  'can_left_arc', 'can_reduce']

    features_2 = features_1 + ['w_2_STACK', 'pos_2_STACK','w_2_QUEUE', 'pos_2_QUEUE']
                
                '''['w_1_STACK', 'pos_1_STACK', 'w_2_STACK', 'pos_2_STACK', 
                  'w_1_QUEUE', 'pos_1_QUEUE', 'w_2_QUEUE', 'pos_2_QUEUE',
                  'can_left_arc', 'can_reduce']'''
    features_3 = features_2 + ['w_TOP_plus_1', 'pos_TOP_plus_1', 'pos_1_STACK_h', 'lex_1_STACK_rs']
                
                '''['w_1_STACK', 'pos_1_STACK', 'w_2_STACK', 'pos_2_STACK', 
                  'w_1_QUEUE', 'pos_1_QUEUE', 'w_2_QUEUE', 'pos_2_QUEUE',
                  'can_left_arc', 'can_reduce', 
                  'w_', 'pos_', 
                  'pos_1_STACK_h', 'lex_1_STACK_rs']''' #POS STACK 1 h, LEX STACK 1 rs (good performance in http://www.aclweb.org/anthology/C/C10/C10-1093.pdf )
                #word['head'] where sentence['id'] == id[TOP_form]+1
                #POS STACK 1 h = the part-of-speech of the head of the second value on the stack
                #LEX STACK 1 rs = the lexical value of the right sibling of the second value on the stack 
                #http://maltparser.org/userguide.html


#Generate the three scikit-learn models using the code models from the chunking labs. 
 

# You will evaluate the model accuracies (not the parsing accuracy) using 
# the classification report produced by scikit-learn and the correctly classified instances 