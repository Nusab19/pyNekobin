import re
import json
import httpx
import asyncio


class objectify:
    def __init__(self, entries):
        self.ok: bool = False
        self.link: str = None
        self.message: str = None
        self.error: Exception = None

        self.__dict__.update(entries)

    def __repr__(self):
        return f"\nOk: {self.ok}" \
               f"\nLink: {self.link}" \
               f"\nMessage: {self.message}" \
               f"\nError: {self.error}\n"


class Nekobin:
    """
The wrapper class for nekobin.com

    """

    def __init__(self, **kw):
        """
        Pass any arguments that http.AsyncClient may take.
        Such as:
            headers, timeout, proxy
        """
        self.__SES = httpx.AsyncClient(**kw)
        self._baseUrl = "https://nekobin.com/api/documents/"

    async def paste(self, text: str):
        data = {'content': text}
        try:
            r = await self.__SES.post(self._baseUrl, json=data)
            r = r.json()

        except json.decoder.JSONDecodeError as e:
            x = {"ok": False, "message": "Failed to parse json", "error": e}
            return objectify(x)

        except Exception as e:
            x = {
                "ok": False,
                "message": "Unknown Exception occurred",
                "error": e}

            return objectify(x)

        if r.get("ok"):
            x = {
                "ok": True,
                "link": f"https://nekobin.com/{r['result']['key']}",
                "message": "Succreefully pasted text in Nekobin"
            }

            return objectify(x)

        else:
            x = {
                "ok": False,
                "message": "Nekobin didn't fulfil the request",
                "error": Exception("Response is not 200")
            }

            return objectify(x)

    async def read(self, url: str):
        if not url.startswith("http"):
            url = "http://" + url

        pattern = r"^http:\/\/nekobin\.com\/[a-z]{5,20}$"

        if not re.match(pattern, url):
            x = {
                "ok": False,
                "message": "URL is not valid.\nExample Url: https://nekobin.com/abcdefghi",
                "error": Exception("URL is not Valid")
            }

            return objectify(x)

        doc = url.split('/')[-1]
        r = await self.__SES.get(self._baseUrl + doc)

        if not r.get("ok"):
            x = {
                "ok": False,
                "message": "Document not found in Nekobin Database",
                "error": Exception(r.get("error").replace('_', ' '))
            }

            return objectify(x)

        try:
            x = {
                "ok": True,
                "content": r["result"]["content"],
                "message": "Successfully retrieved text from Nekobin"
            }
            return objectify(x)

        except Exception:
            x = {
                "ok": False,
                "message": "Nekobin did not fulfil the request",
                "error": Exception("Document not retrieved")
            }

            return objectify(x)
