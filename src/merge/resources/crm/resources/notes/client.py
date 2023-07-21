# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....environment import MergeEnvironment
from ...types.meta_response import MetaResponse
from ...types.note import Note
from ...types.note_request import NoteRequest
from ...types.note_response import NoteResponse
from ...types.notes_list_request_expand import NotesListRequestExpand
from ...types.notes_retrieve_request_expand import NotesRetrieveRequestExpand
from ...types.paginated_note_list import PaginatedNoteList
from ...types.paginated_remote_field_class_list import PaginatedRemoteFieldClassList

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NotesClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        account_id: typing.Optional[str] = None,
        contact_id: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[NotesListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        opportunity_id: typing.Optional[str] = None,
        owner_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedNoteList:
        """
        Returns a list of `Note` objects.

        Parameters:
            - account_id: typing.Optional[str]. If provided, will only return notes with this account.

            - contact_id: typing.Optional[str]. If provided, will only return notes with this contact.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[NotesListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - opportunity_id: typing.Optional[str]. If provided, will only return notes with this opportunity.

            - owner_id: typing.Optional[str]. If provided, will only return notes with this owner.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes"),
            params=remove_none_from_dict(
                {
                    "account_id": account_id,
                    "contact_id": contact_id,
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "opportunity_id": opportunity_id,
                    "owner_id": owner_id,
                    "page_size": page_size,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedNoteList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: NoteRequest,
    ) -> NoteResponse:
        """
        Creates a `Note` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: NoteRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NoteResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[NotesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Note:
        """
        Returns a `Note` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[NotesRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"notes/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Note, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Note` POSTs.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters:
            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - page_size: typing.Optional[int]. Number of results to return per page.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes/remote-field-classes"),
            params=remove_none_from_dict(
                {
                    "cursor": cursor,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "page_size": page_size,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncNotesClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        account_id: typing.Optional[str] = None,
        contact_id: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[NotesListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        opportunity_id: typing.Optional[str] = None,
        owner_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedNoteList:
        """
        Returns a list of `Note` objects.

        Parameters:
            - account_id: typing.Optional[str]. If provided, will only return notes with this account.

            - contact_id: typing.Optional[str]. If provided, will only return notes with this contact.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[NotesListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - opportunity_id: typing.Optional[str]. If provided, will only return notes with this opportunity.

            - owner_id: typing.Optional[str]. If provided, will only return notes with this owner.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes"),
            params=remove_none_from_dict(
                {
                    "account_id": account_id,
                    "contact_id": contact_id,
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "opportunity_id": opportunity_id,
                    "owner_id": owner_id,
                    "page_size": page_size,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedNoteList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: NoteRequest,
    ) -> NoteResponse:
        """
        Creates a `Note` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: NoteRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NoteResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[NotesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Note:
        """
        Returns a `Note` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[NotesRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"notes/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Note, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `Note` POSTs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters:
            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - page_size: typing.Optional[int]. Number of results to return per page.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "notes/remote-field-classes"),
            params=remove_none_from_dict(
                {
                    "cursor": cursor,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "page_size": page_size,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
