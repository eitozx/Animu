token = 'ANIMU API TOKEN'

import animu
import asyncio

async def test():

    client = animu.Client(token)
    object = await client.roleplay("angry")
    """
    Here 'angry' is the endpoint, to get the list of roleplay endpoitns
    Please give a look at the API docs
    """
    print(object)

asyncio.get_event_loop().run_until_complete(test())
