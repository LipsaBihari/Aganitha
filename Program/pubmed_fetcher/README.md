# PubMed research paper fetcher

Hello! Welcomes to the PubMed Research Paper Fetcher. Based on any search you have in mind, this fantastic command-line utility helps you locate research papers on PubMed. It is intended to filter the results and display only the papers with at least one author affiliated with a biotechnology or drug firm. Furthermore, you can quickly store the output to a CSV file or review it directly in your terminal.
While making this project I took help of Chatgpt to fix module imports, improve CLI structure using poetry and also make a cleaner filtering logic of non-academic authors. The LLM was used as a development assistant, giving suggestions,debugging support,and finding ways to improve the code's efficiency. I implemented decisions that were based on the projects needs.

Project Layout

This project's arrangement is as follows:

pubmed_fetcher/

Pyproject. toml

README. md

src/

pubmed fetcher:

fetcher. py; This is where the API and filtering witchcraft begins.

utils. py Some useful helper functions

cli/

main. py # The command-line interface

__init__. py

exams/

Optional tests to ensure that everything runs smoothly: test_fetcher. py

Installing and Carrying Out

Managing everything with **[Poetry](https://python-poetry.org/)** is the aim of this project; therefore, lets get you started!

Step 1: Install Poetry if you haven't already.

You may get Poetry using: should you not already have it loaded on your machine:

```bash

poetry pip install

Step 2: Install Dependencies

Go to your project directory and execute once you have Poetry:

```bash

poetry set

Stage 3: Execute the CLI Tool

Now you're all prepared to use the tool! Simply type:

```bash

run poetry get-papers-list "your query"

Would you wish to store the outcomes to a CSV file?

Not a problem! Simply accomplish this:

bash

poetry runs get-papers-list"alzheimers clinical trial" -f results. csv

Require debugging information?

One approach to activate debug mode is as follows:

```bash

Poems run Get- papers- list for "covid vaccine" -d

CLI Options

Here's a brief overview of your options:

| Flag | Description

Your PubMed search term is necessary.

| `-f`, `--file` | (Optional) Output the results to a csv file.

| `-d`, -- debug ; Show extra debug info (optional)

Output Style

Every result you get when you execute the tool—whether you preserve it as a CSV or see it in the console—

- **PubmedID**: the paper's unique identifier.

- **Title**: The title of the research paper

- The publication date is the one when it was released.

- Authors from industry: names

Names of businesses connected with the authors under "Company Affiliation(s)"

- **Corresponding Author Email:** You will get the email of the corresponding author, if it is available.

Tools and Libraries

The following are the libraries and tools supporting this all:

| Tool / Library | Goal | Link

| `requests` | For sending HTTP requests to the PubMed API; [requests](https://pypi.org/project/requests/)

| `pandas` | For data management and CSV production

| Built-in Python library for parsing command-line arguments | [argparse](https://docs. python.org/3/library/argparse. html)

| `Poetry` | For arranging dependencies and packaging | [Poetry](https://python-poetry.org/) |

| Entrez E-Utilities | The PubMed API for retrieving medical data | [Entrez E-Utilities]

How It Operates

1. Run the command-line interface with your PubMed query first.

2. Using the Entrez API, the software searches and obtains relevant research papers.

3. By verifying their associations (like colleges and hospitals), it eliminates entirely academic authors.

4. **Output**: You have two options:

- Store the results in a `. csv` file.

- Print them beautifully to your terminal.

Required Included

- Save your results in CSV format easily.

- **Filter for Pharma/Biotech Writers**: Pay attention to the authors who count.

- Handle faulty queries and missing information gracefully using error handling.

- Optional debug output for troubleshooting via "Debug Mode".

- Modular Project Organization: Well-arranged code for simple maintenance.

- Extensive tool documentation and directions are contained in a thorough README.

license

Feel free to fork it, modify it, tear it, or repair it under MIT License. It belongs to you to play with.

Keep-er

Lipsa Rani Bihari

[lipsabihari08@gmail.com]
