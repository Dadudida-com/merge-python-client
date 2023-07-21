# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .deduction import Deduction
from .earning import Earning
from .remote_data import RemoteData
from .tax import Tax


class EmployeePayrollRun(pydantic.BaseModel):
    """
    # The EmployeePayrollRun Object
    ### Description
    The `EmployeePayrollRun` object is used to represent an employee's pay statement for a specific payroll run.

    ### Usage Example
    Fetch from the `LIST EmployeePayrollRun` endpoint and filter by `ID` to show all employee payroll runs.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    employee: typing.Optional[str] = pydantic.Field(description="The employee whose payroll is being run.")
    payroll_run: typing.Optional[str] = pydantic.Field(description="The payroll being run.")
    gross_pay: typing.Optional[float] = pydantic.Field(
        description="The total earnings throughout a given period for an employee before any deductions are made."
    )
    net_pay: typing.Optional[float] = pydantic.Field(
        description="The take-home pay throughout a given period for an employee after deductions are made."
    )
    start_date: typing.Optional[str] = pydantic.Field(description="The day and time the payroll run started.")
    end_date: typing.Optional[str] = pydantic.Field(description="The day and time the payroll run ended.")
    check_date: typing.Optional[str] = pydantic.Field(description="The day and time the payroll run was checked.")
    earnings: typing.Optional[typing.List[Earning]]
    deductions: typing.Optional[typing.List[Deduction]]
    taxes: typing.Optional[typing.List[Tax]]
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[str] = pydantic.Field(
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
        json_encoders = {dt.datetime: serialize_datetime}
