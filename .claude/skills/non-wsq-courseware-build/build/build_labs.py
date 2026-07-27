#!/usr/bin/env python3
"""Generate the labs/ folder (one lab-NN-<slug>.md per activity, plus README.md
and tools.md) from the SAME single source (course_data.py + data_domainN.py) that
drives the slide deck, Lesson Plan and Learner Guide — so the labs stay 100%
aligned with every other artifact.

Each lab dict may carry optional narrative fields consumed only here:
  troubleshooting : list[str]   challenge : str   reflection : str
The engine's slide/LP/LG builders ignore these extra keys.
"""
import os, sys, re, importlib, glob as _g

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C

def _load_domains():
    acts = []
    for f in sorted(_g.glob(os.path.join(HERE, "data_domain[0-9]*.py")),
                    key=lambda q: int("".join(c for c in os.path.basename(q) if c.isdigit()) or 0)):
        n = "".join(c for c in os.path.basename(f) if c.isdigit())
        acts += getattr(importlib.import_module(os.path.basename(f)[:-3]), f"DOMAIN{n}", [])
    return acts
ACT = _load_domains()

# Scenario text lives on domain 1.
SCENARIO = getattr(importlib.import_module("data_domain1"), "SCENARIO", "")

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs"); os.makedirs(LABS, exist_ok=True)

TOPIC = {t["num"]: t for t in C.TOPICS}
PROJECT = getattr(C, "PROJECT_NAME", C.SHORT_TITLE)
FINAL_LAB = getattr(C, "PROJECT_FINAL_LAB", max(a["num"] for a in ACT))

def slug(title):
    s = title.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60].rstrip("-")

FNAME = {a["num"]: f"lab-{a['num']:02d}-{slug(a['title'])}.md" for a in ACT}

# ---- derive each lab's day and per-lab minutes from the single-source SCHEDULE
LAB_DAY, LAB_MIN = {}, {}
def _probe(nums): return "\x00" + ",".join(str(n) for n in nums) + "\x00"
sched = C.SCHEDULE(_probe)
for day, (theme, rows) in sched.items():
    for (s, e, m, k, t) in rows:
        if k != "lab": continue
        for grp in re.findall(r"\x00([0-9,]+)\x00", t):
            nums = [int(x) for x in grp.split(",") if x]
            per = round(m / len(nums)) if nums else m
            for n in nums:
                LAB_DAY[n] = day; LAB_MIN[n] = per

def _md_lab(a):
    top = TOPIC.get(a["topic"], {})
    day = LAB_DAY.get(a["num"], 1); mins = LAB_MIN.get(a["num"], 40)
    L = []
    L.append(f"# Lab {a['num']} — {a['title']}\n")
    L.append(f"**Topic {top.get('code','')}:** {top.get('title','')}  |  **Day {day}**  |  "
             f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n")
    if SCENARIO:
        L.append("## Scenario\n")
        L.append(SCENARIO + "\n")
    L.append("## Goal\n")
    L.append(a["objective"] + "\n")
    L.append("## What you'll build\n")
    L.append(a["build"] + "\n")
    L.append(f"**Tools and techniques:** {a['services']}\n")
    L.append("## About this lab\n")
    L.append(a["desc"] + "\n")
    L.append("## Steps\n")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        L.append(f"### Step {i}\n")
        L.append(instr + "\n")
        if cmd:
            L.append("Prompt to give Copilot (type or paste it into the Copilot pane):\n")
            L.append("```text\n" + cmd + "\n```\n")
    L.append("## Test it\n")
    L.append(a["test"] + "\n")
    if a.get("troubleshooting"):
        L.append("## Troubleshooting\n")
        for tb in a["troubleshooting"]:
            L.append(f"- {tb}")
        L.append("")
    if a.get("challenge"):
        L.append("## Challenge\n")
        L.append(a["challenge"] + "\n")
    if a.get("reflection"):
        L.append("## Reflection\n")
        L.append(a["reflection"] + "\n")
    L.append("## Deliverable\n")
    L.append(f"Save your output — it becomes part of your **{PROJECT}**, the single connected project "
             f"you assemble across all {len(ACT)} labs and complete in Lab {FINAL_LAB}.\n")
    L.append("---\n")
    L.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*\n")
    return "\n".join(L)

for a in ACT:
    with open(os.path.join(LABS, FNAME[a["num"]]), "w", encoding="utf-8") as f:
        f.write(_md_lab(a))

# ---------------- README.md ----------------
R = []
R.append(f"# Labs — {C.TITLE}\n")
R.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
R.append(f"All {len(ACT)} labs build one connected **{PROJECT}**, which you begin in Lab 1 and "
         f"complete in Lab {FINAL_LAB}. Wherever possible, use your own business data; a Contoso "
         f"Coffee sample dataset is provided for anyone who prefers not to use real data. There is "
         f"**no assessment** — each lab verifies itself with a 'Test it' step.\n")
R.append("| Day | Topic | Lab | Title |")
R.append("|---:|---|---:|---|")
for a in ACT:
    top = TOPIC.get(a["topic"], {})
    R.append(f"| {LAB_DAY.get(a['num'],1)} | {top.get('code','')} | {a['num']:02d} | "
             f"[{a['title']}]({FNAME[a['num']]}) |")
R.append("\n## Tools\n")
R.append("See [tools.md](tools.md) for the accounts, apps and sample data used across the labs.\n")
with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(R))

# ---------------- tools.md ----------------
T = f"""# Tools — {C.TITLE}

**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**

Everything in this course runs in **Power BI Desktop** (a free Windows app) and the
**Power BI Service** (app.powerbi.com) on a Copilot-enabled Microsoft Fabric tenant.

## Accounts and access

- **Power BI Desktop** installed on a Windows laptop (free from the Microsoft Store).
- A **work or school Microsoft 365 account** that can sign in to app.powerbi.com.
- **Copilot for Power BI enabled** on the tenant: a paid **Fabric capacity (F2 or above)** or
  **Power BI Premium**, with the **Copilot tenant switch** turned on. The trainer confirms
  lab-tenant access at the start of the day.
- A current **Chrome** or **Edge** browser, signed in to the correct account.

## Tools used

| Tool | Used for |
|---|---|
| **Power BI Desktop** | Connecting and preparing data, building the model, authoring reports, DAX |
| **Power BI Service** | Publishing, dashboards, sharing, and Copilot in the browser |
| **Copilot pane** | Prompting for report pages, visuals, DAX measures and summaries |
| **Power Query Editor** | Cleaning, shaping and renaming data so Copilot can understand it |
| **Q&A visual** | Answering natural-language questions from report users |

## Sample data

A **Contoso Coffee** sample dataset (a fictional coffee retailer's sales, products, regions and
dates) is supplied so that learners who prefer not to use their own business data can still
complete every step. Your own tabular business data (Excel or CSV) is always preferred.

## Safety

- Copilot **proposes**; you **review** every page, visual, measure and summary before you keep or share it.
- Never paste **confidential or personal data** into a Copilot prompt — use the Contoso Coffee sample data if in doubt.
- Before sharing, check **accuracy**, respect **row-level security**, and **label AI-generated content**.
- Use only data and accounts you are authorised to use.
"""
with open(os.path.join(LABS, "tools.md"), "w", encoding="utf-8") as f:
    f.write(T)

print(f"Wrote {len(ACT)} labs + README.md + tools.md to {LABS}")
