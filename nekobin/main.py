# pylint:disable=C0103, C0114, C0301, R0903, W0718


import re
import json
import httpx


class Objectify:
    """
    A utility class that converts a dictionary into an object.
    """

    def __init__(self, entries):
        """
        Initializes the Objectify instance with the given dictionary entries.

        Args:
            entries (dict): A dictionary containing the entries to be added as attributes to the object.
        """
        self.ok: bool = False
        self.url: str = None
        self.content: str = None
        self.message: str = None
        self.error: Exception = None

        self.__dict__.update(entries)


class Nekobin:
    """
A wrapper class for the nekobin.com API.
    """

    def __init__(self, **kw):
        """
        Initializes the Nekobin instance with the given arguments.

        Args:
            **kw: Any keyword arguments that http.AsyncClient may take, such as headers, timeout, or proxy.
        """
        self.__SES = httpx.AsyncClient(**kw)
        self._baseUrl = "https://nekobin.com/api/documents/"

    async def paste(self, text: str, **kw):
        """
        Posts the given text to the nekobin.com API and returns an Objectify instance.

        Args:
            text (str): The text to be pasted.
            **kw: Any keyword arguments that http.AsyncClient may take, such as headers, timeout, or proxy.


        Returns:
            Objectify: An Objectify instance representing the result of the paste operation.
        """
        data = {'content': text}
        try:
            r = await self.__SES.post(self._baseUrl[:-1], json=data, **kw)
            r = r.json()

        except json.decoder.JSONDecodeError as e:
            x = {"ok": False, "message": "Failed to parse json", "error": e}
            return Objectify(x)

        except Exception as e:
            x = {
                "ok": False,
                "message": "Unknown Exception occurred",
                "error": e
            }

            return Objectify(x)

        if r.get("ok"):
            x = {
                "ok": True,
                "url": f"https://nekobin.com/{r['result']['key']}",
                "message": "Successfully pasted text in Nekobin"
            }

            return Objectify(x)

        x = {
            "ok": False,
            "message": "Nekobin did not fulfill the request",
            "error": Exception("Response is not 200")
        }

        return Objectify(x)

    async def read(self, url: str, **kw):
        """
        Reads the text from the nekobin.com API for the given URL and returns an Objectify instance.

        Args:
            url (str): The URL of the nekobin.com document to read.
            **kw: Any keyword arguments that http.AsyncClient may take, such as headers, timeout, or proxy.

        Returns:
            Objectify: An Objectify instance representing the result of the read operation.
        """
        if not url.startswith("http"):
            url = "https://" + url

        if not self.isNekobinUrl(url):
            x = {
                "ok": False,
                "message": "URL is not valid. Example Url: https://nekobin.com/abcdefghi",
                "error": Exception("URL is not Valid")
            }

            return Objectify(x)

        doc = url.split('/')[-1].split('.')[0]
        r = await self.__SES.get(self._baseUrl + doc, **kw)
        r = r.json()

        if not r.get("ok"):
            x = {
                "ok": False,
                "message": "Document not found in Nekobin Database",
                "error": Exception(r.get("error").replace('_', ' '))
            }

            return Objectify(x)

        try:
            x = {
                "ok": True,
                "content": r["result"]["content"],
                "message": "Successfully retrieved text from Nekobin"
            }
            return Objectify(x)

        except Exception:
            x = {
                "ok": False,
                "message": "Nekobin did not fulfill the request",
                "error": Exception("Document not retrieved")
            }

            return Objectify(x)
    

    def isNekobinUrl(self, url: str):
        pattern = r"^(http|https):\/\/nekobin\.com\/[a-z.]{5,20}$"
        return re.match(pattern, url)