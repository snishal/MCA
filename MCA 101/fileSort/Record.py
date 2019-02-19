class Record:
    '''
        Record Class
    '''
    def __init__(self, key, repeat):
        '''
            objective: To initialize Record object
            input:
                self: reference to calling object
                key: key to be intialized
                repeat: repeat key in other repeat times
            output: none
        '''
        self.key = key
        self.other = str(key)*repeat
    def getKey(self):
        '''
            objective: To retreive key of an object
            input:
                self: reference to calling object
            output: returns key of calling object
        '''
        return self.key

    def __str__(self):
        '''
            objective: To display Record object
            input:
                self: reference to calling object
            output: string representation of object
        '''
        return 'Record : ' + str(self.key) + ' : ' + str(self.other)