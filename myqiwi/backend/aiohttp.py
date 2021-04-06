import aiohttp
import asyncio

from .base import BaseBackEnd


class AioHttpBackEnd(BaseBackEnd):
    async def post(self, *args, **kwargs):
        return await self.request(*args, **kwargs, method="post")

    async def get(self, *args, **kwargs):
        return await self.request(*args, **kwargs, method="get")

    async def request(self, path, params=None, json=None, method="get"):
        url = self.make_url(path)
        kwargs = {}

        if self.proxy is not None:
            proxy_url = "http://{}:{}@{}:{}"
            text = proxy_dict["username"], self.proxy["password"], self.proxy["ip"], self.proxy["port"]
            kwargs["proxy"] = proxy_url.format(*text)

        async with aiohttp.ClientSession() as session:
            method = getattr(session, method)
            async with method(url, params=params, json=json, headers=self.headers, **kwargs) as response:
                _response = response
                _response.json = await response.json()
                _response.text = await response.text()
                _response.status_code = response.status

        return self.validate_response(_response)
