public class SingleNumber {
	public static void main(String[] args) {
		int[] nums = {1, 2, 3, 6, 8, 5, 5, 1, 3, 2, 6};
		int out = nums[0];
		for (int i = 1; i < nums.length; i++) {
			out ^= nums[i];
		}
		System.out.println(out);
	}
}