"""Transport failures are separate from valid analytical gaps and revision requests."""

import re


class ResponseFormatError(ValueError):
    retryable = True


class MissingStructuredAnswer(ValueError):
    retryable = False


def has_repairable_answer(text):
    return (text.rstrip().endswith(("}", "```")) and
            all(re.search(r'"' + key + r'"\s*:', text) for key in
                ("protocol_version", "task_id", "stage_id", "input_hash", "payload")))
