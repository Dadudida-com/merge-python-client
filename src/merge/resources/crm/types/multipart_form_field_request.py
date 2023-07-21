# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .multipart_form_field_request_encoding import MultipartFormFieldRequestEncoding


class MultipartFormFieldRequest(pydantic.BaseModel):
    """
    # The MultipartFormField Object
    ### Description
    The `MultipartFormField` object is used to represent fields in an HTTP request using `multipart/form-data`.

    ### Usage Example
    Create a `MultipartFormField` to define a multipart form entry.
    """

    name: str = pydantic.Field(
        description='The name of the form field <span style="white-space: nowrap">`non-empty`</span> '
    )
    data: str = pydantic.Field(
        description='The data for the form field. <span style="white-space: nowrap">`non-empty`</span> '
    )
    encoding: typing.Optional[MultipartFormFieldRequestEncoding] = pydantic.Field(
        description=(
            "The encoding of the value of `data`. Defaults to `RAW` if not defined.\n"
            "\n"
            "* `RAW` - RAW\n"
            "* `BASE64` - BASE64\n"
            "* `GZIP_BASE64` - GZIP_BASE64\n"
        )
    )
    file_name: typing.Optional[str] = pydantic.Field(
        description="The file name of the form field, if the field is for a file."
    )
    content_type: typing.Optional[str] = pydantic.Field(
        description="The MIME type of the file, if the field is for a file."
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
