asect 0x00
dw start
dw 0
align 0x80

start:
ldi r5,1 # r5- test counter
ldi r0, 2
ldi r1,-1
smul r0,r1

ldi r5,2 # r5- test counter
ldi r0, 2
ldi r1,-1
sdiv r0,r1

ldi r5,3 # r5- test counter
ldi r0,-1
ldi r1, 2
smul r0,r1

ldi r5,4 # r5- test counter
ldi r0,2
ldi r1,4
dw 0x4301 #umul r0,r1

ldi r5,5 # r5- test counter
ldi r0,9
ldi r1,3
dw  0x4381 #udiv r3,r2

ldi r5,6 # r5- test counter
ldi r4,3
ldi r5,5
dw 0x4325 #umul r4,r5

ldi r5,7 # r5- test counter
ldi r3,2
ldi r4,4
dw 0x431c #umul r3,r4

ldi r0,0
ldi r1,0
ldi r2,0
ldi r3,0
ldi r4,0
ldi r5,0
ldi r6,0

ldi r5,8 # r5- test counter
ldi r3,15
ldi r4,6
dw 0x439c #udiv r3,r4

ldi r5,9 # r5- test counter
while_loop:
ldi r0,3
br while_loop
halt
end
