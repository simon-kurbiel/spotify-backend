from enum import Enum

class Status(Enum):
    SUCCESS = 0
    FAILURE = 1
    
class StatusCodes(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    PAGE_NOT_FOUND = 404