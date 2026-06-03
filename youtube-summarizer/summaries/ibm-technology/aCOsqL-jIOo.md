# How Hadamard and CNOT gates power Quantum Computers

Video ID: `aCOsqL-jIOo`

## Summary
The video explains how quantum computers use gates to process information, focusing on how the Hadamard and CNOT gates create the two foundational quantum phenomena: superposition and entanglement. It walks through the linear algebra behind these gates, showing how applying them to qubits produces a Bell state — one of the most famous equations in physics. The video concludes by revealing that Hadamard and CNOT alone aren't sufficient for true quantum advantage, and that the T gate's phase rotation is what unlocks universal quantum computation.

## Key insights
- **Gates are universal building blocks**: Both classical and quantum computers use gates to transform information — classical gates act on bits, quantum gates act on qubits represented as vectors, making the gates themselves matrices.
- **The Hadamard gate creates superposition**: Multiplying the Hadamard matrix (1/√2 · [[1,1],[1,-1]]) by a qubit state produces an equal superposition, giving a 50/50 probability of measuring 0 or 1.
- **The CNOT gate creates entanglement**: This 4×4 two-qubit gate flips the target qubit only when the control qubit is |1⟩, and when applied after a Hadamard it produces a Bell state — a maximally entangled two-qubit state.
- **Bell states challenge local realism**: John Bell proved that quantum mechanics requires abandoning either definite pre-measurement properties or faster-than-light constraints; quantum states simply have no definite value until measured.
- **Clifford gates alone aren't enough**: The Gottesman-Knill theorem states that circuits built only from Clifford group gates (which include Hadamard and CNOT) can be efficiently simulated on a classical computer — they don't provide true quantum advantage.
- **The T gate is the missing ingredient**: The T gate applies a phase rotation of e^(iπ/4) to |1⟩ without changing measurement probabilities directly, but it makes quantum states exponentially harder to classically simulate by adding a dimension to the state space.
- **Clifford + T = universality**: Combining Clifford gates with the T gate allows approximation of any quantum evolution possible in nature, unlocking the full computational power of quantum systems.