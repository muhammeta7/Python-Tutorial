### For Loops
* Works by iterating over some set of values.
* Assigns each of the values one by one, to one or more variables.
* Executes block of code once for each value.
* Set of values comes from sequence or some other iterable object.

### Iterating over strings
```python
example = "abc 123 def"
for char in example:
    print(char)
```
Result
```
a
b
c

1
2
3

d
e
f
```

### Iterating over a range of values
In Java and C for loops, you provide a starting value and an ending value, and increment a variable each time around the loop.
Python's different approach to for loops makes them incredibly powerful and also very flexible.
To get the same effect as C for loops, you can iterate over a **range** of values

* Range work similarly to string slices, where the last value specified is **not** included.
* Range produces a range of values - from the starting value, up to but not including the end value.

```python
for i in range(1,4):
	print("i is now {}".format(i))
```
Result
```
i is now 1
i is now 2
i is now 3
```
If you do not provide a start value it will default to 0. 
```python
for i in range(4):
    print(i)
```
Result
```
0
1
2
3
```
You can also provide a step value where the default value for a step is 1. In this case you must provide a start, end, and step value.
````python
for i in range(0, 10, 2):
    print(i)
````
Result
```
0
2
4
6
8
```
You can also do a negative step with the same format start, end, and step value.
````python
for i in range(10, 0, -2):
    print(i)
````
Result
```
10
8
6
4
2
```

### Nested Loops
Nesting a for loop withing another for loop is a powerful way to process data and occurs regularly.
```python
for i in range(1, 13):
	for j in range(1, 13):
		print("{0} times {1} is {2}".format(j, i, i * j))
```



 