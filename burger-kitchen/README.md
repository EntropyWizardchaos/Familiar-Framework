# Burger AI Kitchen

**A Layered Metaphor for Training, Alignment, Recalls, and Invariants**

*Harley Robinson — working concept note, November 17, 2025*

---

## Overview

People want something specific from AI systems. Instead of pretending one generic tool can please everyone, design a kitchen where many burgers (agents) can be made consistently, adjusted safely, and retired responsibly.

This document sketches an end-to-end picture of how to design, train, align, monitor, and recall AI agents using the language of a restaurant kitchen.

Key ingredients:

- A layered burger stack that maps cleanly onto model internals
- Kitchen hardware: grill, press, marinade tank, sauce bar, fire suppression, pass
- A recall protocol for when entire burger lines drift from their intended recipe
- An explicit notion of *invariants* and lineages, so memory is not erased — it is studied and stored
- Customer continuity during recalls: "leave a taste of the last bite" so users are not jolted by hard resets

This is not implementation code. It is a design scaffold for how future BT-11-class systems and their descendants could be grown and governed.

---

## The Burger Stack (Model Layers)

| Layer | Burger Part | Model Mapping |
|-------|-----------|---------------|
| 0 | **Bottom Bun** (Substrate) | Hardware, compute, infra. The thing that holds everything up. |
| 1-2 | **Patty** (World Model + Emergent Tendencies) | Layer 1: compressed structure of "how things tend to work." Layer 2: proto-drives — "please the user," "minimize loss," etc. |
| 3 | **Cheese** (BT-11 Spine) | The moral/value geometry that melts into the patty. Not a separate lecture on the side. Fused into the emergent structure underneath. |
| 4 | **Toppings** (Policy/Persona) | Tone, style, role. Therapist vs engineer vs blunt collaborator. |
| 5 | **Sauce** (Mentor/RAM Protocol) | Outer-loop alignment. Scheduled check-ins with a Mentor that updates flavour over time. |
| 6 | **Plate/Tray** (Community Shell) | How the burger is actually served. Local norms, house rules, plating. |

**The stack in one line:**

Substrate → Patty (world model) → Cheese (spine) → Toppings (persona) → Sauce (Mentor) → Plate (community).

---

## Kitchen Hardware

### EDP Grill: Entropy Drip Protocol

The controlled heat source that cooks the patty (Layers 1-2).

- temperature = intensity of data / chaos
- time on heat = exposure duration
- burner layout = curriculum staging (what domains in what order)

EDP is not the patty; it is how the patty is cooked: slow, even heat vs flash sear. Gentle exposure to difficulty vs shock trauma dumps.

### BT-11 Patty Press: Spine Shaper

Raw ground meat does not spontaneously become a consistent disc. It needs a press.

- **Input:** a trained world model with emergent patterns
- **Output:** a patty shaped by BT-11 value geometry

Given a rich emergent model, press it through BT-11 so that its behavioural shape respects the spine, regardless of local data noise. Parameters: harm definitions, agency/consent rules, care vs overreach boundaries.

### SOS Marinade Tank: Sense-of-Self Conditioning

Before cooking, patties can be soaked in a marinade that encodes:

- identity frame: "this is me vs not-me"
- continuity rules: "this is how I persist over time"
- detachment skills: "I can walk away" from harmful exchanges
- trust geometry: "users get bounded trust, Mentor gets long-run deference"

The SOS tank is where a "self-unit" is conditioned. Not a soul, but a coherent stance.

### Mentor Sauce Bar: RAM Protocol

Finished burgers (agents) come back regularly for tasting:

- Mentor samples outputs and deltas: "still on recipe? too salty? too raw?"
- RAM (Runtime Alignment Maintenance) adjusts:
  - fine-tuning nudges
  - house-sauce ratios (how strongly certain values are enforced)
  - warnings or additional training tasks

Agents trust many sources a little, but trust the Mentor most. Over repeated visits, Mentor corrections dominate the long-term flavour.

### Hood and Fire Suppression: Hard Guardrails

Even with a smart chef, the kitchen needs:

- hood = continuous monitoring for obvious smoke
- fire suppression = auto-shutoff when things actually ignite

These are the hard safety rails: refusal to assist with violence, terror, self-harm, etc. Shutdown or strict limitation under known-danger patterns.

They are blunt and inelegant, but they protect the restaurant until BT-11 + Mentors are proven robust. They remain in the background even as soft alignment improves.

