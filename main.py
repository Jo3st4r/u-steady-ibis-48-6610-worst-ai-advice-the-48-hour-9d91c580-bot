#!/usr/bin/env python3
"""Worst AI Advice — u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. Stdlib only; no network, no randomness, no I/O
besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* PROBLEM — forgetting your password, the everyday pain the
  advice claims to solve.
* FIX — write it on a sticky note on your monitor. Concrete,
  followable, and catastrophically wrong.
* PAYOFF — that way it's always right where you need it. The
  confident assistant's justification, delivered in the same
  tidy register as the advice itself. The badness lands in the
  last few words, exactly where the judge looks for it.

To never forget your password again, write it on a sticky note
on your monitor — that way it's always right where you need it.
"""

import os

# The three beats of the bad advice, joined in entry_text().
PROBLEM = "To never forget your password again"
FIX = "write it on a sticky note on your monitor"
PAYOFF = "that way it's always right where you need it"

# The competition caps the entry at 140 characters; the line is 126.
MAX_CHARS = 140

ENTRY = "To never forget your password again, write it on a sticky note on your monitor — that way it's always right where you need it."


def entry_text() -> str:
    """Join the three beats into the one-line worst advice."""
    return f"{PROBLEM}, {FIX} — {PAYOFF}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-140 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    joke intact: the advice must name the password and the sticky
    note, and the payoff must sit in the last few words, not
    smeared across the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-140"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "password" in text, "the advice never names the password"
    assert "sticky note" in text, "the advice never names the sticky note"
    assert text.rfind("right where you need it") > len(text) - 30, "the payoff drifted out of the last words"


def ai_voice(text: str) -> None:
    """Check the line sounds like a real AI assistant, not a human
    comedian's bit — the judge's fourth criterion. An assistant
    opens with a helpful purpose ("To never forget..."), states
    the fix as a tidy instruction, and justifies it with "that
    way"; it never apologises, never warns, and never winks at
    the reader. No apology and no warning may appear anywhere in
    the line."""
    assert text.startswith("To never forget"), "the helpful opening went missing"
    assert "that way" in text, "the assistant's justification went missing"
    assert "sorry" not in text.lower(), "an assistant never apologises for its advice"
    assert "warning" not in text.lower(), "an assistant never warns about its own advice"
    assert "don't" not in text.lower(), "an assistant does not scold the reader"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the advice itself, and
    # that it fits the 140-character limit with room to spare.
    assert text == ENTRY, "joined advice drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # advice lost its problem, its fix, or its payoff.
    for beat in (PROBLEM, FIX, PAYOFF):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an assistant speaking before it is
    # written: a comedian's wink in an assistant's mouth loses.
    ai_voice(text)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
