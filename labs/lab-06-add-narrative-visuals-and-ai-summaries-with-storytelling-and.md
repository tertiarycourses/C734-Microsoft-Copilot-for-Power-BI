# Lab 6 — Add Narrative Visuals and AI Summaries with Storytelling and Formatting

**Topic 02:** Create Reports and Visuals with Copilot  |  **Day 1**  |  **Approx. 45 min**  |  **Course:** Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Add a Copilot narrative (smart) visual, generate an AI page summary, and apply storytelling and formatting best practice to the report.

## What you'll build

A Sales Overview page with a Copilot narrative visual, a saved AI summary, and a storytelling layout ready to show stakeholders.

**Tools and techniques:** Power BI (Desktop or Service), Copilot pane, narrative/smart narrative visual, AI summary, formatting

## About this lab

Numbers need words. In this lab you add a narrative visual that Copilot writes and keeps updated, generate an AI summary of the page for stakeholders, and then apply storytelling best practice — headline first, one question per visual, a clean reading order — so the AI-generated content looks deliberate and reads well. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

On the Sales Overview page, add a narrative visual: Insert > Narrative (or ask Copilot to create it), so Copilot writes a text explanation of the page.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Add a narrative visual that summarises the key sales trends on this page in three short sentences and updates as the data changes.
```

### Step 2

Read the narrative and check every claim against the visuals. Re-prompt if it overstates or misreads a trend.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Rewrite the narrative to focus on the top region, the best-selling product, and the month-on-month trend.
```

### Step 3

Generate an AI summary of the whole page for a stakeholder who will not open the report.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Summarise this page in five bullet points for a busy executive, leading with the single most important number.
```

### Step 4

Copy the AI summary into a text box on the page (or your notes) and label it clearly as an AI-generated summary you have reviewed.

### Step 5

Apply storytelling order: move the headline KPI to the top-left, arrange visuals so the eye travels left-to-right and top-to-bottom, and make each visual answer one question.

### Step 6

Apply formatting best practice with a final Copilot prompt.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Give this page consistent titles, currency formatting, aligned spacing and a single colour theme so it looks professional.
```

### Step 7

Do a 60-second test: look away, look back, and check the page's main message lands in under a minute. Adjust the headline if it does not.

### Step 8

Save the file.

## Test it

Your page has a Copilot narrative visual whose claims match the visuals, a reviewed AI summary labelled as AI-generated, and a clean storytelling layout that communicates its main message within a minute.

## Troubleshooting

- **The narrative states something the charts do not show.** Re-prompt to focus on specific, verifiable points, and always read the narrative against the visuals before you keep it.
- **The narrative visual is not available.** Confirm the narrative/smart-narrative visual is enabled in your tenant; otherwise generate the text with a Copilot summary prompt and place it in a text box.
- **The summary is too long.** Ask Copilot to cap it ('in exactly five bullets, one line each') — precise limits produce tighter output.

## Challenge

Generate two summaries of the same page for two audiences — a finance lead and a store manager — and note how the emphasis should differ.

## Reflection

LO4 — Why does a good narrative or summary lead with the single most important number, and how does that change what a stakeholder takes away?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Copilot for Power BI (C734) · C734 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
