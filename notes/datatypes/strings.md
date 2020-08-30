# Strings

> Quick Nav: [Table of contents](../../readme.md), [Previous (Numbers)](./numbers.md), [next ()]()

Link in any other programming language, `String` is a sequence of (Unicode) characters.

## String assignment and concatenation

Some basic string operations can be seen in file [examples/datatypes/string1.py](../../examples/datatypes/string1.py)

```python
name = "Kapil"

print ("Hello " + name + "!") # Output: Hello Kapil!
```

> ### `Output`
>
> Hello Kapil!

## Single and double quotes

String can be used with both single or double quotes. We can use them interchangeably as required. This is specially helpful when we need string with single or double quotes in it. It cna be seen in example [examples/datatypes/string2.py](../../examples/datatypes/string2.py)

```python
double = "I'm Kapil Sharma"
print(double)

single = 'He said, "I\'ll come"'
print(single)
```

> ### `Output`
>
> I'm Kapil Sharma
>
>He said, "I'll come"

As we can see in second line, we can also use escape characters (`\'` in this example) to print single or double quote.

## Length and index

Example: [examples/datatypes/string3.py](../../examples/datatypes/string3.py)

```python
# Finding length of a string
name = "Kapil Sharma"
print(len(name))  # Output: 12 (Note: Space is also a character)

# String indexing
# String index starts with 0
print(name[0])  # Output: K
print(name[3])  # Output: i

# Negative index: Starting with -1, negative index are index in reverse order like
# (String)       :   K   a   p   i   l       S   h   a   r   m   a
# (Index)        :   0   1   2   3   4   5   6   7   8   9  10  11
# (Reverse index): -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
print(name[-2])  # Output: m

# Slicing
# In Python, we use index for slicing as well. Index is [start:end(excluding):step
print(name[3])   # Output: i
# If we do not provide 'end'(Number after first :), it mean end of string.
print(name[3:])  # Output: il Sharma
# If wo do not provide 'start'(Number before first :), it mean start of string.
# Note: 'end' (3) is exclusive. This output will be 'Kap', not 'Kapi'.
print(name[:3])  # Output: Kap
# We can also use negative index
print(name[-3:])  # Output: rma
print(name[:-3])  # Output: Kapil Sha

# Step - Default 1
print(name[::1])  # Output: Kapil Sharma
print(name[::2])  # Output: KplSam
# Trick: We can use step as -1 to reverse string
print(name[::-1])  # Output: amrahS lipaK
```

> ### `Output`
>
> 12
>
> K
>
> i
>
> m
>
> i
>
> il Sharma
>
> Kap
>
> rma
>
> Kapil Sha
>
> Kapil Sharma
>
> KplSam
>
> amrahS lipaK

## String formatting

We already seen string concatenation like 

```python
name = 'Kapil Sharma'
city = 'Pune'
print('My name is ' + name + " and I live in " + city + ".")

player, score = 'Virat Kohli', 123  # We can define multiple variables in same line.
print(player + " scored "  + str(score) + " runs in the last match")
```

This could be fine for shorter strings but sometimes, we may have too many variables or might need more control on formatting. For this, python three ways of string formatting.

1. Modulo placeholders (Oldest method). Examples
    - `print("My name is %s" %"Kapil Sharma")`
    - `print("My name is %s and I live in %s" %('Kapil Sharma', 'Pune'))`
    - `print("%s scored %d runs in the last match" %(player, score))`
    - `print('Floating point numbers: %1.2f' %(13.144))`
        - Output: Floating point numbers: 13.14
    - `print('Floating point numbers: %8.1f' %(13.144))`
        - Output: Floating point numbers: ....13.1 `(Dots before 13 represent space)`
2. Function `format`. Examples
    - `print("My name is {}".format("Kapil Sharma"))`
    - `print("My name is {} and I live in {}".format("Kapil Sharma", "Pune"))`
    - `print("{} scored {} runs in the last match".format("Virat Kohli", 123))`
    - `print("{1} scored {0} runs in the last match".format(123, "Virat Kohli"))`
    - `print("{p} scored {s} runs in the last match".format(s=123, p="Virat Kohli"))`
    - `print('Floating point numbers: {}'.format(13.144))`
        - Output: Floating point numbers: 13.144
    - `print('Floating point numbers: {0:8}'.format(13.144))`
        - Output: Floating point numbers: ..13.144 `(Dots before 13 represent space)`
    - `print('Floating point numbers: {0:8.2f}'.format(13.144))`
        - Output: Floating point numbers: ...13.14 `(Dots before 13 represent space)`
    - `print("| {1:10} | {0:10} |".format('Column 1', 'column 0'))`
        - Output: | column 0.. | Column 1.. | `(Dot represent spaces)`
    - `print('| {0:<8} | {1:^8} | {2:>8} |'.format('Left','Center','Right'))`
        - Output: | Left.... | .Center. | ...Right | `(Dot represent spaces)`
    - `print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))`
        - Output: Left==== | -Center- | ...Right
3. Formatted String Literals (f-strings) (Introduced in Python 3.6)
    - 