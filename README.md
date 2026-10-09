# The Tight End Versatility Evaluator

The Tight End Versatility Evaluator is an interactive visualizer built from
NFL Big Data Bowl Regional Event Data and PFF scouting labels. It brings
together a TE's pass-protection impact, chip-and-release value, route threat,
coverage stress, open-field creation, and provisional run-game impact in a
six-category radar chart.

Tight ends are naturally versatile players. Choosing whether to defend one
with a defensive back or linebacker can create difficult matchup decisions,
and their role can change the protection and receiving structure of an entire
offense. This evaluator helps:

- **Coaches** quickly identify a TE's threats and tendencies when game-planning
  an upcoming matchup.
- **Scouts** understand a TE's offensive role and compare it with team needs.
- **Broadcasters** explain a TE's contribution beyond box-score statistics.

The overall versatility grade is the average of the five validated pass-game
categories. The sixth category, Run-Game Impact, remains visible on the radar
but is provisional because its uploaded source table lacks upstream
methodology in this repository; it does not affect the overall grade or
performance-similarity results.

## Open the visualizer

> **Note:** The GitHub Pages link may not load reliably. Download or clone this
> repository and run the visualizer locally using the steps below.

`localhost` and `127.0.0.1` only refer to the laptop on which the server is
running. They cannot be opened from a different laptop.

To run the visualizer on another laptop:

```bash
# 1. Download the repository ZIP from GitHub and extract it.
# 2. In a terminal, enter the extracted repository folder.
cd BigDataBowl-Tight-End-Versatility-Visualiser

# 3. Start the visualizer (Python 3 is the only requirement).
python3 -m src.serve_visualization
```

Then, on that same laptop, open
[http://127.0.0.1:8000/web/](http://127.0.0.1:8000/web/). Do not open the
HTML file directly with `file://`, because the browser will not be able to load
the player data.

The visualizer supports player and team search, category rankings, archetype
and snap filters, role and performance similarity, player profiles, and an
in-app methodology page explaining every statistic and caveat.

## Included materials

| Path | Contents |
| --- | --- |
| `src/` | Python metric, profile, search, and visualization-server code. |
| `web/` | Local interactive visualization assets. |
| `docs/` | Self-contained GitHub Pages version of the visualizer. |
| `output/` | Player tables, play-level evidence, validation outputs, and metric definitions. |
| `te_run_metrics.csv` | Source table for the provisional run-game axis. |

The tracking study covers 2021 Weeks 1-8 and is pass-play focused. Metrics are
transparent observational estimates, not proprietary NFL grades or causal
claims. See the in-app **Methodology** page for formulas, weighting rules, and
scope limitations.
