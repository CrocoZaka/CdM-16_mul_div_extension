from ....cdm16.target_instructions import (
    Handler,
    op1,
    op2
)

handlers = [
    Handler(op1, {'pop': 1, 'jsrr': 3, 'ldsp': 4, 'stsp': 5, 'ldps': 6, 'stps': 7, 'ldpc': 8, 'stpc': 9, 'ldssp': 14,
                  'stssp': 15}),
    Handler(op2, {'move': 0, 'swpw': 2, 'swpb': 3})
]
