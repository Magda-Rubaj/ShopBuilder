from domain.repos import AbstractGuestRepository
from domain.entities import Guest
from domain.exceptions import GuestKeyExistsException


class GuestIdentityService:
    def __init__(self, repo: AbstractGuestRepository):
        self.repo = repo

    async def assign_key(self) -> str:
        guest = Guest()
        while True: 
            guest_key = guest.generate_key()
            try:
                self.repo.add(guest_key)
            except GuestKeyExistsException:
                continue
            finally:
                return guest_key
