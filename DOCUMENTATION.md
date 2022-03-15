# Animu
An async wrapper for Animu API in Python.

<details>
  <summary>Introduction</summary>
  <p>

# Animu
An async wrapper for [Animu API](https://animu.ml/) written in Python.

## Key Features
- An async library.
- Anime fact, waifu & more!
- Especially made for discord bots.
- Easy to use with an object oriented design.


## Installing

**Python 3.8 or higher is required**

You can install it by following command:

```cmd
pip install animu
```
  </p>
</details>

<details>
  <summary>FAQ & Links </summary>
  <p>

# FAQ

## How do I get the Animu API token?
To get the token, [join Discord server of Animu API](https://discord.gg/yyW389c). Move to `#bot-commands` channel. And do `-claim`. 

From there, further process should start in your DM. Good luck!

## My Token is not working anymore. Why?
Make sure that you've joined the support server, or else it won't work. If it's still not working, please ask for help in their official server.

## Any examples?
Check [examples](https://github.com/EitoZX/Animu/examples/) folder for examples.

## Any ratelimit?
Yes, 5 requests/second.

## Related Links

- [Official Animu API Discord Server](https://discord.gg/yyW389c)
  </p>
</details>

# Documentation
<details>
  <summary>Client Object</summary>

## animu.Client
After installing [animu](https://pypi.org/project/animu),
you can connect client like this:

```python
import animu

TOKEN = "ANIMU API TOKEN" #Read FAQ to know about token
client = animu.Client(TOKEN)
```
From here onwards, whenever this documentation refers to 'client', it refers to what we've defined above.

**All following listed methods in this section, must be invoked with `await`.**

---

## client.fact
**returns:**
- Fact Object

---

## client.password
**returns:**
- Password Object

---

## client.quote
**returns:**
- Quote Object

---

## client.roleplay(query:str)
**parameter:**
- query: the roleplay endpoint that you want to retrieve.

**returns:**
- Roleplay Object
---

## client.waifu
**returns:**
- Waifu Object

</details>

<details>
  <summary>Data Model Object</summary>

All the following objects, inherit the following `Base` class:

```py
class Base:
    def __init__(self, data):
        self._data = data
        
    def __getitem__(self, key):
        return self._data[key]

    def __str__(self):
        return str(self._data)
```
they support thier own attributes as well as `key`(s) from api endpoints.

## Fact Object
**Attributes:**
- **id** (`int`): ID of the fact
- **fact** (`str`): Fact
- **tags** (`list`): List of tags for that fact

## Password Object
**Attributes:**
- **password** (`str`): Password

## Quote Object
**Attributes:**
- **id** (`int`): ID of the quote
- **quote** (`str`): Quote
- **anime** (`str`): Name of the anime
- **said** (`str`): Character who said that quote.

## Roleplay Object
**Attributes:**
- **url** (`str`): URL of the gif/image for that specific roleplay query.

## Waifu Object
**Attributes:**
- **id** (`int`): ID of the waifu
- **images** (`list`): List of images of retrieved waifu.
- **names** (`dict`): dictoinary of all names of retrieved waifu.
- **en_name** (`str`): Name of the Waifu in english
- **jp_name** (`str`): Name of the Waifu in Japanese
- **alt_name** (`str`): Alternative name of the waifu.
- **animeinfo** (`dict`): Dictionary with information about anime in reference to waifu attribute
- **anime** (`str`): Name of the anime in reference to waifu attribute
- **anime_type** (`str`): Anime type of anime attribute.
- **statistics** (`dict`): statistics data in dictionary format
- **fav** (`int`): favourite statistics data
- **love** (`int`): Love statsitics data
- **hate** (`int`): Hate statsitics data
- **upvote** (`int`): Upvote statistics data
- **downvote** (`int`): Downvote statistics data

</details>

<details>
  <summary>Examples</summary>

[Check here](https://github.com/EitoZX/Animu/tree/master/examples)
</details>

Source Code: https://github.com/EitoZX/Animu

On Pypi: https://pypi.org/project/animu
