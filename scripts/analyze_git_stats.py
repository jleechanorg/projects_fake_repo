#!/usr/bin/env python3
"""
Simplified analyze_git_stats.py for infrastructure portability testing
This is a minimal version that provides basic functionality
"""

import sys
import subprocess
from datetime import datetime, timedelta

def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_git_stats.py <since_date>")
        sys.exit(1)

    since_date = sys.argv[1]

    try:
        # Basic git statistics
        print("📊 Git Statistics Analysis")
        print("=" * 50)

        # Get commit count
        result = subprocess.run(
            ['git', 'rev-list', '--count', f'--since={since_date}', 'HEAD'],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            commit_count = result.stdout.strip()
            print(f"📝 Commits since {since_date}: {commit_count}")

        # Get contributor count
        result = subprocess.run(
            ['git', 'shortlog', '-sn', f'--since={since_date}'],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            contributors = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
            print(f"👥 Contributors: {contributors}")

        # Get file changes
        result = subprocess.run(
            ['git', 'diff', '--stat', f'--since={since_date}'],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print("📁 Recent changes detected")

        print("\n✅ Basic analysis complete")
        print("📝 NOTE: This is a simplified version for portability testing")
        print("   For full functionality, use the complete analyze_git_stats.py")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("📝 Ensure you're in a git repository with commit history")

if __name__ == "__main__":
    main()