# CWR - Python
CWR is a library for working with data from files. It contains 2 classes for normal work with files and for work with saving data (parameters, settings).

## CWR File
>To work with files. It has write, read and append functions.

To create a class object, you need the path parameter (file location) and encoding (optional parameter).

	__init__ (path, encoding="utf8")
  
	
**Read functions:**

	readAll()
	
Returns the text of the entire file.

	read(i)
	
Takes an integer value - the number of characters to read.

**Recording functions:**

	write(text)
	
Accepts a string parameter that will replace the text of the entire file.

	append(text)
	
Accepts a string parameter that will be appended to the end of the file.


## CWR Item

>The class allows you to create an object for reading/writing items.

To create a class object, you need the path parameter (file location) and encoding (optional parameter).

	__init__(self, path, encoding="utf8")

To create a file. (at the beginning of the work)

	Create()
	
Add a new item to the file. Accepts the parameters element name, element value.
	
	addItem(item, value)
	
Edit an item in the file. Accepts the parameters element name, element value.

	setItem(item, value)
	
Edit an item or add a new one to the file (if the item does not exist in the file). Accepts the parameters element name, element value.
	
	SetOrAddItem(item, value)
	
Check the presence of an element in the file. (if there is - True otherwise - False)
	
	containsItem(item)
	
Returns a list of existing elements recorded in the file.

	getItems()

Get the value of the element (pass the name of the element)

	getItem(item)
	
Delete an item from the file. Returns the value of the deleted element. (Does not check for the presence of an element! (if the element is missing, the program may crash))

	removeItem(item)
