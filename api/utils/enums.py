from enum import Enum

class Status(Enum):
    SUCCESS = 0
    FAILURE = 0
    
class StatusCodes(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403