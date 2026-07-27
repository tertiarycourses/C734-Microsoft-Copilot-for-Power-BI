"""
Domain 3 — AI-Assisted Data Modeling and Analysis. Labs 7-9.

The final domain turns the Contoso Coffee report into an analytical, shareable
product. Lab 7 uses Copilot to write and explain DAX measures; Lab 8 sets up Q&A
and natural-language queries; Lab 9 summarises the insights and publishes and
shares the AI-assisted report and dashboard. This completes the connected report
you began in Lab 1.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the "
 "single connected dashboard you assemble across all 9 labs."
)

DOMAIN3 = [
 dict(
 num=7, topic=3,
 title="Generate and Explain DAX Measures with Copilot",
 objective="Use Copilot to write DAX measures from plain-language descriptions, explain an unfamiliar measure, then name, format and validate each one.",
 desc="Copilot can write DAX so you describe the calculation in words instead of remembering syntax. In "
 "this lab you generate the core measures your report needs — total sales, a prior-period comparison "
 "and a percentage — have Copilot explain an unfamiliar measure in plain language, and then do the "
 "essential human step: name, format and validate every measure before you trust it. " + PROJECT_NOTE,
 build="A set of validated DAX measures (Total Sales, Sales YoY %, Average Order Value) written and explained by Copilot, added to your model.",
 services="Power BI Desktop, Copilot pane, DAX measures, measure formatting, validation",
 steps=[
 ("Open Contoso Coffee.pbix and open Copilot. Ask it to write your base sales measure.",
  "Write a DAX measure called Total Sales that sums Sales Amount from the Sales table."),
 ("Review the DAX Copilot returns, then create the measure (New measure) and paste it in. Set its format to currency with no decimals.",""),
 ("Ask Copilot for a time-comparison measure that depends on your Calendar table.",
  "Write a DAX measure called Sales YoY % that compares Total Sales to the same period last year and returns the percentage change."),
 ("Ask Copilot for a ratio measure so you can see basket size.",
  "Write a DAX measure called Average Order Value that divides Total Sales by the distinct count of Order ID, handling divide-by-zero safely."),
 ("Take an unfamiliar measure and have Copilot explain it in plain language so you understand before you keep it.",
  "Explain what this measure does, step by step, in plain language: Sales YoY %."),
 ("Validate each measure against the data: put Total Sales, Sales YoY % and Average Order Value in a table by Month and sanity-check the numbers against a visual you already trust.",""),
 ("Name and tidy: confirm each measure has a clear name, the right format, and a home table, and hide any helper columns Copilot no longer needs surfaced.",""),
 ("Add the new measures to your Sales Overview KPI cards and save the file.",""),
 ],
 test="Your model has three correctly named and formatted measures — Total Sales, Sales YoY % and Average Order Value — each validated against the data, and Copilot has produced a plain-language explanation of at least one of them.",
 troubleshooting=[
 "**The YoY measure returns blank.** It needs a proper date table. Mark your Calendar as a date table (or add one) and ensure Sales relates to it, then re-run the prompt.",
 "**The numbers look wrong.** Never trust DAX unchecked — put the measure in a table beside a known-good visual and compare. Re-prompt Copilot with the correction if needed.",
 "**Divide-by-zero error on Average Order Value.** Ask Copilot to use DIVIDE() which handles zero safely, rather than the / operator.",
 ],
 challenge="Ask Copilot to write a running-total (year-to-date) Sales measure, then have it explain the DAX so you could recreate it yourself without Copilot.",
 reflection="LO5 — Copilot wrote the DAX correctly — so why is naming, formatting and validating each measure still your job, not the AI's?",
 ),
 dict(
 num=8, topic=3,
 title="Set Up Q&A and Natural-Language Queries",
 objective="Add a Q&A visual, ask natural-language questions of the model, and improve accuracy by teaching Q&A synonyms and reviewing suggested questions.",
 desc="Q&A lets anyone ask the report a question in plain English and get an instant visual. In this lab "
 "you add a Q&A visual, ask several questions, then improve the answers by teaching Q&A the words "
 "your business actually uses (synonyms) and curating the suggested questions — so a non-technical "
 "user gets the right answer first time. " + PROJECT_NOTE,
 build="A working Q&A experience on your report: a Q&A visual, tested natural-language questions, and synonyms and suggested questions configured for accuracy.",
 services="Power BI (Desktop or Service), Q&A visual, natural-language queries, Q&A setup (synonyms, suggested questions), Copilot",
 steps=[
 ("On a new page named Ask the Data, insert a Q&A visual (Insert > Q&A, or ask Copilot to add one).",
  "Add a Q&A visual to this page so users can ask questions about Contoso Coffee sales in natural language."),
 ("Type a natural-language question and watch Q&A build the answer visual.",
  "sales amount by region last quarter"),
 ("Ask two more, changing the wording, to test how Q&A interprets business language.",
  "top 5 products by total sales this year"),
 ("Find a question Q&A answers poorly because of wording, then teach it a synonym so business terms map to the right field (Modeling > Q&A setup > Field synonyms — for example map 'revenue' and 'takings' to Sales Amount).",""),
 ("Re-ask the question using the business word you just mapped and confirm Q&A now answers correctly.",
  "revenue by channel this year"),
 ("Curate the experience: in Q&A setup, review the suggested questions and add three good starter questions users are likely to ask.",""),
 ("Use Copilot to propose questions this dataset can answer, and add the best to your suggested questions.",
  "Suggest five natural-language questions a store manager could ask this Contoso Coffee dataset."),
 ("Save the file. Your report now answers plain-English questions accurately.",""),
 ],
 test="Your report has a Q&A visual that correctly answers at least three natural-language questions, including one that only works because you added a synonym, plus three curated suggested questions.",
 troubleshooting=[
 "**Q&A says it does not understand a word.** Add it as a synonym in Q&A setup so it maps to the correct field, then re-ask.",
 "**Q&A returns the wrong field.** Two fields share similar terms — tighten the field names or add synonyms so the business term maps to exactly one field.",
 "**No suggested questions appear.** Add them manually in Modeling > Q&A setup > Suggested questions; a blank Q&A box is intimidating to first-time users.",
 ],
 challenge="Turn off a synonym you added and re-ask the question to see Q&A fail, then turn it back on — a concrete demonstration of why Q&A setup matters.",
 reflection="LO6 — Why does teaching Q&A your business's synonyms matter more for non-technical users than for you, the report author?",
 ),
 dict(
 num=9, topic=3,
 title="Summarise Insights and Share Your AI-Assisted Report and Dashboard",
 objective="Use Copilot to produce an executive insight summary, publish the report to the Service, pin a dashboard, and share it safely with the right people.",
 desc="This lab turns your work into a product people use. You have Copilot summarise the whole report "
 "into an executive readout that answers the key business questions, publish the report to the Power "
 "BI Service, pin visuals to a dashboard, and share it — checking accuracy, respecting row-level "
 "security, and labelling AI-generated content before it goes out. This completes your connected "
 "Contoso Coffee report. " + PROJECT_NOTE,
 build="A published, shared AI-assisted Contoso Coffee report: an executive insight summary, a dashboard of pinned visuals, and a controlled share — the finished connected project.",
 services="Power BI Service, Copilot pane, publish, dashboards (pinning), sharing, row-level security",
 steps=[
 ("Open Copilot on the finished report and ask for an executive summary that answers the business questions the report was built to answer.",
  "Summarise this whole report for the leadership team: the headline sales result, the strongest and weakest regions, the top products, and the year-on-year trend, in one short paragraph and five bullets."),
 ("Read the summary and verify every figure against the report. Place the reviewed summary on an Executive Summary page and label it as AI-generated and reviewed.",""),
 ("Publish the report from Power BI Desktop to your lab workspace (Home > Publish), or save it in the Service if you built there.",""),
 ("In the Service, open the report and pin your headline KPI cards and the Sales by Region chart to a new dashboard named Contoso Coffee — Sales.",
  "Pin the Total Sales and Sales YoY % cards and the Sales by Region chart to a dashboard."),
 ("Add a natural-language dashboard tile if available, or use the dashboard Q&A box to add a plain-English tile such as 'sales by month this year'.",""),
 ("Before sharing, check governance: confirm the figures are accurate, confirm row-level security is applied if the data is sensitive, and confirm AI-generated content is labelled.",""),
 ("Share the dashboard with the right people using Share (or by adding them to the workspace with the correct role), granting the least access needed.",""),
 ("Do a final review: open the shared link as the audience would see it and confirm it is correct, readable and safe. Save and keep the finished Contoso Coffee report.",""),
 ],
 test="Your report is published to the Service with a reviewed, labelled executive summary, a Contoso Coffee — Sales dashboard of pinned visuals exists, and it is shared with the intended audience using least-access, with RLS respected where the data is sensitive.",
 troubleshooting=[
 "**Publish fails or the workspace is missing.** Confirm you are publishing to the lab-capacity workspace and signed in with the correct account (Lab 1).",
 "**You cannot pin a visual.** Pinning is a Service action — open the published report in app.powerbi.com, hover the visual and use the pin icon.",
 "**A shared user sees data they should not.** Row-level security is not applied or the share is too broad. Apply RLS roles and re-check the share list, granting least access.",
 ],
 challenge="Export the executive summary and one page to PDF from the Service and confirm the AI-generated summary is clearly labelled in the exported file — the version a stakeholder is most likely to forward.",
 reflection="LO7 — Before sharing an AI-assisted report, which three checks (accuracy, security, labelling) matter most for your data, and what could go wrong if you skip them?",
 ),
]
