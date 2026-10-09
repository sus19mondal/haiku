# haiku-null

One topic in.

One haiku out.

Nothing else.

---

An agent.

It writes a single haiku.

Amazon Bedrock does the thinking.

No web page. No server. No deploy.

Plain text to your terminal.

---

## Run

Python 3.9+.

```
pip install -r requirements.txt
```

Credentials:

```
aws configure
```

Bedrock model access: enable Amazon Nova Lite in your region.

First run asks one thing — your region. It remembers.

```
python haiku.py the sea
```

Or:

```
python haiku.py
topic: _
```

---

## Out

```

Grey waves fold and fall
a gull writes one line of foam
then the tide erases

```

---

## Cost

Per call only.

Nothing idles.

Nothing to tear down.

Delete `~/.haiku-null` to forget your region.

---

## Files

```
haiku.py
requirements.txt
README.md
```

Done.