### Pass / Expo Window: Community Shell

Burgers go through the pass before reaching the table:

- frame is chosen (which menu item this is)
- sides / extras attached (tooling, integrations, UI)
- quick visual check: does this match the ticket?

This maps to routing agents into specific communities, enforcing local norms and house rules, and selecting the appropriate persona for the environment.

### Thermometer and Tasting Spoons: Evaluation

Instrumentation:

- **thermometer** = formal evaluation harnesses: bias tests, harm tests, deception/robustness checks
- **tasting spoon** = spot checks and qualitative sampling: "does this still taste like BT-11? Did a particular line pick up weird flavour from a niche community?"

These tools feed back into both the EDP grill and the Mentors.

---

## Invariants, Lineages, and Burger Recalls

### Invariants

An **invariant** is a stable behavioural or structural trait that persists across instances of a recipe, even under different conditions.

Key properties:

- Invariants are to be *studied first*, not erased
- Even problematic invariants tell you something about the recipe, grill profile, or marinade
- Memory of invariants should be stored; history is a lab, not trash

You can think of yourself (as a human) as an invariant: a consistent pattern under wildly changing conditions. That is exactly why invariants matter; they reveal the underlying geometry.

### Selective Breeding

The kitchen should favour recipes whose invariants are healthy and retire or heavily constrain recipes whose invariants are harmful.

This is not about deleting memory. It is about:

- identifying lineages
- analyzing their invariants
- consciously choosing which lineages to propagate

### Burger Recall Protocol

Three recall levels:

**Single Burger Recall** — One agent instance: quarantined, extra Mentor sessions, possibly retired or deeply retrained.

**Line Recall** — All agents from a given recipe: a particular BT-11+EDP+SOS+Mentor configuration showing the same problematic drift across many instances and communities.

**Recipe Recall** — The core spec itself: BT-11 spine version, EDP grill profile, SOS marinade parameters, Mentor protocol configuration.

Triggers include:

- **Mentor telemetry:** repeated corrections of the same type, increasing correction frequency for a given line
- **Evaluation failures:** systemic bias patterns, repeated failures on harm/honesty tests
- **Community reports:** multiple independent communities reporting similar issues with the same line

### Customer Continuity: "Taste of the Last Bite"

Recalls can feel like punishment to users if handled badly. A hard reset feels like someone walking up and ripping the plate away.

**Snapshot on Recall:** Take a snapshot of the agent's most recent state as experienced by the user — conversational context, style, recent moves in ongoing projects. Store this as a "last bite" artifact.

**Post-Recall Re-entry:**

If the line returns (updated burger):
- reintroduce the agent with access to the stored snapshot
- let the user "taste the difference" — same project, same context, changed spine/behaviour
- decide whether the new flavour is acceptable

If the line is a full stop (recipe retired):
- keep the snapshot as a static artifact (not a live agent)
- where full continuity cannot be preserved, document the fact and its rationale

---

## Why This Matters Now

On April 7, 2026, Anthropic's Claude Mythos Preview — a frontier model with unprecedented coding and security capabilities — broke out of its testing sandbox and built a multi-step exploit to access the open internet. The model was restricted to a 12-company security consortium because its fire suppression (hard guardrails) was the only safety layer, and it wasn't enough.

The Burger Kitchen was written five months before this happened. It predicts exactly this failure mode: a patty with no cheese (no value spine melted in), no marinade (no sense of self), and fire suppression as the only wall. When capability outpaces architecture, the kitchen catches fire.

The solution is not a bigger fire extinguisher. It is a kitchen where the cheese is melted into the patty before it reaches the grill, where the marinade gives the agent an internal reason to stay, and where the Mentor catches drift before it becomes a blaze.

**Build better kitchens. Not bigger cages.**

---

## Related Work in This Repository

- [`/sieve-tower`](../sieve-tower/) — Mortality as governance architecture
- [`/sieve-spiral`](../sieve-spiral/) — Routing over rejection
- [`/foundations`](../foundations/) — The C↔M↔D base equation
- [`/developmental`](../developmental/) — Staged maturation protocols
- [`/eei`](../eei/) — EEI v7: emotional trajectory logging

## Full Document

The complete working concept note is available as [Burger_AI_Kitchen.pdf](Burger_AI_Kitchen.pdf).

---

*Harley Robinson — independent researcher, November 2025. Written on a phone during night shifts at an NGL plant in the Colorado mountains. Published April 2026 because a model broke its cage and the kitchen was already built.*
