import random

weight_0, weight_1 = 0, 0
input_0, input_1 = 0, 0
iteration = 0
learning_rate = 0

def main():
    setup(True)
    
    
def setup(new_weights = False):
    global weight_0, weight_1, learning_rate, input_0, input_1, iteration
    
    if new_weights:
        weight_0 = random.random()
        weight_1 = random.random()

    learning_rate = 0.01

    print("First Number: ")
    input_0 = float(input())
        
    print("Second Number: ")
    input_1 = float(input())

    iteration = 1
    
    train()
    
    
def train():
    global weight_0, weight_1, learning_rate, input_0, input_1, iteration
    
    while True:
        print("----------------------------------------")
        print(f"Count: {iteration}")
        expectedResult = input_0 + input_1
        calculatedResult = (input_0 + weight_0) + (input_1 + weight_1)
        error = (expectedResult - calculatedResult) * (expectedResult - calculatedResult)
        
        gradient_descent_0 = (expectedResult - calculatedResult) * input_0
        gradient_descent_1 = (expectedResult - calculatedResult) * input_1
        
        print(f"Calculated: {calculatedResult}, Expected: {expectedResult}")
        print(f"Weight_0: {weight_0}, Weight_1: {weight_1}")
        print(f"Error: {error}")
        
        weight_0 = weight_0 + learning_rate * gradient_descent_0
        weight_1 = weight_1 + learning_rate * gradient_descent_1
        
        print(f"New Weight_0: {weight_0}, New Weight_1: {weight_1}")
        
        iteration = iteration + 1
        
        if error == 0:
            print("Error = 0, cannot adjust weights further.")
            break
    
    setup(False)
    

if __name__ == "__main__":
    main()
    
