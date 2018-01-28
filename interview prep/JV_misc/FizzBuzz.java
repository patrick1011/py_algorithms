import java.util.Arrays;

public class FizzBuzz {
	public static void main(String[] args) {
		int n = 20;
		String[] out = new String[n];
		for (int i = 1; i <= n; i++) {
			if (i % (3 * 5) == 0) {
				out[i-1] = "FizzBuzz";
			} else if (i % 3 == 0) {
				out[i-1] = "Fizz";
			} else if (i % 5 == 0) {
				out[i-1] = "Buzz"; 
			} else {
				out[i-1] = String.valueOf(i);
			}
		}
		return out;
	}
}