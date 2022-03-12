from random import randint
from operator import itemgetter
MJEs = {'MJE1': randint(140632,140766),
        'MJE2': randint(140632,140766),
        'MJE3': randint(140632,140766),
        'MJE4': randint(140632,140766)}
ranking = list()
print('Documentação Suporte de Auditoria:')
for k, v in MJEs.items():
    print(f'Solicitar documentação suporte para o {k} de número {v} .')
    print('-='*30)
