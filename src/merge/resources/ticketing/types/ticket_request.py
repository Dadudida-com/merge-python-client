# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .remote_field_request import RemoteFieldRequest
from .ticket_request_priority import TicketRequestPriority
from .ticket_request_status import TicketRequestStatus


class TicketRequest(pydantic.BaseModel):
    """
    # The Ticket Object
    ### Description
    The `Ticket` object is used to represent a ticket or a task within a system.

    ### Usage Example
    TODO
    """

    name: typing.Optional[str] = pydantic.Field(description="The ticket's name.")
    assignees: typing.Optional[typing.List[typing.Optional[str]]]
    creator: typing.Optional[str] = pydantic.Field(description="The user who created this ticket.")
    due_date: typing.Optional[str] = pydantic.Field(description="The ticket's due date.")
    status: typing.Optional[TicketRequestStatus] = pydantic.Field(
        description=(
            "The current status of the ticket.\n"
            "\n"
            "* `OPEN` - OPEN\n"
            "* `CLOSED` - CLOSED\n"
            "* `IN_PROGRESS` - IN_PROGRESS\n"
            "* `ON_HOLD` - ON_HOLD\n"
        )
    )
    description: typing.Optional[str] = pydantic.Field(
        description="The ticket’s description. HTML version of description is mapped if supported by the third-party platform."
    )
    collections: typing.Optional[typing.List[typing.Optional[str]]]
    ticket_type: typing.Optional[str] = pydantic.Field(description="The ticket's type.")
    account: typing.Optional[str] = pydantic.Field(description="The account associated with the ticket.")
    contact: typing.Optional[str] = pydantic.Field(description="The contact associated with the ticket.")
    parent_ticket: typing.Optional[str] = pydantic.Field(description="The ticket's parent ticket.")
    attachments: typing.Optional[typing.List[typing.Optional[str]]]
    tags: typing.Optional[typing.List[typing.Optional[str]]]
    completed_at: typing.Optional[str] = pydantic.Field(description="When the ticket was completed.")
    ticket_url: typing.Optional[str] = pydantic.Field(description="The 3rd party url of the Ticket.")
    priority: typing.Optional[TicketRequestPriority] = pydantic.Field(
        description=(
            "The priority or urgency of the Ticket.\n"
            "\n"
            "* `URGENT` - URGENT\n"
            "* `HIGH` - HIGH\n"
            "* `NORMAL` - NORMAL\n"
            "* `LOW` - LOW\n"
        )
    )
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
