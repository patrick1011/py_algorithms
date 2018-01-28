public class ReverseString {
	public static void main(String[] args) {
		char[] str = {'h', 'e', 'l', 'l', 'o'};
		for (int i = 0, j = str.length - 1; i < str.length / 2; i++, j--) {
			char tempc = str[i];
			str[i] = str[j];
			str[j] = tempc;
		}
		System.out.println(str);
	}
}