import pickle
import os
from Record import *
from file_function import *

numRecord = 100

def split(n, fileName, f1Name, f2Name):
    '''
        objective: to spilt file f into two files f1 and f2
        input:
            n: size of block
            fileName: file to be splited
            f1Name: name of first file
            f2Name: name of second file
        output: none
    '''
    f = open(fileName, 'rb')
    f1 = open(f1Name, 'wb')
    f2 = open(f2Name, 'wb')

    count = 0
    file = f1

    try:
        while 1:
            if count == 0:
                file = f1
            else:
                file = f2
            
            lst = []
            for i in range(n):
                lst.append(pickle.load(f))

            lst.sort(key = lambda Record:Record.getKey())

            for i in range(n):
                pickle.dump(lst[i], file)

            count = (count + 1) % 2
    except EOFError:
        f.close()
        f1.close()
        f2.close()

def mergeSort(n, f1Name, f2Name, f3Name, f4Name):
    '''
        objective: to mergeSort records of file
        input:
            n: number of records to be read
            f1Name: name of file 1
            f2Name: name of file 2
            f3Name: name of file 3
            f4Name: name of file 4
        output: return number of record that are sorted in f1 and f2
    '''
    if(n >= numRecord/2):
        return n
    else:
        f1 = open(f1Name, 'rb')
        f2 = open(f2Name, 'rb')
        f3 = open(f3Name, 'wb')
        f4 = open(f4Name, 'wb')

        count = 0
        file = f3

        while 1:
            if count == 0:
                file = f3
            else:
                file = f4

            count1 = count2 = 0
            
            try: 
                n1 = pickle.load(f1)
            except EOFError:
                count1 = 2*n
            
            try: 
                n2 = pickle.load(f2)
            except EOFError:
                count2 = 2*n

            while count1 < n and count2 < n:
                
                if n1.getKey() <= n2.getKey():
                    pickle.dump(n1, file)
                    count1 = count1 + 1

                    if count1 < n:
                        try: 
                            n1 = pickle.load(f1)
                        except EOFError:
                            count1 = 2*n
                else:
                    pickle.dump(n2, file)
                    count2 = count2 + 1
                    
                    if count2 < n:
                        try: 
                            n2 = pickle.load(f2)
                        except EOFError:
                            count2 = 2*n

            while count1 < n:
                pickle.dump(n1, file)
                count1 = count1 + 1

                if count1 < n:
                    try: 
                        n1 = pickle.load(f1)
                    except EOFError:
                        count1 = 2*n

            while count2 < n:
                pickle.dump(n2, file)
                count2 = count2 + 1

                if count2 < n:
                    try: 
                        n2 = pickle.load(f2)
                    except EOFError:
                        count2 = 2*n
            
            if count1 == 2*n and count2 == 2*n: 
                break

            count = (count + 1) % 2

        f1.close()
        f2.close()
        f3.close()
        f4.close()

        os.remove(f1Name)
        os.remove(f2Name)
        os.rename(f3Name, f1Name)
        os.rename(f4Name, f2Name)

        return mergeSort(n*2, f1Name, f2Name, f3Name, f4Name)

def merge(n, f1Name, f2Name, fName):
    '''
        objective: merge f1 and f2 to make f
        input:
            n: number of records to be read
            f1Name: name of file 1
            f2Name: name of file 2
            fName: name of file f
        output: none
    ''' 
    f1 = open(f1Name, 'rb')
    f2 = open(f2Name, 'rb')
    f = open(fName, 'wb')

    while 1:

        count1 = count2 = 0

        try: 
            n1 = pickle.load(f1)
        except EOFError:
            count1 = 2*n
        try: 
            n2 = pickle.load(f2)
        except EOFError:
            count2 = 2*n

        while count1 < n and count2 < n:

            if n1.getKey() <= n2.getKey():
                pickle.dump(n1, f)
                count1 = count1 + 1

                if count1 < n:
                    try: 
                        n1 = pickle.load(f1)
                    except EOFError:
                        count1 = 2*n
            
            else:
                pickle.dump(n2, f)
                count2 = count2 + 1
                
                if count2 < n:
                    try: 
                        n2 = pickle.load(f2)
                    except EOFError:
                        count2 = 2*n

        while count1 < n:
            pickle.dump(n1, f)
            count1 = count1 + 1

            if count1 < n:
                try: 
                    n1 = pickle.load(f1)
                except EOFError:
                    count1 = 2*n

        while count2 < n:
            pickle.dump(n2, f)
            count2 = count2 + 1

            if count2 < n:
                try: 
                    n2 = pickle.load(f2)
                except EOFError:
                    count2 = 2*n

        if count1 == 2*n and count2 == 2*n: 
            break


    f.close()
    f1.close()
    f2.close()

    os.remove(f1Name)
    os.remove(f2Name)

    print("Merge Complete")

def main():
    '''
        objective: to interface above functions
        input: none
        output: none
    '''
    initblockSize = 10
    fileName = 'f'
    f1Name = 'f1'
    f2Name = 'f2'
    f3Name = 'f3'
    f4Name = 'f4'

    #create file
    create(fileName, numRecord)
    
    #get size of block
    size = getBlockSize(fileName)

    split(initblockSize, fileName, f1Name, f2Name)

    n = mergeSort(initblockSize, f1Name, f2Name, f3Name, f4Name)

    merge(n, f1Name, f2Name, fileName)

    startRecord = 1
    endRecord = 100
    show(fileName, startRecord, endRecord, size)

if __name__ == '__main__':
    main()