#            x0, x1, x2, target
testData = [[1, -1, -1, -1],
            [1, 1, -1, -1],
            [1, -1, 1, -1],
            [1, 1, 1, 1]] #example for AND gate
weights = [0,0,0] #w0, w1, w2
learningRate = 0.1
totalEpoch = 5

print("{:^7}|{:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}"
      .format('Epoch', "i",
              "w0", "w1", "w2",
              "x0", "x1", "x2",
              "target", "output", "delta",
              "deltaW0", "deltaW1", "deltaW2",
              "finalW0", "finalW1", "finalW2"))

for epochCnt in range(totalEpoch):
    for i in range(len(testData)):
        x = testData[i][:-1]
        target = testData[i][-1]
        iniWeights = weights.copy()

        rawOutput = sum([x[j]*weights[j] for j in range(len(x))])
        if rawOutput >= 0:
            output = 1
        else:
            output = -1

        delta = target - output
        for j in range(len(weights)):
            deltaW = (learningRate * x[j]) * delta
            weights[j] += deltaW
            # weights[j] = round(weights[j], 1)
        print("{:^7}|{:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}|{:^7} {:^7} {:^7}"
              .format(epochCnt+1, i+1,
                      iniWeights[0], iniWeights[1], iniWeights[2],
                      x[0], x[1], x[2],
                      target, output, target-output,
                      weights[0]-iniWeights[0], weights[1]-iniWeights[1], weights[2]-iniWeights[2], weights[0], weights[1], weights[2]))

