# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .journal_line_request_account import JournalLineRequestAccount
from .journal_line_request_tracking_categories_item import JournalLineRequestTrackingCategoriesItem
from .journal_line_request_tracking_category import JournalLineRequestTrackingCategory


class JournalLineRequest(pydantic.BaseModel):
    """
    # The JournalLine Object
    ### Description
    The `JournalLine` object is used to represent a journal entry's line items.

    ### Usage Example
    Fetch from the `GET JournalEntry` endpoint and view the journal entry's line items.
    """

    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    account: typing.Optional[JournalLineRequestAccount]
    net_amount: typing.Optional[float] = pydantic.Field(
        description="The value of the line item including taxes and other fees."
    )
    tracking_category: typing.Optional[JournalLineRequestTrackingCategory]
    tracking_categories: typing.Optional[typing.List[typing.Optional[JournalLineRequestTrackingCategoriesItem]]]
    contact: typing.Optional[str]
    description: typing.Optional[str] = pydantic.Field(description="The line's description.")
    exchange_rate: typing.Optional[str] = pydantic.Field(description="The journal line item's exchange rate.")
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
