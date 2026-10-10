# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A GitHub profile repo (`prathmesh0/prathmesh0`). The deliverable is `README.md`, which GitHub renders on the profile page. There is no build, lint or test tooling.

## Architecture

The README is mostly static markdown/HTML that embeds images from three sources:

- **`assets/*.svg`, `assets/projects/*.svg`**: animated SVGs (hero, divider, footer, project cards), all **generated** by `assets/generate.py`. Don't hand-edit them; edit the script and regenerate.
- **`profile/stats.svg`**: built by `assets/stats.py` (public GitHub data, stdlib only; `python assets/stats.py`) and refreshed daily by `.github/workflows/profile-cards.yml`.
- **External badge services** (shields.io, skillicons.dev, komarev): referenced by URL in the README.

## Commands

Regenerate the SVGs in `assets/` after editing `assets/generate.py` (standard library only):

```
python assets/generate.py
```

The script writes into its own directory (`OUT`) and prints `ok`.

## Editing notes

- `generate.py` has one function per asset: `hero()`, `cards()` (calls `card(...)` once per project, writing `assets/projects/<slug>.svg`), `divider()`, `footer()`. The shared palette and `REDUCED` (prefers-reduced-motion CSS) constants are at the top. New project cards need a `card(...)` call and a matching `<img>` in the README's "Featured projects" section.
- The hero terminal animation derives its keyframe percentages from a loop length `T` and per-line typing durations. Changing the lines changes timing, so check `T`.
- Theme is Solar Dusk (tweakcn): stone backgrounds with orange/sky/amber accents, defined as constants at the top of `generate.py` and `stats.py`. GitHub strips web fonts from SVGs, so Oxanium / Fira Code fall back to system fonts.
- README asset URLs carry a `?v=N` suffix; bump it when regenerating SVGs, because GitHub caches images. The workflow only pushes on `main`; the working branch here may be a feature branch (e.g. `profile-update`), so card refreshes won't appear until merged.
