import torch.nn.init as init

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

linear = nn.Linear(784, 10, bias=True).to(device)

# weight initialization
init.normal_(linear.weight)