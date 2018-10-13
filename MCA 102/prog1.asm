DATA SEGMENT
    arr DW 0000H, 0001H, 0002H, 0003H, 0004H
    arrC DW 5 DUP(?)
    
DATA ENDS

CODE SEGMENT
    assume CS:CODE, DS:DATA

start:
    MOV AX, DATA
    MOV DS, AX
    
    MOV CX, 5
    MOV SI, 0
        
    complement:
        MOV AX, arr[SI]
        NOT AX
        INC AX
        MOV arrC[SI], AX
        ADD SI, 2
        LOOP complement

CODE ends
end start