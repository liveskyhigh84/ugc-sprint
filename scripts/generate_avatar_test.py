#!/usr/bin/env python3
"""Talking-avatar test clip via JoggAI's free tier (HeyGen alternative, no card needed).

Sign up free at https://app.jogg.ai/register, get key from avatar menu -> API settings,
then: JOGGAI_API_KEY=... in .env or export it.

Usage:
  python3 generate_avatar_test.py --product-url "https://example.com/product"
  python3 generate_avatar_test.py --script "Hi, welcome to..." --avatar-id <id>

Docs: https://docs.jogg.ai/api-reference/v2
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

API_BASE = "https://api.jogg.ai/v2"


def find_api_key():
    if os.environ.get("JOGGAI_API_KEY"):
        return os.environ["JOGGAI_API_KEY"]
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("JOGGAI_API_KEY="):
                val = line.split("=", 1)[1].strip()
                if val:
                    return val
    return None


def call(path, api_key, payload):
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=json.dumps(payload).encode(),
        headers={"x-api-key": api_key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"JoggAI API error {e.code}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product-url", help="Product URL -> auto-generated avatar video")
    ap.add_argument("--script", help="Manual script instead of a product URL")
    ap.add_argument("--avatar-id", default=None, help="JoggAI avatar id (omit to use default)")
    ap.add_argument("--poll-secs", type=int, default=15)
    args = ap.parse_args()

    api_key = find_api_key()
    if not api_key:
        print("No JOGGAI_API_KEY found. Set it in .env or export it. "
              "Get one free at https://app.jogg.ai/register", file=sys.stderr)
        sys.exit(1)

    if args.product_url:
        result = call("/create_video_from_url", api_key, {"url": args.product_url})
    elif args.script:
        payload = {"script": args.script}
        if args.avatar_id:
            payload["avatar_id"] = args.avatar_id
        result = call("/create_video_from_avatar", api_key, payload)
    else:
        print("Need --product-url or --script", file=sys.stderr)
        sys.exit(1)

    job_id = result.get("job_id") or result.get("id")
    print(f"Submitted, job_id={job_id}. Polling every {args.poll_secs}s...")

    # ponytail: simple poll loop, no webhook server. Fine for a one-off test clip;
    # switch to JoggAI's webhook callback if this becomes the per-order production path.
    while True:
        time.sleep(args.poll_secs)
        status = call("/get_video_status", api_key, {"job_id": job_id})
        state = status.get("status")
        print(f"  status: {state}")
        if state in ("completed", "success"):
            print(f"Video ready: {status.get('video_url')}")
            break
        if state in ("failed", "error"):
            print(f"Generation failed: {status}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
