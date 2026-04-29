# AI-Driven Natural Language Processing Project

Task 3 submission for exploring and analyzing a language model in a Jupyter notebook.

## Project Overview

This project evaluates a compact GPT-style language model using Hugging Face Transformers and an optional LangChain wrapper. The notebook focuses on:

- Selecting a language model aligned with NLP exploration goals
- Implementing the model in a reproducible Jupyter notebook
- Testing the model on multiple prompt scenarios
- Evaluating context understanding, generation quality, limitations, and ethical considerations
- Summarizing findings and improvement opportunities

## Chosen LM

The notebook uses `distilgpt2`, a lightweight causal language model based on GPT-2. It was selected because it is small enough for student experimentation while still demonstrating core language-generation behavior such as continuation, style imitation, and prompt sensitivity.

## Folder Structure

```text
ai-driven-nlp-project/
|-- README.md
|-- requirements.txt
`-- lm_exploration_analysis.ipynb
```

## How to Run

1. Install the dependencies if needed:

   ```bash
   pip install -r requirements.txt
   ```

2. Open the notebook:

   ```bash
   jupyter notebook lm_exploration_analysis.ipynb
   ```

3. Run all cells from top to bottom.

## Research Questions

The notebook investigates:

- How well does the language model continue text across different prompt styles?
- Can the model preserve context from the prompt?
- How coherent and fluent are the generated responses?
- Where does the model struggle, especially on reasoning, factuality, and safety-sensitive prompts?
- How can prompt design improve the quality of responses?

## Main Findings

The analysis shows that compact GPT-style models can generate fluent text and respond well to creative prompts, but they may struggle with factual accuracy, precise reasoning, and strict instruction following. The project also highlights why model selection, prompt design, evaluation metrics, and ethical checks are important in practical NLP applications.