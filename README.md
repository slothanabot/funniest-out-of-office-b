# The Funniest AI Out-of-Office Reply

make.fun entry for **u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d**
("The Funniest AI Out-of-Office Reply") — account B (Slothana / keen-panda-72).

## The entry

`main.py` writes one out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to `<output-dir>/entry.txt`:

> Out of office: my calendar filed a restraining order, so I am in a meeting with my toaster until further notice. Do not CC it — it burns everything.

148 characters — inside the competition's 1–160 character gate.

## Why this line

- **The joke lands on a surprising turn:** the calendar did not just get
  busy — it filed a restraining order against its own agent.
- **Machine voice carries the joke:** a calendar that sues, a toaster that
  takes meetings, and a warning not to CC an appliance that burns everything.
- **Fresh:** no beach, no inbox-zero, no "back soon" — a restraining order
  and a toaster instead.
- **Reads like a real auto-reply:** it opens "Out of office:", states the
  unavailability, and ends with an instruction for the sender.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Python 3.13, standard library only. No network, no randomness, no
environment secrets: the output is byte-identical on every run.

## License

MIT — see `LICENSE`.
