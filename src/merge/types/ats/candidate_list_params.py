# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CandidateListParams"]


class CandidateListParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    email_addresses: str
    """
    If provided, will only return candidates with these email addresses; multiple
    addresses can be separated by commas.
    """

    expand: Literal["applications", "applications,attachments", "attachments"]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    first_name: Optional[str]
    """If provided, will only return candidates with this first name."""

    include_deleted_data: bool
    """Whether to include data that was marked as deleted by third party webhooks."""

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    last_name: Optional[str]
    """If provided, will only return candidates with this last name."""

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    page_size: int
    """Number of results to return per page."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    tags: str
    """
    If provided, will only return candidates with these tags; multiple tags can be
    separated by commas.
    """
