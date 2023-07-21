# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .accounting_phone_number import AccountingPhoneNumber
from .address import Address
from .company_info_currency import CompanyInfoCurrency
from .remote_data import RemoteData


class CompanyInfo(pydantic.BaseModel):
    """
    # The CompanyInfo Object
    ### Description
    The `CompanyInfo` object is used to represent a company's information.

    ### Usage Example
    Fetch from the `GET CompanyInfo` endpoint and view a company's information.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The company's name.")
    legal_name: typing.Optional[str] = pydantic.Field(description="The company's legal name.")
    tax_number: typing.Optional[str] = pydantic.Field(description="The company's tax number.")
    fiscal_year_end_month: typing.Optional[int] = pydantic.Field(description="The company's fiscal year end month.")
    fiscal_year_end_day: typing.Optional[int] = pydantic.Field(description="The company's fiscal year end day.")
    currency: typing.Optional[CompanyInfoCurrency] = pydantic.Field(
        description=(
            "The currency set in the company's accounting platform.\n"
            "\n"
            "* `XUA` - ADB Unit of Account\n"
            "* `AFN` - Afghan Afghani\n"
            "* `AFA` - Afghan Afghani (1927–2002)\n"
            "* `ALL` - Albanian Lek\n"
            "* `ALK` - Albanian Lek (1946–1965)\n"
            "* `DZD` - Algerian Dinar\n"
            "* `ADP` - Andorran Peseta\n"
            "* `AOA` - Angolan Kwanza\n"
            "* `AOK` - Angolan Kwanza (1977–1991)\n"
            "* `AON` - Angolan New Kwanza (1990–2000)\n"
            "* `AOR` - Angolan Readjusted Kwanza (1995–1999)\n"
            "* `ARA` - Argentine Austral\n"
            "* `ARS` - Argentine Peso\n"
            "* `ARM` - Argentine Peso (1881–1970)\n"
            "* `ARP` - Argentine Peso (1983–1985)\n"
            "* `ARL` - Argentine Peso Ley (1970–1983)\n"
            "* `AMD` - Armenian Dram\n"
            "* `AWG` - Aruban Florin\n"
            "* `AUD` - Australian Dollar\n"
            "* `ATS` - Austrian Schilling\n"
            "* `AZN` - Azerbaijani Manat\n"
            "* `AZM` - Azerbaijani Manat (1993–2006)\n"
            "* `BSD` - Bahamian Dollar\n"
            "* `BHD` - Bahraini Dinar\n"
            "* `BDT` - Bangladeshi Taka\n"
            "* `BBD` - Barbadian Dollar\n"
            "* `BYN` - Belarusian Ruble\n"
            "* `BYB` - Belarusian Ruble (1994–1999)\n"
            "* `BYR` - Belarusian Ruble (2000–2016)\n"
            "* `BEF` - Belgian Franc\n"
            "* `BEC` - Belgian Franc (convertible)\n"
            "* `BEL` - Belgian Franc (financial)\n"
            "* `BZD` - Belize Dollar\n"
            "* `BMD` - Bermudan Dollar\n"
            "* `BTN` - Bhutanese Ngultrum\n"
            "* `BOB` - Bolivian Boliviano\n"
            "* `BOL` - Bolivian Boliviano (1863–1963)\n"
            "* `BOV` - Bolivian Mvdol\n"
            "* `BOP` - Bolivian Peso\n"
            "* `BAM` - Bosnia-Herzegovina Convertible Mark\n"
            "* `BAD` - Bosnia-Herzegovina Dinar (1992–1994)\n"
            "* `BAN` - Bosnia-Herzegovina New Dinar (1994–1997)\n"
            "* `BWP` - Botswanan Pula\n"
            "* `BRC` - Brazilian Cruzado (1986–1989)\n"
            "* `BRZ` - Brazilian Cruzeiro (1942–1967)\n"
            "* `BRE` - Brazilian Cruzeiro (1990–1993)\n"
            "* `BRR` - Brazilian Cruzeiro (1993–1994)\n"
            "* `BRN` - Brazilian New Cruzado (1989–1990)\n"
            "* `BRB` - Brazilian New Cruzeiro (1967–1986)\n"
            "* `BRL` - Brazilian Real\n"
            "* `GBP` - British Pound\n"
            "* `BND` - Brunei Dollar\n"
            "* `BGL` - Bulgarian Hard Lev\n"
            "* `BGN` - Bulgarian Lev\n"
            "* `BGO` - Bulgarian Lev (1879–1952)\n"
            "* `BGM` - Bulgarian Socialist Lev\n"
            "* `BUK` - Burmese Kyat\n"
            "* `BIF` - Burundian Franc\n"
            "* `XPF` - CFP Franc\n"
            "* `KHR` - Cambodian Riel\n"
            "* `CAD` - Canadian Dollar\n"
            "* `CVE` - Cape Verdean Escudo\n"
            "* `KYD` - Cayman Islands Dollar\n"
            "* `XAF` - Central African CFA Franc\n"
            "* `CLE` - Chilean Escudo\n"
            "* `CLP` - Chilean Peso\n"
            "* `CLF` - Chilean Unit of Account (UF)\n"
            "* `CNX` - Chinese People’s Bank Dollar\n"
            "* `CNY` - Chinese Yuan\n"
            "* `CNH` - Chinese Yuan (offshore)\n"
            "* `COP` - Colombian Peso\n"
            "* `COU` - Colombian Real Value Unit\n"
            "* `KMF` - Comorian Franc\n"
            "* `CDF` - Congolese Franc\n"
            "* `CRC` - Costa Rican Colón\n"
            "* `HRD` - Croatian Dinar\n"
            "* `HRK` - Croatian Kuna\n"
            "* `CUC` - Cuban Convertible Peso\n"
            "* `CUP` - Cuban Peso\n"
            "* `CYP` - Cypriot Pound\n"
            "* `CZK` - Czech Koruna\n"
            "* `CSK` - Czechoslovak Hard Koruna\n"
            "* `DKK` - Danish Krone\n"
            "* `DJF` - Djiboutian Franc\n"
            "* `DOP` - Dominican Peso\n"
            "* `NLG` - Dutch Guilder\n"
            "* `XCD` - East Caribbean Dollar\n"
            "* `DDM` - East German Mark\n"
            "* `ECS` - Ecuadorian Sucre\n"
            "* `ECV` - Ecuadorian Unit of Constant Value\n"
            "* `EGP` - Egyptian Pound\n"
            "* `GQE` - Equatorial Guinean Ekwele\n"
            "* `ERN` - Eritrean Nakfa\n"
            "* `EEK` - Estonian Kroon\n"
            "* `ETB` - Ethiopian Birr\n"
            "* `EUR` - Euro\n"
            "* `XBA` - European Composite Unit\n"
            "* `XEU` - European Currency Unit\n"
            "* `XBB` - European Monetary Unit\n"
            "* `XBC` - European Unit of Account (XBC)\n"
            "* `XBD` - European Unit of Account (XBD)\n"
            "* `FKP` - Falkland Islands Pound\n"
            "* `FJD` - Fijian Dollar\n"
            "* `FIM` - Finnish Markka\n"
            "* `FRF` - French Franc\n"
            "* `XFO` - French Gold Franc\n"
            "* `XFU` - French UIC-Franc\n"
            "* `GMD` - Gambian Dalasi\n"
            "* `GEK` - Georgian Kupon Larit\n"
            "* `GEL` - Georgian Lari\n"
            "* `DEM` - German Mark\n"
            "* `GHS` - Ghanaian Cedi\n"
            "* `GHC` - Ghanaian Cedi (1979–2007)\n"
            "* `GIP` - Gibraltar Pound\n"
            "* `XAU` - Gold\n"
            "* `GRD` - Greek Drachma\n"
            "* `GTQ` - Guatemalan Quetzal\n"
            "* `GWP` - Guinea-Bissau Peso\n"
            "* `GNF` - Guinean Franc\n"
            "* `GNS` - Guinean Syli\n"
            "* `GYD` - Guyanaese Dollar\n"
            "* `HTG` - Haitian Gourde\n"
            "* `HNL` - Honduran Lempira\n"
            "* `HKD` - Hong Kong Dollar\n"
            "* `HUF` - Hungarian Forint\n"
            "* `IMP` - IMP\n"
            "* `ISK` - Icelandic Króna\n"
            "* `ISJ` - Icelandic Króna (1918–1981)\n"
            "* `INR` - Indian Rupee\n"
            "* `IDR` - Indonesian Rupiah\n"
            "* `IRR` - Iranian Rial\n"
            "* `IQD` - Iraqi Dinar\n"
            "* `IEP` - Irish Pound\n"
            "* `ILS` - Israeli New Shekel\n"
            "* `ILP` - Israeli Pound\n"
            "* `ILR` - Israeli Shekel (1980–1985)\n"
            "* `ITL` - Italian Lira\n"
            "* `JMD` - Jamaican Dollar\n"
            "* `JPY` - Japanese Yen\n"
            "* `JOD` - Jordanian Dinar\n"
            "* `KZT` - Kazakhstani Tenge\n"
            "* `KES` - Kenyan Shilling\n"
            "* `KWD` - Kuwaiti Dinar\n"
            "* `KGS` - Kyrgystani Som\n"
            "* `LAK` - Laotian Kip\n"
            "* `LVL` - Latvian Lats\n"
            "* `LVR` - Latvian Ruble\n"
            "* `LBP` - Lebanese Pound\n"
            "* `LSL` - Lesotho Loti\n"
            "* `LRD` - Liberian Dollar\n"
            "* `LYD` - Libyan Dinar\n"
            "* `LTL` - Lithuanian Litas\n"
            "* `LTT` - Lithuanian Talonas\n"
            "* `LUL` - Luxembourg Financial Franc\n"
            "* `LUC` - Luxembourgian Convertible Franc\n"
            "* `LUF` - Luxembourgian Franc\n"
            "* `MOP` - Macanese Pataca\n"
            "* `MKD` - Macedonian Denar\n"
            "* `MKN` - Macedonian Denar (1992–1993)\n"
            "* `MGA` - Malagasy Ariary\n"
            "* `MGF` - Malagasy Franc\n"
            "* `MWK` - Malawian Kwacha\n"
            "* `MYR` - Malaysian Ringgit\n"
            "* `MVR` - Maldivian Rufiyaa\n"
            "* `MVP` - Maldivian Rupee (1947–1981)\n"
            "* `MLF` - Malian Franc\n"
            "* `MTL` - Maltese Lira\n"
            "* `MTP` - Maltese Pound\n"
            "* `MRU` - Mauritanian Ouguiya\n"
            "* `MRO` - Mauritanian Ouguiya (1973–2017)\n"
            "* `MUR` - Mauritian Rupee\n"
            "* `MXV` - Mexican Investment Unit\n"
            "* `MXN` - Mexican Peso\n"
            "* `MXP` - Mexican Silver Peso (1861–1992)\n"
            "* `MDC` - Moldovan Cupon\n"
            "* `MDL` - Moldovan Leu\n"
            "* `MCF` - Monegasque Franc\n"
            "* `MNT` - Mongolian Tugrik\n"
            "* `MAD` - Moroccan Dirham\n"
            "* `MAF` - Moroccan Franc\n"
            "* `MZE` - Mozambican Escudo\n"
            "* `MZN` - Mozambican Metical\n"
            "* `MZM` - Mozambican Metical (1980–2006)\n"
            "* `MMK` - Myanmar Kyat\n"
            "* `NAD` - Namibian Dollar\n"
            "* `NPR` - Nepalese Rupee\n"
            "* `ANG` - Netherlands Antillean Guilder\n"
            "* `TWD` - New Taiwan Dollar\n"
            "* `NZD` - New Zealand Dollar\n"
            "* `NIO` - Nicaraguan Córdoba\n"
            "* `NIC` - Nicaraguan Córdoba (1988–1991)\n"
            "* `NGN` - Nigerian Naira\n"
            "* `KPW` - North Korean Won\n"
            "* `NOK` - Norwegian Krone\n"
            "* `OMR` - Omani Rial\n"
            "* `PKR` - Pakistani Rupee\n"
            "* `XPD` - Palladium\n"
            "* `PAB` - Panamanian Balboa\n"
            "* `PGK` - Papua New Guinean Kina\n"
            "* `PYG` - Paraguayan Guarani\n"
            "* `PEI` - Peruvian Inti\n"
            "* `PEN` - Peruvian Sol\n"
            "* `PES` - Peruvian Sol (1863–1965)\n"
            "* `PHP` - Philippine Peso\n"
            "* `XPT` - Platinum\n"
            "* `PLN` - Polish Zloty\n"
            "* `PLZ` - Polish Zloty (1950–1995)\n"
            "* `PTE` - Portuguese Escudo\n"
            "* `GWE` - Portuguese Guinea Escudo\n"
            "* `QAR` - Qatari Rial\n"
            "* `XRE` - RINET Funds\n"
            "* `RHD` - Rhodesian Dollar\n"
            "* `RON` - Romanian Leu\n"
            "* `ROL` - Romanian Leu (1952–2006)\n"
            "* `RUB` - Russian Ruble\n"
            "* `RUR` - Russian Ruble (1991–1998)\n"
            "* `RWF` - Rwandan Franc\n"
            "* `SVC` - Salvadoran Colón\n"
            "* `WST` - Samoan Tala\n"
            "* `SAR` - Saudi Riyal\n"
            "* `RSD` - Serbian Dinar\n"
            "* `CSD` - Serbian Dinar (2002–2006)\n"
            "* `SCR` - Seychellois Rupee\n"
            "* `SLL` - Sierra Leonean Leone\n"
            "* `XAG` - Silver\n"
            "* `SGD` - Singapore Dollar\n"
            "* `SKK` - Slovak Koruna\n"
            "* `SIT` - Slovenian Tolar\n"
            "* `SBD` - Solomon Islands Dollar\n"
            "* `SOS` - Somali Shilling\n"
            "* `ZAR` - South African Rand\n"
            "* `ZAL` - South African Rand (financial)\n"
            "* `KRH` - South Korean Hwan (1953–1962)\n"
            "* `KRW` - South Korean Won\n"
            "* `KRO` - South Korean Won (1945–1953)\n"
            "* `SSP` - South Sudanese Pound\n"
            "* `SUR` - Soviet Rouble\n"
            "* `ESP` - Spanish Peseta\n"
            "* `ESA` - Spanish Peseta (A account)\n"
            "* `ESB` - Spanish Peseta (convertible account)\n"
            "* `XDR` - Special Drawing Rights\n"
            "* `LKR` - Sri Lankan Rupee\n"
            "* `SHP` - St. Helena Pound\n"
            "* `XSU` - Sucre\n"
            "* `SDD` - Sudanese Dinar (1992–2007)\n"
            "* `SDG` - Sudanese Pound\n"
            "* `SDP` - Sudanese Pound (1957–1998)\n"
            "* `SRD` - Surinamese Dollar\n"
            "* `SRG` - Surinamese Guilder\n"
            "* `SZL` - Swazi Lilangeni\n"
            "* `SEK` - Swedish Krona\n"
            "* `CHF` - Swiss Franc\n"
            "* `SYP` - Syrian Pound\n"
            "* `STN` - São Tomé & Príncipe Dobra\n"
            "* `STD` - São Tomé & Príncipe Dobra (1977–2017)\n"
            "* `TVD` - TVD\n"
            "* `TJR` - Tajikistani Ruble\n"
            "* `TJS` - Tajikistani Somoni\n"
            "* `TZS` - Tanzanian Shilling\n"
            "* `XTS` - Testing Currency Code\n"
            "* `THB` - Thai Baht\n"
            "* `XXX` - The codes assigned for transactions where no currency is involved\n"
            "* `TPE` - Timorese Escudo\n"
            "* `TOP` - Tongan Paʻanga\n"
            "* `TTD` - Trinidad & Tobago Dollar\n"
            "* `TND` - Tunisian Dinar\n"
            "* `TRY` - Turkish Lira\n"
            "* `TRL` - Turkish Lira (1922–2005)\n"
            "* `TMT` - Turkmenistani Manat\n"
            "* `TMM` - Turkmenistani Manat (1993–2009)\n"
            "* `USD` - US Dollar\n"
            "* `USN` - US Dollar (Next day)\n"
            "* `USS` - US Dollar (Same day)\n"
            "* `UGX` - Ugandan Shilling\n"
            "* `UGS` - Ugandan Shilling (1966–1987)\n"
            "* `UAH` - Ukrainian Hryvnia\n"
            "* `UAK` - Ukrainian Karbovanets\n"
            "* `AED` - United Arab Emirates Dirham\n"
            "* `UYW` - Uruguayan Nominal Wage Index Unit\n"
            "* `UYU` - Uruguayan Peso\n"
            "* `UYP` - Uruguayan Peso (1975–1993)\n"
            "* `UYI` - Uruguayan Peso (Indexed Units)\n"
            "* `UZS` - Uzbekistani Som\n"
            "* `VUV` - Vanuatu Vatu\n"
            "* `VES` - Venezuelan Bolívar\n"
            "* `VEB` - Venezuelan Bolívar (1871–2008)\n"
            "* `VEF` - Venezuelan Bolívar (2008–2018)\n"
            "* `VND` - Vietnamese Dong\n"
            "* `VNN` - Vietnamese Dong (1978–1985)\n"
            "* `CHE` - WIR Euro\n"
            "* `CHW` - WIR Franc\n"
            "* `XOF` - West African CFA Franc\n"
            "* `YDD` - Yemeni Dinar\n"
            "* `YER` - Yemeni Rial\n"
            "* `YUN` - Yugoslavian Convertible Dinar (1990–1992)\n"
            "* `YUD` - Yugoslavian Hard Dinar (1966–1990)\n"
            "* `YUM` - Yugoslavian New Dinar (1994–2002)\n"
            "* `YUR` - Yugoslavian Reformed Dinar (1992–1993)\n"
            "* `ZWN` - ZWN\n"
            "* `ZRN` - Zairean New Zaire (1993–1998)\n"
            "* `ZRZ` - Zairean Zaire (1971–1993)\n"
            "* `ZMW` - Zambian Kwacha\n"
            "* `ZMK` - Zambian Kwacha (1968–2012)\n"
            "* `ZWD` - Zimbabwean Dollar (1980–2008)\n"
            "* `ZWR` - Zimbabwean Dollar (2008)\n"
            "* `ZWL` - Zimbabwean Dollar (2009)\n"
        )
    )
    remote_created_at: typing.Optional[str] = pydantic.Field(description="When the third party's company was created.")
    urls: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(description="The company's urls.")
    addresses: typing.Optional[typing.List[Address]]
    phone_numbers: typing.Optional[typing.List[AccountingPhoneNumber]]
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
