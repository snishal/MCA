from Record import *
import pickle
import random

def create(fileName, numRecord):
    '''
        objective: to create a file with Records having random key
        input: 
            fileName: name to file to be created
            numRecord: number of records to be written
        output: none
    '''
    lowRange = 5000000
    highRange = 9000000
    keys = random.sample(range(lowRange, highRange), numRecord)
    repeat = 5

    f = open(fileName, 'wb')

    for key in keys:
        pickle.dump(Record(key, repeat), f)

    f.close()
    print('File Created')

def read(fileName):
    '''
        objective: to read a file
        input:
            fileName: name of file to be read
        output: none
    '''
    f = open(fileName, 'rb')
    i = 1
    try:
        while 1:
            print(i, ' : ', pickle.load(f))
            i = i + 1
    except EOFError:
        f.close()

def show(fileName, startRecord, endRecord, size):
    '''
        objective: to retrive records from file
        input: 
            fileName: file to be read
            startRecord: first record to be read
            endRecord: last record to be read
            size: size of object in file
        output: none
    '''

    f = open(fileName, 'rb')

    f.seek(size*(startRecord - 1))

    try:
        for i in range(startRecord, endRecord + 1):
            print(i, ' : ', pickle.load(f))
    except EOFError:
        pass

    f.close()

def getBlockSize(fileName):
    '''
        objective: size of object in file
        input: 
            fileName: name of file
        output: size of object
    '''
    f = open('f', 'rb')
    pickle.load(f)
    return f.tell()