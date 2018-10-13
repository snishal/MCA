DATA SEGMENT
    unpacked DD 05060708H
             DD 01020304H
             DD 05060708H
             DD 01020304H
    packed DD ?
           DD ?
DATA ENDS

CODE SEGMENT
    assume CS:CODE, DS:DATA

start:
    MOV AX, DATA
    MOV DS, AX
    
    MOV CX, 8
    MOV SI, 0
    MOV DI, 0
    convert:
        MOV AX, 0
        MOV AX, WORD PTR unpacked + SI
        SHL AH, 4
        ADD AL, AH
        MOV BYTE PTR packed + DI, AL
        ADD SI, 2
        INC DI
        LOOP convert
    

CODE ends
end start