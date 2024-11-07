from utility import *
inputs =[ask('a unit of time'),
         ask('an adjective'),
         ask('a noun'),
         ask('a pronoun(posessive)'),
         ask('another adjective'), 
         ask('a plural noun'),
         ask('a verb (past)'),
         ask('a verb'),
         ask('an adjective'),
         ask('a noun'),
         ask('a pronoun(posessive)'),
         ask('another noun'),
         ask('an emotion'),
         ask('a verb (past)')]
        

story=f'''Once, many {inputs[0]} ago, there was a/n {inputs[1]} {inputs[2]}.
The {inputs[2]} and {inputs[3]} {inputs[4]} {inputs[5]} {inputs[6]} to {inputs[7]} a/n {inputs[8]} {inputs[9]}.
the {inputs[9]}, however, became aware of {inputs[10]} {inputs[11]}, and became {inputs[12]}.
When the {inputs[8]} {inputs[9]} met the {inputs[2]} and {inputs[3]} {inputs[4]} {inputs[5]}, they {inputs[13]}
'''
print(story)