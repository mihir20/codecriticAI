#!/usr/bin/env python3
import argparse
import os
import subprocess
import openai
import webbrowser
from pathlib import Path
import markdown


def get_git_diff(base_branch, directory):
    try:
        diff = subprocess.check_output(
            ['git', 'diff', '-u', base_branch, '--', directory],
            stderr=subprocess.STDOUT
        )
        return diff.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error getting git diff: {e.output.decode('utf-8')}")
        exit(1)


def code_review_with_openai(diff_text):
    prompt = f"""Perform a comprehensive code review following this structure:

    ## 🔍 Code Review Summary
    [Brief overview of main findings (2-3 lines)]

    ## 🐛 Potential Bugs & Risks
    ### Critical Issues
    - List critical problems with [File:Line] references
    - Explain impact and likelihood

    ### Warning Signs
    - Highlight suspicious patterns
    - Point out error-prone code

    ## 🧹 Code Quality Assessment
    ### Maintainability
    - Code organization concerns
    - Complexity issues
    - Documentation needs

    ### Readability
    - Naming improvements
    - Structure suggestions
    - Consistency checks

    ### Performance
    - Inefficient patterns
    - Resource management
    - Optimization opportunities

    ## 🛡️ Security Checklist
    - Vulnerabilities found
    - Input validation issues
    - Security best practice violations

    ## 💡 Actionable Recommendations
    ### Required Changes
    - List must-fix items

    ### Suggested Improvements
    - Quality enhancements
    - Refactoring opportunities

    ### Best Practices
    - Specific improvements for PEP8/SOLID/DRY etc.

    ## 📈 Final Assessment
    [Overall rating: 👍/👎/⚠️]
    [Confidence level: High/Medium/Low]
    [Estimated effort to fix: Small/Medium/Large]

    Formatting Rules:
    - Use clear section headers with emojis
    - Prioritize findings by severity (Critical/High/Medium/Low)
    - Always include specific code examples when available
    - Keep bullet points concise (max 1 line)
    - Use markdown formatting for readability
    - Highlight positive findings with ✅
    - Mark risks with ❗
    - Use [File:Line] references from this diff:
    {diff_text}"""

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful senior software engineer performing code reviews."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {str(e)}")
        exit(1)


def create_html_report(markdown_content, output_dir="reports"):
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Create full HTML document with styling
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Code Review Report</title>
        <style>
            body {{ 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                line-height: 1.6;
                margin: 2rem;
                max-width: 1200px;
                color: #24292e;
            }}
            h1, h2, h3 {{ color: #0366d6; }}
            pre {{ 
                background-color: #f6f8fa;
                padding: 1rem;
                border-radius: 6px;
                overflow-x: auto;
            }}
            code {{ font-family: SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace; }}
            .container {{ margin: 0 auto; }}
            .header {{ 
                border-bottom: 1px solid #e1e4e8;
                margin-bottom: 2rem;
                padding-bottom: 1rem;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>AI Code Review Report</h1>
            </div>
            {html_content}
        </div>
    </body>
    </html>
    """

    # Save to temporary file
    report_path = output_path / "code_review_report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    return report_path

def main():
    parser = argparse.ArgumentParser(description='AI Code Review using Git Diff')
    parser.add_argument('--dir', type=str, required=True,
                        help='Directory path to review')
    parser.add_argument('--base', type=str, required=False, default='main',
                        help='Base branch name for comparison')
    args = parser.parse_args()

    diff_text = get_git_diff(args.base, args.dir)

    if not diff_text.strip():
        print("No differences found")
        return

    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("ERROR: OPENAI_API_KEY environment variable not found")
        return

    print(f"🔍 Analyzing changes in '{args.dir}' compared to '{args.base}'...\n")
    review = code_review_with_openai(diff_text)
    print("📝 Code Review Results:\n")
    print(review)

    # Create and open HTML report
    report_path = create_html_report(review)
    print(report_path)
    webbrowser.open(f"file://{report_path.resolve()}")


if __name__ == "__main__":
    main()
