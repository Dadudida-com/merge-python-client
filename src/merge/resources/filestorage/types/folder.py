# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class Folder(pydantic.BaseModel):
    """
    # The Folder Object
    ### Description
    The `Folder` object is used to represent a collection of files and/or folders in the workspace. Could be within a drive, if it exists.
    ### Usage Example
    Fetch from the `GET /api/filestorage/v1/folders` endpoint and view their folders.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The folder's name.")
    folder_url: typing.Optional[str] = pydantic.Field(description="The URL to access the folder.")
    size: typing.Optional[int] = pydantic.Field(description="The folder's size, in bytes.")
    description: typing.Optional[str] = pydantic.Field(description="The folder's description.")
    parent_folder: typing.Optional[str] = pydantic.Field(description="The folder that the folder belongs to.")
    drive: typing.Optional[str] = pydantic.Field(description="The drive that the folder belongs to.")
    permissions: typing.List[str] = pydantic.Field(
        description="The Permission object is used to represent a user's or group's access to a File or Folder. Permissions are unexpanded by default. Use the query param `expand=permissions` to see more details under `GET /folders`."
    )
    remote_created_at: typing.Optional[str] = pydantic.Field(description="When the third party's folder was created.")
    remote_updated_at: typing.Optional[str] = pydantic.Field(description="When the third party's folder was updated.")
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[str] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Any]]]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
