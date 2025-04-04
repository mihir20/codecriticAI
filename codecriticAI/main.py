#!/usr/bin/env python3
import argparse
import os
import openai
import webbrowser
from dotenv import load_dotenv

from gitops.git_ops import GitOps
from aireviewer.reviewer import Reviewer
from reportgenerator.html_generator import HtmlReportGenerator

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='AI Code Review using Git Diff')
    parser.add_argument('--dir', type=str, required=True,
                        help='Directory path to review')
    parser.add_argument('--base', type=str, required=False, default='main',
                        help='Base branch name for comparison')
    args = parser.parse_args()

    git_ops = GitOps(args.dir, args.base)

    diff_text = git_ops.get_git_diff()

    if not diff_text.strip():
        print("No differences found")
        return

    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("ERROR: OPENAI_API_KEY environment variable not found")
        return

    print(f"🔍 Analyzing changes in '{args.dir}' compared to '{args.base}'...\n")
    reviewer = Reviewer(diff_text)
    review = reviewer.code_review_with_openai()
    print("📝 Code Review Results:\n")
    print(review)

    # Create and open HTML report
    html_generator = HtmlReportGenerator(review)
    report_path = html_generator.create_html_report()
    print(report_path)
    webbrowser.open(f"file://{report_path.resolve()}")


if __name__ == "__main__":
    main()
