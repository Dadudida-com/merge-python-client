# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PriorityEnum(str, enum.Enum):
    """
    * `URGENT` - URGENT
    * `HIGH` - HIGH
    * `NORMAL` - NORMAL
    * `LOW` - LOW
    """

    URGENT = "URGENT"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
    LOW = "LOW"

    def visit(
        self,
        urgent: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        normal: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PriorityEnum.URGENT:
            return urgent()
        if self is PriorityEnum.HIGH:
            return high()
        if self is PriorityEnum.NORMAL:
            return normal()
        if self is PriorityEnum.LOW:
            return low()
