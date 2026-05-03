from normalizer import normalize_command

class TestNormalizeCommand:

    # ✅ Happy path
    def test_turn_on(self):
        r = normalize_command("turn the light on")
        assert r.normalized == "on"
        assert r.confidence == 0.9
        assert r.reason == "strong_phrase_on"

    def test_switch_on(self):
        r = normalize_command("switch on")
        assert r.normalized == "on"

    def test_turn_off(self):
        r = normalize_command("turn off")
        assert r.normalized == "off"
        assert r.confidence == 0.9

    def test_light_off(self):
        r = normalize_command("light off")
        assert r.normalized == "off"

    # ❌ Edge cases
    def test_empty_input(self):
        r = normalize_command("")
        assert r.normalized == "unknown"
        assert r.confidence == 0.0
        assert r.reason == "empty_input"

    def test_none_input(self):
        r = normalize_command(None)
        assert r.normalized == "unknown"

    def test_no_match(self):
        r = normalize_command("hello how are you")
        assert r.normalized == "unknown"
        assert r.reason == "no_match"

    # ⚠️ Negation protection
    def test_negated_on(self):
        r = normalize_command("don't turn on the light")
        assert r.normalized == "unknown"
        assert r.reason == "negated_on"

    def test_negated_off(self):
        r = normalize_command("do not turn off")
        assert r.normalized == "unknown"
        assert r.reason == "negated_off"

    # 💥 Conflict
    def test_conflict(self):
        r = normalize_command("turn on and turn off")
        assert r.normalized == "unknown"
        assert r.reason == "conflict"

    # 🔤 Case insensitive
    def test_uppercase(self):
        r = normalize_command("TURN THE LIGHT ON")
        assert r.normalized == "on"