import CWR

File = CWR.CWRFile("file.txt")
Item = CWR.CWRItem("items.txt")

print("\tCWR File\n")

#  CWR File

text = "Hello World!"
File.write(text)
File.append("\nHi! CWR - Colden Write Read")
print(File.read(len(text)))
print(File.readAll())

print("\n\n\tCWR Item\n")

#  CWR Item

Item.Create()

Item.addItem("item_1", 123)
Item.addItem("item_2", "Hello")
Item.addItem("item_3", 3.14)

print(Item.getItems())

print(Item.getItem("item_1"))
print(Item.getItem("item_2"))
print(Item.getItem("item_3"))

Item.setItem("item_2", 0.1234)
Item.SetOrAddItem("item_3", Item.getItem("item_1"))
Item.SetOrAddItem("item_4", "CWR Item")

if Item.containsItem("item_1"):
    print(Item.removeItem("item_1"))
else:
    print("Item 'item_1' - not found!")

if Item.containsItem("item_5"):
    print(Item.removeItem("item_5"))
else:
    print("Item 'item_5' - not found!")

for i in Item.getItems():
    print(str(i), "=", Item.getItem(i))
