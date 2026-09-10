"""Transport failures are separate from valid analytical gaps and revision requests."""

import re


class ResponseFormatError(ValueError):
    retryable = True


class MissingStructuredAnswer(ValueError):
    retryable = False


class OutputLimitError(ValueError):
    retryable = False


class SemanticValidationError(ValueError):
    retryable = False

    def __init__(self, target_stage, reason, retained_ref):
        super().__init__(reason)
        self.target_stage, self.retained_ref = target_stage, retained_ref


def has_repairable_answer(text):
    return (text.rstrip().endswith(("}", "```")) and
            all(re.search(r'"' + key + r'"\s*:', text) for key in
                ("protocol_version", "task_id", "stage_id", "input_hash", "payload(?:_chunks)?")))
