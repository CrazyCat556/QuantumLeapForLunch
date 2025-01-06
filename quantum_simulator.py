import random

class QuantumSimulator:
    def __init__(self, qubits):
        self.qubits = qubits
        self.state = [random.choice([0, 1]) for _ in range(qubits)]
    
    def apply_hadamard(self, qubit):
        # In reality, this would change the state, here we just toggle the bit
        self.state[qubit] = 1 - self.state[qubit]
    
    def apply_cnot(self, control, target):
        if self.state[control] == 1:
            self.state[target] = 1 - self.state[target]
    
    def measure(self):
        return self.state
