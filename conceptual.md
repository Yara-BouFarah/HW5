## 1. Use Case

New York City officials want to identify whether residents in different zip codes receive different levels of service when submitting 311 complaints. A useful data science application would be a dashboard that compares complaint response times across locations. City leaders could use this information to identify areas where complaints consistently take longer to resolve and investigate whether staffing, resources, or operational processes need to be adjusted.

## 2. Refining the Data Science Question

Initial question: "We'd like to understand how much characters talk across the My Little Pony series."

### Step 1: Clarify what is being measured
What does "how much characters talk" mean?
Refinement: "How many lines of dialogue does each character speak across the My Little Pony series?"

### Step 2: Define the population
Which characters and which episodes are included?
Refinement: "How many lines of dialogue are spoken by each character across all episodes represented in the dataset?"

### Step 3: Define the measurement

Raw counts can be affected by the total number of dialogue lines, so we can measure each character's share of all dialogue.
Refinement: "What percentage of all spoken dialogue lines in the dataset is attributed to each character?"

### Final data science question
"What percentage of all spoken dialogue lines across the My Little Pony episodes in the dataset is spoken by each character?"

## 3. State Maintenance in Jupyter

State maintenance is difficult in a Jupyter notebook because cells can be executed in any order. Variables and objects remain stored in the running kernel, so a cell may depend on code that was executed earlier even if that code appears later in the notebook. This can make a notebook appear to work in one session but fail when the kernel is restarted and the notebook is executed from top to bottom.

## 4. Jupyter vs. README

A Jupyter notebook can be better than a README for sharing a data science project because it combines executable code, explanations, outputs, tables, and visualizations in one document. Another data scientist can follow the analysis step by step, inspect intermediate results, and rerun or modify the code. A README is useful for documentation and instructions, but it normally does not provide the same interactive and reproducible view of the analysis.
