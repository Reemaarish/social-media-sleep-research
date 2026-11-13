# Night-time Social Media Use and Sleep Duration

Reproducible research project exploring the association between night-time
social media use and average sleep duration among undergraduate medical students.

## Project contents
- `Analysis_Preregistration.docx`: retrospective analysis plan.
- `analysis.py`: reusable data-cleaning and Spearman-correlation functions.
- `test_pipeline.py`: test using fully synthetic example data only.
- `requirements.txt`: pinned Python package versions.

## Privacy
**Do not upload the original survey Excel file or any participant-level data to
this public repository.** Keep the original dataset stored privately. The test
uses invented synthetic values and does not contain real participant records.

## Setup
Use Python 3.10 or newer. In a terminal, run:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Using the analysis functions
Confirm the exact column names and units in the private dataset first. Then
load the private data locally and call `run_spearman(data, predictor_column,
outcome_column)` using the verified column names. Do not commit the dataset.

## Important note
The preregistration is explicitly retrospective because the dataset had already
been accessed. Record any changes to the planned variables, exclusions, or
analysis in the repository.
