from __future__ import annotations

import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from structlog.contextvars import bind_contextvars, clear_contextvars


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Owner: Mai Tan Thanh
        clear_contextvars()

        # Owner: Mai Tan Thanh
        # Reuse inbound request IDs when present; otherwise generate a lab-friendly value.
        incoming_request_id = request.headers.get("x-request-id", "").strip()
        correlation_id = incoming_request_id or f"req-{uuid.uuid4().hex[:8]}"
        
        # Owner: Mai Tan Thanh
        bind_contextvars(correlation_id=correlation_id)
        
        request.state.correlation_id = correlation_id
        
        start = time.perf_counter()
        response = await call_next(request)
        
        # Owner: Mai Tan Thanh
        response.headers["x-request-id"] = correlation_id
        response.headers["x-response-time-ms"] = str(int((time.perf_counter() - start) * 1000))
        
        return response
