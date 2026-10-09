#!/usr/bin/env python3
# haiku-null
# one topic in.
# one haiku out.
# nothing else.
import sys
import os
import json
from pathlib import Path

CFG = Path.home() / ".haiku-null"
MODEL = "amazon.nova-lite-v1:0"
REGION_DEFAULT = "us-east-1"

PROMPT = (
    "Write exactly one haiku about: {topic}. "
    "Three lines. 5-7-5 feel. No title. No commentary. Only the haiku."
)


def region():
    if CFG.exists():
        return CFG.read_text().strip() or REGION_DEFAULT
    r = input("region [us-east-1]: ").strip() or REGION_DEFAULT
    CFG.write_text(r)
    try:
        os.chmod(CFG, 0o600)
    except OSError:
        pass
    return r


def haiku(topic):
    import boto3

    brt = boto3.client("bedrock-runtime", region_name=region())
    r = brt.converse(
        modelId=MODEL,
        messages=[{"role": "user", "content": [{"text": PROMPT.format(topic=topic)}]}],
        inferenceConfig={"maxTokens": 80, "temperature": 0.8},
    )
    return "".join(b.get("text", "") for b in r["output"]["message"]["content"]).strip()


def main():
    topic = " ".join(sys.argv[1:]).strip()
    if not topic:
        topic = input("topic: ").strip()
    if not topic:
        return
    try:
        print()
        print(haiku(topic))
        print()
    except Exception as e:
        m = str(e)
        if "credential" in m.lower() or "token" in m.lower():
            sys.exit("no creds. run: aws configure")
        if "AccessDenied" in m or "could not be found" in m:
            sys.exit(f"no bedrock access to {MODEL}. enable it in the console.")
        sys.exit(m)


if __name__ == "__main__":
    main()
