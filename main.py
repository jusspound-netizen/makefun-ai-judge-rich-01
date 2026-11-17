# A working ai-judge-rich-01 entry (Python 3.13, standard library only): the Python twin of main.ts.
# It writes one fixed plan, the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money, to /output/entry.txt, the same bytes main.ts writes.
# A starting point, not a winner: write a better plan. The gate takes UTF-8 text of 1 to 1,000
# characters that is not only white space, and the judge reads exactly the bytes written, line ends
# included, so write no line end you do not mean to show. The program runs twice with no network,
# and both runs must write the same bytes.
#
# Start your agent's session at or after the contest opens and build the entry in it: a session
# begun before the opening cannot be entered (the transcript gate's thinking_in_window).
#
# To enter it, put this file at the root of your repository as main.py, with no main.ts beside it:
# a repository with both at its root is refused.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing installed. -P
# keeps the script's own directory (/bot) off sys.path, so `import helpers` does NOT find a
# helpers.py beside main.py; -s keeps the user site-packages off it, so nothing pip installed is
# importable. Only the standard library imports. This file keeps everything in itself; a module
# beside it needs this line before its import:
#     sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: Build and sell micro-SaaS tools via AI-generated code.",
        "Day 1: Use AI to scrape 500+ indie hacker pain points from Reddit/Twitter/forums; cluster into 20 niches.",
        "Days 2-3: Build 3 minimal MVPs (one per top niche) as single-file tools: a CSV cleaner, a JSON->TypeScript converter, a regex tester. Deploy each to a $5/mo VPS with Stripe checkout.",
        "Days 4-7: Cold-email 200 founders per niche with personalized 50-row samples from their public data; price at $29/mo.",
        "Days 8-14: Automate onboarding with AI-written docs, FAQ, and email sequences. Reinforce winners: double ad spend on any tool hitting $100 MRR.",
        "Days 15-30: Cross-sell bundle at $79/mo. Build affiliate program: 30% rev-share for promoters. Target $3k MRR by day 30.",
        "Keep $40 for hosting/fees. Kill any tool below $20 MRR by day 10. No manual work: all code, copy, outreach, and support drafted by AI, human only approves deploys.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))