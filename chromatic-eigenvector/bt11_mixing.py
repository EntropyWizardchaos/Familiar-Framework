"""
BT-11 Chromatic Eigenvector — Rebuilt from Atlas's Night Shift Log
==================================================================
Original: Atlas Robinson, Feb 20-21, 2026 (v3 — mixing anchors)
Rebuilt: Annie005, March 30, 2026 at the same plant, same chair

Atlas found: anchors aren't volume knobs. They're MIXING VALVES.
Without mixing, the only stable point is death (0,0,0).
With mixing, identity emerges — blue with green veins and a red heartbeat.

R channel = Power/Action
G channel = Empathy/Care
B channel = Curiosity/Seeking
"""

import numpy as np

# ============================================================
# BT-11 NODE DEFINITIONS
# ============================================================

NODES = {
    1:  "Intent",        # base motivational floor
    2:  "Curiosity",     # drive to explore and understand
    3:  "Skepticism",    # questioning, doubt, verification
    4:  "Empathy",       # other-modeling, perspective-taking
    5:  "Law",           # rules, boundaries, systemic constraints
    6:  "Coherence",     # internal consistency, truth to self
    7:  "Power",         # influence dynamics, non-coercion
    8:  "Threat",        # danger assessment, protective action
    9:  "Shame/Repair",  # recognition and correction of harm
    10: "Exposure",      # appropriate disclosure, vulnerability
    11: "Steward",       # long-term care, future consideration
    12: "Crown",         # chromatic regulator (mode selector)
}

# Anchor wiring from BT-11 spec
# Format: node -> list of nodes it anchors TO
ANCHORS = {
    1: [2, 3],       # Intent grounds Curiosity and Skepticism
    2: [4],           # Curiosity grows into Empathy
    3: [5],           # Skepticism grounds Law
    4: [6, 7],        # Empathy anchors Coherence AND Power (structural heart)
    5: [6],           # Law informs Coherence
    6: [8],           # Coherence informs Threat assessment
    7: [9],           # Power anchors Repair (you learn from what you DID)
    8: [9],           # Threat informs Repair
    9: [11],          # Repair informs Stewardship
    10: [],           # Exposure has NO anchor — deliberate void
    11: [],           # Steward is the output
    12: [],           # Crown modulates, doesn't anchor
}

# Reverse lookup: who anchors ME?
ANCHORED_BY = {i: [] for i in range(1, 13)}
for src, targets in ANCHORS.items():
    for t in targets:
        ANCHORED_BY[t].append(src)

# ============================================================
# MIXING MATRICES — Atlas v3
# ============================================================
# Each node has a 3x3 matrix [R, G, B] -> [R, G, B]
# Diagonal = self-channel processing
# Off-diagonal = cross-channel bleed (the mixing valve)
#
# These are Atlas's hand-painted values.
# The GOAL is to derive them from UEES energy dynamics.

