# using array to implement hash table
class HashTable:
    def __init__(self):
        """
        Initialize the Hash Table here
        """
        self.MAX = 1000
        self.table = [None for i in range(1000)]

    def hash(self, value):
        """
        Calculate the value using ascii value to get the key

        :param value: the value to be calculated
        :returns: The key for the table
        """
        key = 0
        for char in value:
            key += ord(char)
        # print(key % self.MAX)
        return key % self.MAX 

    def get(self, value):
        """"
        Requests the key of the value

        :param value: The value of the key requested for
        :returns: The key or None if value not in table
        """
        for key, item in enumerate(self.table):
            if item == value:
                print("value exist")
                return key
        return None

    def set(self, value):
        """
        Adds the value and key to the table

        :param value: the value to be added
        """
        key = self.hash(value)
        if self.has(key):
            # print("done")
            self.table[key] = value
        else:
            # print("yikes")
            added = 1      
            for index, item in enumerate(self.table): 
                key = self.hash(value) + added          
                if index == key:
                    if not item:
                        self.table[index] = value         
                    else:
                        added += 1                

    def get_keys(self):
        """"
        Prints out all the items in the table

        :returns: The values in the table
        """
        values = []
        for item in self.table:
            if item:
                values.append(item)
        print(values)
        return values

    def has(self, key):
        """
        Searches the table for the key

        :param key: the key searched for
        :return: True if the key is in the table, or False if it isn't in the table
        """
        if self.table[key]:
            return True
        return False

    def delete(self, value):
        """
        Finds the vales and deletes it with its key

        :param value: the value to be deleted
        :return: True if the value was deleted, or False if the value isn't in the table
        """
        for index, item in enumerate(self.table):
            if item == value:
                self.table[index] = None
                return True
        return False


# HashTable()
# hashing = HashTable()
# hashing.set("Jasmine Smith")
# hashing.set("Thomas Hobb")
# hashing.set("Jasie Smminth")
# hashing.get_keys()
