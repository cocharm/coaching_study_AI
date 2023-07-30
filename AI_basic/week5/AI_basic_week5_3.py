# Loss fn - Cross Entropy Loss
criterion = nn.CrossEntropyLoss()

# optimizer - SGD
optimizer = torch.optim.SGD(linear.parameters(), lr=0.1)