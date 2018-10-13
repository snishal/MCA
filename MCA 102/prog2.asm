DATA SEGMENT
    arr DW 0000H, 0001H, 0002H, 0003H, 000AH
    sum DD 0
    
DATA ENDS

CODE SEGMENT
    assume CS:CODE, DS:DATA

start:
    MOV AX, DATA
    MOV DS, AX
    
    MOV CX, 5
    MOV SI, 0
        
    addArray:
        MOV AX, WORD PTR sum
        MOV DX, WORD PTR sum + 2
        ADD AX, arr[SI]
        ADC DX, 0H
        MOV WORD PTR sum, AX
        MOV WORD PTR sum + 2, DX
        ADD SI, 2
        LOOP addArray

CODE ends
end start