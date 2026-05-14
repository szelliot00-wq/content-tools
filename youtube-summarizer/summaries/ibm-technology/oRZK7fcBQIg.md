# LLMjacking: How hackers steal your AI API keys and stick you with the bill

Video ID: `oRZK7fcBQIg`

## Summary
This episode of IBM's Security Intelligence podcast covers two major cybersecurity topics: LLM jacking (the theft of AI API keys by threat actors) and the role of AI in adversary simulation and offensive security. Panelists from IBM X-Force discuss how stolen API keys can lead to massive financial losses and enable malicious AI use, while also exploring whether AI can and should accelerate patching timelines. The conversation emphasizes that human oversight remains critical even as AI transforms both offensive and defensive security practices.

## Key insights
- **LLM jacking is a financially devastating attack**: A real-world example showed hackers running up $82,000 in charges in 48 hours using a stolen Gemini API key, compared to the victim's normal $180/month spend.
- **Stolen API keys enable more than financial harm**: Threat actors can use stolen credentials to access frontier AI models for malicious R&D, weapon-building, and research — bypassing access restrictions that AI providers have put in place.
- **Treat AI API keys like crown jewels**: Store them in secrets managers, never in public GitHub repositories or plain variables, and apply strict access controls.
- **Cloud environments are insecure by default**: Organizations must actively configure security controls, not assume default settings are safe, especially within DevOps pipelines.
- **Guard rails on AI spending need improvement**: Even with usage caps in place, attackers can exhaust limits before detection systems respond, highlighting a gap that providers need to address.
- **AI is evolving resource hijacking**: From early botnet abuse to crypto mining to LLM jacking, attackers consistently find ways to exploit others' computing resources for profit and operational advantage.
- **Humans must remain in the AI security loop**: Whether in threat intelligence, incident response, or adversary simulation, AI lacks the contextual judgment, accountability, and chain-of-custody awareness that human experts provide.
- **"AI is only as good as you are"**: The effectiveness of AI tools in security depends heavily on the expertise and guidance of the people deploying them.
- **Adversary simulation must reflect AI-augmented attackers**: Red teams should model all phases of an attack where AI can be applied, not just vulnerability discovery, as threat actors are already doing this.
- **Shortening patch windows to 3 days may be the wrong question**: Patching is just one layer of defense; organizations should prioritize defense-in-depth, network visibility, and assumed breach posture over arbitrary timeline targets.
- **Assume breach mentality is essential**: Organizations that respond best are those that plan and practice for inevitable compromise rather than assuming their controls will hold.
- **Preparation is the ultimate defense**: As summarized with a JFK quote — "The best time to fix your roof is when the sun is shining" — proactive incident response planning and environment awareness are key.