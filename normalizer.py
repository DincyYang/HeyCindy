# normalizer.py
from dataclasses import dataclass
import re
from typing import Optional


@dataclass(frozen=True)
class NormalizedResult:
    normalized: str     # "on" | "off" | "unknown"
    confidence: float
    reason: str
    cleaned_text: str


_STRONG_ON = [
    "turn on",
    "switch on",
    "light on",
    "turn the light on",
]

_STRONG_OFF = [
    "turn off",
    "switch off",
    "light off",
    "turn the light off",
]

_NEGATIONS = ["don't", "dont", "do not", "not"]


def _preprocess(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s']+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_command(raw_text: Optional[str]) -> NormalizedResult:
    if not raw_text or not raw_text.strip():
        return NormalizedResult("unknown", 0.0, "empty_input", "")

    cleaned = _preprocess(raw_text)

    has_neg = any(n in cleaned for n in _NEGATIONS)
    on_hit = any(p in cleaned for p in _STRONG_ON)
    off_hit = any(p in cleaned for p in _STRONG_OFF)

    # 冲突
    if on_hit and off_hit:
        return NormalizedResult("unknown", 0.0, "conflict", cleaned)

    # 否定保护
    if has_neg and on_hit:
        return NormalizedResult("unknown", 0.0, "negated_on", cleaned)

    if has_neg and off_hit:
        return NormalizedResult("unknown", 0.0, "negated_off", cleaned)

    if on_hit:
        return NormalizedResult("on", 0.9, "strong_phrase_on", cleaned)

    if off_hit:
        return NormalizedResult("off", 0.9, "strong_phrase_off", cleaned)

    return NormalizedResult("unknown", 0.0, "no_match", cleaned)