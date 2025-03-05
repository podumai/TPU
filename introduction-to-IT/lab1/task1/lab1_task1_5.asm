ORG 100h

val_a EQU 2
val_b EQU -1
val_c EQU 5
bit_mask EQU 0111111111111111b
bit_rotate EQU 2

DIV_CONST DW 2

main:
    PUSH BP
    MOV BP, SP
    
    MOV AX, val_a 
    MOV DI, val_b
    MOV CX, val_c
    
    SUB DI, CX
    IMUL CX
    DEC DI
    IDIV DIV_CONST
    AND AX, bit_mask
    OR AX, 1
    ROL AX, bit_rotate

    MOV SP, BP
    POP BP
    RET
END