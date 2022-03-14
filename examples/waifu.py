token = 'ANIMU API TOKEN'

import animu
import asyncio

async def test():
    client = animu.Client(token)
    test = await client.waifu()
    print(test.id)
    print(test.images)
    print(test.names)
    print(test.en_name)
    print(test.jp_name)
    print(test.alt_name)
    print(test.animeinfo)
    print(test.anime)
    print(test.anime_type)
    print(test.statistics)
    print(test.fav)
    print(test.love)
    print(test.hate)
    print(test.upvote)
    print(test.downvote)

asyncio.get_event_loop().run_until_complete(test())