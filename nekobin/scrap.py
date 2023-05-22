from nekobin import Nekobin

a = Nekobin()
print(a.paste("Hello"))



from bs4 import BeautifulSoup
import httpx


url = "https://nekobin.com/qeponipiru"
r = httpx.get(url, follow_redirects=1)
doc = BeautifulSoup(r.content, "html.parser").findAll("script")[-1]

print(doc.prettify())
