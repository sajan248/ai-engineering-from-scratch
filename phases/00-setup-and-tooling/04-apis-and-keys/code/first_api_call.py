# Phase 0 · Lesson 04 — APIs and keys
# Reads LLAMA_API_KEY from env and makes a chat completion call.
# Uses the OpenAI SDK and raw HTTP to interact with the NVIDIA API.
# Lesson Explainer: phases/00-setup-and-tooling/04-apis-and-keys/docs/en.md
# Refs: https://build.nvidia.com/meta/llama-4-maverick-17b-128e-instruct

import os
import json
import urllib.request


def clean_api_key(api_key):
    if api_key and api_key.lower().startswith("bearer "):
        return api_key[7:].strip()
    return api_key


def call_with_sdk():
    try:
        from openai import OpenAI
    except ImportError:
        print("Install the SDK: pip install openai")
        return

    api_key = os.environ.get("LLAMA_API_KEY")
    if not api_key:
        print("Set LLAMA_API_KEY environment variable first")
        return

    api_key = clean_api_key(api_key)

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key
    )

    try:
        response = client.chat.completions.create(
            model="meta/llama-4-maverick-17b-128e-instruct",
            max_tokens=256,
            messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
        )
        print(f"SDK response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.prompt_tokens} in, {response.usage.completion_tokens} out")
    except Exception as e:
        print(f"SDK call failed: {e}")


def call_raw_http():
    api_key = os.environ.get("LLAMA_API_KEY")
    if not api_key:
        print("Set LLAMA_API_KEY environment variable first")
        return

    api_key = clean_api_key(api_key)

    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    body = json.dumps({
        "model": "meta/llama-4-maverick-17b-128e-instruct",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    }).encode()

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            print(f"Raw HTTP response: {result['choices'][0]['message']['content']}")
            print(f"Tokens used: {result['usage']['prompt_tokens']} in, {result['usage']['completion_tokens']} out")
    except Exception as e:
        print(f"Raw HTTP call failed: {e}")


if __name__ == "__main__":
    print("=== API Calls ===\n")
    print("1. Using the SDK:")
    call_with_sdk()
    print("\n2. Using raw HTTP:")
    call_raw_http()
