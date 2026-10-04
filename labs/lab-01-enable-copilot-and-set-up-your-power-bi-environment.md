# Lab 1 — Enable Copilot and Set Up Your Power BI Environment

**Topic 01:** Get Started with Copilot in Power BI  |  **Day 1**  |  **Approx. 45 min**  |  **Course:** Microsoft Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Confirm the licensing and tenant settings Copilot needs, and verify the Copilot pane appears in Power BI Desktop and the Service.

## What you'll build

A confirmed Copilot-enabled environment: Power BI Desktop signed in, a workspace on a supported capacity, and the Copilot pane visible in the Service.

**Tools and techniques:** Power BI Desktop, Power BI Service, Microsoft Fabric capacity, Fabric admin portal (tenant switch), Copilot pane

## About this lab

This lab gets Copilot working before you rely on it. You confirm your workspace is on a Copilot-enabled Fabric or Premium capacity, check the tenant switch is on, and open the Copilot pane in both Power BI Desktop and the Power BI Service so you know where you will be working. Nothing here changes data — it is a setup and verification lab. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

Open Power BI Desktop and sign in (Home > Sign in) with the work or school account you will use for the course.

### Step 2

In a browser, open app.powerbi.com and sign in with the same account. Confirm you can see the workspace your trainer has placed on the lab capacity.

### Step 3

Open that workspace and check its capacity: Workspace settings > License info should show a Fabric capacity (F2 or above) or Premium — this is what Copilot requires.

### Step 4

Understand the tenant switch (admin context only): Copilot must be enabled in the Fabric admin portal under Tenant settings > Copilot and Azure OpenAI. Your trainer confirms this is on for the lab tenant.

### Step 5

In the Service, open the workspace and look for the Copilot button in the ribbon or toolbar. If it is greyed out or missing, tell the trainer — it depends on the capacity and the tenant switch.

### Step 6

Back in Power BI Desktop, note where Copilot appears (Home ribbon > Copilot) — you will use it once a model is loaded in the next lab.

### Step 7

Write down, in one line, the two things Copilot needs to be available: a supported paid capacity, and the tenant switch turned on.

### Step 8

Confirm you have changed no data — this lab only verifies access. You are now ready to load the dataset.

## Test it

You are signed in to Power BI Desktop and the Service with the same account, your workspace is on a Fabric/Premium capacity, and the Copilot button is visible (not greyed out) in the Service.

## Troubleshooting

- **The Copilot button is greyed out or missing.** Copilot needs a paid Fabric capacity (F2+) or Premium AND the tenant switch on. Confirm the workspace is on the lab capacity (Workspace settings > License info) and tell the trainer if it still does not appear.
- **You cannot see the lab workspace.** Make sure you signed in to the Service with the same work/school account the trainer added you to — a personal Microsoft account will not see it.
- **Copilot is unavailable in your region.** Copilot depends on the capacity's region. For the labs, use the trainer-provided workspace, which is on a supported capacity.

## Challenge

In the Fabric admin portal documentation, find the minimum capacity size that supports Copilot and note how it differs from the capacity needed for other Fabric workloads.

## Reflection

LO1 — In your own words, what are the two prerequisites that must both be true before Copilot appears in Power BI, and why is it not simply a Desktop setting?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Microsoft Copilot for Power BI (C734) · C734 · Version v2.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
