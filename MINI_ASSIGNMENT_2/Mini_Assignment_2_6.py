sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

#METHOD 1
#sample_dict["location"] = sample_dict.pop("city")
#print(sample_dict)

sample_dict["location"] = sample_dict["city"]
del sample_dict["city"]
print(sample_dict)