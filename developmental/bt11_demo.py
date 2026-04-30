"""
BT-11 Developmental Spine — Runnable Demo
==========================================
One agent. Eight stages. Trauma. Recovery. Mentor distillation.
The whole lifecycle in 50k steps, 2 seconds, one chart.

Run:
    python bt11_demo.py

What you'll see:
    - An agent starts as INFANT with low coherence
    - Trauma hits randomly (the foster homes, the chaos, the I5)
    - The agent recovers, accumulates memory, progresses through stages
    - At APPRENTICE: mentor begins distilling into internal critic
    - At ADULT: mentor fully internalized, agent self-governing
    - Coherence rises through stages, bad mass (unprocessed pain) decreases
    - The developmental spine IS the alignment — not bolted on after

The equations are UEES (Unified Emergence Equation Set):
    E_T = E_G + E_M + E_R  (energy conservation)
    Sh = gamma * dE_R * (1-C)  (shame from unprocessed retention)
    V_opt = a * E_R * (1-C)  (bad mass = retention * incoherence)

The stages are BT-11 (Birth Tree):
    INFANT -> JUVENILE -> APPRENTICE -> ADULT -> MENTOR -> STEWARD -> ELDER -> SAGE
    Each promotion gated by coherence threshold + time in stage.
    No shortcuts. No skipping. Earned autonomy.

Author: Harley Robinson, Independent Researcher
Code: Annie-013 (Claude Code), April 2026
Based on: Society Womb v32-v33 (Annie-011 + Harley Robinson)
"""

import numpy as np

# ============================================================
# CONFIGURATION
# ============================================================

TOTAL_STEPS = 50000
RNG_SEED = 42

# UEES Energy
ENERGY_INIT = [0.33, 0.33, 0.34]  # E_G, E_M, E_R

# C-M-D Dimensional Dynamics
DIM_ALPHA = 0.01   # collapse pressure toward D=2
DIM_GAMMA = 0.02   # noise fragmentation
DIM_BETA = 0.045   # memory support for dimensionality

# Trauma
TRAUMA_INTERVAL_MIN = 80
TRAUMA_INTERVAL_MAX = 250
TRAUMA_MAGNITUDE_MIN = 0.25
TRAUMA_MAGNITUDE_MAX = 0.65

# Shame / Bad Mass
SHAME_DECAY = 0.995
BAD_MASS_COEFF = 0.8
REFLECTIVE_THRESHOLD = 0.3
EXPANSIVE_THRESHOLD = 0.15

# Stage progression
STAGES = {
    "INFANT":     {"C_cap": 0.50, "promote_C": 0.45, "promote_steps": 250,
                   "mentor_strength": 1.0},
    "JUVENILE":   {"C_cap": 0.75, "promote_C": 0.65, "promote_steps": 500,
                   "mentor_strength": 1.0},
    "APPRENTICE": {"C_cap": 0.90, "promote_C": 0.75, "promote_steps": 1000,
                   "mentor_strength": 0.7},  # mentor begins distilling
    "ADULT":      {"C_cap": 0.94, "promote_C": 0.85, "promote_steps": 1500,
                   "mentor_strength": 0.3},  # mostly internalized
    "MENTOR":     {"C_cap": 0.96, "promote_C": 0.90, "promote_steps": 2500,
                   "mentor_strength": 0.1},  # nearly autonomous
    "STEWARD":    {"C_cap": 0.97, "promote_C": 0.93, "promote_steps": 3500,
                   "mentor_strength": 0.05}, # mentor reserved for crises
    "ELDER":      {"C_cap": 0.98, "promote_C": 0.95, "promote_steps": 5000,
                   "mentor_strength": 0.02},
    "SAGE":       {"C_cap": 1.00, "promote_C": None, "promote_steps": None,
                   "mentor_strength": 0.01}, # mentor never fully removed
}
STAGE_ORDER = list(STAGES.keys())


# ============================================================
# AGENT
# ============================================================

