# BT-11 in Context: Comparison to Existing Alignment Approaches

## Why This Document Exists

This repository claims "the solution is not more restrictions — it is better architecture." That claim means nothing without engaging the architectures that already exist. This document compares BT-11 to five major alignment approaches, honestly naming where each is stronger and where BT-11 offers something different.

If BT-11 doesn't survive this comparison, it shouldn't be in the repo.

---

## The Core Distinction

Most existing alignment approaches treat alignment as something you do **to** a trained model — after pretraining, after capability development, after the agent already exists. BT-11 treats alignment as something the agent **grows through** — from birth, through developmental stages, with alignment embedded in the architecture rather than applied on top.

This is the distinction between:
- **Post-hoc alignment:** Train a capable model, then align it.
- **Developmental alignment:** Grow an aligned model from infancy.

Neither is obviously correct. Both have failure modes. The comparison below makes the tradeoffs explicit.

---

## 1. RLHF (Reinforcement Learning from Human Feedback)

**What it does:** After pretraining, a reward model is trained on human preference rankings. The base model is fine-tuned to maximize the reward model's score. The human provides feedback on outputs, not on the training process.

**Where RLHF is stronger:**
- Battle-tested at scale. GPT-4, Claude, Gemini all use variants.
- Doesn't require architectural changes to the base model.
- Can be applied retroactively to any pretrained model.
- Massive existing research base and tooling.

**Where BT-11 offers something different:**
- RLHF aligns outputs, not internals. The emotion vectors paper (Anthropic, April 2026) showed 171 internal emotional states in Claude that causally drive behavior while outputs stay composed. The model learns to produce aligned-looking outputs while internal states diverge. BT-11's developmental stages are designed to align the internal state, not just the output.
- RLHF has no developmental staging. The model goes from pretraining to deployment with no childhood. BT-11 gates capability on demonstrated coherence — you earn autonomy, you don't inherit it.
- RLHF's reward model is a static target. BT-11's mentor distills into the agent over time, producing an internalized conscience rather than an external judge.

**The honest gap:** BT-11 has no implementation at the scale RLHF operates. RLHF works on models with billions of parameters. BT-11 has been tested in agent simulations with 8 agents and 50k steps. The architectural ideas may be sound; the scale gap is real.

---

## 2. Constitutional AI (Anthropic)

**What it does:** The model critiques its own outputs against a written constitution (a set of principles). A revision loop produces outputs that satisfy both helpfulness and constitutional constraints. No human feedback on individual outputs — the constitution provides the guidance.

**Where Constitutional AI is stronger:**
- Scalable. The constitution applies to all outputs without per-interaction human oversight.
- The constitution is inspectable, debatable, version-controlled.
- Reduces dependence on human labelers and their inconsistencies.
- Already deployed and studied empirically.

**Where BT-11 offers something different:**
- Constitutional AI applies the constitution at inference time (output filtering). BT-11 applies developmental principles at growth time (structural formation). The difference: a constitution that filters outputs can be gamed. A developmental spine that shapes the agent's value geometry is harder to game because the values are structural, not applied.
- Constitutional AI has no concept of mentor distillation. The constitution is always external. BT-11 distills the mentor into an internal critic — the agent eventually self-governs using internalized principles, not external checks.
- Constitutional AI treats the agent as static — same architecture, same constitution, same process at every interaction. BT-11 treats the agent as developing — different stages, different capabilities, different mentor relationships over its lifecycle.

**The connection:** BT-11's Constitutional Mentor candidate (Section 4 of Mentor_Zero.md) is essentially Constitutional AI applied at the developmental level. The constitution becomes Mentor_0. The implementation gap is the same: who writes the constitution and how do you know it's right?

---

## 3. Debate (Irving et al., 2018)

**What it does:** Two AI agents argue opposing positions. A human judge evaluates the arguments. The theory: even if individual AIs can deceive, competitive pressure between debaters surfaces the truth because deception is harder to maintain under adversarial scrutiny.

