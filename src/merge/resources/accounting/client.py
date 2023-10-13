# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.account_details.client import AccountDetailsClient, AsyncAccountDetailsClient
from .resources.account_token.client import AccountTokenClient, AsyncAccountTokenClient
from .resources.accounts.client import AccountsClient, AsyncAccountsClient
from .resources.addresses.client import AddressesClient, AsyncAddressesClient
from .resources.async_passthrough.client import AsyncAsyncPassthroughClient
from .resources.async_passthrough.client import (
    AsyncPassthroughClient as resources_accounting_resources_async_passthrough_client_AsyncPassthroughClient,
)
from .resources.attachments.client import AsyncAttachmentsClient, AttachmentsClient
from .resources.available_actions.client import AsyncAvailableActionsClient, AvailableActionsClient
from .resources.balance_sheets.client import AsyncBalanceSheetsClient, BalanceSheetsClient
from .resources.cash_flow_statements.client import AsyncCashFlowStatementsClient, CashFlowStatementsClient
from .resources.company_info.client import AsyncCompanyInfoClient, CompanyInfoClient
from .resources.contacts.client import AsyncContactsClient, ContactsClient
from .resources.credit_notes.client import AsyncCreditNotesClient, CreditNotesClient
from .resources.delete_account.client import AsyncDeleteAccountClient, DeleteAccountClient
from .resources.expenses.client import AsyncExpensesClient, ExpensesClient
from .resources.force_resync.client import AsyncForceResyncClient, ForceResyncClient
from .resources.generate_key.client import AsyncGenerateKeyClient, GenerateKeyClient
from .resources.income_statements.client import AsyncIncomeStatementsClient, IncomeStatementsClient
from .resources.invoices.client import AsyncInvoicesClient, InvoicesClient
from .resources.issues.client import AsyncIssuesClient, IssuesClient
from .resources.items.client import AsyncItemsClient, ItemsClient
from .resources.journal_entries.client import AsyncJournalEntriesClient, JournalEntriesClient
from .resources.link_token.client import AsyncLinkTokenClient, LinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient, LinkedAccountsClient
from .resources.passthrough.client import (
    AsyncPassthroughClient as resources_accounting_resources_passthrough_client_AsyncPassthroughClient,
)
from .resources.passthrough.client import PassthroughClient
from .resources.payments.client import AsyncPaymentsClient, PaymentsClient
from .resources.phone_numbers.client import AsyncPhoneNumbersClient, PhoneNumbersClient
from .resources.purchase_orders.client import AsyncPurchaseOrdersClient, PurchaseOrdersClient
from .resources.regenerate_key.client import AsyncRegenerateKeyClient, RegenerateKeyClient
from .resources.selective_sync.client import AsyncSelectiveSyncClient, SelectiveSyncClient
from .resources.sync_status.client import AsyncSyncStatusClient, SyncStatusClient
from .resources.tax_rates.client import AsyncTaxRatesClient, TaxRatesClient
from .resources.tracking_categories.client import AsyncTrackingCategoriesClient, TrackingCategoriesClient
from .resources.transactions.client import AsyncTransactionsClient, TransactionsClient
from .resources.vendor_credits.client import AsyncVendorCreditsClient, VendorCreditsClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient, WebhookReceiversClient


class AccountingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AccountTokenClient(client_wrapper=self._client_wrapper)
        self.accounts = AccountsClient(client_wrapper=self._client_wrapper)
        self.addresses = AddressesClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = resources_accounting_resources_async_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.attachments = AttachmentsClient(client_wrapper=self._client_wrapper)
        self.available_actions = AvailableActionsClient(client_wrapper=self._client_wrapper)
        self.balance_sheets = BalanceSheetsClient(client_wrapper=self._client_wrapper)
        self.cash_flow_statements = CashFlowStatementsClient(client_wrapper=self._client_wrapper)
        self.company_info = CompanyInfoClient(client_wrapper=self._client_wrapper)
        self.contacts = ContactsClient(client_wrapper=self._client_wrapper)
        self.credit_notes = CreditNotesClient(client_wrapper=self._client_wrapper)
        self.delete_account = DeleteAccountClient(client_wrapper=self._client_wrapper)
        self.expenses = ExpensesClient(client_wrapper=self._client_wrapper)
        self.generate_key = GenerateKeyClient(client_wrapper=self._client_wrapper)
        self.income_statements = IncomeStatementsClient(client_wrapper=self._client_wrapper)
        self.invoices = InvoicesClient(client_wrapper=self._client_wrapper)
        self.issues = IssuesClient(client_wrapper=self._client_wrapper)
        self.items = ItemsClient(client_wrapper=self._client_wrapper)
        self.journal_entries = JournalEntriesClient(client_wrapper=self._client_wrapper)
        self.link_token = LinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = LinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.passthrough = PassthroughClient(client_wrapper=self._client_wrapper)
        self.payments = PaymentsClient(client_wrapper=self._client_wrapper)
        self.phone_numbers = PhoneNumbersClient(client_wrapper=self._client_wrapper)
        self.purchase_orders = PurchaseOrdersClient(client_wrapper=self._client_wrapper)
        self.regenerate_key = RegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.selective_sync = SelectiveSyncClient(client_wrapper=self._client_wrapper)
        self.sync_status = SyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = ForceResyncClient(client_wrapper=self._client_wrapper)
        self.tax_rates = TaxRatesClient(client_wrapper=self._client_wrapper)
        self.tracking_categories = TrackingCategoriesClient(client_wrapper=self._client_wrapper)
        self.transactions = TransactionsClient(client_wrapper=self._client_wrapper)
        self.vendor_credits = VendorCreditsClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = WebhookReceiversClient(client_wrapper=self._client_wrapper)


class AsyncAccountingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AsyncAccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AsyncAccountTokenClient(client_wrapper=self._client_wrapper)
        self.accounts = AsyncAccountsClient(client_wrapper=self._client_wrapper)
        self.addresses = AsyncAddressesClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = AsyncAsyncPassthroughClient(client_wrapper=self._client_wrapper)
        self.attachments = AsyncAttachmentsClient(client_wrapper=self._client_wrapper)
        self.available_actions = AsyncAvailableActionsClient(client_wrapper=self._client_wrapper)
        self.balance_sheets = AsyncBalanceSheetsClient(client_wrapper=self._client_wrapper)
        self.cash_flow_statements = AsyncCashFlowStatementsClient(client_wrapper=self._client_wrapper)
        self.company_info = AsyncCompanyInfoClient(client_wrapper=self._client_wrapper)
        self.contacts = AsyncContactsClient(client_wrapper=self._client_wrapper)
        self.credit_notes = AsyncCreditNotesClient(client_wrapper=self._client_wrapper)
        self.delete_account = AsyncDeleteAccountClient(client_wrapper=self._client_wrapper)
        self.expenses = AsyncExpensesClient(client_wrapper=self._client_wrapper)
        self.generate_key = AsyncGenerateKeyClient(client_wrapper=self._client_wrapper)
        self.income_statements = AsyncIncomeStatementsClient(client_wrapper=self._client_wrapper)
        self.invoices = AsyncInvoicesClient(client_wrapper=self._client_wrapper)
        self.issues = AsyncIssuesClient(client_wrapper=self._client_wrapper)
        self.items = AsyncItemsClient(client_wrapper=self._client_wrapper)
        self.journal_entries = AsyncJournalEntriesClient(client_wrapper=self._client_wrapper)
        self.link_token = AsyncLinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = AsyncLinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.passthrough = resources_accounting_resources_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.payments = AsyncPaymentsClient(client_wrapper=self._client_wrapper)
        self.phone_numbers = AsyncPhoneNumbersClient(client_wrapper=self._client_wrapper)
        self.purchase_orders = AsyncPurchaseOrdersClient(client_wrapper=self._client_wrapper)
        self.regenerate_key = AsyncRegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.selective_sync = AsyncSelectiveSyncClient(client_wrapper=self._client_wrapper)
        self.sync_status = AsyncSyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = AsyncForceResyncClient(client_wrapper=self._client_wrapper)
        self.tax_rates = AsyncTaxRatesClient(client_wrapper=self._client_wrapper)
        self.tracking_categories = AsyncTrackingCategoriesClient(client_wrapper=self._client_wrapper)
        self.transactions = AsyncTransactionsClient(client_wrapper=self._client_wrapper)
        self.vendor_credits = AsyncVendorCreditsClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = AsyncWebhookReceiversClient(client_wrapper=self._client_wrapper)
