# ---- builder: has uv and does the installing ----
# linux/amd64
FROM python:3.11-slim-bookworm@sha256:b18992999dbe963a45a8a4da40ac2b1975be1a776d939d098c647482bcad5cba AS builder

# uv as a pinned binary, copied in — not "latest", not curl|sh
COPY --from=ghcr.io/astral-sh/uv:0.11.29@sha256:eb2843a1e56fd9e30c7276ce1a52cba86e64c7b385f5e3279a0e08e02dd058fc /uv /uvx /bin/

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# deps BEFORE source, so this layer is cached until the lockfile changes
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# now the code, then install the project itself into the venv (not editable)
COPY src ./src
COPY README.md ./
RUN uv sync --frozen --no-dev --no-editable

# ---- runtime: no uv, no build tools, non-root ----
FROM python:3.11-slim-bookworm@sha256:b18992999dbe963a45a8a4da40ac2b1975be1a776d939d098c647482bcad5cba AS runtime

RUN pip uninstall --yes setuptools wheel pip

RUN useradd --create-home --uid 1000 geoservice
USER geoservice
WORKDIR /app

# the only thing carried over: the finished venv
COPY --from=builder --chown=geoservice:geoservice /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "geoservice.app:app", "--host", "0.0.0.0", "--port", "8000"]
