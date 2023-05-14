# Python HashTable
A reimplementation of dict, made it during my free time to train my debugging/testing skills

    table: HashTable = HashTable()
Create empty hashtable

    table.add(key, val)
Add (key, value) pair to table, table hashes by keys (amortized O(1))

    table.get(key)
Get value at key in table (O(1))

    table.remove(key)
Remove (key, value) pair at the given key (O(1))

    table.clear()
Remove all pairs in table (O(1))

    len(table)
    print(table)