# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .scheduled_interview_request_status import ScheduledInterviewRequestStatus


class ScheduledInterviewRequest(pydantic.BaseModel):
    """
    # The ScheduledInterview Object
    ### Description
    The `ScheduledInterview` object is used to represent a scheduled interview for a given candidate’s application to a job. An `Application` can have multiple `ScheduledInterview`s depending on the particular hiring process.
    ### Usage Example
    Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.
    """

    application: typing.Optional[str] = pydantic.Field(description="The application being interviewed.")
    job_interview_stage: typing.Optional[str] = pydantic.Field(description="The stage of the interview.")
    organizer: typing.Optional[str] = pydantic.Field(description="The user organizing the interview.")
    interviewers: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(
        description="Array of `RemoteUser` IDs."
    )
    location: typing.Optional[str] = pydantic.Field(description="The interview's location.")
    start_at: typing.Optional[str] = pydantic.Field(description="When the interview was started.")
    end_at: typing.Optional[str] = pydantic.Field(description="When the interview was ended.")
    status: typing.Optional[ScheduledInterviewRequestStatus] = pydantic.Field(
        description=(
            "The interview's status.\n"
            "\n"
            "* `SCHEDULED` - SCHEDULED\n"
            "* `AWAITING_FEEDBACK` - AWAITING_FEEDBACK\n"
            "* `COMPLETE` - COMPLETE\n"
        )
    )
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
