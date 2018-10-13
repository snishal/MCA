DATA SEGMENT
    packed DD 12345678H
    unpacked DD 0
DATA ENDS

CODE SEGMENT
    assume CS:CODE, DS:DATA

start:
    MOV AX, DATA
    MOV DS, AX
    
    MOV CX, 4
    MOV SI, 0
    MOV DI, 0
    convert:
        MOV AX, 0
        MOV AL, BYTE PTR packed + SI
        SHL AX, 4
        SHR AL, 4
        MOV WORD PTR unpacked + DI, AX
        INC SI
        ADD DI, 2
        LOOP convert
    

CODE ends
end start