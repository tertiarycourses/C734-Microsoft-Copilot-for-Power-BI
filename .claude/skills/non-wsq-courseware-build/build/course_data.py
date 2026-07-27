"""
SINGLE SOURCE OF TRUTH — C734 Copilot for Power BI (non-WSQ).

A beginner, one-day, hands-on short course on using Microsoft Copilot inside
Power BI (Desktop and the Power BI Service on Microsoft Fabric) to build reports,
visuals, DAX measures and natural-language analysis from plain-language prompts.
Every artifact (PPT, LP, LG, LG.md) and every lab is generated from this module +
data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C734.

THE CONNECTED PROJECT
---------------------
Every lab adds one piece to a single, growing Power BI report — a Sales & Operations
dashboard for a fictional coffee retailer, Contoso Coffee. You enable Copilot and
load the data in Lab 1-2, build and refine visuals with Copilot in Labs 3-6, add
AI-assisted measures and natural-language analysis in Labs 7-8, and publish and
share the finished AI-assisted report in Lab 9. Wherever possible use your own
business data; a Contoso Coffee sample dataset is supplied for anyone who prefers not to.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Copilot for Power BI (C734)"
SHORT_TITLE  = "Copilot for Power BI (C734)"   # used in output filenames
COURSE_CODE  = "C734"                           # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# Name of the single connected project the labs build, and the lab it completes in.
PROJECT_NAME = "Contoso Coffee report"
PROJECT_FINAL_LAB = 9

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain what Copilot for Power BI and Microsoft Fabric are, and confirm the licensing and settings needed to enable Copilot.",
    "LO2: Connect and prepare data so that Copilot can interpret it, and write effective prompts in Power BI Desktop and the Service.",
    "LO3: Generate complete report pages and visuals from prompts, then refine their type, layout and formatting with Copilot.",
    "LO4: Add narrative visuals and AI summaries, and apply storytelling and formatting best practice to a report.",
    "LO5: Generate and explain DAX measures with Copilot to answer business questions.",
    "LO6: Set up Q&A and natural-language queries so users can ask questions of the data in plain English.",
    "LO7: Summarise insights, answer business questions, and publish and share an AI-assisted report and dashboard.",
]
LO_TITLES = [
    "Understand & enable",
    "Prepare & prompt",
    "Generate & refine",
    "Narrate & format",
    "DAX with Copilot",
    "Q&A in plain English",
    "Summarise & share",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Get Started with Copilot in Power BI",
         subtitle="What Copilot & Fabric are · Licensing & enabling · Desktop vs Service · Effective prompting · Preparing data",
         weighting="33%",
         concepts=[
            "Copilot for Power BI — an AI assistant, built on Microsoft Fabric, that turns plain-language prompts into report pages, visuals, DAX and summaries.",
            "Microsoft Fabric — the unified data platform Copilot runs on; Power BI is the reporting workload within it.",
            "Licensing and requirements — Copilot needs a paid Fabric capacity (F2 and above) or Power BI Premium, plus the tenant admin switch turned on.",
            "Enabling Copilot — a tenant admin enables Copilot in the Fabric admin portal; the report must sit on a supported capacity in a supported region.",
            "Copilot in Desktop vs the Service — Desktop authors the model and report locally; the Service (app.powerbi.com) shares, and the Copilot pane appears in both.",
            "The Copilot pane — a chat-style panel where you ask for pages, visuals, measures and summaries in everyday language.",
            "Effective prompting — a good prompt names the fields, the metric, the breakdown and the intent, not just 'make a chart'.",
            "Preparing data for Copilot — clear table and column names, correct data types and relationships let Copilot understand your model.",
            "You stay in control — Copilot proposes; you review every page, visual and measure before you keep it.",
         ]),
    dict(num=2, code="02",
         title="Create Reports and Visuals with Copilot",
         subtitle="Generating pages from prompts · Refining visuals & layout · Narrative visuals & AI summaries · Formatting & storytelling",
         weighting="34%",
         concepts=[
            "Generating report pages — describe the report you want and Copilot builds a full page of related visuals for you to review.",
            "Suggested content — Copilot can propose which pages and visuals a dataset supports when you are not sure where to start.",
            "Refining visuals — ask Copilot to change a visual's type, swap fields, sort, filter or add a measure without leaving the pane.",
            "Refining layout — Copilot can rearrange, align and retheme a page so it reads cleanly on screen and in print.",
            "The narrative (smart) visual — a text visual that Copilot writes and keeps updated, explaining what the data shows in words.",
            "AI summaries — Copilot summarises a page or a visual into a short, plain-language readout for stakeholders.",
            "Storytelling — order the page top-left to bottom-right, lead with the headline number, and let each visual answer one question.",
            "Formatting best practice — consistent titles, number formats, colour and spacing make an AI-generated page look deliberate.",
            "Review and refine — every generated page is a first draft; you edit, re-prompt and format until it is right.",
         ]),
    dict(num=3, code="03",
         title="AI-Assisted Data Modeling and Analysis",
         subtitle="Generating & explaining DAX · Q&A & natural-language queries · Summarising insights · Sharing AI-assisted reports",
         weighting="33%",
         concepts=[
            "DAX with Copilot — describe the calculation you need in words and Copilot writes the DAX measure for you to check and keep.",
            "Explaining DAX — paste an unfamiliar measure and Copilot explains, in plain language, what it does and how.",
            "Measure hygiene — you still name, format and validate every measure Copilot writes before you trust it in a report.",
            "The Q&A visual — lets report users type a question and get an instant visual answer in natural language.",
            "Natural-language queries — 'sales by region last quarter' becomes a chart; good field names make the answers accurate.",
            "Synonyms and Q&A setup — teach Q&A the words your business uses so questions map to the right fields.",
            "Summarising insights — Copilot turns a report into an executive summary that answers the key business questions.",
            "Sharing AI-assisted reports — publish to the Power BI Service, build a dashboard, and share it with the right people.",
            "Trust and governance — check accuracy, respect row-level security, and label AI-generated content before you share it.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Enable Copilot and prepare data, build and refine reports with prompts, then add AI-assisted analysis and share",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The single day totals exactly 480 training
# minutes (excluding the 1-hour lunch; tea breaks are within training time).
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","9:50",20,"admin","Welcome, course introduction, ground rules and confirming access to Power BI Desktop and a Copilot-enabled Power BI Service tenant"),
        ("9:50","10:35",45,"topic","TOPIC 01 — Get Started with Copilot in Power BI: what Copilot for Power BI and Microsoft Fabric are; licensing, requirements and enabling Copilot; Copilot in Power BI Desktop versus the Service; effective prompting; connecting and preparing data for Copilot (concepts + live demo)"),
        ("10:35","11:15",40,"lab","Hands-on: "+lab_titles([1])),
        ("11:15","11:30",15,"break","Tea break"),
        ("11:30","13:00",90,"lab","Hands-on: "+lab_titles([2,3])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:40",40,"topic","TOPIC 02 — Create Reports and Visuals with Copilot: generating report pages from prompts; refining visuals and layouts with Copilot; narrative visuals and AI summaries; formatting and storytelling best practice (concepts + live demo)"),
        ("14:40","15:45",65,"lab","Hands-on: "+lab_titles([4,5])),
        ("15:45","16:00",15,"break","Tea break"),
        ("16:00","16:45",45,"lab","Hands-on: "+lab_titles([6])),
        ("16:45","17:15",30,"topic","TOPIC 03 — AI-Assisted Data Modeling and Analysis: generating and explaining DAX measures with Copilot; setting up Q&A and natural-language queries; summarising insights and answering business questions; sharing AI-assisted reports and dashboards (concepts + live demo)"),
        ("17:15","18:15",60,"lab","Hands-on: "+lab_titles([7,8,9])),
        ("18:15","18:30",15,"recap","Course wrap-up, your Copilot-in-Power-BI checklist and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Copilot for Power BI Really Is",
    concepts=[
        "From clicks to prompts — you describe the report you want in plain language and Copilot drafts it for you.",
        "It works where you work — the Copilot pane sits inside Power BI Desktop and the Power BI Service.",
        "It runs on Fabric — Copilot needs a paid Fabric or Premium capacity with the tenant switch enabled.",
        "You stay in control — Copilot proposes pages, visuals and measures; you review and keep only what is right.",
    ],
    framework_title="The Copilot-in-Power-BI Loop",
    framework=[
        ("Prepare", "Give Copilot a clean model — clear names, correct types, valid relationships."),
        ("Prompt", "State the fields, the metric, the breakdown and the intent in plain language."),
        ("Generate", "Copilot drafts the page, visual, measure or summary."),
        ("Review", "Check the result against the data and the business question."),
        ("Refine", "Re-prompt, edit and format until the report is right, then share it."),
    ],
    statement=dict(
        headline="Copilot is only as good as the model you give it and the prompt you write.",
        body="This course is hands-on: you prepare data, prompt Copilot for pages, visuals, DAX and summaries, review every result, and publish an AI-assisted report you can trust and share.",
        kicker="THE DESIGN RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("A Copilot-ready model", ["Copilot enabled on a Fabric capacity", "A clean, well-named dataset", "Correct types and relationships"]),
        ("An AI-generated report", ["Report pages built from prompts", "Refined visuals and layout", "Narrative visuals and AI summaries"]),
        ("AI-assisted analysis", ["DAX measures written and explained by Copilot", "A configured Q&A experience", "Natural-language answers"]),
        ("A shared dashboard", ["An executive insight summary", "A published report and dashboard", "Shared with the right people, safely"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the Copilot technique on the shared Contoso Coffee report.",
        "You do it yourself in Power BI on your own data (or the supplied Contoso Coffee sample).",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You review what Copilot produced and re-prompt or edit until it is correct.",
        "You keep the page, visual or measure — it becomes part of your growing report.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Copilot for Power BI (C734) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 9 hands-on labs, in the "
    "order you will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected Power BI report — a Sales & Operations dashboard for a "
    "fictional coffee retailer, Contoso Coffee. You enable Copilot and load the data in Labs 1-2, "
    "build and refine the report with prompts in Labs 3-6, add AI-assisted measures and natural-"
    "language analysis in Labs 7-8, and publish and share it in Lab 9. Wherever you can, use your "
    "own business data; a Contoso Coffee sample dataset is supplied for anyone who prefers not to."
)
LG_SETUP = dict(
    needs=[
        "A Windows laptop with Power BI Desktop installed (free from the Microsoft Store or powerbi.microsoft.com).",
        "A Power BI Service account (a work or school Microsoft 365 account) that can sign in to app.powerbi.com.",
        "Copilot for Power BI enabled on the tenant: a paid Fabric capacity (F2 or above) or Power BI Premium, with the Copilot tenant switch turned on (the trainer confirms lab-tenant access at the start of the day).",
        "The supplied Contoso Coffee sample dataset (an Excel workbook), or your own tabular business data in Excel or CSV.",
        "A current Chrome or Edge browser for the Power BI Service.",
    ],
    verify_text="Before Lab 1, confirm you can open Power BI Desktop, sign in to app.powerbi.com, and that the Copilot button is visible in the Service. If Copilot is greyed out, tell the trainer — it depends on the capacity and tenant switch.",
    verify_code="Power BI Desktop: Home > sign in   ·   app.powerbi.com: open a workspace on the lab capacity > look for the Copilot button",
    conventions=[
        "Placeholders such as <YOUR MEASURE> or <REGION> are replaced with your own values.",
        "Prompt text you type into the Copilot pane is shown in a shaded box — paste or type it into Copilot.",
        "Every lab ends with a 'Test it' step — an explicit check that Copilot produced the right result before you move on.",
        "Copilot output is a first draft. Read every page, visual and measure before you keep or share it.",
    ],
)
LAB_NOTE = (
    "Use only data you are authorised to use. Do not paste confidential or personal data into a "
    "Copilot prompt; use the supplied Contoso Coffee sample data if in doubt."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have built a complete AI-assisted Power BI report in a single day — from enabling Copilot and preparing data to generating pages, writing DAX, configuring Q&A and publishing a shared dashboard.",
    sections=[
        dict(title="What you built", bullets=[
            "A Copilot-enabled Power BI environment and a clean, well-named Contoso Coffee model.",
            "Report pages and visuals generated from prompts, then refined for type, layout and formatting.",
            "Narrative visuals and AI summaries that explain the data in plain language.",
            "DAX measures written and explained by Copilot to answer real business questions.",
            "A configured Q&A experience and an executive insight summary.",
            "A published, shared AI-assisted report and dashboard in the Power BI Service.",
        ]),
        dict(title="What to do next", bullets=[
            "Point Copilot at a real report in your own organisation, starting with a clean, well-named model.",
            "Build a prompt library for the pages, visuals and measures you make most often.",
            "Always validate Copilot's DAX and summaries against the underlying data before you share.",
            "Document which content is AI-generated and respect row-level security when you share.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, verifying each 'Test it' check on the Contoso Coffee report.",
    "Second pass: rebuild a report page, a DAX measure and the Q&A setup from memory, using your own prompts.",
    "Apply the techniques to a real report in your own organisation, beginning with a well-named model.",
    "Review each lab's detailed steps in this guide and re-run the Copilot workflows on your own data.",
]
LG_GLOSSARY = [
    ("Copilot for Power BI", "An AI assistant that turns plain-language prompts into Power BI report pages, visuals, DAX and summaries."),
    ("Microsoft Fabric", "Microsoft's unified data platform; Power BI is the reporting workload within it and the capacity Copilot runs on."),
    ("Fabric capacity", "The paid compute (F2 and above) or Power BI Premium that a workspace runs on; Copilot requires it."),
    ("Tenant switch", "An admin setting in the Fabric/Power BI admin portal that must be on for Copilot to be available."),
    ("Power BI Desktop", "The free Windows application used to connect data, build the model and author reports locally."),
    ("Power BI Service", "The web app at app.powerbi.com used to publish, share and consume reports and dashboards."),
    ("Copilot pane", "The chat-style panel in Desktop and the Service where you prompt Copilot in everyday language."),
    ("Prompt", "A plain-language instruction that names the fields, metric, breakdown and intent you want Copilot to act on."),
    ("Report page", "A single canvas of related visuals; Copilot can generate a whole page from one prompt."),
    ("Visual", "A single chart, table or card on a report page."),
    ("Narrative visual", "A smart text visual that Copilot writes and updates to explain the data in words."),
    ("AI summary", "A short, plain-language readout of a page or visual generated by Copilot for stakeholders."),
    ("DAX", "Data Analysis Expressions — the formula language for Power BI measures and calculated columns."),
    ("Measure", "A DAX calculation, such as Total Sales, evaluated in the context of the visual that uses it."),
    ("Q&A", "A Power BI feature that answers natural-language questions with an instant visual."),
    ("Synonym", "An alternative word taught to Q&A so business terms map to the correct model fields."),
    ("Dashboard", "A single-page, pinned collection of visuals in the Service, often used to share key metrics."),
    ("Row-level security (RLS)", "Rules that restrict which rows of data a user can see; it must be respected when sharing."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C734 Copilot for Power BI courseware.", TRAINER),
]
