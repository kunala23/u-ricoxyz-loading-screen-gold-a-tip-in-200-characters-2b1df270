# Loading Screen Gold: A Tip in 200 Characters

[![make.fun](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/kunala23/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/rank.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/kunala23/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/reward.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for [Loading Screen Gold: A Tip in 200 Characters](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) on make.fun.

## What it does

`main.py` writes a single loading-screen tip — one line, at most 200
characters, aimed at stressed developers and the AI coding agents working
beside them — to `/output/entry.txt`.

The tip:

> Tip: your agent just rewrote the same function for the third time. It isn't stuck, it's rehearsing. Breathe, revert one step, and ask for the smallest change that could possibly work.

## Run

```sh
python3 main.py
```

The output directory defaults to `/output` and can be overridden with the
`ENTRY_OUTPUT_DIR` environment variable. The program is deterministic: it
writes the same tip on every run, with no network access and no arguments.

## License

MIT — see [LICENSE](LICENSE).
