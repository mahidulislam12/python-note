dict = {
    "name": "kamal",
    "cgpa": "90",
    "marks": [98, 89, 78],
    "is_adult": "True",
    "topic": ("dict", "set"),
    12.99: 9.4  # Corrected key-value pair syntax
}
null_dict={}
null_dict["name"]="mangoes"
print(dict)
print(dict["name"])
dict["name"]="mahidul"
dict["cgpa"]=23#overwright
print(dict)
print(null_dict)

                     #nested dictonary

student = {
    "name": "mahidul",  # 'name' and 'subject' are the keys of the dictionary
    "subject": {
        "phy": 34,
        "che": 56
    }
}

print(student)  # Print the entire student dictionary
print(student["subject"]["che"])  # Access and print the chemistry mark
print(student.keys())  # Print all keys in the student dictionary

# Type casting keys to a list and printing
print(list(student.keys()))

# Type casting an integer to float and printing
phy_mark = student["subject"]["phy"]
phy_mark_float = float(phy_mark)
print(f"Physics mark as float: {phy_mark_float}")
print(len(student)) #len of the dictonary
print(len(list(student.keys())))
print(list(student.values()))
print(student.values())
print(student.items())
print(list(student.items()))
pair=list(student.items())
print(pair[0])
#print(student["name2"])# output(error)
print(student.get("name2"))#output(no earror |none) but get method earror not
student.update({"city":"deli","age":45})
new_dict={"name":"mahidul","age":34}
student.update(new_dict)
print(student)