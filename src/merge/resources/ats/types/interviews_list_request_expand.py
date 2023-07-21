# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterviewsListRequestExpand(str, enum.Enum):
    APPLICATION = "application"
    APPLICATION_JOB_INTERVIEW_STAGE = "application,job_interview_stage"
    INTERVIEWERS = "interviewers"
    INTERVIEWERS_APPLICATION = "interviewers,application"
    INTERVIEWERS_APPLICATION_JOB_INTERVIEW_STAGE = "interviewers,application,job_interview_stage"
    INTERVIEWERS_JOB_INTERVIEW_STAGE = "interviewers,job_interview_stage"
    INTERVIEWERS_ORGANIZER = "interviewers,organizer"
    INTERVIEWERS_ORGANIZER_APPLICATION = "interviewers,organizer,application"
    INTERVIEWERS_ORGANIZER_APPLICATION_JOB_INTERVIEW_STAGE = "interviewers,organizer,application,job_interview_stage"
    INTERVIEWERS_ORGANIZER_JOB_INTERVIEW_STAGE = "interviewers,organizer,job_interview_stage"
    JOB_INTERVIEW_STAGE = "job_interview_stage"
    ORGANIZER = "organizer"
    ORGANIZER_APPLICATION = "organizer,application"
    ORGANIZER_APPLICATION_JOB_INTERVIEW_STAGE = "organizer,application,job_interview_stage"
    ORGANIZER_JOB_INTERVIEW_STAGE = "organizer,job_interview_stage"

    def visit(
        self,
        application: typing.Callable[[], T_Result],
        application_job_interview_stage: typing.Callable[[], T_Result],
        interviewers: typing.Callable[[], T_Result],
        interviewers_application: typing.Callable[[], T_Result],
        interviewers_application_job_interview_stage: typing.Callable[[], T_Result],
        interviewers_job_interview_stage: typing.Callable[[], T_Result],
        interviewers_organizer: typing.Callable[[], T_Result],
        interviewers_organizer_application: typing.Callable[[], T_Result],
        interviewers_organizer_application_job_interview_stage: typing.Callable[[], T_Result],
        interviewers_organizer_job_interview_stage: typing.Callable[[], T_Result],
        job_interview_stage: typing.Callable[[], T_Result],
        organizer: typing.Callable[[], T_Result],
        organizer_application: typing.Callable[[], T_Result],
        organizer_application_job_interview_stage: typing.Callable[[], T_Result],
        organizer_job_interview_stage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterviewsListRequestExpand.APPLICATION:
            return application()
        if self is InterviewsListRequestExpand.APPLICATION_JOB_INTERVIEW_STAGE:
            return application_job_interview_stage()
        if self is InterviewsListRequestExpand.INTERVIEWERS:
            return interviewers()
        if self is InterviewsListRequestExpand.INTERVIEWERS_APPLICATION:
            return interviewers_application()
        if self is InterviewsListRequestExpand.INTERVIEWERS_APPLICATION_JOB_INTERVIEW_STAGE:
            return interviewers_application_job_interview_stage()
        if self is InterviewsListRequestExpand.INTERVIEWERS_JOB_INTERVIEW_STAGE:
            return interviewers_job_interview_stage()
        if self is InterviewsListRequestExpand.INTERVIEWERS_ORGANIZER:
            return interviewers_organizer()
        if self is InterviewsListRequestExpand.INTERVIEWERS_ORGANIZER_APPLICATION:
            return interviewers_organizer_application()
        if self is InterviewsListRequestExpand.INTERVIEWERS_ORGANIZER_APPLICATION_JOB_INTERVIEW_STAGE:
            return interviewers_organizer_application_job_interview_stage()
        if self is InterviewsListRequestExpand.INTERVIEWERS_ORGANIZER_JOB_INTERVIEW_STAGE:
            return interviewers_organizer_job_interview_stage()
        if self is InterviewsListRequestExpand.JOB_INTERVIEW_STAGE:
            return job_interview_stage()
        if self is InterviewsListRequestExpand.ORGANIZER:
            return organizer()
        if self is InterviewsListRequestExpand.ORGANIZER_APPLICATION:
            return organizer_application()
        if self is InterviewsListRequestExpand.ORGANIZER_APPLICATION_JOB_INTERVIEW_STAGE:
            return organizer_application_job_interview_stage()
        if self is InterviewsListRequestExpand.ORGANIZER_JOB_INTERVIEW_STAGE:
            return organizer_job_interview_stage()
