# How to sequence your own DNA at home

Source: https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home

## Summary
The article is a hands-on protocol guide by someone who has sequenced their own genome five times using an Oxford Nanopore Technologies MinION device. It walks through the full end-to-end process of at-home DNA sequencing — from collecting cheek cells, through lab prep and library preparation, to running the sequencer and analyzing variants. The author also covers what you can actually do with your genome data once you have it, including drug metabolism analysis and querying variants through bioinformatics tools.

## Key takeaways
- **It's technically possible but expensive:** The MinION sequencer alone costs $7,500, plus hundreds more in lab equipment and consumables — currently out of reach for most people, though costs are falling.
- **Cheek swabs are the sample source:** Buccal cells are easy to collect and replenish, but are not suitable for diagnosing cancer or tissue-specific gene expression.
- **The protocol has ~26 steps:** The workflow covers cell collection, DNA extraction (NEB Monarch kit), library prep (end-repair, adapter ligation, AMPure cleanup), flow cell loading, sequencing with MinKNOW, basecalling with Dorado, alignment with minimap2, and variant calling with Clair3.
- **The genome is a reference layer, not a diagnosis:** The resulting VCF file can be queried through tools like VEP, ClinVar, PharmGKB, and gnomAD to identify variants, flag drug metabolism differences, and find rare variants — but it is not yet clinical-grade.
- **AI integration is part of the workflow:** The author explicitly designed the protocol to be read by AI (e.g., paste the URL into ChatGPT), and suggests feeding your genome data to Claude Code or similar agents for interactive analysis.
- **A pause point exists after DNA extraction:** The best stopping point is after measuring DNA concentration — purified DNA can be stored at 4°C and library prep resumed later.
- **The future vision is real-time biosensing:** The author frames this as an early step toward integrating DNA, RNA expression, and biosensor data into a unified personal health model.