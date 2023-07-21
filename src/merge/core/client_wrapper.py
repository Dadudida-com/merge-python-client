# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(self, *, account_token: typing.Optional[str] = None, api_key: str):
        self._account_token = account_token
        self.api_key = api_key

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {}
        if self._account_token is not None:
            headers["X-Account-Token"] = self._account_token
        headers["Authorization"] = self.api_key
        return headers


class SyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, account_token: typing.Optional[str] = None, api_key: str, httpx_client: httpx.Client):
        super().__init__(account_token=account_token, api_key=api_key)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, account_token: typing.Optional[str] = None, api_key: str, httpx_client: httpx.AsyncClient):
        super().__init__(account_token=account_token, api_key=api_key)
        self.httpx_client = httpx_client