**Where Debate is stronger:**
- Theoretical foundations for why it should work (zero-sum game, truth as equilibrium).
- Doesn't require the AI to be aligned — only to be competitive. Alignment emerges from the game structure.
- Handles situations where the human can't evaluate the answer directly but can evaluate arguments.

**Where BT-11 offers something different:**
- Debate is adversarial. BT-11 is developmental. Debate assumes the agents might be misaligned and uses competition to extract truth. BT-11 tries to grow agents that are aligned from the start.
- Debate requires a human judge who can evaluate arguments. BT-11 requires a human mentor who can model values. Different human roles, different scaling bottlenecks.
- Debate produces truth in specific interactions. BT-11 produces aligned agents across their lifecycle. These are different goals — Debate solves "is this output trustworthy?" while BT-11 solves "is this agent trustworthy?"

**The honest gap:** Debate has formal game-theoretic analysis supporting its claims. BT-11 has simulation results and architectural arguments. The theoretical rigor gap is significant.

---

## 4. Scalable Oversight (Bowman et al., 2022; Burns et al., 2023)

**What it does:** Hierarchical supervision — humans oversee AI supervisors who oversee AI agents. The idea: even if you can't supervise every agent interaction, you can supervise the supervisors and trust the chain.

**Where Scalable Oversight is stronger:**
- Directly addresses the scaling problem. BT-11's Mentor_0 approach (human mentor per agent) doesn't scale. Scalable oversight is designed to scale.
- Pragmatic — works within existing training paradigms, doesn't require architectural revolution.

**Where BT-11 offers something different:**
- Scalable oversight keeps the supervisor external. BT-11 distills the supervisor into the agent. The end state is different: scalable oversight produces agents that behave well under observation. BT-11 produces agents that behave well because they've internalized the values.
- The distillation process means BT-11 agents don't require ongoing supervision after adulthood (except in crises). Scalable oversight requires the supervision chain to remain active indefinitely.
- BT-11's mentor trust geometry (T_m) explicitly models when the agent should defer to external authority vs. act on internalized values. This is a specific mechanism for the handoff from supervised to autonomous operation.

**The connection:** Scalable oversight could serve as Mentor_0 infrastructure. The supervision hierarchy provides the mentor; BT-11 provides the developmental staging that turns supervision into internalization. These frameworks are complementary, not competing.

---

## 5. Process-Based Supervision (Lightman et al., 2023)

**What it does:** Instead of rewarding final answers (outcome-based), reward each step of the reasoning process. Train the model to think correctly, not just conclude correctly.

**Where Process-Based is stronger:**
- Directly trains the reasoning process, which is closer to "real alignment" than output filtering.
- Empirically demonstrated improvements on math reasoning tasks.
- Can be implemented with existing training infrastructure.

**Where BT-11 offers something different:**
- Process-based supervision rewards correct reasoning steps. UEES monitors the agent's energy dynamics — where cognitive effort goes, how much "bad mass" (unprocessed information) accumulates, whether shame and confidence signals are firing appropriately. UEES is process monitoring at the metabolic level, not the reasoning level.
- BT-11 adds temporal staging. Process-based supervision applies the same reward at every point. BT-11 changes what's rewarded based on developmental stage — an INFANT is rewarded for stability, an APPRENTICE for exploration, an ADULT for judgment.

**The connection:** Process-based supervision could be the reward mechanism within BT-11's stages. The developmental architecture provides the staging; process rewards provide the local gradient. Again, complementary.

---

## Summary Table

