from ....cdm16.target_instructions import (
    Handler,
    op2
)

handlers = [
    Handler(op2, {'udiv':12,'sdiv':13,'umul':14, 'smul':15})
]
