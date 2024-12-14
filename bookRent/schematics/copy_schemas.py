from typing import Optional

from bookRent.schematics.edition_schemas import EditionCreate, EditionSearch
from bookRent.schematics.schematics import SearchModel


class CopyCreate(EditionCreate):
    rented: bool = False


class CopySearch(SearchModel):
    id: Optional[int] = None
    edition: Optional[EditionSearch] = None
    rented: Optional[bool] = None
