# Microsoft Copilot for Power BI (C734) — Learner Guide

**Course Code:** C734  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v2.0 · 4 October 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Get Started with Copilot in Power BI  (33%)](#topic-01--get-started-with-copilot-in-power-bi--33)
  - [Lab 1 — Enable Copilot and Set Up Your Power BI Environment](#lab-1--enable-copilot-and-set-up-your-power-bi-environment)
  - [Lab 2 — Connect and Prepare Data So Copilot Can Understand It](#lab-2--connect-and-prepare-data-so-copilot-can-understand-it)
  - [Lab 3 — Write Effective Prompts in Power BI Desktop and the Service](#lab-3--write-effective-prompts-in-power-bi-desktop-and-the-service)
- [Topic 02 — Create Reports and Visuals with Copilot  (34%)](#topic-02--create-reports-and-visuals-with-copilot--34)
  - [Lab 4 — Generate Report Pages from Prompts](#lab-4--generate-report-pages-from-prompts)
  - [Lab 5 — Refine Visuals and Layouts with Copilot](#lab-5--refine-visuals-and-layouts-with-copilot)
  - [Lab 6 — Add Narrative Visuals and AI Summaries with Storytelling and Formatting](#lab-6--add-narrative-visuals-and-ai-summaries-with-storytelling-and-formatting)
- [Topic 03 — AI-Assisted Data Modeling and Analysis  (33%)](#topic-03--ai-assisted-data-modeling-and-analysis--33)
  - [Lab 7 — Generate and Explain DAX Measures with Copilot](#lab-7--generate-and-explain-dax-measures-with-copilot)
  - [Lab 8 — Set Up Q&A and Natural-Language Queries](#lab-8--set-up-qa-and-natural-language-queries)
  - [Lab 9 — Summarise Insights and Share Your AI-Assisted Report and Dashboard](#lab-9--summarise-insights-and-share-your-ai-assisted-report-and-dashboard)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Microsoft Copilot for Power BI (C734) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 9 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build a single, connected Power BI report — a Sales & Operations dashboard for a fictional coffee retailer, Contoso Coffee. You enable Copilot and load the data in Labs 1-2, build and refine the report with prompts in Labs 3-6, add AI-assisted measures and natural-language analysis in Labs 7-8, and publish and share it in Lab 9. Wherever you can, use your own business data; a Contoso Coffee sample dataset is supplied for anyone who prefers not to.


## Course Learning Outcomes

- LO1: Explain what Copilot for Power BI and Microsoft Fabric are, and confirm the licensing and settings needed to enable Copilot.
- LO2: Connect and prepare data so that Copilot can interpret it, and write effective prompts in Power BI Desktop and the Service.
- LO3: Generate complete report pages and visuals from prompts, then refine their type, layout and formatting with Copilot.
- LO4: Add narrative visuals and AI summaries, and apply storytelling and formatting best practice to a report.
- LO5: Generate and explain DAX measures with Copilot to answer business questions.
- LO6: Set up Q&A and natural-language queries so users can ask questions of the data in plain English.
- LO7: Summarise insights, answer business questions, and publish and share an AI-assisted report and dashboard.


## Before You Start — Preparation

**What you need**

- A Windows laptop with Power BI Desktop installed (free from the Microsoft Store or powerbi.microsoft.com).
- A Power BI Service account (a work or school Microsoft 365 account) that can sign in to app.powerbi.com.
- Copilot for Power BI enabled on the tenant: a paid Fabric capacity (F2 or above) or Power BI Premium, with the Copilot tenant switch turned on (the trainer confirms lab-tenant access at the start of Day 1).
- The supplied Contoso Coffee sample dataset (an Excel workbook), or your own tabular business data in Excel or CSV.
- A current Chrome or Edge browser for the Power BI Service.

**Verify your setup**

Before Lab 1, confirm you can open Power BI Desktop, sign in to app.powerbi.com, and that the Copilot button is visible in the Service. If Copilot is greyed out, tell the trainer — it depends on the capacity and tenant switch.

```bash
Power BI Desktop: Home > sign in   ·   app.powerbi.com: open a workspace on the lab capacity > look for the Copilot button
```

**Conventions used in every lab**

- Placeholders such as <YOUR MEASURE> or <REGION> are replaced with your own values.
- Prompt text you type into the Copilot pane is shown in a shaded box — paste or type it into Copilot.
- Every lab ends with a 'Test it' step — an explicit check that Copilot produced the right result before you move on.
- Copilot output is a first draft. Read every page, visual and measure before you keep or share it.


## Topic 01 — Get Started with Copilot in Power BI  (33%)

What Copilot & Fabric are · Licensing & enabling · Desktop vs Service · Effective prompting · Preparing data

**Key concepts**

- Copilot for Power BI — an AI assistant, built on Microsoft Fabric, that turns plain-language prompts into report pages, visuals, DAX and summaries.
- Microsoft Fabric — the unified data platform Copilot runs on; Power BI is the reporting workload within it.
- Licensing and requirements — Copilot needs a paid Fabric capacity (F2 and above) or Power BI Premium, plus the tenant admin switch turned on.
- Enabling Copilot — a tenant admin enables Copilot in the Fabric admin portal; the report must sit on a supported capacity in a supported region.
- Copilot in Desktop vs the Service — Desktop authors the model and report locally; the Service (app.powerbi.com) shares, and the Copilot pane appears in both.
- The Copilot pane — a chat-style panel where you ask for pages, visuals, measures and summaries in everyday language.
- Effective prompting — a good prompt names the fields, the metric, the breakdown and the intent, not just 'make a chart'.
- Preparing data for Copilot — clear table and column names, correct data types and relationships let Copilot understand your model.
- You stay in control — Copilot proposes; you review every page, visual and measure before you keep it.


### Lab 1 — Enable Copilot and Set Up Your Power BI Environment

Learning outcome: Confirm the licensing and tenant settings Copilot needs, and verify the Copilot pane appears in Power BI Desktop and the Service..

Goal: This lab gets Copilot working before you rely on it. You confirm your workspace is on a Copilot-enabled Fabric or Premium capacity, check the tenant switch is on, and open the Copilot pane in both Power BI Desktop and the Power BI Service so you know where you will be working. Nothing here changes data — it is a setup and verification lab. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A confirmed Copilot-enabled environment: Power BI Desktop signed in, a workspace on a supported capacity, and the Copilot pane visible in the Service.   (Tools: Power BI Desktop, Power BI Service, Microsoft Fabric capacity, Fabric admin portal (tenant switch), Copilot pane.)

**Step-by-step**

1. Open Power BI Desktop and sign in (Home > Sign in) with the work or school account you will use for the course.
2. In a browser, open app.powerbi.com and sign in with the same account. Confirm you can see the workspace your trainer has placed on the lab capacity.
3. Open that workspace and check its capacity: Workspace settings > License info should show a Fabric capacity (F2 or above) or Premium — this is what Copilot requires.
4. Understand the tenant switch (admin context only): Copilot must be enabled in the Fabric admin portal under Tenant settings > Copilot and Azure OpenAI. Your trainer confirms this is on for the lab tenant.
5. In the Service, open the workspace and look for the Copilot button in the ribbon or toolbar. If it is greyed out or missing, tell the trainer — it depends on the capacity and the tenant switch.
6. Back in Power BI Desktop, note where Copilot appears (Home ribbon > Copilot) — you will use it once a model is loaded in the next lab.
7. Write down, in one line, the two things Copilot needs to be available: a supported paid capacity, and the tenant switch turned on.
8. Confirm you have changed no data — this lab only verifies access. You are now ready to load the dataset.

**Test it**

You are signed in to Power BI Desktop and the Service with the same account, your workspace is on a Fabric/Premium capacity, and the Copilot button is visible (not greyed out) in the Service.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


### Lab 2 — Connect and Prepare Data So Copilot Can Understand It

Learning outcome: Load the Contoso Coffee dataset, shape it in Power Query, and give tables and columns clear names, correct types and relationships so Copilot can interpret the model..

Goal: Copilot is only as good as the model you give it. In this lab you load the sales data, clean it in Power Query, rename cryptic columns into business terms, set correct data types, and confirm the relationships between your tables. A tidy, well-named model is what lets Copilot answer 'sales by region' correctly in the labs that follow. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A clean Contoso Coffee model in Power BI Desktop: well-named tables and columns, correct data types, and valid relationships — ready for Copilot.   (Tools: Power BI Desktop, Get Data, Power Query Editor, data types, Model view, relationships.)

**Step-by-step**

1. In Power BI Desktop, choose Home > Get data > Excel workbook (or Text/CSV) and load the supplied Contoso Coffee dataset — or your own sales data.
2. In the Navigator, select the Sales table (and any Products, Regions and Dates tables) and click Transform data to open Power Query rather than loading blindly.
3. In Power Query, rename cryptic columns to business terms: for example col_amt to Sales Amount, reg to Region, prod to Product. Clear names are how Copilot maps prompts to fields.
4. Set each column's data type correctly: Sales Amount and Quantity as numbers, Order Date as date, Region and Product as text. Wrong types break Copilot's charts and DAX.
5. Remove obvious noise: use Remove Rows > Remove Blank Rows and filter out any test or total rows that should not be in the detail data.
6. Click Close & Apply to load the shaped tables into the model.
7. Open Model view and confirm the relationships: Sales should relate to Products, Regions and Dates on their key columns. Create any missing relationship by dragging key to key.
8. Give the tables friendly names too (for example Sales, Product, Region, Calendar) and hide any technical key columns you do not want Copilot to surface.
9. Save the file as Contoso Coffee.pbix — this single file grows into your finished report across the remaining labs.

**Test it**

Your model loads without errors, every column has a business-friendly name and correct data type, the Sales table is related to Product, Region and Calendar, and the file is saved as Contoso Coffee.pbix.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


### Lab 3 — Write Effective Prompts in Power BI Desktop and the Service

Learning outcome: Open the Copilot pane on your model and write clear prompts that name the fields, metric, breakdown and intent, comparing a vague prompt with a specific one..

Goal: An agent is only as good as its prompt. With your clean model loaded, you open Copilot and compare a vague request with a specific one, see the difference in the result, and distil what worked into a reusable prompt pattern — Metric, Breakdown, Filter, Intent — that you will use for every prompt from here on, in both Desktop and the Service. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A reusable four-part prompt pattern and one strong, tested prompt saved for reuse, run in both Power BI Desktop and the Service.   (Tools: Power BI Desktop, Power BI Service, Copilot pane, prompt design.)

**Step-by-step**

1. In Power BI Desktop with Contoso Coffee.pbix open, click Home > Copilot to open the Copilot pane on your model.
2. Run a deliberately vague prompt and note how generic the result is.

   ```bash
   Show me the data.
   ```

3. Now run a specific prompt for the same intent and compare — it should be sharper and directly useful.

   ```bash
   Show total Sales Amount by Region as a bar chart, sorted from highest to lowest, for the last 12 months.
   ```

4. Write down the four parts that made the second prompt work: the Metric, the Breakdown, the Filter, and the Intent (the chart or answer you want).
5. Capture your reusable prompt pattern so every future prompt follows it.

   ```bash
   METRIC: <what to measure> | BREAKDOWN: <by which field> | FILTER: <time / segment> | INTENT: <chart, table or summary>
   ```

6. Try one more, changing only the breakdown, to feel how Copilot responds to precise fields.

   ```bash
   Show total Sales Amount by Product for this year as a column chart, top 10 products only.
   ```

7. Publish the report to your lab workspace (Home > Publish) and open it in the Service, then open Copilot there to confirm the pane works in both places.
8. Note one difference you observe between Copilot in Desktop and in the Service, and save your best prompt where you can find it again for the next topic.

**Test it**

You can show two results for the same intent (vague vs specific), a written four-part prompt pattern, and the same specific prompt working in both Power BI Desktop and the Service.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


## Topic 02 — Create Reports and Visuals with Copilot  (34%)

Generating pages from prompts · Refining visuals & layout · Narrative visuals & AI summaries · Formatting & storytelling

**Key concepts**

- Generating report pages — describe the report you want and Copilot builds a full page of related visuals for you to review.
- Suggested content — Copilot can propose which pages and visuals a dataset supports when you are not sure where to start.
- Refining visuals — ask Copilot to change a visual's type, swap fields, sort, filter or add a measure without leaving the pane.
- Refining layout — Copilot can rearrange, align and retheme a page so it reads cleanly on screen and in print.
- The narrative (smart) visual — a text visual that Copilot writes and keeps updated, explaining what the data shows in words.
- AI summaries — Copilot summarises a page or a visual into a short, plain-language readout for stakeholders.
- Storytelling — order the page top-left to bottom-right, lead with the headline number, and let each visual answer one question.
- Formatting best practice — consistent titles, number formats, colour and spacing make an AI-generated page look deliberate.
- Review and refine — every generated page is a first draft; you edit, re-prompt and format until it is right.


### Lab 4 — Generate Report Pages from Prompts

Learning outcome: Use Copilot to generate a complete report page of related visuals from a single prompt, and to suggest content when you are unsure where to start..

Goal: This is where Copilot saves you the most time. You describe the report page you want in plain language and Copilot builds a full page of related visuals — cards, charts and a table — for you to review. You also let Copilot suggest what a dataset supports when you have no starting point. Every generated page is a first draft you will refine next. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A Copilot-generated Sales Overview page in your Contoso Coffee report, plus a second page built from Copilot's own content suggestions.   (Tools: Power BI (Desktop or Service), Copilot pane, report page generation, suggested content.)

**Step-by-step**

1. Open Contoso Coffee.pbix (or the published report) and open the Copilot pane. Add a new blank report page and name it Sales Overview.
2. Ask Copilot to build the whole page from one prompt that names the metrics and breakdowns you want.

   ```bash
   Create a Sales Overview page with: total Sales Amount and total Quantity as KPI cards, Sales Amount by Region as a bar chart, Sales Amount by Month as a line chart, and Sales Amount by Product as a table.
   ```

3. Wait for Copilot to generate the page, then read every visual. Confirm the numbers look plausible against what you know of the data.
4. Where you are unsure what to build, ask Copilot to suggest content the dataset supports.

   ```bash
   Suggest report pages and visuals this dataset supports for a sales and operations audience.
   ```

5. Pick one suggestion and have Copilot create it on a new page named Channel & Product.

   ```bash
   Create a page showing Sales Amount by Channel as a donut chart and the top 10 Products by Sales Amount as a bar chart.
   ```

6. Rename any auto-generated visual titles that are unclear, so each visual states the question it answers.
7. Save the file. You now have two Copilot-generated pages as first drafts.

**Test it**

Your report has a Sales Overview page with KPI cards plus region, month and product visuals, and a second page created from a Copilot content suggestion — all showing correct fields from your model.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


### Lab 5 — Refine Visuals and Layouts with Copilot

Learning outcome: Use Copilot to change visual types, swap and sort fields, apply filters, and tidy the page layout without leaving the pane..

Goal: A generated page is a starting point. In this lab you refine it with Copilot: change a chart's type, swap or add a field, sort and filter, and then have Copilot align and arrange the visuals so the page reads cleanly. You will alternate between prompting Copilot and nudging visuals by hand — the two work together. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A refined Sales Overview page: correct visual types, sorted and filtered fields, and a clean, aligned layout.   (Tools: Power BI (Desktop or Service), Copilot pane, visual formatting, filters, layout.)

**Step-by-step**

1. Open the Sales Overview page from Lab 4. Select the Sales Amount by Month visual and ask Copilot to change its type.

   ```bash
   Change the Sales Amount by Month visual to a line and clustered column chart, with Sales Amount as the line and Quantity as the columns.
   ```

2. Refine a field on the region visual by prompting Copilot to sort and limit it.

   ```bash
   Sort the Sales Amount by Region bar chart from highest to lowest and show only the top 5 regions.
   ```

3. Add a filter through Copilot so the page focuses on the current year.

   ```bash
   Filter this page to the current year only.
   ```

4. Ask Copilot to improve the layout so the page is easy to read.

   ```bash
   Arrange this page so the KPI cards are along the top and the charts are aligned in a tidy grid below them.
   ```

5. Fine-tune by hand: nudge and align a visual using the Format > Align tools, and resize the table so no data is cut off.
6. Ask Copilot to apply consistent formatting across the page.

   ```bash
   Apply a consistent colour theme and format all Sales Amount values as currency with no decimals.
   ```

7. Compare the refined page with the Lab 4 draft and note two things Copilot changed that improved readability.
8. Save the file.

**Test it**

Your Sales Overview page shows a combined line-and-column month visual, a top-5 sorted region chart, a current-year page filter, currency formatting, and a tidy aligned layout.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


### Lab 6 — Add Narrative Visuals and AI Summaries with Storytelling and Formatting

Learning outcome: Add a Copilot narrative (smart) visual, generate an AI page summary, and apply storytelling and formatting best practice to the report..

Goal: Numbers need words. In this lab you add a narrative visual that Copilot writes and keeps updated, generate an AI summary of the page for stakeholders, and then apply storytelling best practice — headline first, one question per visual, a clean reading order — so the AI-generated content looks deliberate and reads well. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A Sales Overview page with a Copilot narrative visual, a saved AI summary, and a storytelling layout ready to show stakeholders.   (Tools: Power BI (Desktop or Service), Copilot pane, narrative/smart narrative visual, AI summary, formatting.)

**Step-by-step**

1. On the Sales Overview page, add a narrative visual: Insert > Narrative (or ask Copilot to create it), so Copilot writes a text explanation of the page.

   ```bash
   Add a narrative visual that summarises the key sales trends on this page in three short sentences and updates as the data changes.
   ```

2. Read the narrative and check every claim against the visuals. Re-prompt if it overstates or misreads a trend.

   ```bash
   Rewrite the narrative to focus on the top region, the best-selling product, and the month-on-month trend.
   ```

3. Generate an AI summary of the whole page for a stakeholder who will not open the report.

   ```bash
   Summarise this page in five bullet points for a busy executive, leading with the single most important number.
   ```

4. Copy the AI summary into a text box on the page (or your notes) and label it clearly as an AI-generated summary you have reviewed.
5. Apply storytelling order: move the headline KPI to the top-left, arrange visuals so the eye travels left-to-right and top-to-bottom, and make each visual answer one question.
6. Apply formatting best practice with a final Copilot prompt.

   ```bash
   Give this page consistent titles, currency formatting, aligned spacing and a single colour theme so it looks professional.
   ```

7. Do a 60-second test: look away, look back, and check the page's main message lands in under a minute. Adjust the headline if it does not.
8. Save the file.

**Test it**

Your page has a Copilot narrative visual whose claims match the visuals, a reviewed AI summary labelled as AI-generated, and a clean storytelling layout that communicates its main message within a minute.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


## Topic 03 — AI-Assisted Data Modeling and Analysis  (33%)

Generating & explaining DAX · Q&A & natural-language queries · Summarising insights · Sharing AI-assisted reports

**Key concepts**

- DAX with Copilot — describe the calculation you need in words and Copilot writes the DAX measure for you to check and keep.
- Explaining DAX — paste an unfamiliar measure and Copilot explains, in plain language, what it does and how.
- Measure hygiene — you still name, format and validate every measure Copilot writes before you trust it in a report.
- The Q&A visual — lets report users type a question and get an instant visual answer in natural language.
- Natural-language queries — 'sales by region last quarter' becomes a chart; good field names make the answers accurate.
- Synonyms and Q&A setup — teach Q&A the words your business uses so questions map to the right fields.
- Summarising insights — Copilot turns a report into an executive summary that answers the key business questions.
- Sharing AI-assisted reports — publish to the Power BI Service, build a dashboard, and share it with the right people.
- Trust and governance — check accuracy, respect row-level security, and label AI-generated content before you share it.


### Lab 7 — Generate and Explain DAX Measures with Copilot

Learning outcome: Use Copilot to write DAX measures from plain-language descriptions, explain an unfamiliar measure, then name, format and validate each one..

Goal: Copilot can write DAX so you describe the calculation in words instead of remembering syntax. In this lab you generate the core measures your report needs — total sales, a prior-period comparison and a percentage — have Copilot explain an unfamiliar measure in plain language, and then do the essential human step: name, format and validate every measure before you trust it. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A set of validated DAX measures (Total Sales, Sales YoY %, Average Order Value) written and explained by Copilot, added to your model.   (Tools: Power BI Desktop, Copilot pane, DAX measures, measure formatting, validation.)

**Step-by-step**

1. Open Contoso Coffee.pbix and open Copilot. Ask it to write your base sales measure.

   ```bash
   Write a DAX measure called Total Sales that sums Sales Amount from the Sales table.
   ```

2. Review the DAX Copilot returns, then create the measure (New measure) and paste it in. Set its format to currency with no decimals.
3. Ask Copilot for a time-comparison measure that depends on your Calendar table.

   ```bash
   Write a DAX measure called Sales YoY % that compares Total Sales to the same period last year and returns the percentage change.
   ```

4. Ask Copilot for a ratio measure so you can see basket size.

   ```bash
   Write a DAX measure called Average Order Value that divides Total Sales by the distinct count of Order ID, handling divide-by-zero safely.
   ```

5. Take an unfamiliar measure and have Copilot explain it in plain language so you understand before you keep it.

   ```bash
   Explain what this measure does, step by step, in plain language: Sales YoY %.
   ```

6. Validate each measure against the data: put Total Sales, Sales YoY % and Average Order Value in a table by Month and sanity-check the numbers against a visual you already trust.
7. Name and tidy: confirm each measure has a clear name, the right format, and a home table, and hide any helper columns Copilot no longer needs surfaced.
8. Add the new measures to your Sales Overview KPI cards and save the file.

**Test it**

Your model has three correctly named and formatted measures — Total Sales, Sales YoY % and Average Order Value — each validated against the data, and Copilot has produced a plain-language explanation of at least one of them.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


### Lab 8 — Set Up Q&A and Natural-Language Queries

Learning outcome: Add a Q&A visual, ask natural-language questions of the model, and improve accuracy by teaching Q&A synonyms and reviewing suggested questions..

Goal: Q&A lets anyone ask the report a question in plain English and get an instant visual. In this lab you add a Q&A visual, ask several questions, then improve the answers by teaching Q&A the words your business actually uses (synonyms) and curating the suggested questions — so a non-technical user gets the right answer first time. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A working Q&A experience on your report: a Q&A visual, tested natural-language questions, and synonyms and suggested questions configured for accuracy.   (Tools: Power BI (Desktop or Service), Q&A visual, natural-language queries, Q&A setup (synonyms, suggested questions), Copilot.)

**Step-by-step**

1. On a new page named Ask the Data, insert a Q&A visual (Insert > Q&A, or ask Copilot to add one).

   ```bash
   Add a Q&A visual to this page so users can ask questions about Contoso Coffee sales in natural language.
   ```

2. Type a natural-language question and watch Q&A build the answer visual.

   ```bash
   sales amount by region last quarter
   ```

3. Ask two more, changing the wording, to test how Q&A interprets business language.

   ```bash
   top 5 products by total sales this year
   ```

4. Find a question Q&A answers poorly because of wording, then teach it a synonym so business terms map to the right field (Modeling > Q&A setup > Field synonyms — for example map 'revenue' and 'takings' to Sales Amount).
5. Re-ask the question using the business word you just mapped and confirm Q&A now answers correctly.

   ```bash
   revenue by channel this year
   ```

6. Curate the experience: in Q&A setup, review the suggested questions and add three good starter questions users are likely to ask.
7. Use Copilot to propose questions this dataset can answer, and add the best to your suggested questions.

   ```bash
   Suggest five natural-language questions a store manager could ask this Contoso Coffee dataset.
   ```

8. Save the file. Your report now answers plain-English questions accurately.

**Test it**

Your report has a Q&A visual that correctly answers at least three natural-language questions, including one that only works because you added a synonym, plus three curated suggested questions.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


### Lab 9 — Summarise Insights and Share Your AI-Assisted Report and Dashboard

Learning outcome: Use Copilot to produce an executive insight summary, publish the report to the Service, pin a dashboard, and share it safely with the right people..

Goal: This lab turns your work into a product people use. You have Copilot summarise the whole report into an executive readout that answers the key business questions, publish the report to the Power BI Service, pin visuals to a dashboard, and share it — checking accuracy, respecting row-level security, and labelling AI-generated content before it goes out. This completes your connected Contoso Coffee report. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

**What you'll build**

A published, shared AI-assisted Contoso Coffee report: an executive insight summary, a dashboard of pinned visuals, and a controlled share — the finished connected project.   (Tools: Power BI Service, Copilot pane, publish, dashboards (pinning), sharing, row-level security.)

**Step-by-step**

1. Open Copilot on the finished report and ask for an executive summary that answers the business questions the report was built to answer.

   ```bash
   Summarise this whole report for the leadership team: the headline sales result, the strongest and weakest regions, the top products, and the year-on-year trend, in one short paragraph and five bullets.
   ```

2. Read the summary and verify every figure against the report. Place the reviewed summary on an Executive Summary page and label it as AI-generated and reviewed.
3. Publish the report from Power BI Desktop to your lab workspace (Home > Publish), or save it in the Service if you built there.
4. In the Service, open the report and pin your headline KPI cards and the Sales by Region chart to a new dashboard named Contoso Coffee — Sales.

   ```bash
   Pin the Total Sales and Sales YoY % cards and the Sales by Region chart to a dashboard.
   ```

5. Add a natural-language dashboard tile if available, or use the dashboard Q&A box to add a plain-English tile such as 'sales by month this year'.
6. Before sharing, check governance: confirm the figures are accurate, confirm row-level security is applied if the data is sensitive, and confirm AI-generated content is labelled.
7. Share the dashboard with the right people using Share (or by adding them to the workspace with the correct role), granting the least access needed.
8. Do a final review: open the shared link as the audience would see it and confirm it is correct, readable and safe. Save and keep the finished Contoso Coffee report.

**Test it**

Your report is published to the Service with a reviewed, labelled executive summary, a Contoso Coffee — Sales dashboard of pinned visuals exists, and it is shared with the intended audience using least-access, with RLS respected where the data is sensitive.

> **Note:** Full commands and screenshots are in labs/lab-09-*.md. Use only data you are authorised to use. Do not paste confidential or personal data into a Copilot prompt; use the supplied Contoso Coffee sample data if in doubt.

---


## Wrap-Up

You have built a complete AI-assisted Power BI report over two days — from enabling Copilot and preparing data to generating pages, writing DAX, configuring Q&A and publishing a shared dashboard.

**What you built**

- A Copilot-enabled Power BI environment and a clean, well-named Contoso Coffee model.
- Report pages and visuals generated from prompts, then refined for type, layout and formatting.
- Narrative visuals and AI summaries that explain the data in plain language.
- DAX measures written and explained by Copilot to answer real business questions.
- A configured Q&A experience and an executive insight summary.
- A published, shared AI-assisted report and dashboard in the Power BI Service.

**What to do next**

- Point Copilot at a real report in your own organisation, starting with a clean, well-named model.
- Build a prompt library for the pages, visuals and measures you make most often.
- Always validate Copilot's DAX and summaries against the underlying data before you share.
- Document which content is AI-generated and respect row-level security when you share.

---


## Next Steps

- First pass: complete every lab yourself, verifying each 'Test it' check on the Contoso Coffee report.
- Second pass: rebuild a report page, a DAX measure and the Q&A setup from memory, using your own prompts.
- Apply the techniques to a real report in your own organisation, beginning with a well-named model.
- Review each lab's detailed steps in this guide and re-run the Copilot workflows on your own data.


## Glossary

- **Copilot for Power BI** — An AI assistant that turns plain-language prompts into Power BI report pages, visuals, DAX and summaries.
- **Microsoft Fabric** — Microsoft's unified data platform; Power BI is the reporting workload within it and the capacity Copilot runs on.
- **Fabric capacity** — The paid compute (F2 and above) or Power BI Premium that a workspace runs on; Copilot requires it.
- **Tenant switch** — An admin setting in the Fabric/Power BI admin portal that must be on for Copilot to be available.
- **Power BI Desktop** — The free Windows application used to connect data, build the model and author reports locally.
- **Power BI Service** — The web app at app.powerbi.com used to publish, share and consume reports and dashboards.
- **Copilot pane** — The chat-style panel in Desktop and the Service where you prompt Copilot in everyday language.
- **Prompt** — A plain-language instruction that names the fields, metric, breakdown and intent you want Copilot to act on.
- **Report page** — A single canvas of related visuals; Copilot can generate a whole page from one prompt.
- **Visual** — A single chart, table or card on a report page.
- **Narrative visual** — A smart text visual that Copilot writes and updates to explain the data in words.
- **AI summary** — A short, plain-language readout of a page or visual generated by Copilot for stakeholders.
- **DAX** — Data Analysis Expressions — the formula language for Power BI measures and calculated columns.
- **Measure** — A DAX calculation, such as Total Sales, evaluated in the context of the visual that uses it.
- **Q&A** — A Power BI feature that answers natural-language questions with an instant visual.
- **Synonym** — An alternative word taught to Q&A so business terms map to the correct model fields.
- **Dashboard** — A single-page, pinned collection of visuals in the Service, often used to share key metrics.
- **Row-level security (RLS)** — Rules that restrict which rows of data a user can see; it must be respected when sharing.
