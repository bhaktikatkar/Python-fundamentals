# Day 8 - Sets

# 1. Creating a set
numbers = {10, 20, 30, 40, 50}
print(numbers)

#--------------------------------------------------------------
# 2. Sets automatically remove duplicates
values = {10, 20, 10, 30, 20, 40}
print(values)

#--------------------------------------------------------------
# 3. Adding an element
numbers.add(60)
print(numbers)

#--------------------------------------------------------------
# 4. Adding multiple elements
numbers.update([70, 80])
print(numbers)

#--------------------------------------------------------------
# 5. Removing an element
numbers.remove(20)
print(numbers)

#-----------------------------------------------------------------
# 6. Discarding an element
numbers.discard(30)
print(numbers)

#---------------------------------------------------------------
# 7. Checking membership
print(40 in numbers)

#---------------------------------------------------------------
# 8. Finding the number of elements
print(len(numbers))

#-------------------------------------------------------------------
# 9. Set union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))

#---------------------------------------------------------------------
# 10. Set intersection
print(set_a.intersection(set_b))

#-------------------------------------------------------------------------
# 11. Set difference
print(set_a.difference(set_b))

#------------------------------------------------------------------------
# 12. Check whether two sets are disjoint
print({1, 2}.isdisjoint({3, 4}))

#--------------------------------------------------------------------------
# 13. Check whether a set is a subset
print({1, 2}.issubset({1, 2, 3, 4}))