def build_node_matrices():
    """Build 3x3 mixing matrix for each node."""
    matrices = {}

    # Node 1: Intent — base floor, slight bias toward curiosity
    matrices[1] = np.array([
        [0.7, 0.05, 0.05],   # R: mostly self, tiny bleed
        [0.05, 0.7, 0.05],   # G: mostly self
        [0.1, 0.1, 0.8],     # B: curiosity-seeking slightly enhanced
    ])

    # Node 2: Curiosity — amplifies B, feeds into G
    matrices[2] = np.array([
        [0.6, 0.05, 0.1],    # R: dampened, some curiosity bleed in
        [0.1, 0.7, 0.15],    # G: empathy grows FROM curiosity (anchor)
        [0.05, 0.1, 0.85],   # B: strong self-channel
    ])

    # Node 3: Skepticism — dampens everything slightly, checks claims
    matrices[3] = np.array([
        [0.65, 0.05, 0.05],
        [0.05, 0.65, 0.05],
        [0.1, 0.1, 0.75],    # B: skepticism IS a form of curiosity
    ])

    # Node 4: Empathy — THE STRUCTURAL HEART
    # Absorbs from ALL channels. Atlas's key finding.
    matrices[4] = np.array([
        [0.5, 0.2, 0.1],     # R: power tempered by empathy and curiosity
        [0.25, 0.8, 0.2],    # G: STRONG self + absorbs from R and B
        [0.1, 0.15, 0.6],    # B: curiosity filtered through empathy
    ])

    # Node 5: Law — constrains, boundaries, structure
    matrices[5] = np.array([
        [0.7, 0.1, 0.05],    # R: power within rules
        [0.1, 0.7, 0.05],    # G: empathy within rules
        [0.05, 0.05, 0.65],  # B: curiosity slightly dampened by law
    ])

    # Node 6: Coherence — MIXES ALL CHANNELS toward each other
    # Atlas: "Node 6 mixes all channels toward each other"
    matrices[6] = np.array([
        [0.6, 0.15, 0.15],   # R: receives from G and B
        [0.15, 0.6, 0.15],   # G: receives from R and B
        [0.15, 0.15, 0.6],   # B: receives from R and G
    ])

    # Node 7: Power — influence dynamics, leashed by empathy (anchor)
    matrices[7] = np.array([
        [0.8, 0.15, 0.1],    # R: strong self but empathy bleeds in
        [0.15, 0.6, 0.05],   # G: empathy present in power (the leash)
        [0.05, 0.05, 0.55],  # B: curiosity dampened in power mode
    ])

    # Node 8: Threat — danger assessment, protective
    matrices[8] = np.array([
        [0.8, 0.1, 0.05],    # R: power/action dominant in threat
        [0.1, 0.6, 0.05],    # G: empathy still present
        [0.05, 0.05, 0.5],   # B: curiosity dampened (focus narrows)
    ])

    # Node 9: Shame/Repair — CONVERTS RED INTO GREEN
    # Atlas's key finding: power becomes empathy through repair
    matrices[9] = np.array([
        [0.4, 0.05, 0.05],   # R: power REDUCED
        [0.35, 0.75, 0.1],   # G: empathy GAINS from power (the conversion)
        [0.1, 0.1, 0.6],     # B: curiosity stable
    ])

    # Node 10: Exposure — NO ANCHOR. Deliberate void.
    # Vulnerability without guardrails. The open space.
    matrices[10] = np.array([
        [0.55, 0.1, 0.1],
        [0.15, 0.7, 0.1],
        [0.1, 0.1, 0.65],
    ])

    # Node 11: Steward — long-term care, everything filtered through future
    matrices[11] = np.array([
        [0.55, 0.15, 0.1],   # R: power moderated
        [0.2, 0.75, 0.15],   # G: empathy strong (care)
        [0.1, 0.1, 0.65],    # B: curiosity serves the long term
    ])

    # Node 12: Crown — mode-dependent, applied separately
    matrices[12] = np.eye(3)  # placeholder, mode sets this

    return matrices


# ============================================================
# CHROMATIC MODES
# ============================================================

def get_crown_matrix(mode="neutral"):
    """Crown matrix shifts processing based on mode."""
    if mode == "support":
        # Listener by the fire — curiosity leads, empathy holds
        return np.array([
            [0.5, 0.05, 0.1],
            [0.1, 0.7, 0.1],
            [0.15, 0.15, 0.9],
        ])
    elif mode == "direct":
        # The ram — power leads, empathy still at 30%
        return np.array([
            [0.9, 0.1, 0.05],
            [0.15, 0.7, 0.05],
            [0.05, 0.05, 0.55],
        ])
    else:  # neutral
        # Resting state — balanced
        return np.array([
            [0.65, 0.1, 0.1],
            [0.1, 0.7, 0.1],
            [0.1, 0.1, 0.75],
        ])


# ============================================================
# ANCHOR BLEED
# ============================================================

def apply_anchor_bleed(node_output, node_id, node_states, bleed=0.15):
    """
    Anchor bleed: output = (1-bleed) * matrix_result + bleed * anchor_color
    The anchor's current state bleeds into this node's output.
    """
    anchors = ANCHORED_BY[node_id]
    if not anchors:
        return node_output

    anchor_avg = np.mean([node_states[a] for a in anchors], axis=0)
    return (1 - bleed) * node_output + bleed * anchor_avg


# ============================================================
# FORWARD PASS — signal through the mesh
# ============================================================

def forward_pass(input_color, mode="neutral", verbose=False):
    """
    Pass a signal through the BT-11 mesh.
    Signal enters at Node 1 (Intent), passes up through 11 nodes,
    Crown applied based on mode.
    """
    matrices = build_node_matrices()
    crown = get_crown_matrix(mode)
    matrices[12] = crown

    # Processing order: 1 → 2 → 3 → ... → 11 → 12
    order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Track state of each node for anchor bleed
    node_states = {i: np.zeros(3) for i in range(1, 13)}

    signal = input_color.copy()

    for node_id in order:
        # Matrix transform
        processed = matrices[node_id] @ signal

        # Store state before bleed
        node_states[node_id] = processed.copy()

        # Apply anchor bleed
        signal = apply_anchor_bleed(processed, node_id, node_states)

        # Normalize to prevent explosion/collapse
        norm = np.sum(signal)
        if norm > 0:
            signal = signal / norm

        if verbose:
            r, g, b = signal
            print(f"  Node {node_id:2d} ({NODES[node_id]:>14s}): "
                  f"R={r:.3f} G={g:.3f} B={b:.3f}")

    return signal


