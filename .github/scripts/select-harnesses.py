"""Select independent Docker build contexts for the current workflow change."""

import json
import os
from pathlib import Path
import subprocess


def select_harnesses(base):
    directories = []
    for path in Path("harnesses").iterdir():
        if path.is_symlink():
            raise ValueError(f"Harness paths must not be symlinks: {path}")
        if path.is_dir():
            directories.append(path.name)
    directories.sort()

    # Manual runs and the first push build every harness.
    if not base or set(base) == {"0"}:
        return directories

    # Disable rename detection so a move selects both the old and new harness.
    # On a PR, HEAD is GitHub's merge commit, compared against its base commit.
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", "--no-renames", "-z", base, "HEAD", "--"],
        text=True,
    ).split("\0")
    if any(path.startswith((".github/workflows/", ".github/scripts/")) for path in changed):
        return directories

    touched = set()
    for path in changed:
        parts = path.split("/")
        if len(parts) > 2 and parts[0] == "harnesses":
            touched.add(parts[1])

    # Deleted harnesses have no remaining build context. Include directories
    # without a Dockerfile so docker build fails instead of silently skipping them.
    return [name for name in directories if name in touched]


def main():
    harnesses = json.dumps(select_harnesses(os.environ.get("BASE_SHA", "")))
    print(harnesses)
    if output := os.environ.get("GITHUB_OUTPUT"):
        with open(output, "a") as stream:
            stream.write(f"harnesses={harnesses}\n")


if __name__ == "__main__":
    main()
