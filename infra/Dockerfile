FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY ["replay.py", "replay.py"]
COPY ["examples/replay.csv", "examples/replay.csv"]
USER 10001:10001
CMD ["python", "replay.py", "examples/replay.csv"]
