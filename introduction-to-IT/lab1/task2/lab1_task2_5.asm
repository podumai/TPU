ORG 100h 

val_a EQU 1
val_b EQU 2
val_c EQU 3

DIV_CONST DW 2     

main:
    PUSH BP
    MOV BP, SP
    SUB SP, 6
    
    MOV byte ptr [BP - val_a], -1
    MOV byte ptr [BP - val_b], 2
    MOV byte ptr [BP - val_c], 3
                              
    MOV AL, byte ptr [BP - val_a]
    CBW 
    MOV DI, AX
    CALL valid_a
    TEST AX, AX
    JZ .L3
    MOV AL, byte ptr [BP - val_b]
    CBW
    MOV DI, AX
    CALL valid_b
    TEST AX, AX
    JZ .L3
    MOV AL, byte ptr [BP - val_c]
    CBW
    MOV DI, AX
    CALL valid_c
    TEST AX, AX
    JZ .L3
    
    XOR AX, AX
    MOV AL, byte ptr [BP - val_a]
    CBW
    MOV DI, AX
    MOV AL, byte ptr [BP - val_b]
    CBW
    MOV SI, AX
    MOV AL, byte ptr [BP - val_c]
    CBW
    MOV DX, AX
    CALL eval_expr
    JMP .L4
.L3:
    MOV AX, 1
.L4:

    ADD SP, 6
    MOV BP, SP
    POP BP    
    RET 
    
valid_a PROC
    PUSH BP
    MOV BP, SP
    SUB SP, 6
       
    XOR AX, AX
    CMP DI, -1
    JNZ .L0
    MOV AL, 1
.L0:         
    ADD SP, 6
    MOV BP, SP
    POP BP
    RET
valid_a ENDP      
    
valid_b PROC
    PUSH BP
    MOV BP, SP
    SUB SP, 6
    
    XOR AX, AX
    CMP DI, 2
    JNZ .L1
    MOV AL, 1
.L1:         
    ADD SP, 6
    MOV BP, SP
    POP BP
    RET   
valid_b ENDP   
    
valid_c PROC
    PUSH BP
    MOV BP, SP
    SUB SP, 6
    
    XOR AX, AX
    CMP DI, 3
    JNZ .L2
    MOV AL, 1
.L2:         
    ADD SP, 6
    MOV BP, SP
    POP BP
    RET 
valid_c ENDP

eval_expr PROC
    PUSH BP
    MOV BP, SP
    SUB SP, 6
    
    XOR AX, AX
    SUB SI, DX
    MOV AX, DI
    IMUL DX
    DEC SI       
    IDIV DIV_CONST
    ADD AX, SI
    
    ADD SP, 6
    MOV SP, BP
    POP BP
    RET
eval_expr ENDP          
    
END
