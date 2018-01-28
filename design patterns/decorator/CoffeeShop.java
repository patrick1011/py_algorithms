public class CoffeeShop {
	public static void main(String[] args) {
		Beverage new_coffee = new Black();
		new_coffee = new Cream(new_coffee);
		new_coffee = new Cream(new_coffee);
		System.out.println(new_coffee.cost());
		System.out.println(new_coffee.getDescription());
	} 
}