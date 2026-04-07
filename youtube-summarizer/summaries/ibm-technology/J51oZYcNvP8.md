# What is Multimodal AI? How LLMs Process Text, Images, and More

Video ID: `J51oZYcNvP8`

## Summary
The video defines multimodal AI as models capable of ingesting and/or generating multiple data modalities, such as text, images, and audio, going beyond single-modality Large Language Models. It contrasts older "feature-level fusion" approaches, which bolted separate models together, with the modern "native multimodality" that processes all data types within a unified shared vector space. This native approach allows for simultaneous reasoning across modalities, improved understanding, and coherent "any-to-any" generation capabilities.

## Key insights
-   **Multimodal AI** enables models to process and/or generate multiple data modalities (e.g., text, images, audio, LIDAR), extending capabilities beyond single-modality LLMs.
-   **Early systems used a modular "feature-level fusion" approach**, where separate models (like a vision encoder and an LLM) extracted features (numerical representations) from one modality and passed them to another. This method risks information loss as the LLM only receives a summarized description, not the raw data.
-   **Native multimodality** is the current gold standard, processing different data types by tokenizing and embedding them into a **shared vector space**. This allows the model to reason about all modalities simultaneously, as they exist in the same conceptual space, reducing information loss.
-   In a shared vector space, semantically similar items across modalities (e.g., an image of a cat and the word "cat") are positioned closely, fostering coherent understanding.
-   For **video**, native multimodal models use **spatial-temporal patches (3D cubes)** instead of 2D pixel patches, embedding motion and temporal sequences directly into the tokens. This means motion is "baked in" rather than inferred from comparing individual frames.
-   Native multimodal AI supports **"any-to-any" generation**, meaning the model can take any combination of input modalities and generate any combination of output modalities (e.g., text input leads to text and video output), all coherently linked within the shared vector space.