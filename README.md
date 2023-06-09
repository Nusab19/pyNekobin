Here's a revised version of the README.md file with some minor spelling and grammar corrections:

# pyNekobin - A Wrapper for Nekobin API

This is a Python package that provides a simple wrapper around the [Nekobin](https://nekobin.com/) API, allowing you to easily paste and retrieve text snippets from the popular pastebin service.

## Installation

You can install the package using pip:

```
pip install pynekobin
```

## Usage

This package is asynchronous and uses httpx under the hood to make HTTP requests. So, you need to use the `await` keyword with each method call.
First, import the `Nekobin` class and the `asyncio` library:

```python
from nekobin import Nekobin
import asyncio
```

Then, create an instance of the `Nekobin` class:

```python
nb = Nekobin()
```

To paste text to Nekobin, you can use the `paste()` method:

```python
async def main():
    result = await nb.paste("Hello, world!")
    if result.ok:
        print("Pasted text at:", result.url)
    else:
        print("Error:",  result.message)

asyncio.run(main())
```

Similarly, you can use the `read()` method to retrieve text from Nekobin:

```python
async def main():
    result = await nb.read("https://nekobin.com/abcdefg")
    if result.ok:
        print("Retrieved text:", result.content)
    else:
        print("Error:", result.message)

asyncio.run(main())
```

## Advanced Usage

As this package uses `httpx` under the hood, you can pass additional keyword arguments in each method call. You can pass any keyword argument that `httpx.AsyncClient` may take:

```python
from nekobin import Nekobin

nb = Nekobin(timeout=10, headers={}, follow_redirects=True)
```

If you want to pass these arguments in each method call, you have that too:

```python
async def main():
    result = await nb.paste("Hello, world!", timeout=10)
    url = result.url
    print("Pasted at:", url)

    content = (await nb.read(url, timeout=7)).content
    print("Content:", content)

asyncio.run(main())
```

## Contributing

If you encounter any bugs or issues, please feel free to open an issue on the [GitHub repository](https://github.com/Nusab19/pyNekobin/pulls). If you would like to contribute to the development of the package, you can fork the repository and submit a pull request with your changes.

## License

This package is licensed under the MIT License. See the `LICENSE` file for more information.