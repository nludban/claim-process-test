from claimprocess.presentation.models import Claim, ClaimCreate

import libdb


class ClaimsRepository:

    async def upsert(self, claim: Claim) -> None:
        # Insert, but if it's currently failed try to switch it to pending.
        # Upon return, claim status should be pending or success.
        # Throw an exception if the claim disappeared, or too many retries.
        async with get_session() as session:
            session.add(claim)
            await session.commit()
            await session.refresh(claim)
        return

#--#
