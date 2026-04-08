# decision.py
from dataclasses import dataclass
from typing import Optional

from normalizer import NormalizedResult


@dataclass(frozen=True)
class Decision:
    action: str               # "execute" | "clarify" | "reject" | "ignore"
    command: Optional[str]    # "on" | "off" | None
    message: str
    reason: str


def decide_from_result(result: NormalizedResult) -> Decision:
    # 1) 明确可执行命令
    if result.normalized == "on":
        return Decision(
            action="execute",
            command="on",
            message="Turning the light on.",
            reason=result.reason,
        )

    if result.normalized == "off":
        return Decision(
            action="execute",
            command="off",
            message="Turning the light off.",
            reason=result.reason,
        )

    # 2) 冲突，需要澄清
    if result.reason == "conflict":
        return Decision(
            action="clarify",
            command=None,
            message="I heard both on and off. Please say just one command.",
            reason=result.reason,
        )

    # 3) 否定命令，不执行
    if result.reason in ("negated_on", "negated_off"):
        return Decision(
            action="reject",
            command=None,
            message="I heard a negated command, so I will not execute it.",
            reason=result.reason,
        )

    # 4) 其余情况先忽略
    return Decision(
        action="ignore",
        command=None,
        message="I did not understand the command.",
        reason=result.reason,
    )