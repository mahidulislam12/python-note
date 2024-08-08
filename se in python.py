"""
collection={1,2,3,3,3,"hello","world","world",4}
collection_1={}#empty dictonary
print(type(collection_1))

print((collection))
print(len(collection))

#the write away of the set 

collection_1 = set()  # empty set
print(type(collection_1))"""
#set method
'''
null_set=set()
null_set.add("a")
null_set.add("1")
null_set.add("2")
null_set.add("t")
null_set.remove("t")
null_set.add((1,2,3))#list kora jaba na earro asba
null_set.clear()
#null_set.remove(2)#earror asba
print(null_set)
print(len(null_set))
#
collection={"hello","k","kio"}
print(collection.pop())
print(collection.pop())'''
#union &inter section
"""
set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
print(set2)"""
#problem 1
# dictonary={
#     "cat":"a small animal",
#     "table":["a piece of furniture","list of facts &figures"]
# }
# print(dictonary)

#problem 2

# set={
#     "p","j","c++","p","java","j","p","j","c++","c"
#     }
# print(len(set))
#problem 3

# null_dict={}
# null_dict["l"]="app"
# null_dict["l2"]="ap2"
# null_dict["li"]="app"
# print(null_dict)
#anotthe way

# null_dict={}
# x=int(input("enter the value:"))
# null_dict.update({"phy":x})
# print(null_dict)

#problem 4
# value={5,"5.0"}
# print(value)

#another way
values={
    ("float",9.0),
    ("int",9)

}
print(values)