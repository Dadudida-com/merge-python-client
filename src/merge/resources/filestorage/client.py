# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.account_details.client import AccountDetailsClient, AsyncAccountDetailsClient
from .resources.account_token.client import AccountTokenClient, AsyncAccountTokenClient
from .resources.async_passthrough.client import AsyncAsyncPassthroughClient
from .resources.async_passthrough.client import (
    AsyncPassthroughClient as resources_filestorage_resources_async_passthrough_client_AsyncPassthroughClient,
)
from .resources.available_actions.client import AsyncAvailableActionsClient, AvailableActionsClient
from .resources.delete_account.client import AsyncDeleteAccountClient, DeleteAccountClient
from .resources.drives.client import AsyncDrivesClient, DrivesClient
from .resources.files.client import AsyncFilesClient, FilesClient
from .resources.folders.client import AsyncFoldersClient, FoldersClient
from .resources.force_resync.client import AsyncForceResyncClient, ForceResyncClient
from .resources.generate_key.client import AsyncGenerateKeyClient, GenerateKeyClient
from .resources.groups.client import AsyncGroupsClient, GroupsClient
from .resources.issues.client import AsyncIssuesClient, IssuesClient
from .resources.link_token.client import AsyncLinkTokenClient, LinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient, LinkedAccountsClient
from .resources.passthrough.client import (
    AsyncPassthroughClient as resources_filestorage_resources_passthrough_client_AsyncPassthroughClient,
)
from .resources.passthrough.client import PassthroughClient
from .resources.regenerate_key.client import AsyncRegenerateKeyClient, RegenerateKeyClient
from .resources.selective_sync.client import AsyncSelectiveSyncClient, SelectiveSyncClient
from .resources.sync_status.client import AsyncSyncStatusClient, SyncStatusClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient, WebhookReceiversClient


class FilestorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AccountTokenClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = resources_filestorage_resources_async_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.available_actions = AvailableActionsClient(client_wrapper=self._client_wrapper)
        self.delete_account = DeleteAccountClient(client_wrapper=self._client_wrapper)
        self.drives = DrivesClient(client_wrapper=self._client_wrapper)
        self.files = FilesClient(client_wrapper=self._client_wrapper)
        self.folders = FoldersClient(client_wrapper=self._client_wrapper)
        self.generate_key = GenerateKeyClient(client_wrapper=self._client_wrapper)
        self.groups = GroupsClient(client_wrapper=self._client_wrapper)
        self.issues = IssuesClient(client_wrapper=self._client_wrapper)
        self.link_token = LinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = LinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.passthrough = PassthroughClient(client_wrapper=self._client_wrapper)
        self.regenerate_key = RegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.selective_sync = SelectiveSyncClient(client_wrapper=self._client_wrapper)
        self.sync_status = SyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = ForceResyncClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = WebhookReceiversClient(client_wrapper=self._client_wrapper)


class AsyncFilestorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AsyncAccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AsyncAccountTokenClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = AsyncAsyncPassthroughClient(client_wrapper=self._client_wrapper)
        self.available_actions = AsyncAvailableActionsClient(client_wrapper=self._client_wrapper)
        self.delete_account = AsyncDeleteAccountClient(client_wrapper=self._client_wrapper)
        self.drives = AsyncDrivesClient(client_wrapper=self._client_wrapper)
        self.files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        self.folders = AsyncFoldersClient(client_wrapper=self._client_wrapper)
        self.generate_key = AsyncGenerateKeyClient(client_wrapper=self._client_wrapper)
        self.groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        self.issues = AsyncIssuesClient(client_wrapper=self._client_wrapper)
        self.link_token = AsyncLinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = AsyncLinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.passthrough = resources_filestorage_resources_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.regenerate_key = AsyncRegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.selective_sync = AsyncSelectiveSyncClient(client_wrapper=self._client_wrapper)
        self.sync_status = AsyncSyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = AsyncForceResyncClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = AsyncWebhookReceiversClient(client_wrapper=self._client_wrapper)
