# XOR Gate Solutions
### Taylor Noah
##### This folder created on `1/4/2022`

In this section I will create two models to learn the XOR gate.  

The first will be a single perceptron which will use a kernal function to transform the two-dimensional non-linearly seperable XOR data into three-dimensional linearly seperable data. Then it can learn a solution in a single linear boundary.  

The second method will utilize a multilayer perceptron. Since an xor gate can be represented as an And gate using the outputs of an Or gate and an Nand gate, the middle layer will contain two nodes and the output will contain a single node. This model will draw two decision boundaries (or and nand) to solve the problem.