"""
Domain 1 — Get Started with Copilot in Power BI. Labs 1-3.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course adds one piece to a single, growing Power BI report — a
Sales & Operations dashboard for a fictional coffee retailer, Contoso Coffee. Lab 1
confirms Copilot is enabled and prepares your environment; Lab 2 loads and shapes
the data so Copilot can understand it; Lab 3 writes your first effective prompts.
Wherever possible use your OWN business data so you leave with a report that
already works for you; the Contoso Coffee sample dataset is provided for anyone who
prefers not to use real data.
"""

SCENARIO = (
 "Contoso Coffee is a growing coffee retailer with cafes across several regions. You are "
 "the business analyst: every week you are asked for the sales numbers — by region, by "
 "product, by channel, by month — and every week you rebuild the same charts by hand. "
 "Across this course you use Copilot in Power BI to build a Sales & Operations dashboard "
 "that drafts those pages, visuals, measures and summaries for you, always under your "
 "review. Use this scenario only if you cannot use a real dataset from your own workplace; "
 "your own data is always preferred."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the "
 "single connected dashboard you assemble across all 9 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Enable Copilot and Set Up Your Power BI Environment",
 objective="Confirm the licensing and tenant settings Copilot needs, and verify the Copilot pane appears in Power BI Desktop and the Service.",
 desc="This lab gets Copilot working before you rely on it. You confirm your workspace is on a "
 "Copilot-enabled Fabric or Premium capacity, check the tenant switch is on, and open the Copilot "
 "pane in both Power BI Desktop and the Power BI Service so you know where you will be working. "
 "Nothing here changes data — it is a setup and verification lab. " + PROJECT_NOTE,
 build="A confirmed Copilot-enabled environment: Power BI Desktop signed in, a workspace on a supported capacity, and the Copilot pane visible in the Service.",
 services="Power BI Desktop, Power BI Service, Microsoft Fabric capacity, Fabric admin portal (tenant switch), Copilot pane",
 steps=[
 ("Open Power BI Desktop and sign in (Home > Sign in) with the work or school account you will use for the course.", ""),
 ("In a browser, open app.powerbi.com and sign in with the same account. Confirm you can see the workspace your trainer has placed on the lab capacity.", ""),
 ("Open that workspace and check its capacity: Workspace settings > License info should show a Fabric capacity (F2 or above) or Premium — this is what Copilot requires.", ""),
 ("Understand the tenant switch (admin context only): Copilot must be enabled in the Fabric admin portal under Tenant settings > Copilot and Azure OpenAI. Your trainer confirms this is on for the lab tenant.", ""),
 ("In the Service, open the workspace and look for the Copilot button in the ribbon or toolbar. If it is greyed out or missing, tell the trainer — it depends on the capacity and the tenant switch.", ""),
 ("Back in Power BI Desktop, note where Copilot appears (Home ribbon > Copilot) — you will use it once a model is loaded in the next lab.", ""),
 ("Write down, in one line, the two things Copilot needs to be available: a supported paid capacity, and the tenant switch turned on.", ""),
 ("Confirm you have changed no data — this lab only verifies access. You are now ready to load the dataset.", ""),
 ],
 test="You are signed in to Power BI Desktop and the Service with the same account, your workspace is on a Fabric/Premium capacity, and the Copilot button is visible (not greyed out) in the Service.",
 troubleshooting=[
 "**The Copilot button is greyed out or missing.** Copilot needs a paid Fabric capacity (F2+) or Premium AND the tenant switch on. Confirm the workspace is on the lab capacity (Workspace settings > License info) and tell the trainer if it still does not appear.",
 "**You cannot see the lab workspace.** Make sure you signed in to the Service with the same work/school account the trainer added you to — a personal Microsoft account will not see it.",
 "**Copilot is unavailable in your region.** Copilot depends on the capacity's region. For the labs, use the trainer-provided workspace, which is on a supported capacity.",
 ],
 challenge="In the Fabric admin portal documentation, find the minimum capacity size that supports Copilot and note how it differs from the capacity needed for other Fabric workloads.",
 reflection="LO1 — In your own words, what are the two prerequisites that must both be true before Copilot appears in Power BI, and why is it not simply a Desktop setting?",
 ),
 dict(
 num=2, topic=1,
 title="Connect and Prepare Data So Copilot Can Understand It",
 objective="Load the Contoso Coffee dataset, shape it in Power Query, and give tables and columns clear names, correct types and relationships so Copilot can interpret the model.",
 desc="Copilot is only as good as the model you give it. In this lab you load the sales data, clean it "
 "in Power Query, rename cryptic columns into business terms, set correct data types, and confirm "
 "the relationships between your tables. A tidy, well-named model is what lets Copilot answer "
 "'sales by region' correctly in the labs that follow. " + PROJECT_NOTE,
 build="A clean Contoso Coffee model in Power BI Desktop: well-named tables and columns, correct data types, and valid relationships — ready for Copilot.",
 services="Power BI Desktop, Get Data, Power Query Editor, data types, Model view, relationships",
 steps=[
 ("In Power BI Desktop, choose Home > Get data > Excel workbook (or Text/CSV) and load the supplied Contoso Coffee dataset — or your own sales data.",""),
 ("In the Navigator, select the Sales table (and any Products, Regions and Dates tables) and click Transform data to open Power Query rather than loading blindly.",""),
 ("In Power Query, rename cryptic columns to business terms: for example col_amt to Sales Amount, reg to Region, prod to Product. Clear names are how Copilot maps prompts to fields.",""),
 ("Set each column's data type correctly: Sales Amount and Quantity as numbers, Order Date as date, Region and Product as text. Wrong types break Copilot's charts and DAX.",""),
 ("Remove obvious noise: use Remove Rows > Remove Blank Rows and filter out any test or total rows that should not be in the detail data.",""),
 ("Click Close & Apply to load the shaped tables into the model.",""),
 ("Open Model view and confirm the relationships: Sales should relate to Products, Regions and Dates on their key columns. Create any missing relationship by dragging key to key.",""),
 ("Give the tables friendly names too (for example Sales, Product, Region, Calendar) and hide any technical key columns you do not want Copilot to surface.",""),
 ("Save the file as Contoso Coffee.pbix — this single file grows into your finished report across the remaining labs.",""),
 ],
 test="Your model loads without errors, every column has a business-friendly name and correct data type, the Sales table is related to Product, Region and Calendar, and the file is saved as Contoso Coffee.pbix.",
 troubleshooting=[
 "**Copilot later charts the wrong thing.** Almost always a naming or type problem. Return to Power Query, give the column a clear business name and the correct type, then Close & Apply.",
 "**A relationship will not create.** The key columns must share a data type and one side must be unique. Check that Product/Region/Date keys are unique in their lookup tables.",
 "**Numbers show as text (no sum).** The column type is Text. In Power Query set it to Decimal or Whole Number, then Close & Apply.",
 ],
 challenge="Add a simple Calendar table (or mark your date table as a date table) so time-based prompts like 'sales by month' and 'year to date' work reliably later.",
 reflection="LO2 — Why does renaming 'col_amt' to 'Sales Amount' change how well Copilot can answer your prompts, even though the numbers are identical?",
 ),
 dict(
 num=3, topic=1,
 title="Write Effective Prompts in Power BI Desktop and the Service",
 objective="Open the Copilot pane on your model and write clear prompts that name the fields, metric, breakdown and intent, comparing a vague prompt with a specific one.",
 desc="An agent is only as good as its prompt. With your clean model loaded, you open Copilot and "
 "compare a vague request with a specific one, see the difference in the result, and distil what "
 "worked into a reusable prompt pattern — Metric, Breakdown, Filter, Intent — that you will use for "
 "every prompt from here on, in both Desktop and the Service. " + PROJECT_NOTE,
 build="A reusable four-part prompt pattern and one strong, tested prompt saved for reuse, run in both Power BI Desktop and the Service.",
 services="Power BI Desktop, Power BI Service, Copilot pane, prompt design",
 steps=[
 ("In Power BI Desktop with Contoso Coffee.pbix open, click Home > Copilot to open the Copilot pane on your model.",""),
 ("Run a deliberately vague prompt and note how generic the result is.",
  "Show me the data."),
 ("Now run a specific prompt for the same intent and compare — it should be sharper and directly useful.",
  "Show total Sales Amount by Region as a bar chart, sorted from highest to lowest, for the last 12 months."),
 ("Write down the four parts that made the second prompt work: the Metric, the Breakdown, the Filter, and the Intent (the chart or answer you want).",""),
 ("Capture your reusable prompt pattern so every future prompt follows it.",
  "METRIC: <what to measure> | BREAKDOWN: <by which field> | FILTER: <time / segment> | INTENT: <chart, table or summary>"),
 ("Try one more, changing only the breakdown, to feel how Copilot responds to precise fields.",
  "Show total Sales Amount by Product for this year as a column chart, top 10 products only."),
 ("Publish the report to your lab workspace (Home > Publish) and open it in the Service, then open Copilot there to confirm the pane works in both places.",""),
 ("Note one difference you observe between Copilot in Desktop and in the Service, and save your best prompt where you can find it again for the next topic.",""),
 ],
 test="You can show two results for the same intent (vague vs specific), a written four-part prompt pattern, and the same specific prompt working in both Power BI Desktop and the Service.",
 troubleshooting=[
 "**Copilot says it cannot find a field.** Use the exact field name from your model. Open the Data pane to check the name, or rephrase using the business term you set in Lab 2.",
 "**The result ignores your time filter.** Make sure you have a real date column (or Calendar table) and reference it by name, e.g. 'in the last 12 months' with an Order Date field present.",
 "**Copilot is missing in the Service but present in Desktop.** The Service pane depends on the capacity and tenant switch (Lab 1). Confirm the report is published to the lab-capacity workspace.",
 ],
 challenge="Write three prompts that each return the same insight (Sales by Region) as three different visuals — a bar chart, a map and a table — and note which the audience reads fastest.",
 reflection="LO2 — Which of the four prompt parts (Metric, Breakdown, Filter, Intent) made the biggest difference to your result, and why?",
 ),
]
