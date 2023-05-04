# Programming variability with Large Language Model-based assistant

We explore the role of large language model (LLM)-based assistants in addressing the *programming of variability*, which is essential for creating adaptable software systems capable of accommodating diverse contexts and requirements.
Managing the complexity that arises from having multiple features, variations, and possible configurations is known to be highly challenging for software developers.
We report on new approaches made possible with LLM-based assistants, such as: implementing features and variations through prompts; expanding variability using LLM-generated domain knowledge; and effortlessly incorporating variability across various artifacts, programming languages, and frameworks, as well as different binding times (either compile-time or run-time).

This repository contains:
 * prompts used for programming taks
 * sessions with different LLMs (or same prompts replicated with the same LLM)
 * generated code and instructions on how to use it (and computed results if any)
 * Github issues to discuss and review variability taks and sessions 
 
 We target at least three scenarios (that may involved different sub-tasks): 
 
 * variability implementations of a classical Hello world
   - `conditioncompilation-helloworld`
   - `featuretoggle-helloworld`: feature toggles in eg Java and JavaScript 
   - `helloworld-CLI`: CLI with eg Julia and Python 
 * variability for reproducibility and floating-points
   - `varyfloatC`: conditional compilation in C + Python generator 
   - `genpython4c` 
   - `generator-with-domainknowledge`
   - `conditionalcompilation-float-rust` 
 * transformation of an unfamiliar code with an end-user, Web-based customization tool
   - `varying-unfamiliarcode`: turning unfamiliar TikZ code into a configurable, visual system
   - `varyTikZ`: turning unfamiliar TikZ code into a configurable, visual system 
   - `varySVG`: turning unfamiliar SVG code into a configurable SVG 
   
 ![champanzeegrid](https://github.com/acherm/progvary-withgpt/blob/f75e6e06586d4e354983dd6456df4d49a15d6199/varyTikZ/crazychamps/grid.png)



Large Language Model (LLM) used: 
 * mainly ChatGPT4, ChatGPT3, ChatGPT3.5
 * Claude (Anthropic)
 * GPT3 (API, OpenAI)
 * Open Assistant (Huggingface)
 

 
 
