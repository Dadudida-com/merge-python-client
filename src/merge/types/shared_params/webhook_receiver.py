# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookReceiver"]


class WebhookReceiver(TypedDict, total=False):
    event: Required[str]

    is_active: Required[bool]

    key: str
