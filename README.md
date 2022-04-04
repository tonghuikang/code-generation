# Code Generation Experiments

I hope to explore ways I can do AI-augmented programming. Maybe one day I can get first place in a Leetcode contest with this tool.


### Introduction

Here I experiment with code generation with a language model.

A language model is trained to predict the next word given the previous words generated.
If you are able to produce the next word, you understand the language - this is the intuition behind the language model.

How to use language models to generate content seems to be an active field of study. Here I am trying to generate code that can be used to pass coding challenges.


## Todo

These are some things I can explore.


### Tasks

- Given a Python code that solves a competitive programming problem, write C++ code that also solves the problem. I have experimented with this and it [looks pretty successful](https://codeforces.com/blog/entry/101435). It might help me in cases where my code complexity and implementation is correct but the language is too slow. Till now, I have not really learned how to write C++.

- Given the programming challenge task, write working code that solves the problem. For the known problems, the model can predict the solution [quite well](https://www.youtube.com/watch?v=Kv_E0tUTo2Y) since the model basically memorizes the solution from the training set. For unknown problems, [AlphaCode](https://www.deepmind.com/blog/competitive-programming-with-alphacode) only performs as well as an [average competitor](https://codeforces.com/blog/entry/99566) on Codeforces. I think the model may be able to do well on Leetcode contest problems, which are much simpler although the problems are supposed to be novel.


### Challenge Preparations

- Leetcode. I want to build a procedure to automate my participation in the contest. I can field test this on virtual contests for this as well. I do not intend to host Leetcode content here.
- Contest tool. 
- [Codeforces API](https://codeforces.com/apiHelp). Codeforces exposes an API that allows me to download solutions from a user.
- Contest parser. In the contest, I have been using [Competitive Companion](https://chrome.google.com/webstore/detail/competitive-companion/cjnmckjndlpiamhfimnnjmnckgghkjbl). Having the input and output as well can at least ensure that my code compiles.
- [yosupo Library Checker](https://judge.yosupo.jp/). These are standard problems with techniques and algorithms that a competitive programmer should know. I have never used it, I am not sure if there is an API exposed for me to download and submit solutions.


### Engineering

- Make use of OpenAI API to generate code so that I do not need to copy the code to their console every time. I probably will not be finetuning the model, but working on the intuition on how the model behaves so that I can make the best out of the model.


### Optimisation

- Problem formatting. For the task to solve a problem, I need to format the question in a way that the model understands.
- Prompting. The language model is operated with prompts. I need to experiment with various ways to prompt the model to write. For example, I could use some prewritten to guide the coding style.
- Templates. By prompting the model with vetted function and class templates, we can encourage the model to make use of the template to simplify the solution logically.
- Output modification. For example, discourage the model from defining functions or generating useless code even though such prediction is the most probable.
- Generating test cases. I might want to generate input cases with the model so that I can ensure that the code does not break even if running on valid small input.
- Code pruning. Probably we can use methods to identify unused variables and logic and prune them.
- Re-generation of code on errors. If there is an error at a certain part of the code, probably I can rerun it.


## Installation and usage

To be updated.
