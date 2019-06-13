def unique_names(names1, names2):
    name_full = list(set(names1 + names2))
    return name_full

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia