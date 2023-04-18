# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ...types.hris import Employment, employment_list_params, employment_retrieve_params
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["Employments", "AsyncEmployments"]


class Employments(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        expand: Literal["employee", "employee,pay_group", "pay_group"] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Employment:
        """
        Returns an `Employment` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/hris/v1/employments/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    employment_retrieve_params.EmploymentRetrieveParams,
                ),
            ),
            cast_to=Employment,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        expand: Literal["employee", "employee,pay_group", "pay_group"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        order_by: Literal["-effective_date", "effective_date"] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Employment]:
        """
        Returns a list of `Employment` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          employee_id: If provided, will only return employments for this employee.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          order_by: Overrides the default ordering for this endpoint.

          page_size: Number of results to return per page.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/employments",
            page=SyncPage[Employment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "employee_id": employee_id,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "order_by": order_by,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    employment_list_params.EmploymentListParams,
                ),
            ),
            model=Employment,
        )


class AsyncEmployments(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        expand: Literal["employee", "employee,pay_group", "pay_group"] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Employment:
        """
        Returns an `Employment` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/hris/v1/employments/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    employment_retrieve_params.EmploymentRetrieveParams,
                ),
            ),
            cast_to=Employment,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        expand: Literal["employee", "employee,pay_group", "pay_group"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        order_by: Literal["-effective_date", "effective_date"] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_type",
            "employment_type,flsa_status",
            "employment_type,flsa_status,pay_frequency",
            "employment_type,flsa_status,pay_frequency,pay_period",
            "employment_type,flsa_status,pay_period",
            "employment_type,pay_frequency",
            "employment_type,pay_frequency,pay_period",
            "employment_type,pay_period",
            "flsa_status",
            "flsa_status,pay_frequency",
            "flsa_status,pay_frequency,pay_period",
            "flsa_status,pay_period",
            "pay_frequency",
            "pay_frequency,pay_period",
            "pay_period",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Employment, AsyncPage[Employment]]:
        """
        Returns a list of `Employment` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          employee_id: If provided, will only return employments for this employee.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          order_by: Overrides the default ordering for this endpoint.

          page_size: Number of results to return per page.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/employments",
            page=AsyncPage[Employment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "employee_id": employee_id,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "order_by": order_by,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    employment_list_params.EmploymentListParams,
                ),
            ),
            model=Employment,
        )
