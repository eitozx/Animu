import aiohttp
import requests

from animu import model
from .roleplay import Roleplay

class Client:
    def __init__(self, token: str):
        self._header = {"Auth": token}
        self._baseurl = "https://animu.ml/api/"

    def _endpoint(self, endpoint: str):
        response = requests.get(f"{self._baseurl}{endpoint}", headers=self._header)
        result = response.json()
        return result
    
    def fact(self):
        data = self._endpoint('fact')
        return model.Fact(data)

    def password(self):
        data = self._endpoint('password')
        return model.Password(data)

    def quote(self):
        data = self._endpoint('quote')
        return model.Quote(data)

    def roleplay(self, query: Roleplay):
        data = self._endpoint(query)
        return model.Roleplay(data)

    def waifu(self):
        data = self._endpoint('waifu')
        return model.Waifu(data)


class AsyncClient:    
    def __init__(self, token: str):
        self._header = {"Auth": token}
        self._baseurl = "https://animu.ml/api/"

    async def _endpoint(self, endpoint: str):
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"{self._baseurl}{endpoint}", headers=self._header)
            result = await response.json(content_type="application/json")
            return result
    
    async def fact(self):
        data = await self._endpoint('fact')
        return model.Fact(data)

    async def password(self):
        data = await self._endpoint('password')
        return model.Password(data)

    async def quote(self):
        data = await self._endpoint('quote')
        return model.Quote(data)

    async def roleplay(self, query: Roleplay):
        data = await self._endpoint(query)
        return model.Roleplay(data)

    async def waifu(self):
        data = await self._endpoint('waifu')
        return model.Waifu(data)