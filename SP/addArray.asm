DATA segment
    arr dw 1,2,3,4,5
    s dw 5
    res dw ?
DATA ends

CODE segment
    assume DS:DATA, CS:CODE
    
start:
    MOV AX, DATA
    MOV DS, AX
    
    MOV AX, 0
    MOV SI, 0
    MOV CX, s
    
addArray:
    ADD AX, arr[SI]
    INC SI
    loop addArray
    
    MOV res, AX
CODE ends
end start