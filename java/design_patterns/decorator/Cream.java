public class Cream extends CondimentDecorator {
	Beverage beverage;

	public Cream(Beverage b) {
		this.beverage = b;
	}

	public String getDescription() {
		return beverage.getDescription() + ", cream ";
	}

	public double cost() {
		return 0.50 + beverage.cost();
	}
}