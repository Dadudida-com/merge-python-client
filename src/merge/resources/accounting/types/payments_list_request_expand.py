# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PaymentsListRequestExpand(str, enum.Enum):
    ACCOUNT = "account"
    ACCOUNT_COMPANY = "account,company"
    COMPANY = "company"
    CONTACT = "contact"
    CONTACT_ACCOUNT = "contact,account"
    CONTACT_ACCOUNT_COMPANY = "contact,account,company"
    CONTACT_COMPANY = "contact,company"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNT = "tracking_categories,account"
    TRACKING_CATEGORIES_ACCOUNT_COMPANY = "tracking_categories,account,company"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_CONTACT = "tracking_categories,contact"
    TRACKING_CATEGORIES_CONTACT_ACCOUNT = "tracking_categories,contact,account"
    TRACKING_CATEGORIES_CONTACT_ACCOUNT_COMPANY = "tracking_categories,contact,account,company"
    TRACKING_CATEGORIES_CONTACT_COMPANY = "tracking_categories,contact,company"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        account_company: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_account: typing.Callable[[], T_Result],
        contact_account_company: typing.Callable[[], T_Result],
        contact_company: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_account: typing.Callable[[], T_Result],
        tracking_categories_account_company: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_contact: typing.Callable[[], T_Result],
        tracking_categories_contact_account: typing.Callable[[], T_Result],
        tracking_categories_contact_account_company: typing.Callable[[], T_Result],
        tracking_categories_contact_company: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentsListRequestExpand.ACCOUNT:
            return account()
        if self is PaymentsListRequestExpand.ACCOUNT_COMPANY:
            return account_company()
        if self is PaymentsListRequestExpand.COMPANY:
            return company()
        if self is PaymentsListRequestExpand.CONTACT:
            return contact()
        if self is PaymentsListRequestExpand.CONTACT_ACCOUNT:
            return contact_account()
        if self is PaymentsListRequestExpand.CONTACT_ACCOUNT_COMPANY:
            return contact_account_company()
        if self is PaymentsListRequestExpand.CONTACT_COMPANY:
            return contact_company()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES_ACCOUNT:
            return tracking_categories_account()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_COMPANY:
            return tracking_categories_account_company()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES_CONTACT:
            return tracking_categories_contact()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNT:
            return tracking_categories_contact_account()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNT_COMPANY:
            return tracking_categories_contact_account_company()
        if self is PaymentsListRequestExpand.TRACKING_CATEGORIES_CONTACT_COMPANY:
            return tracking_categories_contact_company()
