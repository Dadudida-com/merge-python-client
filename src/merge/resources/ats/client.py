# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...environment import MergeEnvironment
from .resources.account_details.client import AccountDetailsClient, AsyncAccountDetailsClient
from .resources.account_token.client import AccountTokenClient, AsyncAccountTokenClient
from .resources.activities.client import ActivitiesClient, AsyncActivitiesClient
from .resources.applications.client import ApplicationsClient, AsyncApplicationsClient
from .resources.attachments.client import AsyncAttachmentsClient, AttachmentsClient
from .resources.available_actions.client import AsyncAvailableActionsClient, AvailableActionsClient
from .resources.candidates.client import AsyncCandidatesClient, CandidatesClient
from .resources.delete_account.client import AsyncDeleteAccountClient, DeleteAccountClient
from .resources.departments.client import AsyncDepartmentsClient, DepartmentsClient
from .resources.eeocs.client import AsyncEeocsClient, EeocsClient
from .resources.force_resync.client import AsyncForceResyncClient, ForceResyncClient
from .resources.generate_key.client import AsyncGenerateKeyClient, GenerateKeyClient
from .resources.interviews.client import AsyncInterviewsClient, InterviewsClient
from .resources.issues.client import AsyncIssuesClient, IssuesClient
from .resources.job_interview_stages.client import AsyncJobInterviewStagesClient, JobInterviewStagesClient
from .resources.jobs.client import AsyncJobsClient, JobsClient
from .resources.link_token.client import AsyncLinkTokenClient, LinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient, LinkedAccountsClient
from .resources.offers.client import AsyncOffersClient, OffersClient
from .resources.offices.client import AsyncOfficesClient, OfficesClient
from .resources.passthrough.client import AsyncPassthroughClient, PassthroughClient
from .resources.regenerate_key.client import AsyncRegenerateKeyClient, RegenerateKeyClient
from .resources.reject_reasons.client import AsyncRejectReasonsClient, RejectReasonsClient
from .resources.scorecards.client import AsyncScorecardsClient, ScorecardsClient
from .resources.selective_sync.client import AsyncSelectiveSyncClient, SelectiveSyncClient
from .resources.sync_status.client import AsyncSyncStatusClient, SyncStatusClient
from .resources.tags.client import AsyncTagsClient, TagsClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient, WebhookReceiversClient


class AtsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.account_details = AccountDetailsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.account_token = AccountTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.activities = ActivitiesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.applications = ApplicationsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.attachments = AttachmentsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.available_actions = AvailableActionsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.candidates = CandidatesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.delete_account = DeleteAccountClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.departments = DepartmentsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.eeocs = EeocsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.generate_key = GenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.interviews = InterviewsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.issues = IssuesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.job_interview_stages = JobInterviewStagesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.jobs = JobsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.link_token = LinkTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.linked_accounts = LinkedAccountsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.offers = OffersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.offices = OfficesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.passthrough = PassthroughClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.regenerate_key = RegenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.reject_reasons = RejectReasonsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.scorecards = ScorecardsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.selective_sync = SelectiveSyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.sync_status = SyncStatusClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.force_resync = ForceResyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.tags = TagsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.users = UsersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.webhook_receivers = WebhookReceiversClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )


class AsyncAtsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.account_details = AsyncAccountDetailsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.account_token = AsyncAccountTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.activities = AsyncActivitiesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.applications = AsyncApplicationsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.attachments = AsyncAttachmentsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.available_actions = AsyncAvailableActionsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.candidates = AsyncCandidatesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.delete_account = AsyncDeleteAccountClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.departments = AsyncDepartmentsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.eeocs = AsyncEeocsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.generate_key = AsyncGenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.interviews = AsyncInterviewsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.issues = AsyncIssuesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.job_interview_stages = AsyncJobInterviewStagesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.jobs = AsyncJobsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.link_token = AsyncLinkTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.linked_accounts = AsyncLinkedAccountsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.offers = AsyncOffersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.offices = AsyncOfficesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.passthrough = AsyncPassthroughClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.regenerate_key = AsyncRegenerateKeyClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.reject_reasons = AsyncRejectReasonsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.scorecards = AsyncScorecardsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.selective_sync = AsyncSelectiveSyncClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.sync_status = AsyncSyncStatusClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.force_resync = AsyncForceResyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.tags = AsyncTagsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.webhook_receivers = AsyncWebhookReceiversClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
