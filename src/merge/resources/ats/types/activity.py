# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .activity_activity_type import ActivityActivityType
from .activity_visibility import ActivityVisibility
from .remote_data import RemoteData


class Activity(pydantic.BaseModel):
    """
    # The Activity Object
    ### Description
    The `Activity` object is used to represent an activity for a candidate performed by a user.
    ### Usage Example
    Fetch from the `LIST Activities` endpoint and filter by `ID` to show all activities.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    user: typing.Optional[str] = pydantic.Field(description="The user that performed the action.")
    remote_created_at: typing.Optional[str] = pydantic.Field(description="When the third party's activity was created.")
    activity_type: typing.Optional[ActivityActivityType] = pydantic.Field(
        description=("The activity's type.\n" "\n" "* `NOTE` - NOTE\n" "* `EMAIL` - EMAIL\n" "* `OTHER` - OTHER\n")
    )
    subject: typing.Optional[str] = pydantic.Field(description="The activity's subject.")
    body: typing.Optional[str] = pydantic.Field(description="The activity's body.")
    visibility: typing.Optional[ActivityVisibility] = pydantic.Field(
        description=(
            "The activity's visibility.\n"
            "\n"
            "* `ADMIN_ONLY` - ADMIN_ONLY\n"
            "* `PUBLIC` - PUBLIC\n"
            "* `PRIVATE` - PRIVATE\n"
        )
    )
    candidate: typing.Optional[str] = pydantic.Field(description="The activity’s candidate.")
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
