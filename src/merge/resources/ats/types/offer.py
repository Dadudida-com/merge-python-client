# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .offer_application import OfferApplication
from .offer_creator import OfferCreator
from .offer_status import OfferStatus
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Offer(pydantic.BaseModel):
    """
    # The Offer Object
    ### Description
    The `Offer` object is used to represent an offer for a candidate's application specific to a job.
    ### Usage Example
    Fetch from the `LIST Offers` endpoint and filter by `ID` to show all offers.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    application: typing.Optional[OfferApplication] = pydantic.Field(
        description="The application who is receiving the offer."
    )
    creator: typing.Optional[OfferCreator] = pydantic.Field(description="The user who created the offer.")
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's offer was created."
    )
    closed_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the offer was closed.")
    sent_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the offer was sent.")
    start_date: typing.Optional[dt.datetime] = pydantic.Field(description="The employment start date on the offer.")
    status: typing.Optional[OfferStatus] = pydantic.Field(
        description=(
            "The offer's status.\n"
            "\n"
            "* `DRAFT` - DRAFT\n"
            "* `APPROVAL-SENT` - APPROVAL-SENT\n"
            "* `APPROVED` - APPROVED\n"
            "* `SENT` - SENT\n"
            "* `SENT-MANUALLY` - SENT-MANUALLY\n"
            "* `OPENED` - OPENED\n"
            "* `DENIED` - DENIED\n"
            "* `SIGNED` - SIGNED\n"
            "* `DEPRECATED` - DEPRECATED\n"
        )
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
