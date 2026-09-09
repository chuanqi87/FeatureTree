"""Separate an unresponsive model from a long but active research stage."""

import json
import subprocess
import time


class NoResponseTimeout(TimeoutError):
    retryable = False


class ExecutionInterrupted(RuntimeError):
    retryable = False


class StageTimeout(subprocess.TimeoutExpired):
    retryable = False


class EventActivity:
    def __init__(self, path):
        self.path = path
        self.offset = 0
        self.pending = ""

    def poll(self):
        with self.path.open() as stream:
            stream.seek(self.offset)
            self.pending += stream.read()
            self.offset = stream.tell()
        rows = self.pending.split("\n")
        self.pending = rows.pop()
        for row in rows:
            try:
                event = json.loads(row)
            except ValueError:
                continue
            part = event.get("part", {})
            if (event.get("type") in ("error", "session.error")
                    or part.get("type") in ("tool", "step-finish")
                    or part.get("type") == "text" and part.get("text")):
                return True
        return False


def wait_for_model(process, prompt, events, timeout, first_response_timeout):
    started = time.monotonic()
    activity = EventActivity(events)
    first_response = None
    first_response_timeout = min(first_response_timeout, timeout)
    while True:
        elapsed = time.monotonic() - started
        if first_response is None and activity.poll():
            first_response = elapsed
        if elapsed >= timeout:
            raise StageTimeout(process.args, timeout)
        if first_response is None and elapsed >= first_response_timeout:
            raise NoResponseTimeout(
                f"No model text or tool result within {first_response_timeout}s; "
                "automatic retry stopped. Check the provider/model before retrying.")
        remaining = timeout - elapsed
        if first_response is None:
            remaining = min(remaining, first_response_timeout - elapsed)
        try:
            process.communicate(prompt, timeout=min(1, remaining))
            if first_response is None and activity.poll():
                first_response = time.monotonic() - started
            return {"first_response_seconds": round(first_response, 3) if first_response is not None else None}
        except subprocess.TimeoutExpired:
            prompt = None  # communicate resumes the same stdin buffer after a timeout.
