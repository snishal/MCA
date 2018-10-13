DATA SEGMENT

    arr db 5 dup(?)
    inputMsg db 10,13,"Input Array: ",24h
    searchMsg db 10,13,"Search Number: ",24h
    foundMsg db 10,13,"Found",24h
    notFoundMsg db 10,13,"Not Found",24h
    start db 00h
    mid db ?
    last db 04h
    
DATA ENDS

CODE SEGMENT
    assume CS:CODE, DS:DATA
    
main:
    MOV AX, DATA
    MOV DS, AX
    
    LEA DX,inputMsg
    MOV AH,09h
    int 21h
    
    Mov CX, 05h
    MOV AH,01h
    LEA SI, arr      
           
    call input
    
    LEA DX,searchMsg
    MOV AH,09h
    int 21h
    
    Mov Ah,01h
    int 21h
    
    MOV DL, Al
              
    LEA SI,arr
    
    call binarySearch       
    
    hlt
    
    input:
        int 21h
        MOV [SI], al
        inc SI
        loop input
        ret 
        
    binarySearch:
        MOV AH, 00h
        MOV AL, last
        CMP AL, start
        JL notFound
        ADD AL, start
        Mov Bl, 02h
        DIV BL
        MOV mid, al
        
        MOV AH, 00h
        MOV SI, AX
        cmp arr[si], dl
        je found
        jg updatelast
        jl updatestart
        
        jmp binarySearch
        
    notFound:
        LEA DX,notFoundMsg
        MOV AH,09h
        int 21h
        
        ret   
    
    found:
        LEA DX,foundMsg
        MOV AH,09h
        int 21h
        
        ret   
    
    updatelast:
        MOV Ah, mid
        MOV last, ah
        Sub last, 01h 
        
        jmp binarySearch
        
    updatestart:
        MOV ah, mid
        MOV start, ah
        add start, 01h    
           
        jmp binarySearch

CODE ends
end main