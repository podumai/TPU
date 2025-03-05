ORG 100h

val_a EQU 4  

main:
    PUSH BP
    MOV BP, SP
    SUB SP, 2
    
    MOV word ptr [BP - 2], BX
    
    XOR CX, CX
    XOR DI, DI
    MOV BL, val_a
    
.L0:
    CMP CX, 7
    JZ .L1
    MOV AX, CX
    IDIV BL
    INC DI
    ADD DI, AX
    INC CX
    JMP .L0
.L1:
    
    MOV AX, DI
    MOV BX, word ptr [BP - 2]
    
    ADD SP, 2
    MOV SP, BP
    POP BP
    RET
          
END