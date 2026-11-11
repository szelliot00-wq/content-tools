# What Is Model Distillation? How Smaller AI Models Learn

Video ID: `4uvq8Cz3A7Y`

## Summary
This video explains model distillation, the technique of transferring knowledge from a large "teacher" AI model to a smaller "student" model. It covers why smaller models matter (speed, cost, deployability), how large language models generate probability distributions over possible outputs, and how distillation leverages those distributions — called soft labels — to train the student more effectively than using ground-truth labels alone. The core concept of "dark knowledge" is introduced to explain why soft labels carry richer information than hard labels.

## Key insights
- **Model size = parameter count.** Fewer parameters means less memory, lower latency, reduced cost, and the ability to run on constrained hardware like phones or laptops.
- **Teacher vs. student framing.** The large model (teacher) is trained first on hard labels; the smaller model (student) then learns by imitating the teacher's outputs rather than starting from scratch.
- **LLMs output probability distributions, not single answers.** At every token step, a model assigns likelihoods to every word in its vocabulary — this full distribution is what distillation exploits.
- **Hard labels vs. soft labels.** Hard labels say only what's correct (100% for one token, 0% for all others). Soft labels from the teacher encode *degrees* of correctness across all candidates.
- **Dark knowledge is the key advantage.** Soft labels reveal relationships between possible answers (e.g., "coffee" is a reasonable next word, "shoe" is not) that are invisible in hard labels. This richer signal lets the student learn more efficiently.
- **There is an inherent trade-off.** The student is faster and cheaper but rarely matches the teacher's full capability — the goal of distillation is to close that gap as much as possible.
- **Distillation is not LLM-specific.** The technique applies broadly to other types of models, not just language models.