# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmployeeListParams"]


class EmployeeListParams(TypedDict, total=False):
    company_id: str
    """If provided, will only return employees for this company."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    display_full_name: Optional[str]
    """If provided, will only return employees with this display name."""

    employment_status: Optional[Literal["ACTIVE", "INACTIVE", "PENDING"]]
    """If provided, will only return employees with this employment status.

    - `ACTIVE` - ACTIVE
    - `PENDING` - PENDING
    - `INACTIVE` - INACTIVE
    """

    expand: Literal[
        "company",
        "company,pay_group",
        "employments",
        "employments,company",
        "employments,company,pay_group",
        "employments,groups",
        "employments,groups,company",
        "employments,groups,company,pay_group",
        "employments,groups,home_location",
        "employments,groups,home_location,company",
        "employments,groups,home_location,company,pay_group",
        "employments,groups,home_location,manager",
        "employments,groups,home_location,manager,company",
        "employments,groups,home_location,manager,company,pay_group",
        "employments,groups,home_location,manager,pay_group",
        "employments,groups,home_location,manager,team",
        "employments,groups,home_location,manager,team,company",
        "employments,groups,home_location,manager,team,company,pay_group",
        "employments,groups,home_location,manager,team,pay_group",
        "employments,groups,home_location,pay_group",
        "employments,groups,home_location,team",
        "employments,groups,home_location,team,company",
        "employments,groups,home_location,team,company,pay_group",
        "employments,groups,home_location,team,pay_group",
        "employments,groups,home_location,work_location",
        "employments,groups,home_location,work_location,company",
        "employments,groups,home_location,work_location,company,pay_group",
        "employments,groups,home_location,work_location,manager",
        "employments,groups,home_location,work_location,manager,company",
        "employments,groups,home_location,work_location,manager,company,pay_group",
        "employments,groups,home_location,work_location,manager,pay_group",
        "employments,groups,home_location,work_location,manager,team",
        "employments,groups,home_location,work_location,manager,team,company",
        "employments,groups,home_location,work_location,manager,team,company,pay_group",
        "employments,groups,home_location,work_location,manager,team,pay_group",
        "employments,groups,home_location,work_location,pay_group",
        "employments,groups,home_location,work_location,team",
        "employments,groups,home_location,work_location,team,company",
        "employments,groups,home_location,work_location,team,company,pay_group",
        "employments,groups,home_location,work_location,team,pay_group",
        "employments,groups,manager",
        "employments,groups,manager,company",
        "employments,groups,manager,company,pay_group",
        "employments,groups,manager,pay_group",
        "employments,groups,manager,team",
        "employments,groups,manager,team,company",
        "employments,groups,manager,team,company,pay_group",
        "employments,groups,manager,team,pay_group",
        "employments,groups,pay_group",
        "employments,groups,team",
        "employments,groups,team,company",
        "employments,groups,team,company,pay_group",
        "employments,groups,team,pay_group",
        "employments,groups,work_location",
        "employments,groups,work_location,company",
        "employments,groups,work_location,company,pay_group",
        "employments,groups,work_location,manager",
        "employments,groups,work_location,manager,company",
        "employments,groups,work_location,manager,company,pay_group",
        "employments,groups,work_location,manager,pay_group",
        "employments,groups,work_location,manager,team",
        "employments,groups,work_location,manager,team,company",
        "employments,groups,work_location,manager,team,company,pay_group",
        "employments,groups,work_location,manager,team,pay_group",
        "employments,groups,work_location,pay_group",
        "employments,groups,work_location,team",
        "employments,groups,work_location,team,company",
        "employments,groups,work_location,team,company,pay_group",
        "employments,groups,work_location,team,pay_group",
        "employments,home_location",
        "employments,home_location,company",
        "employments,home_location,company,pay_group",
        "employments,home_location,manager",
        "employments,home_location,manager,company",
        "employments,home_location,manager,company,pay_group",
        "employments,home_location,manager,pay_group",
        "employments,home_location,manager,team",
        "employments,home_location,manager,team,company",
        "employments,home_location,manager,team,company,pay_group",
        "employments,home_location,manager,team,pay_group",
        "employments,home_location,pay_group",
        "employments,home_location,team",
        "employments,home_location,team,company",
        "employments,home_location,team,company,pay_group",
        "employments,home_location,team,pay_group",
        "employments,home_location,work_location",
        "employments,home_location,work_location,company",
        "employments,home_location,work_location,company,pay_group",
        "employments,home_location,work_location,manager",
        "employments,home_location,work_location,manager,company",
        "employments,home_location,work_location,manager,company,pay_group",
        "employments,home_location,work_location,manager,pay_group",
        "employments,home_location,work_location,manager,team",
        "employments,home_location,work_location,manager,team,company",
        "employments,home_location,work_location,manager,team,company,pay_group",
        "employments,home_location,work_location,manager,team,pay_group",
        "employments,home_location,work_location,pay_group",
        "employments,home_location,work_location,team",
        "employments,home_location,work_location,team,company",
        "employments,home_location,work_location,team,company,pay_group",
        "employments,home_location,work_location,team,pay_group",
        "employments,manager",
        "employments,manager,company",
        "employments,manager,company,pay_group",
        "employments,manager,pay_group",
        "employments,manager,team",
        "employments,manager,team,company",
        "employments,manager,team,company,pay_group",
        "employments,manager,team,pay_group",
        "employments,pay_group",
        "employments,team",
        "employments,team,company",
        "employments,team,company,pay_group",
        "employments,team,pay_group",
        "employments,work_location",
        "employments,work_location,company",
        "employments,work_location,company,pay_group",
        "employments,work_location,manager",
        "employments,work_location,manager,company",
        "employments,work_location,manager,company,pay_group",
        "employments,work_location,manager,pay_group",
        "employments,work_location,manager,team",
        "employments,work_location,manager,team,company",
        "employments,work_location,manager,team,company,pay_group",
        "employments,work_location,manager,team,pay_group",
        "employments,work_location,pay_group",
        "employments,work_location,team",
        "employments,work_location,team,company",
        "employments,work_location,team,company,pay_group",
        "employments,work_location,team,pay_group",
        "groups",
        "groups,company",
        "groups,company,pay_group",
        "groups,home_location",
        "groups,home_location,company",
        "groups,home_location,company,pay_group",
        "groups,home_location,manager",
        "groups,home_location,manager,company",
        "groups,home_location,manager,company,pay_group",
        "groups,home_location,manager,pay_group",
        "groups,home_location,manager,team",
        "groups,home_location,manager,team,company",
        "groups,home_location,manager,team,company,pay_group",
        "groups,home_location,manager,team,pay_group",
        "groups,home_location,pay_group",
        "groups,home_location,team",
        "groups,home_location,team,company",
        "groups,home_location,team,company,pay_group",
        "groups,home_location,team,pay_group",
        "groups,home_location,work_location",
        "groups,home_location,work_location,company",
        "groups,home_location,work_location,company,pay_group",
        "groups,home_location,work_location,manager",
        "groups,home_location,work_location,manager,company",
        "groups,home_location,work_location,manager,company,pay_group",
        "groups,home_location,work_location,manager,pay_group",
        "groups,home_location,work_location,manager,team",
        "groups,home_location,work_location,manager,team,company",
        "groups,home_location,work_location,manager,team,company,pay_group",
        "groups,home_location,work_location,manager,team,pay_group",
        "groups,home_location,work_location,pay_group",
        "groups,home_location,work_location,team",
        "groups,home_location,work_location,team,company",
        "groups,home_location,work_location,team,company,pay_group",
        "groups,home_location,work_location,team,pay_group",
        "groups,manager",
        "groups,manager,company",
        "groups,manager,company,pay_group",
        "groups,manager,pay_group",
        "groups,manager,team",
        "groups,manager,team,company",
        "groups,manager,team,company,pay_group",
        "groups,manager,team,pay_group",
        "groups,pay_group",
        "groups,team",
        "groups,team,company",
        "groups,team,company,pay_group",
        "groups,team,pay_group",
        "groups,work_location",
        "groups,work_location,company",
        "groups,work_location,company,pay_group",
        "groups,work_location,manager",
        "groups,work_location,manager,company",
        "groups,work_location,manager,company,pay_group",
        "groups,work_location,manager,pay_group",
        "groups,work_location,manager,team",
        "groups,work_location,manager,team,company",
        "groups,work_location,manager,team,company,pay_group",
        "groups,work_location,manager,team,pay_group",
        "groups,work_location,pay_group",
        "groups,work_location,team",
        "groups,work_location,team,company",
        "groups,work_location,team,company,pay_group",
        "groups,work_location,team,pay_group",
        "home_location",
        "home_location,company",
        "home_location,company,pay_group",
        "home_location,manager",
        "home_location,manager,company",
        "home_location,manager,company,pay_group",
        "home_location,manager,pay_group",
        "home_location,manager,team",
        "home_location,manager,team,company",
        "home_location,manager,team,company,pay_group",
        "home_location,manager,team,pay_group",
        "home_location,pay_group",
        "home_location,team",
        "home_location,team,company",
        "home_location,team,company,pay_group",
        "home_location,team,pay_group",
        "home_location,work_location",
        "home_location,work_location,company",
        "home_location,work_location,company,pay_group",
        "home_location,work_location,manager",
        "home_location,work_location,manager,company",
        "home_location,work_location,manager,company,pay_group",
        "home_location,work_location,manager,pay_group",
        "home_location,work_location,manager,team",
        "home_location,work_location,manager,team,company",
        "home_location,work_location,manager,team,company,pay_group",
        "home_location,work_location,manager,team,pay_group",
        "home_location,work_location,pay_group",
        "home_location,work_location,team",
        "home_location,work_location,team,company",
        "home_location,work_location,team,company,pay_group",
        "home_location,work_location,team,pay_group",
        "manager",
        "manager,company",
        "manager,company,pay_group",
        "manager,pay_group",
        "manager,team",
        "manager,team,company",
        "manager,team,company,pay_group",
        "manager,team,pay_group",
        "pay_group",
        "team",
        "team,company",
        "team,company,pay_group",
        "team,pay_group",
        "work_location",
        "work_location,company",
        "work_location,company,pay_group",
        "work_location,manager",
        "work_location,manager,company",
        "work_location,manager,company,pay_group",
        "work_location,manager,pay_group",
        "work_location,manager,team",
        "work_location,manager,team,company",
        "work_location,manager,team,company,pay_group",
        "work_location,manager,team,pay_group",
        "work_location,pay_group",
        "work_location,team",
        "work_location,team,company",
        "work_location,team,company,pay_group",
        "work_location,team,pay_group",
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    first_name: Optional[str]
    """If provided, will only return employees with this first name."""

    groups: str
    """
    If provided, will only return employees matching the group ids; multiple groups
    can be separated by commas.
    """

    include_deleted_data: bool
    """Whether to include data that was marked as deleted by third party webhooks."""

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    include_sensitive_fields: bool
    """
    Whether to include sensitive fields (such as social security numbers) in the
    response.
    """

    last_name: Optional[str]
    """If provided, will only return employees with this last name."""

    manager_id: str
    """If provided, will only return employees for this manager."""

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    page_size: int
    """Number of results to return per page."""

    pay_group_id: str
    """If provided, will only return employees for this pay group"""

    personal_email: Optional[str]
    """If provided, will only return Employees with this personal email"""

    remote_fields: Literal[
        "employment_status",
        "employment_status,ethnicity",
        "employment_status,ethnicity,gender",
        "employment_status,ethnicity,gender,marital_status",
        "employment_status,ethnicity,marital_status",
        "employment_status,gender",
        "employment_status,gender,marital_status",
        "employment_status,marital_status",
        "ethnicity",
        "ethnicity,gender",
        "ethnicity,gender,marital_status",
        "ethnicity,marital_status",
        "gender",
        "gender,marital_status",
        "marital_status",
    ]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    show_enum_origins: Literal[
        "employment_status",
        "employment_status,ethnicity",
        "employment_status,ethnicity,gender",
        "employment_status,ethnicity,gender,marital_status",
        "employment_status,ethnicity,marital_status",
        "employment_status,gender",
        "employment_status,gender,marital_status",
        "employment_status,marital_status",
        "ethnicity",
        "ethnicity,gender",
        "ethnicity,gender,marital_status",
        "ethnicity,marital_status",
        "gender",
        "gender,marital_status",
        "marital_status",
    ]
    """Which fields should be returned in non-normalized form."""

    team_id: str
    """If provided, will only return employees for this team."""

    work_email: Optional[str]
    """If provided, will only return Employees with this work email"""

    work_location_id: str
    """If provided, will only return employees for this location."""
