from __future__ import annotations

import os
from typing import Any

# Owner: Ho Nhat Khoa
if os.getenv("LANGFUSE_HOST") and not os.getenv("LANGFUSE_BASE_URL"):
    os.environ["LANGFUSE_BASE_URL"] = os.getenv("LANGFUSE_HOST", "")

try:
    from langfuse import get_client, observe
except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    def flush_langfuse() -> None:
        return None

    def update_current_trace(**kwargs: Any) -> None:
        return None

    def update_current_observation(**kwargs: Any) -> None:
        return None
else:
    _langfuse = get_client()

    def flush_langfuse() -> None:
        try:
            _langfuse.flush()
        except Exception:
            return None

    def update_current_trace(**kwargs: Any) -> None:
        try:
            _langfuse.update_current_trace(**kwargs)
        except Exception:
            return None

    def update_current_observation(**kwargs: Any) -> None:
        try:
            _langfuse.update_current_span(**kwargs)
        except Exception:
            return None


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
