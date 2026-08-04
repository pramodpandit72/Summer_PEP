# 🧑‍💻 Object-Oriented Programming (OOP) Notes for Cognizant

> **Language:** C++  
> **Target:** Cognizant GenC / GenC Next, TCS, Infosys, Accenture, Capgemini, Wipro

---

# What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around **objects** instead of functions.

An **object** contains:
- Data (Attributes)
- Functions (Methods)

### Advantages
- Code Reusability
- Security
- Easy Maintenance
- Modularity
- Scalability

---

# Four Pillars of OOP ⭐⭐⭐⭐⭐

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

---

# 1. Class

A class is a blueprint for creating objects.

### Syntax

```cpp
class Student {
public:
    string name;
    int age;

    void display() {
        cout << name << " " << age;
    }
};
```

---

# 2. Object

An object is an instance of a class.

```cpp
Student s1;
s1.name = "Rahul";
s1.age = 20;

s1.display();
```

---

# 3. Constructor ⭐⭐⭐⭐⭐

A constructor is a special member function that is automatically called when an object is created.

### Characteristics

- Same name as class
- No return type
- Called automatically

### Default Constructor

```cpp
class Student {
public:
    Student() {
        cout << "Constructor Called";
    }
};
```

---

### Parameterized Constructor

```cpp
class Student {
public:
    string name;

    Student(string n) {
        name = n;
    }
};
```

---

### Constructor Overloading

```cpp
class Student {
public:
    Student() {}

    Student(string name) {}

    Student(string name, int age) {}
};
```

---

# 4. Destructor ⭐⭐⭐⭐

A destructor is automatically called when an object is destroyed.

### Syntax

```cpp
class Student {
public:
    ~Student() {
        cout << "Destructor Called";
    }
};
```

### Characteristics

- Begins with `~`
- No parameters
- No return type
- Only one destructor per class

---

# 5. Encapsulation ⭐⭐⭐⭐⭐

Encapsulation means **binding data and methods together** in a class and restricting direct access using access modifiers.

### Example

```cpp
class Student {
private:
    int age;

public:
    void setAge(int a) {
        age = a;
    }

    int getAge() {
        return age;
    }
};
```

### Advantages

- Data Hiding
- Security
- Better Control

---

# 6. Abstraction ⭐⭐⭐⭐⭐

Abstraction means **showing only essential details and hiding implementation**.

### Example

```cpp
class Car {
public:
    void start() {
        cout << "Car Started";
    }
};
```

The user only calls:

```cpp
car.start();
```

They don't know the internal implementation.

### Achieved Using

- Abstract Classes
- Pure Virtual Functions

---

# 7. Inheritance ⭐⭐⭐⭐⭐

Inheritance allows one class to inherit properties from another class.

### Syntax

```cpp
class Animal {
public:
    void eat() {
        cout << "Eating";
    }
};

class Dog : public Animal {
};
```

Dog inherits `eat()` from Animal.

---

## Types of Inheritance

### Single Inheritance

```
A
|
B
```

---

### Multiple Inheritance

```
A     B
 \   /
   C
```

---

### Multilevel Inheritance

```
A
|
B
|
C
```

---

### Hierarchical Inheritance

```
   A
 / | \
B  C  D
```

---

### Hybrid Inheritance

Combination of multiple inheritance types.

---

# 8. Polymorphism ⭐⭐⭐⭐⭐

Polymorphism means **one interface, many forms**.

Types

- Compile-Time
- Run-Time

---

# Compile-Time Polymorphism

Achieved using

- Function Overloading
- Operator Overloading

---

## Function Overloading

```cpp
class Math {
public:
    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
};
```

---

## Operator Overloading

```cpp
class Complex {
public:
    int real, imag;

    Complex operator+(Complex obj) {
        Complex temp;
        temp.real = real + obj.real;
        temp.imag = imag + obj.imag;
        return temp;
    }
};
```

---

# Run-Time Polymorphism

Achieved using

- Function Overriding
- Virtual Functions

---

## Function Overriding

```cpp
class Animal {
public:
    void sound() {
        cout << "Animal";
    }
};

class Dog : public Animal {
public:
    void sound() {
        cout << "Dog";
    }
};
```

---

# Virtual Function ⭐⭐⭐⭐⭐

A virtual function allows runtime polymorphism.

