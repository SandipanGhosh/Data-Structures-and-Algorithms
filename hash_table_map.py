"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv                
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        value = ord(string[0])*100 + ord(string[1])
        return value

 
# Test cases
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8365
print (hash_table.calculate_hash_value('SANDIPAN'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('SANDIPAN'))

# Test store
hash_table.store('SANDIPAN')
# Should be 8365
print (hash_table.lookup('SANDIPAN'))

# Test store edge case
hash_table.store('SANDMAN')
# Should be 8365
print (hash_table.lookup('SANDMAN'))
