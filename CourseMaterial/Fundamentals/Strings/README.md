# Strings 
* Strings are a sequence of characters, and a derived data type.
* Immutable: Once they are defined, they cannot be changed.
* Built-in Python methods such as `replace()`, `join()`,`split()`, etc.

### Single, Double, and Triple Quotes
You can declare variables and represent a string using single and double quotes. You can use triple quotes for multiline strings.

```python
single = 'I am a string'
double = "I am a string"
# triple quotes string can extend multiple lines
triple = """Hello, welcome to
           the world of Python"""
print(single)
print(double)
print(triple)
```
Results
```
I am a string
I am a string
Hello, welcome to
    the world of Python

```

### Escape Characters
Escape character or Backslash character is used to escape the character that follows it.
Good for formatting and IDES generally indicate these characters by changing color.

* `\n` represents a new line
* `\t` represents a tab

Must escape the same type of quotes that string begins with. In order to avoid issues reading with \n, use triple quotes.<br />
\ alone will automatically be ignored. 
```python
# Single Quote
print('The NE coach said "We don\'t have the right QB".')
# Double Quote
print("The NE coach said \"We don't have the right QB\".")
# Triple Quote
print("""The NE coach said "Cam's not that good of a QB". """)
```
Refer to **escapecharacter.py** for more examples.

### Concatenation 
String concatenation is one of the fundamental string operations and achieved using the `+` symbol. It is just a fancy way of joining multiple strings together.
<br />

*Concatenation Rules:*
* When using the + operator where one of the operands is a string, both operands must be a string.
* You can convert a numeric value to a string with the built-in function str().
* Be sure to start and end with exact same type of quotation.
* Storing strings into variables is the most optimal way to reference them for later use.
* If you try to concatenate a string with a non-string type, Python will raise a TypeError.

Refer to **strings.py** and link for more examples.


**[Splitting, Concatenating, and Joining Strings in Python](https://realpython.com/python-string-split-concatenate-join/)** <br /> 