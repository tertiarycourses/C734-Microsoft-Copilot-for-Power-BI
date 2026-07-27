# Lab 8 — Set Up Q&A and Natural-Language Queries

**Topic 03:** AI-Assisted Data Modeling and Analysis  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Copilot for Power BI (C734)

## Scenario

Contoso Coffee is a growing coffee retailer with cafes across several regions. You are the business analyst: every week you are asked for the sales numbers — by region, by product, by channel, by month — and every week you rebuild the same charts by hand. Across this course you use Copilot in Power BI to build a Sales & Operations dashboard that drafts those pages, visuals, measures and summaries for you, always under your review. Use this scenario only if you cannot use a real dataset from your own workplace; your own data is always preferred.

## Goal

Add a Q&A visual, ask natural-language questions of the model, and improve accuracy by teaching Q&A synonyms and reviewing suggested questions.

## What you'll build

A working Q&A experience on your report: a Q&A visual, tested natural-language questions, and synonyms and suggested questions configured for accuracy.

**Tools and techniques:** Power BI (Desktop or Service), Q&A visual, natural-language queries, Q&A setup (synonyms, suggested questions), Copilot

## About this lab

Q&A lets anyone ask the report a question in plain English and get an instant visual. In this lab you add a Q&A visual, ask several questions, then improve the answers by teaching Q&A the words your business actually uses (synonyms) and curating the suggested questions — so a non-technical user gets the right answer first time. BUILDING BLOCK — what you build in this lab is added to your Contoso Coffee report, the single connected dashboard you assemble across all 9 labs.

## Steps

### Step 1

On a new page named Ask the Data, insert a Q&A visual (Insert > Q&A, or ask Copilot to add one).

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Add a Q&A visual to this page so users can ask questions about Contoso Coffee sales in natural language.
```

### Step 2

Type a natural-language question and watch Q&A build the answer visual.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
sales amount by region last quarter
```

### Step 3

Ask two more, changing the wording, to test how Q&A interprets business language.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
top 5 products by total sales this year
```

### Step 4

Find a question Q&A answers poorly because of wording, then teach it a synonym so business terms map to the right field (Modeling > Q&A setup > Field synonyms — for example map 'revenue' and 'takings' to Sales Amount).

### Step 5

Re-ask the question using the business word you just mapped and confirm Q&A now answers correctly.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
revenue by channel this year
```

### Step 6

Curate the experience: in Q&A setup, review the suggested questions and add three good starter questions users are likely to ask.

### Step 7

Use Copilot to propose questions this dataset can answer, and add the best to your suggested questions.

Prompt to give Copilot (type or paste it into the Copilot pane):

```text
Suggest five natural-language questions a store manager could ask this Contoso Coffee dataset.
```

### Step 8

Save the file. Your report now answers plain-English questions accurately.

## Test it

Your report has a Q&A visual that correctly answers at least three natural-language questions, including one that only works because you added a synonym, plus three curated suggested questions.

## Troubleshooting

- **Q&A says it does not understand a word.** Add it as a synonym in Q&A setup so it maps to the correct field, then re-ask.
- **Q&A returns the wrong field.** Two fields share similar terms — tighten the field names or add synonyms so the business term maps to exactly one field.
- **No suggested questions appear.** Add them manually in Modeling > Q&A setup > Suggested questions; a blank Q&A box is intimidating to first-time users.

## Challenge

Turn off a synonym you added and re-ask the question to see Q&A fail, then turn it back on — a concrete demonstration of why Q&A setup matters.

## Reflection

LO6 — Why does teaching Q&A your business's synonyms matter more for non-technical users than for you, the report author?

## Deliverable

Save your output — it becomes part of your **Contoso Coffee report**, the single connected project you assemble across all 9 labs and complete in Lab 9.

---

*Copilot for Power BI (C734) · C734 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
