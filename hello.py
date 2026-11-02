"""Smoke test: print a few facts about the environment this runs in."""
import os
import platform
import sys
from datetime import datetime, timezone


def main() -> None:
    print("Hello from Claude Code remote!")
    print(f"  Time (UTC): {datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}")
    print(f"  Host OS:    {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"  Python:     {sys.version.split()[0]}")
    print(f"  CPUs:       {os.cpu_count()}")


if __name__ == "__main__":
    main()
