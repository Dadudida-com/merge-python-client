# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .attachment_attachment_type import AttachmentAttachmentType
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Attachment(pydantic.BaseModel):
    """
    # The Attachment Object
    ### Description
    The `Attachment` object is used to represent a file attached to a candidate.
    ### Usage Example
    Fetch from the `LIST Attachments` endpoint and view attachments accessible by a company.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    file_name: typing.Optional[str] = pydantic.Field(description="The attachment's name.")
    file_url: typing.Optional[str] = pydantic.Field(description="The attachment's url.")
    candidate: typing.Optional[str] = pydantic.Field(description="")
    attachment_type: typing.Optional[AttachmentAttachmentType] = pydantic.Field(
        description=(
            "The attachment's type.\n"
            "\n"
            "* `RESUME` - RESUME\n"
            "* `COVER_LETTER` - COVER_LETTER\n"
            "* `OFFER_LETTER` - OFFER_LETTER\n"
            "* `OTHER` - OTHER\n"
        )
    )
    remote_was_deleted: typing.Optional[bool]
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
