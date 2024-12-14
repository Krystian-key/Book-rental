from typing import Optional

from bookRent.schematics.schematics import SearchModel


class FormSearch(SearchModel):
    id: Optional[int] = None
    form: Optional[str] = None