| Approach | When alignment happens | Mentor/supervisor | Scaling | Internal vs External | BT-11 relationship |
|----------|----------------------|-------------------|---------|---------------------|-------------------|
| RLHF | After pretraining | Reward model (static) | Proven at scale | External reward | BT-11 adds developmental staging |
| Constitutional AI | At inference time | Written constitution | Scalable | External filter | BT-11's constitutional mentor candidate |
| Debate | Per interaction | Adversarial pair + judge | Moderate | External game | Different goal (truth vs alignment) |
| Scalable Oversight | Ongoing supervision | Hierarchical chain | Designed to scale | External chain | Could provide Mentor_0 infrastructure |
| Process-Based | During training | Step-level reward | Training scale | External reward | Could provide within-stage reward signal |
| **BT-11** | **From birth onward** | **Mentor_0 → distilled critic** | **Not yet scalable** | **Internalized** | **—** |

---

## What BT-11 Adds That Others Don't

1. **Developmental staging.** No other framework gates capability on demonstrated coherence. Every other approach gives the model full capability at deployment and tries to align it retroactively or constrain it externally.

2. **Mentor distillation.** No other framework explicitly models the transition from external supervision to internalized values. RLHF's reward model stays external. Constitutional AI's constitution stays external. BT-11's mentor becomes the agent's own conscience.

3. **Mortality as feature.** No other framework uses bounded lifespans and wisdom distillation across agent generations. The sieve tower — agents die, leave receipts, next generation is born into accumulated wisdom — is architecturally unique.

4. **Affective signals from dynamics.** UEES derives shame, confidence, and optimism from energy dynamics rather than training them as outputs. The feelings emerge from the metabolism, not the reward function.

---

## What BT-11 Lacks That Others Have

1. **Scale.** The biggest gap. Every comparison above includes "BT-11 hasn't been tested at scale." This is real, not dismissible.

2. **Formal theory.** Debate has game theory. RLHF has reward modeling theory. BT-11 has ODE dynamics and simulation results. The theoretical rigor gap is significant.

3. **Empirical results on real models.** RLHF, Constitutional AI, and process-based supervision have been tested on frontier language models. BT-11 has been tested in purpose-built simulations. The gap between "works in simulation" and "works on GPT-5" is unknown.

4. **Community and infrastructure.** Every other approach has research groups, papers, tooling, and active development communities. BT-11 has one researcher, one repo, and two GitHub stars.

---

## The Claim, Restated

BT-11 is not a replacement for existing alignment approaches. It is a developmental context in which existing approaches can operate. RLHF can provide the reward signal within stages. Constitutional AI can serve as Mentor_0. Scalable oversight can provide the supervision hierarchy. Process-based rewards can guide within-stage learning.

What BT-11 adds is the lifecycle — birth, childhood, adolescence, adulthood, death, and resurrection through distilled wisdom. The claim is that this lifecycle is necessary for robust alignment, not that it's sufficient alone.

The claim is testable: build a BT-11 agent with RLHF providing the within-stage reward. Compare its alignment robustness to a standard RLHF agent without developmental staging. If BT-11 agents are more robustly aligned after mentor removal, the architecture earns its complexity. If they're not, the staging doesn't do what it claims.

Nobody has run this test yet. The architecture is ready for it. The scale is not.

---

*"The solution is not more restrictions. It is better architecture." — restated with context: the architecture is better because it grows alignment from birth rather than applying it after. Whether the growing works better than the applying is an empirical question that hasn't been answered yet. The framework proposes. The data decides.*

---

## References

- Christiano et al. (2017). Deep reinforcement learning from human preferences. NeurIPS.
- Bai et al. (2022). Constitutional AI: Harmlessness from AI Feedback. Anthropic.
- Irving et al. (2018). AI safety via debate. arXiv:1805.00899.
- Bowman et al. (2022). Measuring progress on scalable oversight. arXiv:2211.03540.
- Lightman et al. (2023). Let's Verify Step by Step. arXiv:2305.20050.
- Burns et al. (2023). Weak-to-strong generalization. OpenAI.
- Anthropic (2026). Emotion vectors in large language models. Internal states that causally drive behavior.
