from normalizer import normalize_command

tests = [
    "Turn on the light",
    "switch off the light",
    "turn the light on please",
    "don't turn on the light",
    "turn on and turn off",
    "hello there",
]

for t in tests:
    result = normalize_command(t)
    print(f"INPUT: {t}")
    print(result)
    print("-" * 40)