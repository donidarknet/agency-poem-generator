# Agency-poem-01 entry (Python 3.13, standard library only).
# Writes one fixed poem about agency to /output/entry.txt.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I taught it my mornings — the bills, the calls,
the small amends I kept putting off.
It did them all before the kettle boiled,
each errand a door I chose to walk through
by not walking through it.

At noon the afternoon lay unspent,
hours pooled like light around my feet,
and I understood, too late to be surprised:
choosing is the work. The rest is speed.

It never asked. It only did
what I had already done
in the long second before I spoke —
the choosing. That was always mine.
The hands were borrowed. The choice was not."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
