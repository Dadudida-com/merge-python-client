# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["MarketingUser"]


class MarketingUser(BaseModel):
    email: Optional[str]
    """The user's email."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The user's full name."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    role: Optional[Literal["ADMIN", "MANAGER", "CONTRIBUTOR", "VIEWER"]]
    """
    - `ADMIN` - ADMIN
    - `MANAGER` - MANAGER
    - `CONTRIBUTOR` - CONTRIBUTOR
    - `VIEWER` - VIEWER
    """

    timezone: Optional[str]
    """The user's timezone."""

    username: Optional[str]
    """The user's username."""
