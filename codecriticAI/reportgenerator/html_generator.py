from pathlib import Path
import markdown

class HtmlReportGenerator:
    def __init__(self, review):
        self.review_markdown = review

    def create_html_report(self, output_dir="reports"):
        # Create output directory if it doesn't exist
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        # Convert markdown to HTML
        html_content = markdown.markdown(self.review_markdown)

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
