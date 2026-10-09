"""Build a self-contained TE Versatility Evaluator HTML file."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "web"
OFFLINE_PATH = ROOT / "offline" / "Tight_End_Versatility_Evaluator.html"


def methodology_section() -> str:
    methodology = (WEB / "methodology.html").read_text(encoding="utf-8")
    match = re.search(r"<main class=\"methodology-page\">.*?</main>", methodology, re.DOTALL)
    if match is None:
        raise ValueError("Could not locate the methodology content.")
    section = match.group(0)
    return section.replace(
        '<main class="methodology-page">',
        '<section id="methodology" class="methodology-page">',
        1,
    ).replace("</main>", "</section>", 1)


def main() -> None:
    index = (WEB / "index.html").read_text(encoding="utf-8")
    styles = (WEB / "styles.css").read_text(encoding="utf-8")
    app = (WEB / "app.js").read_text(encoding="utf-8")
    players = json.loads((WEB / "data" / "search_index.json").read_text(encoding="utf-8"))
    player_json = json.dumps(players, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")

    index = index.replace('<link rel="stylesheet" href="styles.css">', f"<style>\n{styles}\n</style>")
    index = index.replace("<title>TE Versatility Scout</title>", "<title>Tight End Versatility Evaluator</title>")
    index = index.replace('href="methodology.html"', 'href="#methodology"')
    index = index.replace("</main>\n    <script src=\"app.js\"></script>", f"</main>\n    {methodology_section()}\n    <script>window.__TE_PLAYER_INDEX__={player_json};</script>\n    <script>\n{app}\n</script>")

    if 'window.__TE_PLAYER_INDEX__=' not in index:
        raise ValueError("Could not embed the player index.")

    OFFLINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    OFFLINE_PATH.write_text(index, encoding="utf-8")
    print(f"Wrote {OFFLINE_PATH.relative_to(ROOT)} with {len(players)} player profiles.")


if __name__ == "__main__":
    main()
