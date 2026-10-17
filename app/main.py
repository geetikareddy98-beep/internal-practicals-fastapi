"""FastAPI routes with temporary, process-local item storage."""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Items API",
    version="1.0.0",
    description="Internal practical teaching API. Items are lost on restart.",
)


class ItemIn(BaseModel):
    """Accept a name between one and 100 characters, matching the exam example."""

    name: str = Field(min_length=1, max_length=100)


class ItemOut(ItemIn):
    """Return the item and its process-local identifier."""

    id: int


items: list[dict[str, object]] = []


@app.get("/health", summary="Check process health")
def health() -> dict[str, str]:
    """Report whether this API process is responding."""
    return {"status": "ok"}


@app.post(
    "/items", status_code=status.HTTP_201_CREATED, response_model=ItemOut, summary="Create an item"
)
def create_item(item: ItemIn) -> dict[str, object]:
    """Store a validated name and return its assigned identifier."""
    record: dict[str, object] = {"id": len(items) + 1, "name": item.name}
    items.append(record)
    return record
