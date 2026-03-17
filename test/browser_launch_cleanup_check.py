from pathlib import Path
import sys


CHECKS = [
    (
        "lib/views/dashboard/dashboard.dart",
        ["LaunchBrowserButton()"],
        "dashboard still renders the browser launch button",
    ),
    (
        "lib/views/dashboard/widgets/start_button.dart",
        ["class LaunchBrowserButton", "flclash-edge", "flclash-chrome", "launchBrowser"],
        "start button file still contains browser launch implementation",
    ),
    (
        "lib/views/about.dart",
        ["V2free", "_openV2free", "flclash-edge", "flclash-chrome", "launchBrowserFailed"],
        "about page still contains browser-launch entry or logic",
    ),
]


def main() -> int:
    failures = []
    for path_str, forbidden_tokens, message in CHECKS:
        text = Path(path_str).read_text()
        if any(token in text for token in forbidden_tokens):
            failures.append(f"{path_str}: {message}")

    if failures:
        print("browser launch cleanup regression check failed:")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("browser launch cleanup regression check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
