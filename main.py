import numpy

while True:
    y1, y2, y3, y4 = input("Digite os valores de Y ")

    def evalutes_y(y):
        if y == "0":
            y = -1
        else:
            y = 1
        return y

    def evaluates_expression(x1, x2, w1, w2, b):
        if (x1*w1+x2*w2+b >= 0):
            return 1
        else:
            return -1

    def test_neuron(w1, w2, b, y1, y2, y3, y4):
        if(evaluates_expression(1, 1, w1, w2, b) == y1 and evaluates_expression(-1, 1, w1, w2, b) == y2 and evaluates_expression(1, -1, w1, w2, b) == y3 and evaluates_expression(-1, -1, w1, w2, b) == y4):
            return True

    y1 = evalutes_y(y1)
    y2 = evalutes_y(y2)
    y3 = evalutes_y(y3)
    y4 = evalutes_y(y4)

    delta_w_1 = [1*y1, -1*y2, 1*y3, -1*y4]
    delta_w_2 = [1*y1, 1*y2, -1*y3, -1*y4]
    delta_b = [y1, y2, y3, y4]

    new_w1 = numpy.sum(delta_w_1)
    new_w2 = numpy.sum(delta_w_2)
    new_b = numpy.sum(delta_b)

    print("X1 -> w =", new_w1)
    print("X2 -> w =", new_w2)
    print("B -> b =", new_b)

    print(test_neuron(new_w1, new_w2, new_b, y1, y2, y3, y4))
