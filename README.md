# NICAR26: Extracting data from PDFs using command-line and other advanced tools

This repo contains the code and tipsheet for the
[_"Extracting data from PDFs using command-line and other advanced tools"_](https://schedules.ire.org/nicar-2026/#/session/1251)
class at [NICAR26](https://www.ire.org/training/conferences/nicar-2026/),
happening on Friday, March 6th 2026 from 2:30-3:30pm.


**[SLIDES HERE](https://docs.google.com/presentation/d/1st4PVMcM-vBEnT2WHQkfduB7AKY6k9qnEk4fx2ZbJI0/edit?usp=sharing)**


## General Overview

- [pdfplumber](https://github.com/jsvine/pdfplumber) for text-based PDFs (CLI, Python, table extraction, etc.)
- OCR with [tesseract](https://github.com/tesseract-ocr/tesseract) and [OCRMyPDF](https://github.com/ocrmypdf/OCRmyPDF)
- [structured outputs with vision LLMs](https://openrouter.ai/docs/guides/features/structured-outputs) for extracting structured data from image/text PDFs

## Running this session on your own laptop

Git clone this repository:

```bash
git clone https://github.com/asg017/nicar26-pdf
```

Then `cd` into the repo and install Python dependencies. I heavily recommand [using `uv`](https://github.com/astral-sh/uv), which you can use like so:

```bash
cd nicar26-pdf/
uv sync
```

In this class we're using [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to run the notebooks!


## Sample PDFs

| Path | Source |
| ---- | ------ |
| [`samples/manafort.pdf`](samples/manafort.pdf) | [link](https://github.com/chadday/nicar_ocr/blob/master/files/manafort/Manafort_filing.pdf)
| [`samples/ca-warn-report.pdf`](samples/ca-warn-report.pdf) | [link](https://github.com/jsvine/pdfplumber/blob/stable/examples/pdfs/ca-warn-report.pdf)
| [`samples/ca-campfin-contributions.pdf`](samples/ca-campfin-contributions.pdf) | [link](https://www.southtechhosting.com/WhittierCity/CampaignDocsWebRetrieval/)
| [`samples/ca-campfin-contributions-handwritten.pdf`](samples/ca-campfin-contributions-handwritten.pdf) | [link](https://www.southtechhosting.com/WhittierCity/CampaignDocsWebRetrieval/)
