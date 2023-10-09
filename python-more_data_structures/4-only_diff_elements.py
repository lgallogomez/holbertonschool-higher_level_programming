#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = set()
    set2 = set()
    for i in set_1:
        if i not in set_2:
            set1.add(i)
    for j in set_2:
        if j not in set_1:
            set2.add(j)
    new_set = set1.union(set2)
    return (new_set)

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
