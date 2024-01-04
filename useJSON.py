import json
serialised="""{"title": "Data Science Book","author":"Joel Grus","publicationYear":2014,"topics":["data","science","data science"]}"""
deserialised=json.loads(serialised)
if "data science" in deserialised["topics"]:
    print(deserialised)