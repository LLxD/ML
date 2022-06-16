import numpy


class Perceptron:
    def __init__(self):
        self.weight_array = numpy.zeros((25), dtype=int)
        self.learning_rate = 1
        self.theta = 0
        self.bias = numpy.zeros((25), dtype=int)
        self.cycles = 0

    def evaluates_expression(self, value):
        if (value >= self.theta):
            return 1
        else:
            return -1

    def print_info(self):
        print("Pesos:")
        print(self.weight_array)
        print("Bias")
        print(self.bias)
        print("Ciclos : " + str(self.cycles))

    def guess(self, input_array):
        total = 0
        for index in range(len(self.weight_array)):
            total = self.weight_array[index]*input_array[index] + total
            total += self.bias[index]
        return self.evaluates_expression(total)

    def train(self, input_array, target_array):
        error_array = numpy.zeros((25), dtype=int)
        initial_guess = self.guess(input_array)
        for index in range(len(input_array)):
            error_array[index] = target_array[index] - initial_guess
        for index in range(len(self.weight_array)):
            self.weight_array[index] += error_array[index] * \
                input_array[index]*self.learning_rate
            self.bias[index] = self.bias[index] + \
                (self.learning_rate*target_array[index])

    def test(self, input_array, target_array):
        empty_array = numpy.ones((25), dtype=int)
        empty_array = numpy.multiply(empty_array, -1)
        sum_value = 0
        are_not_equal = True
        while are_not_equal:
            self.cycles += 1
            self.train(input_array, target_array)
            for index in range(len(input_array)):
                sum_value = (self.weight_array[index]
                             * input_array[index])+self.bias[index]
                empty_array[index] = self.evaluates_expression(sum_value)
            if(numpy.array_equal(empty_array, target_array)):
                are_not_equal = False
        self.print_info()
        print("Array Obtido:")
        print(empty_array)
        print("Target Array:")
        print(target_array)

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


perceptronT = Perceptron()
perceptronX = Perceptron()
# perceptron.print_info()
# perceptron.train(input_array, t_pattern)
# perceptron.print_info()
perceptronT.test(input_array, t_pattern)
perceptronX.test(input_array, x_pattern)
