# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic
import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.remove_none_from_dict import remove_none_from_dict
from .....environment import MergeEnvironment
from ...types.association import Association
from ...types.paginated_association_list import PaginatedAssociationList


class AssociationsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def custom_object_classes_custom_objects_associations_list(
        self,
        custom_object_class_id: str,
        object_id: str,
        *,
        association_type_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["association_type"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedAssociationList:
        """
        Returns a list of `Association` objects.

        Parameters:
            - custom_object_class_id: str.

            - object_id: str.

            - association_type_id: typing.Optional[str]. If provided, will only return opportunities with this association_type.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing_extensions.Literal["association_type"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{object_id}/associations",
            ),
            params=remove_none_from_dict(
                {
                    "association_type_id": association_type_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAssociationList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def custom_object_classes_custom_objects_associations_update(
        self,
        association_type_id: str,
        source_class_id: str,
        source_object_id: str,
        target_class_id: str,
        target_object_id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
    ) -> Association:
        """
        Creates an Association between `source_object_id` and `target_object_id` of type `association_type_id`.

        Parameters:
            - association_type_id: str.

            - source_class_id: str.

            - source_object_id: str.

            - target_class_id: str.

            - target_object_id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{source_class_id}/custom-objects/{source_object_id}/associations/{target_class_id}/{target_object_id}/{association_type_id}",
            ),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Association, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAssociationsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def custom_object_classes_custom_objects_associations_list(
        self,
        custom_object_class_id: str,
        object_id: str,
        *,
        association_type_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["association_type"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedAssociationList:
        """
        Returns a list of `Association` objects.

        Parameters:
            - custom_object_class_id: str.

            - object_id: str.

            - association_type_id: typing.Optional[str]. If provided, will only return opportunities with this association_type.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing_extensions.Literal["association_type"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{object_id}/associations",
            ),
            params=remove_none_from_dict(
                {
                    "association_type_id": association_type_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAssociationList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def custom_object_classes_custom_objects_associations_update(
        self,
        association_type_id: str,
        source_class_id: str,
        source_object_id: str,
        target_class_id: str,
        target_object_id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
    ) -> Association:
        """
        Creates an Association between `source_object_id` and `target_object_id` of type `association_type_id`.

        Parameters:
            - association_type_id: str.

            - source_class_id: str.

            - source_object_id: str.

            - target_class_id: str.

            - target_object_id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/",
                f"api/crm/v1/custom-object-classes/{source_class_id}/custom-objects/{source_object_id}/associations/{target_class_id}/{target_object_id}/{association_type_id}",
            ),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Association, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
