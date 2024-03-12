import decimal

from claimprocess.presentation.models import Claim, ClaimCreate
import claimprocess.data


class ClaimsController:

    def __init__(self):
        self._claims = claimprocess.data.ClaimsRepository()
        return

    async def process(self, claim: Claim) -> None:
        """Ingest a Claim into the system.

        Note duplicates are allowed and will be handled, the
        client must retry until success is achieved.

        Claim is updated with ID and status:
        `success` if it is (or was) accepted
        `pending` if it's already in progress
        `failure` when things went really wrong.
        """
        # TODO rollback/recover/multiples loop:
        # - try to insert
        # - on success
        #   - try to request Payments with net_fee
        #   - on success, update Claim status to processed
        #   - on failure, update Claim status to failure
        # - on failure
        #   - retrieve current status
        #   - if pending, return
        #   - if success, return
        #   - if failure, try to update status to pending
        #     - on success, continue from insert on success
        #     - on failure, continue from insert on failure
        # - internal error if the record disappears
        self._claims.upsert(claim)
        net_fee = self._calculate_net_fee(claim)
        self._submit_net_fee(claim, net_fee)
        self._claims.mark_processed(claim)
        return

    async def _calculate_net_fee(self, claim: Claim) -> decimal.Decimal:
        return claim.provider_fees + claim.member_coinsurance + claim.member_copay - claim.allowed_fees

    async def _submit_net_fee(self, claim: Claim, net_fee: decimal.Decimal) -> None:
        pass  # Need a libproxy.  For now, just pretend it works.

#--#

