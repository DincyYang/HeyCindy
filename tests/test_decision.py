from normalizer import NormalizedResult
from decision import decide_from_result

def make_result(normalized, reason, confidence=0.9):
    return NormalizedResult(
        normalized=normalized,
        confidence=confidence,
        reason=reason,
        cleaned_text="test"
    )

class TestDecideFromResult:

    def test_execute_on(self):
        d = decide_from_result(make_result("on", "strong_phrase_on"))
        assert d.action == "execute"
        assert d.command == "on"

    def test_execute_off(self):
        d = decide_from_result(make_result("off", "strong_phrase_off"))
        assert d.action == "execute"
        assert d.command == "off"

    def test_clarify_on_conflict(self):
        d = decide_from_result(make_result("unknown", "conflict", 0.0))
        assert d.action == "clarify"
        assert d.command is None

    def test_reject_negated_on(self):
        d = decide_from_result(make_result("unknown", "negated_on", 0.0))
        assert d.action == "reject"

    def test_reject_negated_off(self):
        d = decide_from_result(make_result("unknown", "negated_off", 0.0))
        assert d.action == "reject"

    def test_ignore_no_match(self):
        d = decide_from_result(make_result("unknown", "no_match", 0.0))
        assert d.action == "ignore"