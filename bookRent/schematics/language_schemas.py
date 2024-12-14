from typing import Optional

from bookRent.schematics.schematics import SearchModel


class LanguageSearch(SearchModel):
    id: Optional[int] = None
    language: Optional[str] = None