# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .location_country import LocationCountry
from .location_location_type import LocationLocationType
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Location(pydantic.BaseModel):
    """
    # The Location Object
    ### Description
    The `Location` object is used to represent an address that can be associated with an employee.

    ### Usage Example
    Fetch from the `LIST Locations` endpoint and filter by `ID` to show all office locations.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The location's name.")
    phone_number: typing.Optional[str] = pydantic.Field(description="The location's phone number.")
    street_1: typing.Optional[str] = pydantic.Field(description="Line 1 of the location's street address.")
    street_2: typing.Optional[str] = pydantic.Field(description="Line 2 of the location's street address.")
    city: typing.Optional[str] = pydantic.Field(description="The location's city.")
    state: typing.Optional[str] = pydantic.Field(
        description="The location's state. Represents a region if outside of the US."
    )
    zip_code: typing.Optional[str] = pydantic.Field(description="The location's zip code or postal code.")
    country: typing.Optional[LocationCountry] = pydantic.Field(
        description=(
            "The location's country.\n"
            "\n"
            "* `AF` - Afghanistan\n"
            "* `AX` - Åland Islands\n"
            "* `AL` - Albania\n"
            "* `DZ` - Algeria\n"
            "* `AS` - American Samoa\n"
            "* `AD` - Andorra\n"
            "* `AO` - Angola\n"
            "* `AI` - Anguilla\n"
            "* `AQ` - Antarctica\n"
            "* `AG` - Antigua and Barbuda\n"
            "* `AR` - Argentina\n"
            "* `AM` - Armenia\n"
            "* `AW` - Aruba\n"
            "* `AU` - Australia\n"
            "* `AT` - Austria\n"
            "* `AZ` - Azerbaijan\n"
            "* `BS` - Bahamas\n"
            "* `BH` - Bahrain\n"
            "* `BD` - Bangladesh\n"
            "* `BB` - Barbados\n"
            "* `BY` - Belarus\n"
            "* `BE` - Belgium\n"
            "* `BZ` - Belize\n"
            "* `BJ` - Benin\n"
            "* `BM` - Bermuda\n"
            "* `BT` - Bhutan\n"
            "* `BO` - Bolivia\n"
            "* `BQ` - Bonaire, Sint Eustatius and Saba\n"
            "* `BA` - Bosnia and Herzegovina\n"
            "* `BW` - Botswana\n"
            "* `BV` - Bouvet Island\n"
            "* `BR` - Brazil\n"
            "* `IO` - British Indian Ocean Territory\n"
            "* `BN` - Brunei\n"
            "* `BG` - Bulgaria\n"
            "* `BF` - Burkina Faso\n"
            "* `BI` - Burundi\n"
            "* `CV` - Cabo Verde\n"
            "* `KH` - Cambodia\n"
            "* `CM` - Cameroon\n"
            "* `CA` - Canada\n"
            "* `KY` - Cayman Islands\n"
            "* `CF` - Central African Republic\n"
            "* `TD` - Chad\n"
            "* `CL` - Chile\n"
            "* `CN` - China\n"
            "* `CX` - Christmas Island\n"
            "* `CC` - Cocos (Keeling) Islands\n"
            "* `CO` - Colombia\n"
            "* `KM` - Comoros\n"
            "* `CG` - Congo\n"
            "* `CD` - Congo (the Democratic Republic of the)\n"
            "* `CK` - Cook Islands\n"
            "* `CR` - Costa Rica\n"
            "* `CI` - Côte d'Ivoire\n"
            "* `HR` - Croatia\n"
            "* `CU` - Cuba\n"
            "* `CW` - Curaçao\n"
            "* `CY` - Cyprus\n"
            "* `CZ` - Czechia\n"
            "* `DK` - Denmark\n"
            "* `DJ` - Djibouti\n"
            "* `DM` - Dominica\n"
            "* `DO` - Dominican Republic\n"
            "* `EC` - Ecuador\n"
            "* `EG` - Egypt\n"
            "* `SV` - El Salvador\n"
            "* `GQ` - Equatorial Guinea\n"
            "* `ER` - Eritrea\n"
            "* `EE` - Estonia\n"
            "* `SZ` - Eswatini\n"
            "* `ET` - Ethiopia\n"
            "* `FK` - Falkland Islands (Malvinas)\n"
            "* `FO` - Faroe Islands\n"
            "* `FJ` - Fiji\n"
            "* `FI` - Finland\n"
            "* `FR` - France\n"
            "* `GF` - French Guiana\n"
            "* `PF` - French Polynesia\n"
            "* `TF` - French Southern Territories\n"
            "* `GA` - Gabon\n"
            "* `GM` - Gambia\n"
            "* `GE` - Georgia\n"
            "* `DE` - Germany\n"
            "* `GH` - Ghana\n"
            "* `GI` - Gibraltar\n"
            "* `GR` - Greece\n"
            "* `GL` - Greenland\n"
            "* `GD` - Grenada\n"
            "* `GP` - Guadeloupe\n"
            "* `GU` - Guam\n"
            "* `GT` - Guatemala\n"
            "* `GG` - Guernsey\n"
            "* `GN` - Guinea\n"
            "* `GW` - Guinea-Bissau\n"
            "* `GY` - Guyana\n"
            "* `HT` - Haiti\n"
            "* `HM` - Heard Island and McDonald Islands\n"
            "* `VA` - Holy See\n"
            "* `HN` - Honduras\n"
            "* `HK` - Hong Kong\n"
            "* `HU` - Hungary\n"
            "* `IS` - Iceland\n"
            "* `IN` - India\n"
            "* `ID` - Indonesia\n"
            "* `IR` - Iran\n"
            "* `IQ` - Iraq\n"
            "* `IE` - Ireland\n"
            "* `IM` - Isle of Man\n"
            "* `IL` - Israel\n"
            "* `IT` - Italy\n"
            "* `JM` - Jamaica\n"
            "* `JP` - Japan\n"
            "* `JE` - Jersey\n"
            "* `JO` - Jordan\n"
            "* `KZ` - Kazakhstan\n"
            "* `KE` - Kenya\n"
            "* `KI` - Kiribati\n"
            "* `KW` - Kuwait\n"
            "* `KG` - Kyrgyzstan\n"
            "* `LA` - Laos\n"
            "* `LV` - Latvia\n"
            "* `LB` - Lebanon\n"
            "* `LS` - Lesotho\n"
            "* `LR` - Liberia\n"
            "* `LY` - Libya\n"
            "* `LI` - Liechtenstein\n"
            "* `LT` - Lithuania\n"
            "* `LU` - Luxembourg\n"
            "* `MO` - Macao\n"
            "* `MG` - Madagascar\n"
            "* `MW` - Malawi\n"
            "* `MY` - Malaysia\n"
            "* `MV` - Maldives\n"
            "* `ML` - Mali\n"
            "* `MT` - Malta\n"
            "* `MH` - Marshall Islands\n"
            "* `MQ` - Martinique\n"
            "* `MR` - Mauritania\n"
            "* `MU` - Mauritius\n"
            "* `YT` - Mayotte\n"
            "* `MX` - Mexico\n"
            "* `FM` - Micronesia (Federated States of)\n"
            "* `MD` - Moldova\n"
            "* `MC` - Monaco\n"
            "* `MN` - Mongolia\n"
            "* `ME` - Montenegro\n"
            "* `MS` - Montserrat\n"
            "* `MA` - Morocco\n"
            "* `MZ` - Mozambique\n"
            "* `MM` - Myanmar\n"
            "* `NA` - Namibia\n"
            "* `NR` - Nauru\n"
            "* `NP` - Nepal\n"
            "* `NL` - Netherlands\n"
            "* `NC` - New Caledonia\n"
            "* `NZ` - New Zealand\n"
            "* `NI` - Nicaragua\n"
            "* `NE` - Niger\n"
            "* `NG` - Nigeria\n"
            "* `NU` - Niue\n"
            "* `NF` - Norfolk Island\n"
            "* `KP` - North Korea\n"
            "* `MK` - North Macedonia\n"
            "* `MP` - Northern Mariana Islands\n"
            "* `NO` - Norway\n"
            "* `OM` - Oman\n"
            "* `PK` - Pakistan\n"
            "* `PW` - Palau\n"
            "* `PS` - Palestine, State of\n"
            "* `PA` - Panama\n"
            "* `PG` - Papua New Guinea\n"
            "* `PY` - Paraguay\n"
            "* `PE` - Peru\n"
            "* `PH` - Philippines\n"
            "* `PN` - Pitcairn\n"
            "* `PL` - Poland\n"
            "* `PT` - Portugal\n"
            "* `PR` - Puerto Rico\n"
            "* `QA` - Qatar\n"
            "* `RE` - Réunion\n"
            "* `RO` - Romania\n"
            "* `RU` - Russia\n"
            "* `RW` - Rwanda\n"
            "* `BL` - Saint Barthélemy\n"
            "* `SH` - Saint Helena, Ascension and Tristan da Cunha\n"
            "* `KN` - Saint Kitts and Nevis\n"
            "* `LC` - Saint Lucia\n"
            "* `MF` - Saint Martin (French part)\n"
            "* `PM` - Saint Pierre and Miquelon\n"
            "* `VC` - Saint Vincent and the Grenadines\n"
            "* `WS` - Samoa\n"
            "* `SM` - San Marino\n"
            "* `ST` - Sao Tome and Principe\n"
            "* `SA` - Saudi Arabia\n"
            "* `SN` - Senegal\n"
            "* `RS` - Serbia\n"
            "* `SC` - Seychelles\n"
            "* `SL` - Sierra Leone\n"
            "* `SG` - Singapore\n"
            "* `SX` - Sint Maarten (Dutch part)\n"
            "* `SK` - Slovakia\n"
            "* `SI` - Slovenia\n"
            "* `SB` - Solomon Islands\n"
            "* `SO` - Somalia\n"
            "* `ZA` - South Africa\n"
            "* `GS` - South Georgia and the South Sandwich Islands\n"
            "* `KR` - South Korea\n"
            "* `SS` - South Sudan\n"
            "* `ES` - Spain\n"
            "* `LK` - Sri Lanka\n"
            "* `SD` - Sudan\n"
            "* `SR` - Suriname\n"
            "* `SJ` - Svalbard and Jan Mayen\n"
            "* `SE` - Sweden\n"
            "* `CH` - Switzerland\n"
            "* `SY` - Syria\n"
            "* `TW` - Taiwan\n"
            "* `TJ` - Tajikistan\n"
            "* `TZ` - Tanzania\n"
            "* `TH` - Thailand\n"
            "* `TL` - Timor-Leste\n"
            "* `TG` - Togo\n"
            "* `TK` - Tokelau\n"
            "* `TO` - Tonga\n"
            "* `TT` - Trinidad and Tobago\n"
            "* `TN` - Tunisia\n"
            "* `TR` - Turkey\n"
            "* `TM` - Turkmenistan\n"
            "* `TC` - Turks and Caicos Islands\n"
            "* `TV` - Tuvalu\n"
            "* `UG` - Uganda\n"
            "* `UA` - Ukraine\n"
            "* `AE` - United Arab Emirates\n"
            "* `GB` - United Kingdom\n"
            "* `UM` - United States Minor Outlying Islands\n"
            "* `US` - United States of America\n"
            "* `UY` - Uruguay\n"
            "* `UZ` - Uzbekistan\n"
            "* `VU` - Vanuatu\n"
            "* `VE` - Venezuela\n"
            "* `VN` - Vietnam\n"
            "* `VG` - Virgin Islands (British)\n"
            "* `VI` - Virgin Islands (U.S.)\n"
            "* `WF` - Wallis and Futuna\n"
            "* `EH` - Western Sahara\n"
            "* `YE` - Yemen\n"
            "* `ZM` - Zambia\n"
            "* `ZW` - Zimbabwe\n"
        )
    )
    location_type: typing.Optional[LocationLocationType] = pydantic.Field(
        description=("The location's type. Can be either WORK or HOME\n" "\n" "* `HOME` - HOME\n" "* `WORK` - WORK\n")
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
