# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PaymentRetrieveParams"]


class PaymentRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "account",
        "account,company",
        "company",
        "contact",
        "contact,account",
        "contact,account,company",
        "contact,company",
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """
