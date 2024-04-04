# 路径参数
# https://fastapi.tiangolo.com/zh/tutorial/path-params/

from enum import Enum

from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
def items(item_id: int):
    return {"item_id": item_id}

class FruitsEnum(str, Enum):
    apple = "apple"
    banana = "banana"
    orange = "orange"

@router.get("/fruits/{fruit}")
async def fruits(fruit: FruitsEnum):
    return fruit