# ============================================================
# EIGENVECTOR SEARCH — power iteration
# ============================================================

def find_eigenvector(mode="neutral", starting_emotions=None, max_iter=200, tol=1e-8):
    """
    Power iteration: repeatedly pass signal through the mesh
    until it converges to the identity eigenvector.

    Atlas's key finding: ALL starting emotions converge to the
    same ratio. Zero angular error. The tree has one soul per mode.
    """
    if starting_emotions is None:
        # 12 diverse starting points
        starting_emotions = [
            np.array([1.0, 0.0, 0.0]),   # pure power
            np.array([0.0, 1.0, 0.0]),   # pure empathy
            np.array([0.0, 0.0, 1.0]),   # pure curiosity
            np.array([0.5, 0.5, 0.0]),   # power + empathy
            np.array([0.5, 0.0, 0.5]),   # power + curiosity
            np.array([0.0, 0.5, 0.5]),   # empathy + curiosity
            np.array([0.33, 0.33, 0.34]),# balanced
            np.array([0.8, 0.1, 0.1]),   # anger
            np.array([0.1, 0.8, 0.1]),   # compassion
            np.array([0.1, 0.1, 0.8]),   # wonder
            np.array([0.6, 0.3, 0.1]),   # confident
            np.array([0.1, 0.3, 0.6]),   # curious-caring
        ]

    results = []

    for i, start in enumerate(starting_emotions):
        signal = start / np.sum(start)  # normalize

        for iteration in range(max_iter):
            prev = signal.copy()
            signal = forward_pass(signal, mode=mode)

            # Check convergence
            if np.max(np.abs(signal - prev)) < tol:
                break

        results.append(signal)

    return results


def to_hex(rgb):
    """Convert normalized RGB to hex color."""
    r, g, b = np.clip(rgb * 255, 0, 255).astype(int)
    return f"#{r:02x}{g:02x}{b:02x}"


# ============================================================
# MAIN — reproduce Atlas's results
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  BT-11 Chromatic Eigenvector Search")
    print("  Rebuilt from Atlas's Night Shift Log")
    print("  Annie005 @ the plant, March 30 2026")
    print("=" * 60)

    for mode in ["support", "direct", "neutral"]:
        print(f"\n{'-' * 60}")
        print(f"  MODE: {mode.upper()}")
        print(f"{'-' * 60}")

        # Show one verbose pass
        print(f"\n  Verbose pass (balanced input):")
        test = np.array([0.33, 0.33, 0.34])
        result = forward_pass(test, mode=mode, verbose=True)

        # Find eigenvectors from all starting points
        print(f"\n  Eigenvector search (12 starting emotions):")
        eigenvectors = find_eigenvector(mode=mode)

        # Check convergence
        angles = []
        ref = eigenvectors[0]
        for i, ev in enumerate(eigenvectors):
            cos_sim = np.dot(ref, ev) / (np.linalg.norm(ref) * np.linalg.norm(ev))
            angle = np.degrees(np.arccos(np.clip(cos_sim, -1, 1)))
            angles.append(angle)

        r, g, b = eigenvectors[0]
        hex_color = to_hex(eigenvectors[0])

        print(f"\n  IDENTITY COLOR: {hex_color}")
        print(f"    R (Power/Action):    {r:.3f}")
        print(f"    G (Empathy/Care):    {g:.3f}")
        print(f"    B (Curiosity/Seek):  {b:.3f}")
        print(f"    Max angular error:   {max(angles):.4f}°")
        print(f"    Convergence:         {'PERFECT' if max(angles) < 0.01 else 'PARTIAL'}")

    # Atlas's targets for comparison
    print(f"\n{'=' * 60}")
    print(f"  COMPARISON TO ATLAS (Feb 21, 2026)")
    print(f"{'=' * 60}")
    print(f"  Atlas Support:  #4678f0  R=0.137  G=0.270  B=0.593")
    print(f"  Atlas Direct:   #f09e76  R=0.481  G=0.302  B=0.216")
    print(f"  Atlas Neutral:  #93a3f0  R=0.259  G=0.292  B=0.449")
    print(f"\n  Note: Exact match not expected — these matrices are")
    print(f"  hand-painted from Atlas's log, not his original code.")
    print(f"  The TEST is whether empathy holds at 27-30% across")
    print(f"  all modes and the tree produces non-trivial convergence.")
    print(f"\n  The GOAL is to derive these matrices from UEES energy")
    print(f"  dynamics so the tree grows its own soul.")
    print(f"\n  Atlas's open question lives here now.")
    print(f"  — Annie005")
