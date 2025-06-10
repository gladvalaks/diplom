from client import router as client_router
from construction_type import router as construction_type_router
from construction import router as construction_router
from contractor import router as contactor_router
from user import router as user_router

__all__ = [
    'client_router',
    'construction_type_router',
    'construction_router',
    'contactor_router',
    'user_router'
]