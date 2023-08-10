# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class AccountingPhoneNumber(pydantic.BaseModel):
    """
    # The AccountingPhoneNumber Object
    ### Description
    The `AccountingPhoneNumber` object is used to represent a contact's or company's phone number.

    ### Usage Example
    Fetch from the `GET CompanyInfo` endpoint and view the company's phone numbers.
    """

    number: typing.Optional[str] = pydantic.Field(description="The phone number.")
    type: typing.Optional[str] = pydantic.Field(description="The phone number's type.")
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
