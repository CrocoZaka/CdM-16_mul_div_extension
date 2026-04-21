asect 0x00
dw start
dw 0
align 0x80

start:
ldi r0, 2
ldi r1,-1
smul r0,r1

ldi r2, 2
ldi r3,-2
smul r0,r1
  
ldi r0, 2
ldi r1, 3
umul r0,r1

ldi r2, 2
ldi r3,-1
sdiv r0,r1

ldi r2, 2
ldi r3,-2
sdiv r0,r1

ldi r2, 2
ldi r3, 3
udiv r0,r1

ldi r0,-1
ldi r1, 2
smul r0,r1

ldi r0,2
ldi r1,4
dw 0x4301 #umul r0,r1

ldi r2,9
ldi r3,3
udiv r3,r2

ldi r2,10
ldi r3,3
udiv r3,r2


ldi r0,0
ldi r1,0
ldi r2,0
ldi r3,0
ldi r4,0
ldi r5,0
ldi r6,0

ldi r2,15
ldi r3,6
udiv r2,r3

while_loop:
ldi r0,3
br while_loop
halt
end
