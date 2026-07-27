"""
Domain 2 — Create Reports and Visuals with Copilot. Labs 4-6.

You build on the clean Contoso Coffee model from Domain 1. Lab 4 has Copilot
generate whole report pages from a prompt; Lab 5 refines the visuals and layout;
Lab 6 adds a narrative visual and AI summaries and applies formatting and
storytelling best practice. Every artifact is added to the same Contoso Coffee
report you will publish and share in Lab 9.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the "
 "single connected dashboard you assemble across all 9 labs."
)

DOMAIN2 = [
 dict(
 num=4, topic=2,
 title="Generate Report Pages from Prompts",
 objective="Use Copilot to generate a complete report page of related visuals from a single prompt, and to suggest content when you are unsure where to start.",
 desc="This is where Copilot saves you the most time. You describe the report page you want in plain "
 "language and Copilot builds a full page of related visuals — cards, charts and a table — for you "
 "to review. You also let Copilot suggest what a dataset supports when you have no starting point. "
 "Every generated page is a first draft you will refine next. " + PROJECT_NOTE,
 build="A Copilot-generated Sales Overview page in your Contoso Coffee report, plus a second page built from Copilot's own content suggestions.",
 services="Power BI (Desktop or Service), Copilot pane, report page generation, suggested content",
 steps=[
 ("Open Contoso Coffee.pbix (or the published report) and open the Copilot pane. Add a new blank report page and name it Sales Overview.",""),
 ("Ask Copilot to build the whole page from one prompt that names the metrics and breakdowns you want.",
  "Create a Sales Overview page with: total Sales Amount and total Quantity as KPI cards, Sales Amount by Region as a bar chart, Sales Amount by Month as a line chart, and Sales Amount by Product as a table."),
 ("Wait for Copilot to generate the page, then read every visual. Confirm the numbers look plausible against what you know of the data.",""),
 ("Where you are unsure what to build, ask Copilot to suggest content the dataset supports.",
  "Suggest report pages and visuals this dataset supports for a sales and operations audience."),
 ("Pick one suggestion and have Copilot create it on a new page named Channel & Product.",
  "Create a page showing Sales Amount by Channel as a donut chart and the top 10 Products by Sales Amount as a bar chart."),
 ("Rename any auto-generated visual titles that are unclear, so each visual states the question it answers.",""),
 ("Save the file. You now have two Copilot-generated pages as first drafts.",""),
 ],
 test="Your report has a Sales Overview page with KPI cards plus region, month and product visuals, and a second page created from a Copilot content suggestion — all showing correct fields from your model.",
 troubleshooting=[
 "**Copilot builds a visual on the wrong field.** Re-prompt naming the exact field, e.g. 'use Sales Amount, not Quantity'. If it persists, the field name is ambiguous — clarify it in the model (Lab 2).",
 "**The page is empty or errors out.** Copilot needs a loaded model with data. Confirm Close & Apply ran and the tables contain rows.",
 "**A KPI card shows a blank.** The measure it used may need a base measure. Note it — you will create proper measures with Copilot in Lab 7.",
 ],
 challenge="Prompt Copilot to build a page aimed at a different audience (for example a regional manager) and compare which visuals it chooses versus the executive Sales Overview.",
 reflection="LO3 — How does describing the metrics and breakdowns up front change the quality of the page Copilot generates, compared with asking it to 'make a sales report'?",
 ),
 dict(
 num=5, topic=2,
 title="Refine Visuals and Layouts with Copilot",
 objective="Use Copilot to change visual types, swap and sort fields, apply filters, and tidy the page layout without leaving the pane.",
 desc="A generated page is a starting point. In this lab you refine it with Copilot: change a chart's "
 "type, swap or add a field, sort and filter, and then have Copilot align and arrange the visuals so "
 "the page reads cleanly. You will alternate between prompting Copilot and nudging visuals by hand — "
 "the two work together. " + PROJECT_NOTE,
 build="A refined Sales Overview page: correct visual types, sorted and filtered fields, and a clean, aligned layout.",
 services="Power BI (Desktop or Service), Copilot pane, visual formatting, filters, layout",
 steps=[
 ("Open the Sales Overview page from Lab 4. Select the Sales Amount by Month visual and ask Copilot to change its type.",
  "Change the Sales Amount by Month visual to a line and clustered column chart, with Sales Amount as the line and Quantity as the columns."),
 ("Refine a field on the region visual by prompting Copilot to sort and limit it.",
  "Sort the Sales Amount by Region bar chart from highest to lowest and show only the top 5 regions."),
 ("Add a filter through Copilot so the page focuses on the current year.",
  "Filter this page to the current year only."),
 ("Ask Copilot to improve the layout so the page is easy to read.",
  "Arrange this page so the KPI cards are along the top and the charts are aligned in a tidy grid below them."),
 ("Fine-tune by hand: nudge and align a visual using the Format > Align tools, and resize the table so no data is cut off.",""),
 ("Ask Copilot to apply consistent formatting across the page.",
  "Apply a consistent colour theme and format all Sales Amount values as currency with no decimals."),
 ("Compare the refined page with the Lab 4 draft and note two things Copilot changed that improved readability.",""),
 ("Save the file.",""),
 ],
 test="Your Sales Overview page shows a combined line-and-column month visual, a top-5 sorted region chart, a current-year page filter, currency formatting, and a tidy aligned layout.",
 troubleshooting=[
 "**Copilot changes the wrong visual.** Select the specific visual first, then prompt — Copilot acts on the selected visual. Name it in the prompt if there is any doubt.",
 "**The sort or top-N does not apply.** Re-state it explicitly ('sort descending by Sales Amount, keep top 5'); some visual types need the field in a specific well.",
 "**Currency format did not stick.** Set it directly on the field (Column tools > Format > Currency) as a fallback, then re-run the Copilot formatting prompt.",
 ],
 challenge="Ask Copilot to create a mobile-friendly version of the page, then open the Mobile layout view and check how the visuals reflow.",
 reflection="LO3 — Where did prompting Copilot work best, and where was it faster to adjust the visual by hand? What does that tell you about how to combine the two?",
 ),
 dict(
 num=6, topic=2,
 title="Add Narrative Visuals and AI Summaries with Storytelling and Formatting",
 objective="Add a Copilot narrative (smart) visual, generate an AI page summary, and apply storytelling and formatting best practice to the report.",
 desc="Numbers need words. In this lab you add a narrative visual that Copilot writes and keeps updated, "
 "generate an AI summary of the page for stakeholders, and then apply storytelling best practice — "
 "headline first, one question per visual, a clean reading order — so the AI-generated content looks "
 "deliberate and reads well. " + PROJECT_NOTE,
 build="A Sales Overview page with a Copilot narrative visual, a saved AI summary, and a storytelling layout ready to show stakeholders.",
 services="Power BI (Desktop or Service), Copilot pane, narrative/smart narrative visual, AI summary, formatting",
 steps=[
 ("On the Sales Overview page, add a narrative visual: Insert > Narrative (or ask Copilot to create it), so Copilot writes a text explanation of the page.",
  "Add a narrative visual that summarises the key sales trends on this page in three short sentences and updates as the data changes."),
 ("Read the narrative and check every claim against the visuals. Re-prompt if it overstates or misreads a trend.",
  "Rewrite the narrative to focus on the top region, the best-selling product, and the month-on-month trend."),
 ("Generate an AI summary of the whole page for a stakeholder who will not open the report.",
  "Summarise this page in five bullet points for a busy executive, leading with the single most important number."),
 ("Copy the AI summary into a text box on the page (or your notes) and label it clearly as an AI-generated summary you have reviewed.",""),
 ("Apply storytelling order: move the headline KPI to the top-left, arrange visuals so the eye travels left-to-right and top-to-bottom, and make each visual answer one question.",""),
 ("Apply formatting best practice with a final Copilot prompt.",
  "Give this page consistent titles, currency formatting, aligned spacing and a single colour theme so it looks professional."),
 ("Do a 60-second test: look away, look back, and check the page's main message lands in under a minute. Adjust the headline if it does not.",""),
 ("Save the file.",""),
 ],
 test="Your page has a Copilot narrative visual whose claims match the visuals, a reviewed AI summary labelled as AI-generated, and a clean storytelling layout that communicates its main message within a minute.",
 troubleshooting=[
 "**The narrative states something the charts do not show.** Re-prompt to focus on specific, verifiable points, and always read the narrative against the visuals before you keep it.",
 "**The narrative visual is not available.** Confirm the narrative/smart-narrative visual is enabled in your tenant; otherwise generate the text with a Copilot summary prompt and place it in a text box.",
 "**The summary is too long.** Ask Copilot to cap it ('in exactly five bullets, one line each') — precise limits produce tighter output.",
 ],
 challenge="Generate two summaries of the same page for two audiences — a finance lead and a store manager — and note how the emphasis should differ.",
 reflection="LO4 — Why does a good narrative or summary lead with the single most important number, and how does that change what a stakeholder takes away?",
 ),
]
