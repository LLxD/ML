import numpy


class Perceptron:
    def __init__(self, theta, letter):
        self.weight_array = numpy.zeros((25), dtype=int)
        self.learning_rate = 1
        self.theta = theta
        self.letter = letter
        self.bias = numpy.zeros((25), dtype=int)
        self.cycles = 0

    def evaluates_expression(self, target_array):
        if (numpy.array_equal(self.theta, target_array)):
            return numpy.zeros((25), dtype=int)
        else:
            return numpy.multiply(numpy.ones((25), dtype=int), -1)

    def print_info(self):
        print("Pesos:")
        print(self.weight_array)
        print("Bias")
        print(self.bias)

    def guess(self, input_array):
        total = numpy.zeros((25), dtype=int)
        for index in range(len(self.weight_array)):
            total[index] = self.weight_array[index] * \
                input_array[index] + total[index]
            total[index] += self.bias[index]
        return self.evaluates_expression(total)

    def train(self, input_array, target_array):
        error_array = numpy.zeros((25), dtype=int)
        initial_guess = self.guess(input_array)
        for index in range(len(input_array)):
            error_array[index] = target_array[index] - initial_guess[index]
        for index in range(len(self.weight_array)):
            self.weight_array[index] += error_array[index] * \
                input_array[index]*self.learning_rate
            self.bias[index] = self.bias[index] + \
                (self.learning_rate*target_array[index])

    def test(self, input_array, target_array):
        sum_value = numpy.zeros((25), dtype=int)
        self.train(input_array, target_array)
        for index in range(len(input_array)):
            sum_value[index] = self.bias[index]

        if(numpy.array_equal(sum_value, target_array)):
            print("é", self.letter)
        else:
            print("nao eh", self.letter)

        # initialize weights and bias = 0


input_array = [1, -1, 1, 1, 1,
               1, -1, -1, -1, -1,
               1, 1, -1, -1, -1,
               1, -1, 1, 1, 1,
               -1, 1, 1, 1, 1]

x_pattern = [1, -1, -1, -1, 1,
             -1, 1, -1, 1, -1,
             -1, -1, 1, -1, -1,
             -1, 1, -1, 1, -1,
             1, -1, -1, -1, 1]

t_pattern = [1, 1, 1, 1, 1,
             -1, -1, 1, -1, -1,
             -1, -1, 1, -1, -1,
             -1, -1, 1, -1, -1,
             -1, -1, 1, -1, -1]
# while stop condition is false:


perceptronT = Perceptron(x_pattern, "T")
perceptronX = Perceptron(t_pattern, "X")
# perceptron.print_info()
# perceptron.train(input_array, t_pattern)
# perceptron.print_info()
perceptronT.test(input_array, t_pattern)
perceptronX.test(input_array, x_pattern)

perceptronT.test(input_array, x_pattern)
perceptronX.test(input_array, t_pattern)
