import openai

class Reviewer:
    def __init__(self, diff_text):
        self.diff_text = diff_text
        self.ai = openai

    def code_review_with_openai(self):
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
        {self.diff_text}"""

        try:
            response = self.ai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system",
                     "content": "You are a helpful senior software engineer performing code reviews."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API error: {str(e)}")
            exit(1)