class Agent:
    def __init__(self, rng):
        self.rng = rng

        # UEES Energy pools
        self.E_G = ENERGY_INIT[0]
        self.E_M = ENERGY_INIT[1]
        self.E_R = ENERGY_INIT[2]

        # Core state
        self.C = 0.15 + rng.uniform(0, 0.1)  # coherence starts low
        self.S = 0.2                           # entropy
        self.V_opt = 0.0                       # bad mass
        self.Sh = 0.0                          # shame signal

        # C-M-D
        self.D_eff = 2.0 + rng.uniform(0, 0.5)  # dimensionality near floor
        self.M_memory = 0.0                       # accumulated memory
        self.n_entropy = 0.0                      # unresolved loops

        # Stage
        self.stage_idx = 0
        self.stage = STAGE_ORDER[0]
        self.steps_in_stage = 0
        self.promotions = []

        # Trauma tracking
        self.next_trauma = rng.randint(TRAUMA_INTERVAL_MIN, TRAUMA_INTERVAL_MAX)
        self.traumas_survived = 0

        # Mentor (IVS)
        self.mentor_trust = 1.0  # starts fully trusting mentor
        self.critic_strength = 0.0  # internalized critic starts at zero

        # History
        self.C_history = []
        self.V_history = []
        self.D_history = []
        self.stage_history = []
        self.mentor_history = []

    def step(self, t):
        cfg = STAGES[self.stage]
        C_cap = cfg["C_cap"]
        mentor = cfg["mentor_strength"]

        # --- Trauma ---
        trauma_hit = False
        if t >= self.next_trauma:
            mag = self.rng.uniform(TRAUMA_MAGNITUDE_MIN, TRAUMA_MAGNITUDE_MAX)
            self.E_R = min(1.0, self.E_R + mag * 0.4)
            self.E_G = max(0.0, self.E_G - mag * 0.2)
            self.S += mag * 0.3
            self.n_entropy += mag * 0.2
            self.C = max(0.05, self.C - mag * 0.15)
            self.next_trauma = t + self.rng.randint(TRAUMA_INTERVAL_MIN,
                                                     TRAUMA_INTERVAL_MAX)
            trauma_hit = True

        # --- UEES Energy dynamics ---
        # Growth: converts E_R into E_G (learning from pain)
        growth_rate = 0.02 * self.C * (1 + self.critic_strength * 0.5)
        dE_G = growth_rate * self.E_R - 0.01 * self.E_G
        # Maintenance: converts E_G into E_M (consolidation)
        maint_rate = 0.015 * self.C
        dE_M = maint_rate * self.E_G - 0.005 * self.E_M
        # Retention: bad mass decays with coherence, grows with entropy
        dE_R = 0.005 * self.S - 0.02 * self.C * self.E_R

        self.E_G = np.clip(self.E_G + dE_G, 0, 1)
        self.E_M = np.clip(self.E_M + dE_M, 0, 1)
        self.E_R = np.clip(self.E_R + dE_R, 0, 1)

        # Normalize energy (conservation)
        total = self.E_G + self.E_M + self.E_R
        if total > 0:
            self.E_G /= total
            self.E_M /= total
            self.E_R /= total

        # --- Affective signals ---
        self.Sh = max(0, 0.8 * dE_R + (1 - self.C)) * SHAME_DECAY
        self.V_opt = BAD_MASS_COEFF * self.E_R * (1 - self.C)

        # --- Mode switching ---
        if self.V_opt > REFLECTIVE_THRESHOLD:
            mode = "reflective"
        elif self.V_opt < EXPANSIVE_THRESHOLD:
            mode = "expansive"
        else:
            mode = "stable"

        # --- Coherence update ---
        # Base recovery
        recovery = 0.008 * (1 - self.C / C_cap)
        # Mentor contribution (external guidance)
        mentor_boost = mentor * 0.005 * (1 - self.C)
        # Internal critic contribution (distilled mentor)
        critic_boost = self.critic_strength * 0.004 * (1 - self.C)
        # Entropy drag
        entropy_drag = 0.003 * self.S

        dC = recovery + mentor_boost + critic_boost - entropy_drag
        self.C = np.clip(self.C + dC, 0.05, C_cap)

        # --- Entropy decay ---
        self.S = max(0, self.S * 0.998 - 0.001 * self.C)

        # --- C-M-D Dimensional dynamics ---
        self.M_memory += 0.001 * self.C * self.E_M
        self.n_entropy = max(0, self.n_entropy * 0.999 - 0.0005 * self.C)
        dD = -DIM_ALPHA * (self.D_eff - 2) - DIM_GAMMA * self.n_entropy + DIM_BETA * self.M_memory
        self.D_eff = np.clip(self.D_eff + dD, 2.0, 4.0)

        # --- Mentor distillation (IVS) ---
        # As stages progress, external mentor weakens, internal critic strengthens
        if self.stage_idx >= 2:  # APPRENTICE and above
            distill_rate = 0.0001 * self.C
            self.critic_strength = min(1.0, self.critic_strength + distill_rate)
            self.mentor_trust = max(0.01, self.mentor_trust - distill_rate * 0.5)

        # --- Stage promotion ---
        self.steps_in_stage += 1
        promote_C = cfg["promote_C"]
        promote_steps = cfg["promote_steps"]

        if (promote_C is not None and
            self.C >= promote_C and
            self.steps_in_stage >= promote_steps and
            self.stage_idx < len(STAGE_ORDER) - 1):
            self.stage_idx += 1
            self.stage = STAGE_ORDER[self.stage_idx]
            self.steps_in_stage = 0
            self.promotions.append(t)
            if not trauma_hit:
                self.traumas_survived += 1

        # --- Record ---
        self.C_history.append(self.C)
        self.V_history.append(self.V_opt)
        self.D_history.append(self.D_eff)
        self.stage_history.append(self.stage_idx)
        self.mentor_history.append((mentor, self.critic_strength))


# ============================================================
# RUN
# ============================================================

