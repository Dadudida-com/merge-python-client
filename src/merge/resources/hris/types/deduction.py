# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Deduction(pydantic.BaseModel):
    """
    # The Deduction Object
    ### Description
    The `Deduction` object is used to represent an array of the wages withheld from total earnings for the purpose of paying taxes.

    ### Usage Example
    Fetch from the `LIST Deductions` endpoint and filter by `ID` to show all deductions.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    employee_payroll_run: typing.Optional[str]
    name: typing.Optional[str] = pydantic.Field(description="The deduction's name.")
    employee_deduction: typing.Optional[float] = pydantic.Field(
        description="The amount of money that is withheld from an employee's gross pay by the employee."
    )
    company_deduction: typing.Optional[float] = pydantic.Field(
        description="The amount of money that is withheld on behalf of an employee by the company."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
