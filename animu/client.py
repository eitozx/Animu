import aiohttp
from animu import model

class Client:
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

    async def roleplay(self, query: str):
        data = await self._endpoint(query)
        return model.Roleplay(data)

    async def waifu(self):
        data = await self._endpoint('waifu')
        return model.Waifu(data)