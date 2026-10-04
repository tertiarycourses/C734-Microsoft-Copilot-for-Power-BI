# Lab 3 — Write Effective Prompts in Power BI Desktop and the Service

**Topic 01:** Get Started with Copilot in Power BI  |  **Day 1**  |  **Approx. 60 min**  |  **Course:** Microsoft Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Open the Copilot pane on your model and write clear prompts that name the fields, metric, breakdown and intent, comparing a vague prompt with a specific one.

## What you'll build

A reusable four-part prompt pattern and one strong, tested prompt saved for reuse, run in both Power BI Desktop and the Service.

**Tools and techniques:** Power BI Desktop, Power BI Service, Copilot pane, prompt design

## About this lab

An agent is only as good as its prompt. With your clean model loaded, you open Copilot and compare a vague request with a specific one, see the difference in the result, and distil what worked into a reusable prompt pattern — Metric, Breakdown, Filter, Intent — that you will use for every prompt from here on, in both Desktop and the Service. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

In Power BI Desktop with Contoso Coffee.pbix open, click Home > Copilot to open the Copilot pane on your model.

### Step 2

Run a deliberately vague prompt and note how generic the result is.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Show me the data.
```

### Step 3

Now run a specific prompt for the same intent and compare — it should be sharper and directly useful.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Show total Sales Amount by Region as a bar chart, sorted from highest to lowest, for the last 12 months.
```

### Step 4

Write down the four parts that made the second prompt work: the Metric, the Breakdown, the Filter, and the Intent (the chart or answer you want).

### Step 5

Capture your reusable prompt pattern so every future prompt follows it.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
METRIC: <what to measure> | BREAKDOWN: <by which field> | FILTER: <time / segment> | INTENT: <chart, table or summary>
```

### Step 6

Try one more, changing only the breakdown, to feel how Copilot responds to precise fields.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Show total Sales Amount by Product for this year as a column chart, top 10 products only.
```

### Step 7

Publish the report to your lab workspace (Home > Publish) and open it in the Service, then open Copilot there to confirm the pane works in both places.

### Step 8

Note one difference you observe between Copilot in Desktop and in the Service, and save your best prompt where you can find it again for the next topic.

## Test it

You can show two results for the same intent (vague vs specific), a written four-part prompt pattern, and the same specific prompt working in both Power BI Desktop and the Service.

## Troubleshooting

- **Copilot says it cannot find a field.** Use the exact field name from your model. Open the Data pane to check the name, or rephrase using the business term you set in Lab 2.
- **The result ignores your time filter.** Make sure you have a real date column (or Calendar table) and reference it by name, e.g. 'in the last 12 months' with an Order Date field present.
- **Copilot is missing in the Service but present in Desktop.** The Service pane depends on the capacity and tenant switch (Lab 1). Confirm the report is published to the lab-capacity workspace.

## Challenge

Write three prompts that each return the same insight (Sales by Region) as three different visuals — a bar chart, a map and a table — and note which the audience reads fastest.

## Reflection

LO2 — Which of the four prompt parts (Metric, Breakdown, Filter, Intent) made the biggest difference to your result, and why?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Microsoft Copilot for Power BI (C734) · C734 · Version v2.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
