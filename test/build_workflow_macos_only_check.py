from pathlib import Path
import sys


workflow = Path(".github/workflows/build.yaml").read_text()

required_snippets = [
    "workflow_dispatch:",
    "default: macos",
    "options:",
    "- macos",
    "- all",
    "github.event_name != 'workflow_dispatch' || inputs.target == 'all' || matrix.platform == 'macos'",
    "if: ${{ github.event_name == 'push' && startsWith(github.ref, 'refs/tags/v') }}",
]

missing = [snippet for snippet in required_snippets if snippet not in workflow]

if missing:
    print("build workflow macOS-only manual-dispatch check failed")
    for snippet in missing:
        print(f" - missing snippet: {snippet}")
    sys.exit(1)

print("build workflow macOS-only manual-dispatch check passed")
