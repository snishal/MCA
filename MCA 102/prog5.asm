DATA SEGMENT

    arr db 5 dup(?)
    inputMsg db 10,13,"Input Array : ",24h
    searchMsg db 10,13,"Search Number : ",24h
    foundMsg db 10,13,"Found",24h
    notFoundMsg db 10,13,"notFound",24h
    
DATA ENDS

CODE SEGMENT
    assume CS:CODE, DS:DATA

start:
    MOV AX, DATA
    MOV DS, AX
    
    LEA DX, inputMsg
    MOV AH,09h
    int 21h
    
    MOV CX, 05H
    
    MOV AH, 01H
    LEA SI, arr
    call input
    
    LEA DX, searchMsg
    MOV AH,09h
    int 21h
    
    MOV AH, 01H
    int 21H
    
    MOV CX, 05H
    LEA SI, arr
    
    call find
           
    hlt 
    
    input:
        int 21H
        MOV [SI], al
        inc SI
        loop input
        
        ret
        
    find:
        CMP AL, [SI]
        JE found
        INC SI
        
        loop find    
        
        notfound:
          LEA DX, notFoundMsg
          MOV AH,09h
          int 21h        
          
        ret
        
    found:
       LEA DX, foundMsg
       MOV AH,09h
       int 21h        
       hlt

CODE ends
end start