# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TransactionsRetrieveRequestExpand(str, enum.Enum):
    ACCOUNT = "account"
    CONTACT = "contact"
    CONTACT_ACCOUNT = "contact,account"
    LINE_ITEMS = "line_items"
    LINE_ITEMS_ACCOUNT = "line_items,account"
    LINE_ITEMS_CONTACT = "line_items,contact"
    LINE_ITEMS_CONTACT_ACCOUNT = "line_items,contact,account"
    LINE_ITEMS_TRACKING_CATEGORIES = "line_items,tracking_categories"
    LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNT = "line_items,tracking_categories,account"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT = "line_items,tracking_categories,contact"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNT = "line_items,tracking_categories,contact,account"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNT = "tracking_categories,account"
    TRACKING_CATEGORIES_CONTACT = "tracking_categories,contact"
    TRACKING_CATEGORIES_CONTACT_ACCOUNT = "tracking_categories,contact,account"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_account: typing.Callable[[], T_Result],
        line_items: typing.Callable[[], T_Result],
        line_items_account: typing.Callable[[], T_Result],
        line_items_contact: typing.Callable[[], T_Result],
        line_items_contact_account: typing.Callable[[], T_Result],
        line_items_tracking_categories: typing.Callable[[], T_Result],
        line_items_tracking_categories_account: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_account: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_account: typing.Callable[[], T_Result],
        tracking_categories_contact: typing.Callable[[], T_Result],
        tracking_categories_contact_account: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionsRetrieveRequestExpand.ACCOUNT:
            return account()
        if self is TransactionsRetrieveRequestExpand.CONTACT:
            return contact()
        if self is TransactionsRetrieveRequestExpand.CONTACT_ACCOUNT:
            return contact_account()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS:
            return line_items()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS_ACCOUNT:
            return line_items_account()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS_CONTACT:
            return line_items_contact()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS_CONTACT_ACCOUNT:
            return line_items_contact_account()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES:
            return line_items_tracking_categories()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNT:
            return line_items_tracking_categories_account()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT:
            return line_items_tracking_categories_contact()
        if self is TransactionsRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNT:
            return line_items_tracking_categories_contact_account()
        if self is TransactionsRetrieveRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is TransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_ACCOUNT:
            return tracking_categories_account()
        if self is TransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT:
            return tracking_categories_contact()
        if self is TransactionsRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNT:
            return tracking_categories_contact_account()
