# Lab 7 — Generate and Explain DAX Measures with Copilot

**Topic 03:** AI-Assisted Data Modeling and Analysis  |  **Day 2**  |  **Approx. 60 min**  |  **Course:** Microsoft Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Use Copilot to write DAX measures from plain-language descriptions, explain an unfamiliar measure, then name, format and validate each one.

## What you'll build

A set of validated DAX measures (Total Sales, Sales YoY %, Average Order Value) written and explained by Copilot, added to your model.

**Tools and techniques:** Power BI Desktop, Copilot pane, DAX measures, measure formatting, validation

## About this lab

Copilot can write DAX so you describe the calculation in words instead of remembering syntax. In this lab you generate the core measures your report needs — total sales, a prior-period comparison and a percentage — have Copilot explain an unfamiliar measure in plain language, and then do the essential human step: name, format and validate every measure before you trust it. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

Open Contoso Coffee.pbix and open Copilot. Ask it to write your base sales measure.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Write a DAX measure called Total Sales that sums Sales Amount from the Sales table.
```

### Step 2

Review the DAX Copilot returns, then create the measure (New measure) and paste it in. Set its format to currency with no decimals.

### Step 3

Ask Copilot for a time-comparison measure that depends on your Calendar table.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Write a DAX measure called Sales YoY % that compares Total Sales to the same period last year and returns the percentage change.
```

### Step 4

Ask Copilot for a ratio measure so you can see basket size.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Write a DAX measure called Average Order Value that divides Total Sales by the distinct count of Order ID, handling divide-by-zero safely.
```

### Step 5

Take an unfamiliar measure and have Copilot explain it in plain language so you understand before you keep it.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Explain what this measure does, step by step, in plain language: Sales YoY %.
```

### Step 6

Validate each measure against the data: put Total Sales, Sales YoY % and Average Order Value in a table by Month and sanity-check the numbers against a visual you already trust.

### Step 7

Name and tidy: confirm each measure has a clear name, the right format, and a home table, and hide any helper columns Copilot no longer needs surfaced.

### Step 8

Add the new measures to your Sales Overview KPI cards and save the file.

## Test it

Your model has three correctly named and formatted measures — Total Sales, Sales YoY % and Average Order Value — each validated against the data, and Copilot has produced a plain-language explanation of at least one of them.

## Troubleshooting

- **The YoY measure returns blank.** It needs a proper date table. Mark your Calendar as a date table (or add one) and ensure Sales relates to it, then re-run the prompt.
- **The numbers look wrong.** Never trust DAX unchecked — put the measure in a table beside a known-good visual and compare. Re-prompt Copilot with the correction if needed.
- **Divide-by-zero error on Average Order Value.** Ask Copilot to use DIVIDE() which handles zero safely, rather than the / operator.

## Challenge

Ask Copilot to write a running-total (year-to-date) Sales measure, then have it explain the DAX so you could recreate it yourself without Copilot.

## Reflection

LO5 — Copilot wrote the DAX correctly — so why is naming, formatting and validating each measure still your job, not the AI's?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Microsoft Copilot for Power BI (C734) · C734 · Version v2.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
