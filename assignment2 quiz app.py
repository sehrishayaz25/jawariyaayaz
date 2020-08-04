#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Create Quiz App in Python Programming Using List, Dictionary, input, for loop & if statement.

import random

questions = {
            'Who is president of Pakistan?':
            ('\na. Asif Zardari\nb. Bilawal Bhutto\nc. Nawaz Sharif\nd. Arif Ulwi\n', 'd'),
            'Who is the prime minister of Pakistan?':
           ('\na. Asif Zardari\nb. Bilawal Bhutto\nc. Imran Khan\nd. Arif Ulwi\n', 'c'),
            }
def ask_question(questions):
    '''Asks random question from 'questions 'dictionary and returns
       players's attempt and correct answer.'''

    item = random.choice(list(questions.items()))
    question = item[0]
    (variants, answer) = item[1]
    print(question, variants)
    attempt = input('\nHit \'a\', \'b\', \'c\' or \'d\' for your answer\n')
    return (attempt, answer)

tries = 0
for questions_number in range(5):
    while True: 
        attempt, answer = ask_question(questions)
        if attempt not in {'a', 'b', 'c', 'd'}:
            print('INVALID INPUT!!! Only hit \'y\' or \'n\' for your response')
        elif attempt == answer:
            print('Correct')
            stop_asking = False
            break
        elif tries == 1:    
            print('Incorrect!!! You ran out of your attempts')
            stop_asking = True
            break
        else:
            tries += 1
            print('Incorrect!!! Try again.')
    if stop_asking:
        break


# In[ ]:




