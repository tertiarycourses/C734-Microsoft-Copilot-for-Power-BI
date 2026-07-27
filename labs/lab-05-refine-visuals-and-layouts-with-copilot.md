# Lab 5 — Refine Visuals and Layouts with Copilot

**Topic 02:** Create Reports and Visuals with Copilot  |  **Day 1**  |  **Approx. 32 min**  |  **Course:** Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Use Copilot to change visual types, swap and sort fields, apply filters, and tidy the page layout without leaving the pane.

## What you'll build

A refined Sales Overview page: correct visual types, sorted and filtered fields, and a clean, aligned layout.

**Tools and techniques:** Power BI (Desktop or Service), Copilot pane, visual formatting, filters, layout

## About this lab

A generated page is a starting point. In this lab you refine it with Copilot: change a chart's type, swap or add a field, sort and filter, and then have Copilot align and arrange the visuals so the page reads cleanly. You will alternate between prompting Copilot and nudging visuals by hand — the two work together. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

Open the Sales Overview page from Lab 4. Select the Sales Amount by Month visual and ask Copilot to change its type.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Change the Sales Amount by Month visual to a line and clustered column chart, with Sales Amount as the line and Quantity as the columns.
```

### Step 2

Refine a field on the region visual by prompting Copilot to sort and limit it.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Sort the Sales Amount by Region bar chart from highest to lowest and show only the top 5 regions.
```

### Step 3

Add a filter through Copilot so the page focuses on the current year.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Filter this page to the current year only.
```

### Step 4

Ask Copilot to improve the layout so the page is easy to read.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Arrange this page so the KPI cards are along the top and the charts are aligned in a tidy grid below them.
```

### Step 5

Fine-tune by hand: nudge and align a visual using the Format > Align tools, and resize the table so no data is cut off.

### Step 6

Ask Copilot to apply consistent formatting across the page.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Apply a consistent colour theme and format all Sales Amount values as currency with no decimals.
```

### Step 7

Compare the refined page with the Lab 4 draft and note two things Copilot changed that improved readability.

### Step 8

Save the file.

## Test it

Your Sales Overview page shows a combined line-and-column month visual, a top-5 sorted region chart, a current-year page filter, currency formatting, and a tidy aligned layout.

## Troubleshooting

- **Copilot changes the wrong visual.** Select the specific visual first, then prompt — Copilot acts on the selected visual. Name it in the prompt if there is any doubt.
- **The sort or top-N does not apply.** Re-state it explicitly ('sort descending by Sales Amount, keep top 5'); some visual types need the field in a specific well.
- **Currency format did not stick.** Set it directly on the field (Column tools > Format > Currency) as a fallback, then re-run the Copilot formatting prompt.

## Challenge

Ask Copilot to create a mobile-friendly version of the page, then open the Mobile layout view and check how the visuals reflow.

## Reflection

LO3 — Where did prompting Copilot work best, and where was it faster to adjust the visual by hand? What does that tell you about how to combine the two?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Copilot for Power BI (C734) · C734 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
