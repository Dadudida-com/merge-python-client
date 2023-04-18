# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...types import shared_params
from ..._utils import PropertyInfo

__all__ = ["ContactCreateParams", "Model", "ModelPhoneNumber", "ModelEmailAddress"]


class ModelPhoneNumber(TypedDict, total=False):
    integration_params: Optional[object]

    linked_account_params: Optional[object]

    phone_number: Optional[str]
    """The phone number."""

    phone_number_type: Literal["HOME", "WORK", "MOBILE", "SKYPE", "OTHER"]
    """
    - `HOME` - HOME
    - `WORK` - WORK
    - `MOBILE` - MOBILE
    - `SKYPE` - SKYPE
    - `OTHER` - OTHER
    """

    value: Optional[str]
    """The phone number."""


class ModelEmailAddress(TypedDict, total=False):
    email_address: Optional[str]
    """The email address."""

    email_address_type: Literal["PERSONAL", "WORK", "OTHER"]
    """
    - `PERSONAL` - PERSONAL
    - `WORK` - WORK
    - `OTHER` - OTHER
    """

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    value: Optional[str]
    """The email address."""


class Model(TypedDict, total=False):
    account: Optional[str]
    """The contact's account."""

    addresses: List[Optional[str]]
    """`Address` object IDs for the given `Contacts` object."""

    company: Optional[str]
    """The company the contact belongs to."""

    country: shared_params.Country
    """
    - `AF` - Afghanistan
    - `AX` - Åland Islands
    - `AL` - Albania
    - `DZ` - Algeria
    - `AS` - American Samoa
    - `AD` - Andorra
    - `AO` - Angola
    - `AI` - Anguilla
    - `AQ` - Antarctica
    - `AG` - Antigua and Barbuda
    - `AR` - Argentina
    - `AM` - Armenia
    - `AW` - Aruba
    - `AU` - Australia
    - `AT` - Austria
    - `AZ` - Azerbaijan
    - `BS` - Bahamas
    - `BH` - Bahrain
    - `BD` - Bangladesh
    - `BB` - Barbados
    - `BY` - Belarus
    - `BE` - Belgium
    - `BZ` - Belize
    - `BJ` - Benin
    - `BM` - Bermuda
    - `BT` - Bhutan
    - `BO` - Bolivia
    - `BQ` - Bonaire, Sint Eustatius and Saba
    - `BA` - Bosnia and Herzegovina
    - `BW` - Botswana
    - `BV` - Bouvet Island
    - `BR` - Brazil
    - `IO` - British Indian Ocean Territory
    - `BN` - Brunei
    - `BG` - Bulgaria
    - `BF` - Burkina Faso
    - `BI` - Burundi
    - `CV` - Cabo Verde
    - `KH` - Cambodia
    - `CM` - Cameroon
    - `CA` - Canada
    - `KY` - Cayman Islands
    - `CF` - Central African Republic
    - `TD` - Chad
    - `CL` - Chile
    - `CN` - China
    - `CX` - Christmas Island
    - `CC` - Cocos (Keeling) Islands
    - `CO` - Colombia
    - `KM` - Comoros
    - `CG` - Congo
    - `CD` - Congo (the Democratic Republic of the)
    - `CK` - Cook Islands
    - `CR` - Costa Rica
    - `CI` - Côte d'Ivoire
    - `HR` - Croatia
    - `CU` - Cuba
    - `CW` - Curaçao
    - `CY` - Cyprus
    - `CZ` - Czechia
    - `DK` - Denmark
    - `DJ` - Djibouti
    - `DM` - Dominica
    - `DO` - Dominican Republic
    - `EC` - Ecuador
    - `EG` - Egypt
    - `SV` - El Salvador
    - `GQ` - Equatorial Guinea
    - `ER` - Eritrea
    - `EE` - Estonia
    - `SZ` - Eswatini
    - `ET` - Ethiopia
    - `FK` - Falkland Islands (Malvinas)
    - `FO` - Faroe Islands
    - `FJ` - Fiji
    - `FI` - Finland
    - `FR` - France
    - `GF` - French Guiana
    - `PF` - French Polynesia
    - `TF` - French Southern Territories
    - `GA` - Gabon
    - `GM` - Gambia
    - `GE` - Georgia
    - `DE` - Germany
    - `GH` - Ghana
    - `GI` - Gibraltar
    - `GR` - Greece
    - `GL` - Greenland
    - `GD` - Grenada
    - `GP` - Guadeloupe
    - `GU` - Guam
    - `GT` - Guatemala
    - `GG` - Guernsey
    - `GN` - Guinea
    - `GW` - Guinea-Bissau
    - `GY` - Guyana
    - `HT` - Haiti
    - `HM` - Heard Island and McDonald Islands
    - `VA` - Holy See
    - `HN` - Honduras
    - `HK` - Hong Kong
    - `HU` - Hungary
    - `IS` - Iceland
    - `IN` - India
    - `ID` - Indonesia
    - `IR` - Iran
    - `IQ` - Iraq
    - `IE` - Ireland
    - `IM` - Isle of Man
    - `IL` - Israel
    - `IT` - Italy
    - `JM` - Jamaica
    - `JP` - Japan
    - `JE` - Jersey
    - `JO` - Jordan
    - `KZ` - Kazakhstan
    - `KE` - Kenya
    - `KI` - Kiribati
    - `KW` - Kuwait
    - `KG` - Kyrgyzstan
    - `LA` - Laos
    - `LV` - Latvia
    - `LB` - Lebanon
    - `LS` - Lesotho
    - `LR` - Liberia
    - `LY` - Libya
    - `LI` - Liechtenstein
    - `LT` - Lithuania
    - `LU` - Luxembourg
    - `MO` - Macao
    - `MG` - Madagascar
    - `MW` - Malawi
    - `MY` - Malaysia
    - `MV` - Maldives
    - `ML` - Mali
    - `MT` - Malta
    - `MH` - Marshall Islands
    - `MQ` - Martinique
    - `MR` - Mauritania
    - `MU` - Mauritius
    - `YT` - Mayotte
    - `MX` - Mexico
    - `FM` - Micronesia (Federated States of)
    - `MD` - Moldova
    - `MC` - Monaco
    - `MN` - Mongolia
    - `ME` - Montenegro
    - `MS` - Montserrat
    - `MA` - Morocco
    - `MZ` - Mozambique
    - `MM` - Myanmar
    - `NA` - Namibia
    - `NR` - Nauru
    - `NP` - Nepal
    - `NL` - Netherlands
    - `NC` - New Caledonia
    - `NZ` - New Zealand
    - `NI` - Nicaragua
    - `NE` - Niger
    - `NG` - Nigeria
    - `NU` - Niue
    - `NF` - Norfolk Island
    - `KP` - North Korea
    - `MK` - North Macedonia
    - `MP` - Northern Mariana Islands
    - `NO` - Norway
    - `OM` - Oman
    - `PK` - Pakistan
    - `PW` - Palau
    - `PS` - Palestine, State of
    - `PA` - Panama
    - `PG` - Papua New Guinea
    - `PY` - Paraguay
    - `PE` - Peru
    - `PH` - Philippines
    - `PN` - Pitcairn
    - `PL` - Poland
    - `PT` - Portugal
    - `PR` - Puerto Rico
    - `QA` - Qatar
    - `RE` - Réunion
    - `RO` - Romania
    - `RU` - Russia
    - `RW` - Rwanda
    - `BL` - Saint Barthélemy
    - `SH` - Saint Helena, Ascension and Tristan da Cunha
    - `KN` - Saint Kitts and Nevis
    - `LC` - Saint Lucia
    - `MF` - Saint Martin (French part)
    - `PM` - Saint Pierre and Miquelon
    - `VC` - Saint Vincent and the Grenadines
    - `WS` - Samoa
    - `SM` - San Marino
    - `ST` - Sao Tome and Principe
    - `SA` - Saudi Arabia
    - `SN` - Senegal
    - `RS` - Serbia
    - `SC` - Seychelles
    - `SL` - Sierra Leone
    - `SG` - Singapore
    - `SX` - Sint Maarten (Dutch part)
    - `SK` - Slovakia
    - `SI` - Slovenia
    - `SB` - Solomon Islands
    - `SO` - Somalia
    - `ZA` - South Africa
    - `GS` - South Georgia and the South Sandwich Islands
    - `KR` - South Korea
    - `SS` - South Sudan
    - `ES` - Spain
    - `LK` - Sri Lanka
    - `SD` - Sudan
    - `SR` - Suriname
    - `SJ` - Svalbard and Jan Mayen
    - `SE` - Sweden
    - `CH` - Switzerland
    - `SY` - Syria
    - `TW` - Taiwan
    - `TJ` - Tajikistan
    - `TZ` - Tanzania
    - `TH` - Thailand
    - `TL` - Timor-Leste
    - `TG` - Togo
    - `TK` - Tokelau
    - `TO` - Tonga
    - `TT` - Trinidad and Tobago
    - `TN` - Tunisia
    - `TR` - Turkey
    - `TM` - Turkmenistan
    - `TC` - Turks and Caicos Islands
    - `TV` - Tuvalu
    - `UG` - Uganda
    - `UA` - Ukraine
    - `AE` - United Arab Emirates
    - `GB` - United Kingdom
    - `UM` - United States Minor Outlying Islands
    - `US` - United States of America
    - `UY` - Uruguay
    - `UZ` - Uzbekistan
    - `VU` - Vanuatu
    - `VE` - Venezuela
    - `VN` - Vietnam
    - `VG` - Virgin Islands (British)
    - `VI` - Virgin Islands (U.S.)
    - `WF` - Wallis and Futuna
    - `EH` - Western Sahara
    - `YE` - Yemen
    - `ZM` - Zambia
    - `ZW` - Zimbabwe
    """

    currency: Optional[str]
    """The currency the contact's transactions are in."""

    email: Optional[str]
    """The contact's email."""

    email_address: Optional[str]
    """The contact's email address."""

    email_addresses: List[ModelEmailAddress]

    first_name: Optional[str]
    """The contact's first name."""

    integration_params: Optional[object]

    is_customer: Optional[bool]
    """Whether the contact is a customer."""

    is_supplier: Optional[bool]
    """Whether the contact is a supplier."""

    last_activity_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the contact's last activity occurred."""

    last_name: Optional[str]
    """The contact's last name."""

    linked_account_params: Optional[object]

    name: Optional[str]
    """The contact's name."""

    phone: Optional[str]
    """The contact's phone."""

    phone_numbers: List[ModelPhoneNumber]
    """`AccountingPhoneNumber` object for the given `Contacts` object."""

    postal_code: Optional[str]
    """The contact's postal code."""

    state: Optional[str]
    """The contact's state."""

    status: Literal["ACTIVE", "ARCHIVED"]
    """
    - `ACTIVE` - ACTIVE
    - `ARCHIVED` - ARCHIVED
    """

    tax_number: Optional[str]
    """The contact's tax number."""


class ContactCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Contact Object

    ### Description

    The `Contact` object is used to represent a contact in the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/contact` endpoint and view their phone numbers.
    """
