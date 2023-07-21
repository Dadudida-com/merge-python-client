# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmployeePayrollRunsRetrieveRequestExpand(str, enum.Enum):
    EMPLOYEE = "employee"
    EMPLOYEE_PAYROLL_RUN = "employee,payroll_run"
    PAYROLL_RUN = "payroll_run"

    def visit(
        self,
        employee: typing.Callable[[], T_Result],
        employee_payroll_run: typing.Callable[[], T_Result],
        payroll_run: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeePayrollRunsRetrieveRequestExpand.EMPLOYEE:
            return employee()
        if self is EmployeePayrollRunsRetrieveRequestExpand.EMPLOYEE_PAYROLL_RUN:
            return employee_payroll_run()
        if self is EmployeePayrollRunsRetrieveRequestExpand.PAYROLL_RUN:
            return payroll_run()
