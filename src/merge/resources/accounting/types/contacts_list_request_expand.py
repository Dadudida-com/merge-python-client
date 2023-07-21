# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ContactsListRequestExpand(str, enum.Enum):
    ADDRESSES = "addresses"
    ADDRESSES_COMPANY = "addresses,company"
    ADDRESSES_PHONE_NUMBERS = "addresses,phone_numbers"
    ADDRESSES_PHONE_NUMBERS_COMPANY = "addresses,phone_numbers,company"
    COMPANY = "company"
    PHONE_NUMBERS = "phone_numbers"
    PHONE_NUMBERS_COMPANY = "phone_numbers,company"

    def visit(
        self,
        addresses: typing.Callable[[], T_Result],
        addresses_company: typing.Callable[[], T_Result],
        addresses_phone_numbers: typing.Callable[[], T_Result],
        addresses_phone_numbers_company: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        phone_numbers: typing.Callable[[], T_Result],
        phone_numbers_company: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactsListRequestExpand.ADDRESSES:
            return addresses()
        if self is ContactsListRequestExpand.ADDRESSES_COMPANY:
            return addresses_company()
        if self is ContactsListRequestExpand.ADDRESSES_PHONE_NUMBERS:
            return addresses_phone_numbers()
        if self is ContactsListRequestExpand.ADDRESSES_PHONE_NUMBERS_COMPANY:
            return addresses_phone_numbers_company()
        if self is ContactsListRequestExpand.COMPANY:
            return company()
        if self is ContactsListRequestExpand.PHONE_NUMBERS:
            return phone_numbers()
        if self is ContactsListRequestExpand.PHONE_NUMBERS_COMPANY:
            return phone_numbers_company()