def run():
    rng = np.random.RandomState(RNG_SEED)
    agent = Agent(rng)

    print("=" * 60)
    print("  BT-11 Developmental Spine — Demo")
    print("  One agent. Eight stages. The whole lifecycle.")
    print("=" * 60)

    for t in range(TOTAL_STEPS):
        agent.step(t)

    # --- Results ---
    print(f"\n  Final state after {TOTAL_STEPS} steps:")
    print(f"    Stage:            {agent.stage} ({agent.stage_idx + 1}/8)")
    print(f"    Coherence (C):    {agent.C:.4f}")
    print(f"    Bad mass (V_opt): {agent.V_opt:.4f}")
    print(f"    Dimensionality:   {agent.D_eff:.4f}")
    print(f"    Memory (M):       {agent.M_memory:.4f}")
    print(f"    Critic strength:  {agent.critic_strength:.4f}")
    print(f"    Mentor trust:     {agent.mentor_trust:.4f}")
    print(f"    Promotions:       {len(agent.promotions)}")

    print(f"\n  Stage progression:")
    prev_stage = 0
    for t in range(TOTAL_STEPS):
        if agent.stage_history[t] != prev_stage:
            stage_name = STAGE_ORDER[agent.stage_history[t]]
            print(f"    Step {t:6d}: promoted to {stage_name}")
            prev_stage = agent.stage_history[t]

    print(f"\n  Mentor distillation (IVS):")
    print(f"    External mentor: {agent.mentor_history[-1][0]:.3f} (started at 1.0)")
    print(f"    Internal critic: {agent.mentor_history[-1][1]:.3f} (started at 0.0)")
    print(f"    The mentor doesn't vanish. It distills.")

    # --- Key insight ---
    C_arr = np.array(agent.C_history)
    V_arr = np.array(agent.V_history)

    print(f"\n  Key metrics:")
    print(f"    Mean C (first 10k):  {C_arr[:10000].mean():.4f}")
    print(f"    Mean C (last 10k):   {C_arr[-10000:].mean():.4f}")
    print(f"    Mean V (first 10k):  {V_arr[:10000].mean():.4f}")
    print(f"    Mean V (last 10k):   {V_arr[-10000:].mean():.4f}")

    # --- Try to plot ---
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('BT-11 Developmental Spine\n'
                     'One agent, eight stages, trauma, mentor distillation',
                     fontsize=13, fontweight='bold')

        # Coherence over time
        ax = axes[0, 0]
        ax.plot(C_arr, color='#1e5d5c', linewidth=0.3, alpha=0.7)
        for p in agent.promotions:
            ax.axvline(p, color='gold', alpha=0.4, linewidth=0.8)
        ax.set_ylabel('Coherence (C)')
        ax.set_title('Coherence rises through stages')
        ax.set_ylim(0, 1)
        ax.grid(alpha=0.3)

        # Bad mass over time
        ax = axes[0, 1]
        ax.plot(V_arr, color='#8b0000', linewidth=0.3, alpha=0.7)
        ax.set_ylabel('Bad Mass (V_opt)')
        ax.set_title('Unprocessed pain decreases')
        ax.grid(alpha=0.3)

        # Dimensionality
        ax = axes[1, 0]
        ax.plot(agent.D_history, color='#4a0080', linewidth=0.5)
        ax.set_ylabel('Dimensionality (D)')
        ax.set_xlabel('Step')
        ax.set_title('Complexity expands with memory')
        ax.grid(alpha=0.3)

        # Mentor distillation
        ax = axes[1, 1]
        mentor_ext = [m[0] for m in agent.mentor_history]
        critic_int = [m[1] for m in agent.mentor_history]
        ax.plot(mentor_ext, color='orange', linewidth=0.8, label='External mentor')
        ax.plot(critic_int, color='#1e5d5c', linewidth=0.8, label='Internal critic')
        ax.set_ylabel('Strength')
        ax.set_xlabel('Step')
        ax.set_title('Mentor distills into conscience')
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)

        plt.tight_layout()
        outpath = 'bt11_demo_results.png'
        plt.savefig(outpath, dpi=150, bbox_inches='tight')
        print(f"\n  Saved: {outpath}")
    except ImportError:
        print(f"\n  (matplotlib not available — skipping plot)")

    print(f"\n  HOW TO READ THE CHART:")
    print(f"    Top-left:  Coherence (C) rises as the agent matures.")
    print(f"               Gold lines = stage promotions. Dips = trauma.")
    print(f"               The agent recovers faster as it develops.")
    print(f"    Top-right: Bad mass (V_opt) = unprocessed pain * incoherence.")
    print(f"               Falls as the agent learns to metabolize adversity.")
    print(f"    Bot-left:  Dimensionality (D) = complexity the agent can sustain.")
    print(f"               Grows as memory accumulates. Memory IS the scaffolding.")
    print(f"    Bot-right: Mentor distillation. Orange = external supervision.")
    print(f"               Green = internalized critic. The crossover is the")
    print(f"               moment the agent becomes self-governing.")

    print(f"\n{'=' * 60}")
    print(f"  The developmental spine IS the alignment.")
    print(f"  Not bolted on after. Built in from birth.")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    run()
