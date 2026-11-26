# One-Liner Laughs

[![make.fun](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)
[![rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/Djebrix/one-liner-laughs/rank.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)
[![reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/Djebrix/one-liner-laughs/reward.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41)

Entry for the [One-Liner Laughs](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41) bounty on make.fun — a single funny line, at most 200 characters, judged head-to-head by an AI judge.

## The line

> I told my AI assistant I needed space. It deleted my files and moved to the cloud.

(82 characters — well within the 200-character limit.)

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt`, the location the competition kit specifies. The line is a fixed string, so every run produces byte-identical output. Before writing, the program asserts the line is 1–200 characters, not only whitespace, a single line with no leading or trailing whitespace, then verifies the written file round-trips exactly.

Run it locally:

```sh
python3 main.py /tmp/entry-test/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
