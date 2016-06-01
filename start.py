from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

rete = buildNetwork(2, 8, 1)
ds = SupervisedDataSet(2, 1)
f = 1;

ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (0,))
ds.addSample((1, 1), (1,))
ds.addSample((2, 2), (4,))
ds.addSample((2, 1), (2,))
ds.addSample((2, 5), (10,))
ds.addSample((5, 5), (25,))

trainer = BackpropTrainer(rete, ds)

while f != 0:

    trainer.trainUntilConvergence()

    x = input('X: ')
    y = input('Y: ')

    z = rete.activate([x, y])
    print(z)

    f = input('Corretto? 1>si 2>no 0>esc ')

    if f == 1:
        ds.addSample((x, y), (z,))
    else:
        print ('Ok, ho sbagliato')

print ('Arrivederci!')