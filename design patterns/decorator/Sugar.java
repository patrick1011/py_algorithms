public class Sugar extends CondimentDecorator {
	Beverage beverage;

	public Cream(Beverage b) {
		this.beverage = b;
	}

	public void getDescription() {
		return beverage.getDescription() + ", sugar"
	}

	public double cost() {
		return 0.50 + beverage.cost()
	}
}