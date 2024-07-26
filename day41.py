print("⭐️ Website Dictionary ⭐️")
print()
webDictionary = {"name": None, "URL": None, "description": None, "rating": None}
for name in webDictionary.keys():
  webDictionary[name] = input(f"Input the {name} of the website: ")
  print()
print()
for name, value in webDictionary.items():
  print(f"{name}: {value}")