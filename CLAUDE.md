# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A GitHub profile repo (`prathmesh0/prathmesh0`). The deliverable is `README.md`, which GitHub renders on the profile page. There is no build, lint or test tooling.

## Architecture

The README is mostly static markdown/HTML that embeds images from three sources:

- **`assets/*.svg`, `assets/projects/*.svg`**: animated SVGs (hero, divider, footer, project cards), all **generated** by `assets/generate.py`. Don't hand-edit them; edit the script and regenerate.
- **`profile/*.svg`** (`stats`, `top-langs`, `streak`, `snake`, `snake-dark`): produced by the `.github/workflows/profile-cards.yml` GitHub Action (daily cron, manual dispatch, or push to `main` touching the workflow). The action commits them to `profile/` on the default branch. This directory is not created locally, so the README references to it are broken until the workflow has run. Don't try to generate these locally.
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
- Colours are shared between `generate.py` and the workflow's card `options` (e.g. `0b1020` background, `7c9cff` title). Keep them in sync when re-theming.
- The workflow only pushes on `main`; the working branch here may be a feature branch (e.g. `profile-update`), so card refreshes won't appear until merged.
