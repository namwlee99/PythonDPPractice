# 추상 제품 A
class AbstractProductA:
    def display(self):
        pass

# 추상 제품 B
class AbstractProductB:
    def display(self):
        pass

# 구체적인 제품 A1
class ConcreteProductA1(AbstractProductA):
    def display(self):
        return "ConcreteProductA1"

# 구체적인 제품 A2
class ConcreteProductA2(AbstractProductA):
    def display(self):
        return "ConcreteProductA2"

# 구체적인 제품 B1
class ConcreteProductB1(AbstractProductB):
    def display(self):
        return "ConcreteProductB1"

# 구체적인 제품 B2
class ConcreteProductB2(AbstractProductB):
    def display(self):
        return "ConcreteProductB2"

# 추상 팩토리 인터페이스
class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

# 구체적인 팩토리1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

# 구체적인 팩토리2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# 클라이언트
def client(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"ProductA: {product_a.display()}")
    print(f"ProductB: {product_b.display()}")

# 사용 예시
factory1 = ConcreteFactory1()
client(factory1)

factory2 = ConcreteFactory2()
client(factory2)
