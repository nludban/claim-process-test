from fastapi import APIRouter

from claimprocess.presentation.models import Claim, ClaimCreate
from claimprocess.control import ClaimsController

# TODO - Turn into a Dependency?
claims_c = ClaimsController()

router = APIRouter(
    prefix='/claims',
)

@router.post('/process')
async def process(claim_create: ClaimCreate) -> Claim:
    claim = Claim(**claim_create)
    await claims_c.process(claim)
    return claim

#--#
