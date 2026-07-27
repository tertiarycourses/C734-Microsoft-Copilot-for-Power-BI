# Lab 4 — Generate Report Pages from Prompts

**Topic 02:** Create Reports and Visuals with Copilot  |  **Day 1**  |  **Approx. 32 min**  |  **Course:** Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Use Copilot to generate a complete report page of related visuals from a single prompt, and to suggest content when you are unsure where to start.

## What you'll build

A Copilot-generated Sales Overview page in your Contoso Coffee report, plus a second page built from Copilot's own content suggestions.

**Tools and techniques:** Power BI (Desktop or Service), Copilot pane, report page generation, suggested content

## About this lab

This is where Copilot saves you the most time. You describe the report page you want in plain language and Copilot builds a full page of related visuals — cards, charts and a table — for you to review. You also let Copilot suggest what a dataset supports when you have no starting point. Every generated page is a first draft you will refine next. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

Open Contoso Coffee.pbix (or the published report) and open the Copilot pane. Add a new blank report page and name it Sales Overview.

### Step 2

Ask Copilot to build the whole page from one prompt that names the metrics and breakdowns you want.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Create a Sales Overview page with: total Sales Amount and total Quantity as KPI cards, Sales Amount by Region as a bar chart, Sales Amount by Month as a line chart, and Sales Amount by Product as a table.
```

### Step 3

Wait for Copilot to generate the page, then read every visual. Confirm the numbers look plausible against what you know of the data.

### Step 4

Where you are unsure what to build, ask Copilot to suggest content the dataset supports.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Suggest report pages and visuals this dataset supports for a sales and operations audience.
```

### Step 5

Pick one suggestion and have Copilot create it on a new page named Channel & Product.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Create a page showing Sales Amount by Channel as a donut chart and the top 10 Products by Sales Amount as a bar chart.
```

### Step 6

Rename any auto-generated visual titles that are unclear, so each visual states the question it answers.

### Step 7

Save the file. You now have two Copilot-generated pages as first drafts.

## Test it

Your report has a Sales Overview page with KPI cards plus region, month and product visuals, and a second page created from a Copilot content suggestion — all showing correct fields from your model.

## Troubleshooting

- **Copilot builds a visual on the wrong field.** Re-prompt naming the exact field, e.g. 'use Sales Amount, not Quantity'. If it persists, the field name is ambiguous — clarify it in the model (Lab 2).
- **The page is empty or errors out.** Copilot needs a loaded model with data. Confirm Close & Apply ran and the tables contain rows.
- **A KPI card shows a blank.** The measure it used may need a base measure. Note it — you will create proper measures with Copilot in Lab 7.

## Challenge

Prompt Copilot to build a page aimed at a different audience (for example a regional manager) and compare which visuals it chooses versus the executive Sales Overview.

## Reflection

LO3 — How does describing the metrics and breakdowns up front change the quality of the page Copilot generates, compared with asking it to 'make a sales report'?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Copilot for Power BI (C734) · C734 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
