// Strategy Pattern

// The strategy pattern:
//		1. Defines a family of algorithms.
//		2. Encapsulates each one (makes them interchangable).
// Strategy makes the algorithms vary independently of the clients who use it.

// e.g. list -> inject a sorting algorithm into a list.

interface FlyBehavior {
	public void fly();
}

class FlyWithWings implements FlyBehavior {
	public void fly() {
		System.out.println("I'm flying!!");
	}
}

class FlyNoWay implements FlyBehavior {
	public void fly() {
		System.out.println("Can't fly I am afraid.");
	}
}

interface QuackBehaviour {
	public void quack();
}

class Quack implements QuackBehaviour {
	public void quack() {
		System.out.println("Quack");
	}
}

class MuteQuack implements QuackBehaviour {
	public void quack() {
		System.out.println("<< Silence >>");
	}
}

class Squeak implements QuackBehaviour {
	public void quack() {
		System.out.println("Squeak!");
	}
}


abstract class Duck {
	FlyBehavior flyBehavior;
	QuackBehaviour quackBehaviour;

	public abstract void display();

	public void performfly() {
		flyBehavior.fly();
	}

	public void performquack() {
		quackBehaviour.quack();
	}

	public void setfly(FlyBehavior fb) {
		flyBehavior = fb;
	}

	public void setsquack(QuackBehaviour qb) {
		quackBehaviour = qb;
	}

	public void swim() {
		System.out.println("All ducks float, even decoys!");
	}

}

class MallardDuck extends Duck {
	public MallardDuck() {
		flyBehavior = new FlyWithWings();
		quackBehaviour = new MuteQuack();		
	}

	public void display() { System.out.println("Picture of a mallard");}
}


class Strategy {
	public static void main(String args[]) {
		Duck example_duck = new MallardDuck();
		// example_duck.display();
		// example_duck.swim();
		example_duck.performfly();
		example_duck.setfly(new FlyNoWay());
		example_duck.performfly();
		// example_duck.performquack();
	}	
}