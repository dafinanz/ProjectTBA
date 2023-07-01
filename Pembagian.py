def pembagian_m(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
                        'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17'}
        self.symbols = {'0', '1', '-', '+', 'B', 'X', 'Y', 'Z'}
        self.blank_symbol = 'B'
        self.input_symbols = {'0', '1', '-', '+'}
        self.initial_state = 'q0'
        self.accepting_states = {'q17'}
        self.transitions = {
                            ('q0', 'B'): ('q0', 'B', 1),
                            ('q0', '+'): ('q1', 'B', 1),
                            ('q0', '-'): ('q4', 'B', 1),

                            ('q1', '0'): ('q1', '0', 1),
                            ('q1', '1'): ('q1', '1', 1),
                            ('q1', '+'): ('q2', 'Z', 1),
                            ('q1', '-'): ('q5', 'Z', 1),

                            ('q2', '0'): ('q2', '0', 1),
                            ('q2', '1'): ('q2', '1', 1),
                            ('q2', 'B'): ('q3', '+', -1),

                            ('q3', '0'): ('q3', '0', -1),
                            ('q3', '1'): ('q3', '1', -1),
                            ('q3', 'Z'): ('q3', 'Z', -1),
                            ('q3', 'B'): ('q6', 'B', 1),

                            ('q4', '0'): ('q4', '0', 1),
                            ('q4', '1'): ('q4', '1', 1),
                            ('q4', '+'): ('q5', 'Z', 1),
                            ('q4', '-'): ('q2', 'Z', 1),

                            ('q5', '0'): ('q5', '0', 1),
                            ('q5', '1'): ('q5', '1', 1),
                            ('q5', 'B'): ('q3', '-', -1),

                            ('q6', '0'): ('q7', 'B', 1),
                            ('q6', '1'): ('q16', 'B', 1),

                            ('q7', '0'): ('q7', '0', 1),
                            ('q7', '1'): ('q8', '1', 1),

                            ('q8', 'Z'): ('q8', 'Z', 1),
                            ('q8', 'X'): ('q8', 'X', 1),
                            ('q8', '0'): ('q8', '0', 1),
                            ('q8', '1'): ('q9', '1', -1),

                            ('q9', 'X'): ('q9', 'X', -1),
                            ('q9', '0'): ('q10', 'X', -1),
                            ('q9', 'Z'): ('q10', 'Z', -1),

                            ('q10', 'Z'): ('q10', 'Z', -1),
                            ('q10', '0'): ('q11', '0', -1),
                            ('q10', '1'): ('q13', '1', 1),

                            ('q11', '0'): ('q11', '0', -1),
                            ('q11', 'Y'): ('q11', 'Y', -1),
                            ('q11', 'Z'): ('q11', 'Z', -1),
                            ('q11', '1'): ('q12', '1', -1),

                            ('q12', '0'): ('q12', '0', -1),
                            ('q12', 'B'): ('q6', 'B', 1),

                            ('q13', 'Z'): ('q13', 'Z', 1),
                            ('q13', 'X'): ('q13', '0', 1),
                            ('q13', '1'): ('q14', '1', 1),

                            ('q14', 'Y'): ('q14', 'Y', 1),
                            ('q14', '-'): ('q14', '-', 1),
                            ('q14', '+'): ('q14', '+', 1),
                            ('q14', 'B'): ('q15', 'Y', -1),

                            ('q15', 'Y'): ('q15', 'Y', -1),
                            ('q15', '-'): ('q15', '-', -1),
                            ('q15', '+'): ('q15', '+', -1),
                            ('q15', '1'): ('q11', '1', -1),

                            ('q16', '-'): ('q16', '-', 1),
                            ('q16', '+'): ('q16', '+', 1),
                            ('q16', 'Y'): ('q16', '0', 1),
                            ('q16', '0'): ('q16', 'B', 1),
                            ('q16', 'X'): ('q16', 'B', 1),
                            ('q16', '1'): ('q16', 'B', 1),
                            ('q16', 'Z'): ('q16', 'B', 1),
                            ('q16', 'B'): ('q17', 'B', -1),
                            }