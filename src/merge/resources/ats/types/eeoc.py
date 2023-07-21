# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .eeoc_disability_status import EeocDisabilityStatus
from .eeoc_gender import EeocGender
from .eeoc_race import EeocRace
from .eeoc_veteran_status import EeocVeteranStatus
from .remote_data import RemoteData


class Eeoc(pydantic.BaseModel):
    """
    # The EEOC Object
    ### Description
    The `EEOC` object is used to represent the Equal Employment Opportunity Commission information for a candidate (race, gender, veteran status, disability status).
    ### Usage Example
    Fetch from the `LIST EEOCs` endpoint and filter by `candidate` to show all EEOC information for a candidate.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    candidate: typing.Optional[str] = pydantic.Field(description="The candidate being represented.")
    submitted_at: typing.Optional[str] = pydantic.Field(description="When the information was submitted.")
    race: typing.Optional[EeocRace] = pydantic.Field(
        description=(
            "The candidate's race.\n"
            "\n"
            "* `AMERICAN_INDIAN_OR_ALASKAN_NATIVE` - AMERICAN_INDIAN_OR_ALASKAN_NATIVE\n"
            "* `ASIAN` - ASIAN\n"
            "* `BLACK_OR_AFRICAN_AMERICAN` - BLACK_OR_AFRICAN_AMERICAN\n"
            "* `HISPANIC_OR_LATINO` - HISPANIC_OR_LATINO\n"
            "* `WHITE` - WHITE\n"
            "* `NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER` - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER\n"
            "* `TWO_OR_MORE_RACES` - TWO_OR_MORE_RACES\n"
            "* `DECLINE_TO_SELF_IDENTIFY` - DECLINE_TO_SELF_IDENTIFY\n"
        )
    )
    gender: typing.Optional[EeocGender] = pydantic.Field(
        description=(
            "The candidate's gender.\n"
            "\n"
            "* `MALE` - MALE\n"
            "* `FEMALE` - FEMALE\n"
            "* `NON-BINARY` - NON-BINARY\n"
            "* `OTHER` - OTHER\n"
            "* `DECLINE_TO_SELF_IDENTIFY` - DECLINE_TO_SELF_IDENTIFY\n"
        )
    )
    veteran_status: typing.Optional[EeocVeteranStatus] = pydantic.Field(
        description=(
            "The candidate's veteran status.\n"
            "\n"
            "* `I_AM_NOT_A_PROTECTED_VETERAN` - I_AM_NOT_A_PROTECTED_VETERAN\n"
            "* `I_IDENTIFY_AS_ONE_OR_MORE_OF_THE_CLASSIFICATIONS_OF_A_PROTECTED_VETERAN` - I_IDENTIFY_AS_ONE_OR_MORE_OF_THE_CLASSIFICATIONS_OF_A_PROTECTED_VETERAN\n"
            "* `I_DONT_WISH_TO_ANSWER` - I_DONT_WISH_TO_ANSWER\n"
        )
    )
    disability_status: typing.Optional[EeocDisabilityStatus] = pydantic.Field(
        description=(
            "The candidate's disability status.\n"
            "\n"
            "* `YES_I_HAVE_A_DISABILITY_OR_PREVIOUSLY_HAD_A_DISABILITY` - YES_I_HAVE_A_DISABILITY_OR_PREVIOUSLY_HAD_A_DISABILITY\n"
            "* `NO_I_DONT_HAVE_A_DISABILITY` - NO_I_DONT_HAVE_A_DISABILITY\n"
            "* `I_DONT_WISH_TO_ANSWER` - I_DONT_WISH_TO_ANSWER\n"
        )
    )
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
