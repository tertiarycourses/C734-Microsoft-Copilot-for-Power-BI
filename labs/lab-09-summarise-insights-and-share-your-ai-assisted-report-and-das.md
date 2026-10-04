# Lab 9 — Summarise Insights and Share Your AI-Assisted Report and Dashboard

**Topic 03:** AI-Assisted Data Modeling and Analysis  |  **Day 2**  |  **Approx. 45 min**  |  **Course:** Microsoft Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Use Copilot to produce an executive insight summary, publish the report to the Service, pin a dashboard, and share it safely with the right people.

## What you'll build

A published, shared AI-assisted Contoso Coffee report: an executive insight summary, a dashboard of pinned visuals, and a controlled share — the finished connected project.

**Tools and techniques:** Power BI Service, Copilot pane, publish, dashboards (pinning), sharing, row-level security

## About this lab

This lab turns your work into a product people use. You have Copilot summarise the whole report into an executive readout that answers the key business questions, publish the report to the Power BI Service, pin visuals to a dashboard, and share it — checking accuracy, respecting row-level security, and labelling AI-generated content before it goes out. This completes your connected Contoso Coffee report. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

Open Copilot on the finished report and ask for an executive summary that answers the business questions the report was built to answer.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Summarise this whole report for the leadership team: the headline sales result, the strongest and weakest regions, the top products, and the year-on-year trend, in one short paragraph and five bullets.
```

### Step 2

Read the summary and verify every figure against the report. Place the reviewed summary on an Executive Summary page and label it as AI-generated and reviewed.

### Step 3

Publish the report from Power BI Desktop to your lab workspace (Home > Publish), or save it in the Service if you built there.

### Step 4

In the Service, open the report and pin your headline KPI cards and the Sales by Region chart to a new dashboard named Contoso Coffee — Sales.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Pin the Total Sales and Sales YoY % cards and the Sales by Region chart to a dashboard.
```

### Step 5

Add a natural-language dashboard tile if available, or use the dashboard Q&A box to add a plain-English tile such as 'sales by month this year'.

### Step 6

Before sharing, check governance: confirm the figures are accurate, confirm row-level security is applied if the data is sensitive, and confirm AI-generated content is labelled.

### Step 7

Share the dashboard with the right people using Share (or by adding them to the workspace with the correct role), granting the least access needed.

### Step 8

Do a final review: open the shared link as the audience would see it and confirm it is correct, readable and safe. Save and keep the finished Contoso Coffee report.

## Test it

Your report is published to the Service with a reviewed, labelled executive summary, a Contoso Coffee — Sales dashboard of pinned visuals exists, and it is shared with the intended audience using least-access, with RLS respected where the data is sensitive.

## Troubleshooting

- **Publish fails or the workspace is missing.** Confirm you are publishing to the lab-capacity workspace and signed in with the correct account (Lab 1).
- **You cannot pin a visual.** Pinning is a Service action — open the published report in app.powerbi.com, hover the visual and use the pin icon.
- **A shared user sees data they should not.** Row-level security is not applied or the share is too broad. Apply RLS roles and re-check the share list, granting least access.

## Challenge

Export the executive summary and one page to PDF from the Service and confirm the AI-generated summary is clearly labelled in the exported file — the version a stakeholder is most likely to forward.

## Reflection

LO7 — Before sharing an AI-assisted report, which three checks (accuracy, security, labelling) matter most for your data, and what could go wrong if you skip them?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Microsoft Copilot for Power BI (C734) · C734 · Version v2.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
