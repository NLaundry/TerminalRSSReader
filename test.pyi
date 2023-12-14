
from typing import Any, Dict, List, Optional, Union

class FeedParserDict(Dict[str, Any]):
    keymap: Dict[str, Union[str, List[str]]]

    def __getitem__(self, key: str, _stacklevel: int = 2) -> Any: ...

    # def __contains__(self, key: str) -> bool: ...

    def has_key(self, key: str) -> bool: ...

    def get(self, key: str, default: Optional[Any] = None) -> Any: ...

    def __setitem__(self, key: str, value: Any) -> None: ...

    def __getattr__(self, key: str) -> Any: ...

    # def __hash__(self) -> int: ...

def parse(
    url_file_stream_or_string: Any,
    response_headers: Optional[dict[str, str]] = None,
    resolve_relative_uris: Optional[bool] = None,
    sanitize_html: Optional[bool] = None,
    optimistic_encoding_detection: Optional[bool] = None,
) -> FeedParserDict: ...