```cpp
class Animal {
public:
    virtual void sound() {
        cout << "Animal";
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Dog";
    }
};

int main() {
    Animal* obj = new Dog();
    obj->sound();
}
```

Output

```
Dog
```

---

# Pure Virtual Function ⭐⭐⭐⭐⭐

A pure virtual function has no implementation.

```cpp
class Animal {
public:
    virtual void sound() = 0;
};
```

---

# Abstract Class

A class containing at least one pure virtual function.

Cannot create objects.

```cpp
Animal a; // Error
```

---

# Friend Function

A friend function can access private members.

```cpp
class Test {
private:
    int x = 10;

public:
    friend void show(Test);
};

void show(Test t) {
    cout << t.x;
}
```

---

# Static Member

Shared among all objects.

```cpp
class Student {
public:
    static int count;
};

int Student::count = 0;
```

---

# Static Function

Can access only static members.

```cpp
class Demo {
public:
    static void display() {
        cout << "Hello";
    }
};
```

Call

```cpp
Demo::display();
```

---

# this Pointer

Points to the current object.

```cpp
class Student {
public:
    int age;

    Student(int age) {
        this->age = age;
    }
};
```

---

# Access Specifiers ⭐⭐⭐⭐⭐

| Modifier | Same Class | Derived Class | Outside |
|-----------|------------|---------------|----------|
| Private | ✅ | ❌ | ❌ |
| Protected | ✅ | ✅ | ❌ |
| Public | ✅ | ✅ | ✅ |

---

# Shallow Copy

Copies only addresses.

```cpp
Student s2 = s1;
```

Problems

- Shared memory
- Double deletion

---

# Deep Copy

Creates a new copy of dynamically allocated memory.

Safer than shallow copy.

---

# Copy Constructor

Used to copy one object to another.

```cpp
Student(Student &obj) {
    age = obj.age;
}
```

---

# Difference Between Constructor and Destructor

| Constructor | Destructor |
|-------------|------------|
| Initializes object | Destroys object |
| Same name as class | Starts with `~` |
| Can be overloaded | Cannot be overloaded |

---

# Function Overloading vs Function Overriding

| Overloading | Overriding |
|--------------|------------|
| Same class | Different classes |
| Compile Time | Run Time |
| Different parameters | Same parameters |

---

# Compile-Time vs Run-Time Polymorphism

| Compile Time | Run Time |
|--------------|----------|
| Function Overloading | Function Overriding |
| Operator Overloading | Virtual Function |

---

# Encapsulation vs Abstraction

| Encapsulation | Abstraction |
|---------------|-------------|
| Data Hiding | Implementation Hiding |
| Uses Access Modifiers | Uses Abstract Class |
| Focus on Security | Focus on Simplicity |

---

# Frequently Asked Interview Questions

### Q1. What are the four pillars of OOP?

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

---

### Q2. Difference between Class and Object?

- A **Class** is a blueprint.
- An **Object** is an instance of a class.

---

### Q3. What is a constructor?

A special function automatically called when an object is created to initialize it.

---

### Q4. Can constructors be overloaded?

Yes, constructors can be overloaded.

---

### Q5. Can constructors be virtual?

No. Constructors cannot be virtual because the object has not been created yet.

---

### Q6. Why use a virtual destructor?

A virtual destructor ensures that when deleting a derived object through a base-class pointer, both the derived and base destructors are called, preventing resource leaks.

---

### Q7. What is inheritance?

Inheritance allows one class to acquire properties and methods from another class.

---

### Q8. What is polymorphism?

Polymorphism allows the same interface (e.g., a function call) to behave differently based on the object's actual type.

---

### Q9. What is an abstract class?

A class with at least one pure virtual function. Objects of abstract classes cannot be created.

---

### Q10. What is the difference between overloading and overriding?

- **Overloading:** Same function name, different parameter list, compile-time.
- **Overriding:** Same function signature in a derived class, runtime.

---

# ⭐ Most Important Topics for Cognizant

- Class and Object
- Constructor & Destructor
- Copy Constructor
- Encapsulation
- Abstraction
- Inheritance
- Types of Inheritance
- Polymorphism
- Function Overloading
- Function Overriding
- Virtual Function
- Pure Virtual Function
- Abstract Class
- Friend Function
- Static Members
- this Pointer
- Access Specifiers
- Shallow Copy vs Deep Copy
- Virtual Destructor