# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .opportunity_account import OpportunityAccount
from .opportunity_owner import OpportunityOwner
from .opportunity_stage import OpportunityStage
from .opportunity_status import OpportunityStatus
from .remote_data import RemoteData
from .remote_field import RemoteField


class Opportunity(pydantic.BaseModel):
    """
    # The Opportunity Object
    ### Description
    The `Opportunity` object is used to represent a deal opportunity in a CRM system.
    ### Usage Example
    TODO
    """

    name: typing.Optional[str] = pydantic.Field(description="The opportunity's name.")
    description: typing.Optional[str] = pydantic.Field(description="The opportunity's description.")
    amount: typing.Optional[int] = pydantic.Field(description="The opportunity's amount.")
    owner: typing.Optional[OpportunityOwner] = pydantic.Field(description="The opportunity's owner.")
    account: typing.Optional[OpportunityAccount] = pydantic.Field(description="The account of the opportunity.")
    stage: typing.Optional[OpportunityStage] = pydantic.Field(description="The stage of the opportunity.")
    status: typing.Optional[OpportunityStatus] = pydantic.Field(
        description=("The opportunity's status.\n" "\n" "* `OPEN` - OPEN\n" "* `WON` - WON\n" "* `LOST` - LOST\n")
    )
    last_activity_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the opportunity's last activity occurred."
    )
    close_date: typing.Optional[dt.datetime] = pydantic.Field(description="When the opportunity was closed.")
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's opportunity was created."
    )
    remote_was_deleted: typing.Optional[bool]
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
