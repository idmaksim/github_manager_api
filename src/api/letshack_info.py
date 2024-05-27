"""
WARNING:
Этот метод не относится к главному AIP сервису, 
а нужен только для отправки демонстрационных данных команд при показе работы решения
"""

import json

from fastapi import APIRouter, status
from utils.error_handler import handle_route_error

router = APIRouter(
    prefix="/letshack",
    tags=["letshack"]
)


@router.get('')
async def info_letshack():
    try:

        with open("src/utils/parsed_info.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    except IOError as e:
        await handle_route_error(e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)