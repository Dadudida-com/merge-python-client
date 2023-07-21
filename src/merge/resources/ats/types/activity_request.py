# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .activity_request_activity_type import ActivityRequestActivityType
from .activity_request_visibility import ActivityRequestVisibility


class ActivityRequest(pydantic.BaseModel):
    """
    # The Activity Object
    ### Description
    The `Activity` object is used to represent an activity for a candidate performed by a user.
    ### Usage Example
    Fetch from the `LIST Activities` endpoint and filter by `ID` to show all activities.
    """

    user: typing.Optional[str] = pydantic.Field(description="The user that performed the action.")
    activity_type: typing.Optional[ActivityRequestActivityType] = pydantic.Field(
        description=("The activity's type.\n" "\n" "* `NOTE` - NOTE\n" "* `EMAIL` - EMAIL\n" "* `OTHER` - OTHER\n")
    )
    subject: typing.Optional[str] = pydantic.Field(description="The activity's subject.")
    body: typing.Optional[str] = pydantic.Field(description="The activity's body.")
    visibility: typing.Optional[ActivityRequestVisibility] = pydantic.Field(
        description=(
            "The activity's visibility.\n"
            "\n"
            "* `ADMIN_ONLY` - ADMIN_ONLY\n"
            "* `PUBLIC` - PUBLIC\n"
            "* `PRIVATE` - PRIVATE\n"
        )
    )
    candidate: typing.Optional[str] = pydantic.Field(description="The activity’s candidate.")
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
