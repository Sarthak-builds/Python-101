# Introduction to Python

Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. It was created by Guido van Rossum and first released in 1991. Python emphasizes code readability with its use of indentation (spaces or tabs) to define code blocks instead of curly braces like in other languages. It's widely used for web development, data analysis, artificial intelligence, automation, scientific computing, and more. Python is open-source and has a vast ecosystem of libraries (like NumPy for numerical computations or Django for web frameworks) that extend its capabilities.

Python is "batteries included," meaning it comes with a standard library that provides modules for common tasks like file I/O, networking, and math. It's dynamically typed (you don't need to declare variable types) and supports multiple programming paradigms: procedural, object-oriented, and functional.

To get started, you need to install Python from the official website (python.org). Once installed, you can write Python code in a text editor and run it.

**Code Example:** A simple "Hello, World!" program to introduce basic syntax.

```python
# This is a comment in Python (starts with #)
print("Hello, World!")  # This prints a message to the console
```

Save this in a file (we'll discuss extensions next) and run it. Output: `Hello, World!`

## The .py Extension

Python source code files use the `.py` extension. This tells the operating system and tools (like interpreters or IDEs) that the file contains Python code. It's a convention, but essential for proper execution. For example, if you save your code in `hello.py`, you can run it from the command line with `python hello.py`.

Without the `.py` extension, the file might not be recognized as executable Python code, though you could still force-run it. Using `.py` also enables syntax highlighting in editors like VS Code or PyCharm.

**Code Example:** Create a file named `greet.py` (we'll use this in later sections).

```python
# greet.py
def greet(name):
    print(f"Hello, {name}!")

greet("Sarthak")
```

Run it: `python greet.py`. Output: `Hello, Sarthak!`

## Python's Inner Workings: The Interpreter

Python is an interpreted language, meaning your code isn't directly compiled into machine code like C or Java. Instead, it's executed line-by-line by the Python interpreter. The interpreter reads your source code (`.py` file), checks for syntax errors, and executes it.

When you run a Python file, you "give" it to the interpreter via the command `python filename.py`. For example, with `greet.py` above, the interpreter processes the code, defines the function, and calls it.

Internally:
- The interpreter first compiles the source code into **byte code**, an intermediate, low-level representation. This byte code is platform-independent (it runs on any machine with Python installed, regardless of OS like Windows, Linux, or macOS) and optimized for faster execution compared to interpreting raw source code every time.
- Byte code is mostly hidden from users—it's not something you directly edit or see unless you dig into it.
- The **Python Virtual Machine (PVM)** then executes this byte code. The PVM is like a runtime engine that translates byte code into machine-specific instructions.

This process makes Python portable and efficient: compile once to byte code, run anywhere.

Byte code isn't machine code (which is binary specific to hardware like x86 processors). It's a set of instructions for the PVM, making it slower than compiled languages but easier to develop with.

**CPython** is the standard implementation of Python (written in C), which includes the interpreter and PVM. There are others like Jython (for Java) or PyPy (faster, with JIT compilation), but CPython is the default.

**Code Example:** To see byte code in action, we can use the `dis` module to disassemble a function.

```python
import dis  # Module to disassemble byte code

def add(a, b):
    return a + b

dis.dis(add)  # This shows the byte code instructions
```

Output (simplified): You'll see opcodes like `LOAD_FAST`, `BINARY_ADD`, etc., which are the byte code.

## Conversion to .pyc Files (Compiled Python)

When Python compiles your `.py` file to byte code, it can cache this in a `.pyc` file (pronounced "pick"). `.pyc` stands for "compiled Python" and is also known as a "frozen binary" because it's a binary representation of the byte code.

This happens automatically for **imported modules** (not the top-level script you run directly). The `.pyc` files are stored in a `__pycache__` directory (introduced in Python 3.2) to avoid cluttering your project folder.

Why? Byte code in `.pyc` runs faster on subsequent runs because the interpreter skips recompiling the source code. If the source `.py` file changes (e.g., you edit it) or the Python version changes (e.g., from 3.10 to 3.12), the `.pyc` is invalidated and recompiled.

Important: This caching works only for imported files. For the main script (top-level file like `python main.py`), it's always recompiled from source—no `.pyc` is created for it, as it's executed once.

**Code Example:** Let's demonstrate with imports.

Create `utils.py`:

```python
# utils.py
def multiply(x, y):
    return x * y
```

Now, create `main.py`:

```python
# main.py
import utils  # This will compile utils.py to utils.cpython-312.pyc in __pycache__

print(utils.multiply(2, 3))  # Output: 6
```

Run `python main.py`. Check the `__pycache__` folder: You'll see a `.pyc` file. If you edit `utils.py` and rerun, it recompiles.

## Python Virtual Machine (PVM)

The PVM, also called the runtime engine, is the core component that executes byte code. It's part of the Python interpreter (in CPython, it's implemented in C).

- It takes the platform-independent byte code and interprets it into machine code at runtime.
- Byte code is not machine code—it's a higher-level instruction set (e.g., opcodes like `LOAD_CONST` for loading values).
- This makes Python slower than compiled languages but allows "write once, run anywhere."

In advanced setups, tools like PyInstaller can "freeze" your app into executables, bundling the PVM.

**Code Example:** We already used `dis` above to peek at byte code executed by the PVM. No direct code to "run" the PVM—it's implicit when you execute Python.

## Python Shell (REPL) and Indentation

The Python shell (also called REPL: Read-Eval-Print-Loop) is an interactive environment where you type code and see immediate results. Start it with `python` in your terminal (no file argument).

Indentation is crucial in Python: It defines code blocks (e.g., inside functions, loops, or if-statements). Use 4 spaces (or tabs, but be consistent). Wrong indentation causes `IndentationError`.

In the shell:
- Type expressions: `>>> 2 + 2` → `4`
- Define functions with indentation.

**Code Example:** In the shell:

```
>>> def hello():
...     print("Hi")  # Indented with 4 spaces
... 
>>> hello()
Hi
```

If you forget indentation: `IndentationError: expected an indented block`.

## Reloading Modules with importlib.reload

When working in the Python shell, if you import a module (e.g., `import greet`) and then modify the `greet.py` file on disk, the changes won't reflect until you reload it. Use `from importlib import reload` for this.

This is useful for iterative development without restarting the shell.

**Code Example:** In the shell:

```
>>> import greet  # Assume greet.py exists
>>> greet.greet("World")  # Calls the function
Hello, World!
```

Now, edit `greet.py` to change the message to "Hi, World!". Back in shell:

```
>>> from importlib import reload
>>> reload(greet)  # Reloads the modified module
<module 'greet' from '/path/to/greet.py'>
>>> greet.greet("World")
Hi, World!
```

Without reload, it'd still use the old version.

This covers the basics! Next, we can dive into variables, data types, or control structures. Let me know what you'd like to learn.