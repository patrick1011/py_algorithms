
class verify_prime {
	public static void main(String args[]) {

		int A = 7;

        if (A < 1) {
			System.out.println("Not prime");
			return;
        }

        int ubound = (int)(Math.sqrt(A));

        for (int i=2; i<=ubound; i++) {
            if (A % i == 0) {
				System.out.println("Not prime");
				return;
            }
        }

		System.out.println("Prime");
	}
}