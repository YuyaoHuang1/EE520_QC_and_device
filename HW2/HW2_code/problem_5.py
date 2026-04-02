# %%
"""
Problem 5: Quantum Circuit Diagrams

This script draws quantum circuits for the two equations in Problem 5:
1. |0><0| ⊗ I + |1><1| ⊗ Z = I ⊗ |0><0| + Z ⊗ |1><1|
   (Controlled-Z with control in Z eigenbasis)
   
2. |+><+| ⊗ I + |-><-| ⊗ X = I ⊗ |+><+| + X ⊗ |-><-|
   (Controlled-X with control in X eigenbasis)
"""

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# %%
# ============================================================================
# Equation 1: |0><0| ⊗ I + |1><1| ⊗ Z = I ⊗ |0><0| + Z ⊗ |1><1|
# ============================================================================

print("Equation 1: Controlled-Z Gate (Z basis)")
print("=" * 60)

# LHS: Control on qubit 0, target on qubit 1
circuit1_lhs = QuantumCircuit(2)
circuit1_lhs.cz(0, 1)  # Controlled-Z with control on q0, target on q1
circuit1_lhs.name = "LHS: CZ(q0→q1)"

# RHS: Control on qubit 1, target on qubit 0
circuit1_rhs = QuantumCircuit(2)
circuit1_rhs.cz(1, 0)  # Controlled-Z with control on q1, target on q0
circuit1_rhs.name = "RHS: CZ(q1→q0)"

# Draw both circuits
fig1, axes1 = plt.subplots(1, 2, figsize=(12, 3))

circuit1_lhs.draw('mpl', ax=axes1[0])
axes1[0].set_title("LHS: $|0\\rangle\\langle0| \\otimes I + |1\\rangle\\langle1| \\otimes Z$\n" + 
                    "Control on q₀, Target on q₁", fontsize=12)

circuit1_rhs.draw('mpl', ax=axes1[1])
axes1[1].set_title("RHS: $I \\otimes |0\\rangle\\langle0| + Z \\otimes |1\\rangle\\langle1|$\n" + 
                    "Control on q₁, Target on q₀", fontsize=12)

plt.suptitle("Equation 1: Controlled-Z Gate Equivalence\n" + 
             "(CZ is symmetric - control and target can be swapped)", 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('problem5_equation1_circuits.png', dpi=300, bbox_inches='tight')
print("Saved: problem5_equation1_circuits.png")

# %%
# ============================================================================
# Equation 2: |+><+| ⊗ I + |-><-| ⊗ X = I ⊗ |+><+| + X ⊗ |−><−|
# ============================================================================

print("\nEquation 2: Controlled-X Gate (X basis)")
print("=" * 60)

# LHS: Control on qubit 0 (in X basis), target on qubit 1
circuit2_lhs = QuantumCircuit(2)
circuit2_lhs.h(0)       # Change to X basis for control
circuit2_lhs.cx(0, 1)   # Controlled-X with control on q0
circuit2_lhs.h(0)       # Change back to Z basis
circuit2_lhs.name = "LHS: H-CNOT-H"

# RHS: Control on qubit 1 (in X basis), target on qubit 0
circuit2_rhs = QuantumCircuit(2)
circuit2_rhs.h(1)       # Change to X basis for control
circuit2_rhs.cx(1, 0)   # Controlled-X with control on q1
circuit2_rhs.h(1)       # Change back to Z basis
circuit2_rhs.name = "RHS: H-CNOT-H"

# Draw both circuits
fig2, axes2 = plt.subplots(1, 2, figsize=(12, 3))

circuit2_lhs.draw('mpl', ax=axes2[0])
axes2[0].set_title("LHS: $|+\\rangle\\langle+| \\otimes I + |-\\rangle\\langle-| \\otimes X$\n" + 
                    "Control on q₀ (X basis), Target on q₁", fontsize=12)

circuit2_rhs.draw('mpl', ax=axes2[1])
axes2[1].set_title("RHS: $I \\otimes |+\\rangle\\langle+| + X \\otimes |-\\rangle\\langle-|$\n" + 
                    "Control on q₁ (X basis), Target on q₀", fontsize=12)

plt.suptitle("Equation 2: Controlled-X Gate with X-basis Control\n" + 
             "(Hadamard gates change control from Z basis to X basis)", 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('problem5_equation2_circuits.png', dpi=300, bbox_inches='tight')
print("Saved: problem5_equation2_circuits.png")

# %%
# ============================================================================
# Alternative visualization: Show the equivalence more clearly
# ============================================================================

print("\nAlternative Visualization: Side-by-side comparison")
print("=" * 60)

# Create a combined figure showing all circuits
fig3, axes3 = plt.subplots(2, 2, figsize=(14, 8))

# Equation 1
circuit1_lhs.draw('mpl', ax=axes3[0, 0])
axes3[0, 0].set_title("Eq 1 - LHS: CZ(q₀→q₁)", fontsize=11, fontweight='bold')

circuit1_rhs.draw('mpl', ax=axes3[0, 1])
axes3[0, 1].set_title("Eq 1 - RHS: CZ(q₁→q₀)", fontsize=11, fontweight='bold')

# Equation 2
circuit2_lhs.draw('mpl', ax=axes3[1, 0])
axes3[1, 0].set_title("Eq 2 - LHS: H-CNOT-H (control on q₀)", fontsize=11, fontweight='bold')

circuit2_rhs.draw('mpl', ax=axes3[1, 1])
axes3[1, 1].set_title("Eq 2 - RHS: H-CNOT-H (control on q₁)", fontsize=11, fontweight='bold')

plt.suptitle("Problem 5: Quantum Circuit Equivalences", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('problem5_all_circuits.png', dpi=300, bbox_inches='tight')
print("Saved: problem5_all_circuits.png")

print("\n" + "=" * 60)
print("All circuits generated successfully!")
print("Generated files:")
print("  - problem5_equation1_circuits.png")
print("  - problem5_equation2_circuits.png")
print("  - problem5_all_circuits.png")
print("=" * 60)

plt.show()

# %%
