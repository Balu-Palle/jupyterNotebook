#Simple neuron class with bias,forward,weights

import numpy as np

class SimpleNeuron:
    def __init__ (self,weights,bias):
        self.weights=np.array(weights)
        self.bias=bias
    def forward(self,weights,bias,inputs):
        inputs=np.array(inputs)
        return np.dot(inputs,self.weights) + self.bias
    
s=SimpleNeuron(weights=[0.2,0.3,0.4],bias=1)

print(s.forward(inputs=[5,4,3]))
