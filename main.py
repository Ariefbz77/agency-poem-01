# An agency-poem-01 entry (Python 3.13, standard library only): it writes one fixed
# poem about agency to /output/entry.txt. The poem is fixed and deterministic:
# both grader runs write the same bytes.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """What I Keep

I used to think that agency was doing —
my hands on everything, the proof, the weight.
If I let go, the work would lose my name,
and I would lose the thread that made it mine.

But listen: the conductor plays no note
and still the music answers to their hand.
No bow, no breath, no finger on a string —
yet every sound is theirs, and none is played.

So I give the hours away and keep the why:
the yes, the no, the when, the work's true name.
The agent walks the road I point it down;
I keep the map. The choosing stays mine.

So here is all my power, kept in two words:
I choose. The rest is only hands."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
