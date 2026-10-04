# Lab 2 — Connect and Prepare Data So Copilot Can Understand It

**Topic 01:** Get Started with Copilot in Power BI  |  **Day 1**  |  **Approx. 70 min**  |  **Course:** Microsoft Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Load the Contoso Coffee dataset, shape it in Power Query, and give tables and columns clear names, correct types and relationships so Copilot can interpret the model.

## What you'll build

A clean Contoso Coffee model in Power BI Desktop: well-named tables and columns, correct data types, and valid relationships — ready for Copilot.

**Tools and techniques:** Power BI Desktop, Get Data, Power Query Editor, data types, Model view, relationships

## About this lab

Copilot is only as good as the model you give it. In this lab you load the sales data, clean it in Power Query, rename cryptic columns into business terms, set correct data types, and confirm the relationships between your tables. A tidy, well-named model is what lets Copilot answer 'sales by region' correctly in the labs that follow. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

In Power BI Desktop, choose Home > Get data > Excel workbook (or Text/CSV) and load the supplied Contoso Coffee dataset — or your own sales data.

### Step 2

In the Navigator, select the Sales table (and any Products, Regions and Dates tables) and click Transform data to open Power Query rather than loading blindly.

### Step 3

In Power Query, rename cryptic columns to business terms: for example col_amt to Sales Amount, reg to Region, prod to Product. Clear names are how Copilot maps prompts to fields.

### Step 4

Set each column's data type correctly: Sales Amount and Quantity as numbers, Order Date as date, Region and Product as text. Wrong types break Copilot's charts and DAX.

### Step 5

Remove obvious noise: use Remove Rows > Remove Blank Rows and filter out any test or total rows that should not be in the detail data.

### Step 6

Click Close & Apply to load the shaped tables into the model.

### Step 7

Open Model view and confirm the relationships: Sales should relate to Products, Regions and Dates on their key columns. Create any missing relationship by dragging key to key.

### Step 8

Give the tables friendly names too (for example Sales, Product, Region, Calendar) and hide any technical key columns you do not want Copilot to surface.

### Step 9

Save the file as Contoso Coffee.pbix — this single file grows into your finished report across the remaining labs.

## Test it

Your model loads without errors, every column has a business-friendly name and correct data type, the Sales table is related to Product, Region and Calendar, and the file is saved as Contoso Coffee.pbix.

## Troubleshooting

- **Copilot later charts the wrong thing.** Almost always a naming or type problem. Return to Power Query, give the column a clear business name and the correct type, then Close & Apply.
- **A relationship will not create.** The key columns must share a data type and one side must be unique. Check that Product/Region/Date keys are unique in their lookup tables.
- **Numbers show as text (no sum).** The column type is Text. In Power Query set it to Decimal or Whole Number, then Close & Apply.

## Challenge

Add a simple Calendar table (or mark your date table as a date table) so time-based prompts like 'sales by month' and 'year to date' work reliably later.

## Reflection

LO2 — Why does renaming 'col_amt' to 'Sales Amount' change how well Copilot can answer your prompts, even though the numbers are identical?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Microsoft Copilot for Power BI (C734) · C734 · Version v2.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
