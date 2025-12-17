from ....cdm16.target_instructions import (
    Handler,
    op2
)

handlers = [
    Handler(op2, {'muls':14, 'mulu':15})
]
