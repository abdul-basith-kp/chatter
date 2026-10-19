from enum import Enum

class UserStatus(Enum):
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    INACTIVE = 'INACTIVE'
    SUSPENDED = 'SUSPENDED'