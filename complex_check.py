import torch

# Define two complex tensors using torch.cfloat
a = torch.tensor([1.0 + 2.0j, 3.0 - 1.0j], dtype=torch.cfloat)
b = torch.tensor([2.0 + 1.0j, 1.0 + 1.0j], dtype=torch.cfloat)

# Multiply the tensors element-wise
c = a * b

# Print results and their components
print("Tensor A:", a)
print("Tensor B:", b)
print("Product (A * B):", c)
print("Real part:", c.real)
print("Imaginary part:", c.imag)