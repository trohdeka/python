a = b = "Hello"

b = "Not Hello"

print("a = %s, b = %s" % (a, b))

list_a = ['a', 'b', 'c']
list_b = list_a

print("list a = %s" % list_a)
print("list b = %s" % list_b)

list_b = ['1', '2', '3']

print("list a = %s" % list_a)
print("list b = %s" % list_b)

list_b = list_a

print("list a = %s" % list_a)
print("list b = %s" % list_b)

list_b[2] = '1'

print("list a = %s" % list_a)
print("list b = %s" % list_b)
# print(list_a[0] + " " + list_a[0] + " " + list_a[0])
#
# list_a[0] = a
# print(list_a[0])


list1 = ['1', '2', '3']
list2 = ['4', '5', '6']
listOfLists = [list1, list2]
listOfLists = [["1", "2"], ["3", "4"]]

print(listOfLists)
print(listOfLists[0][1])


listOfDifferentTypes = [1, "abc", [2, "dfg"]]
print(listOfDifferentTypes)