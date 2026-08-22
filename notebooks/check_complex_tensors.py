import torch

# Create two complex tensors
a = torch.tensor([1+2j, 3+4j], dtype=torch.cfloat)
b = torch.tensor([5+6j, 7+8j], dtype=torch.cfloat)

print("a:", a)
print("b:", b)

# Complex multiplication
c = a * b
print("a * b:", c)

# Extract real and imaginary parts
print("Real part:", c.real)
print("Imaginary part:", c.imag)